# LinguaBot AI: Multilingual Chatbot Project Documentation

This document serves as a comprehensive, end-to-end explanation of the LinguaBot AI project. It breaks down the system architecture, modules, packages, and interaction flows to provide a deep understanding of how everything works together.

## 1. Project Overview & Architecture

LinguaBot AI is a multilingual NLP application combining **word prediction**, **voice input/output**, and **chatbot conversation capabilities**. It uses a client-server architecture:
- **Client (Frontend)**: Developed using HTML, CSS (Bootstrap 5), and Vanilla JavaScript.
- **Server (Backend)**: Developed in Python using the Flask framework, exposing RESTful API endpoints.

The system supports three languages natively: **English**, **Hindi (हिंदी)**, and **Telugu (తెలుగు)**.

---

## 2. Backend Modules (`backend/`)

The backend is strictly divided into specialized "Engines" and "Modules", allowing logic to remain isolated, testable, and maintainable.

### 2.1 Web Server (`app.py`)
This is the core entry point of the application. It runs a `Flask` server and bridges the frontend requests with backend AI logic. 
- **Initialization**: On startup (`initialize_models()`), it loads the datasets via `DatasetLoader` and trains the individual prediction and chatbot algorithms for *each* language in memory.
- **Routes**:
  - `/predict`: Accepts typed text and a language code. It routes this to the appropriate `WordPredictionEngine`.
  - `/chat`: Accepts user messages. It routes this to the appropriate `ChatbotEngine`.
  - `/voice-to-text`: Triggers the local microphone via `VoiceModule`.
  - `/text-to-speech`: Triggers the local speaker generation via `VoiceModule` and streams an MP3 back.
  - `/change-language`, `/clear-history`, `/get-history`: State management endpoints.

### 2.2 Word Prediction Engine (`prediction_engine.py`)
This module provides the "Smart Suggestions" and auto-complete functionality.
- **Algorithm**: It uses an **N-gram Language Model** (specifically Bigrams by default) built using Python's `collections.Counter` and `defaultdict`.
- **Methodology**: 
  - `train()`: It tokenizes all sentences in the dataset. It creates a dictionary where the "key" is a word (or tuple of words) and the "value" is a count of all words that historically followed it.
  - `predict_next_words()`: Given an input string, it looks at the *last word typed*. It looks up that word in its dictionary and returns the highest frequency matching words (`top_k=5`).
  - If a word has never been seen before, it falls back to suggesting the most common words globally across the dataset.

### 2.3 Chatbot Engine (`chatbot_engine.py`)
This is the conversational logic. It acts as an Information Retrieval (IR) based chatbot.
- **Algorithm**: It employs **TF-IDF (Term Frequency-Inverse Document Frequency)** combined with **Cosine Similarity**.
- **Methodology**:
  - `train()`: It takes conversation datasets. It builds simple pattern responses (using the first 20 characters as a direct key). It then fits the `TfidfVectorizer` to learn the vocabulary and frequency weights of the entire corpus.
  - `generate_response()`: When a user sends a message, it first checks simple pattern maps. If none match, it transforms the user's string into a mathematical vector using TF-IDF. It compares this vector geometrically against all known sentence vectors in the dataset using **Cosine Similarity**. It finds the most mathematically similar text and replies with the *next* logical sentence in the corpus.

### 2.4 Voice Module (`voice_module.py`)
This securely interacts with the system hardware to provide accessibility features.
- **Packages Used**: `speech_recognition` (Speech-to-Text) and `gTTS` (Google Text-to-Speech).
- **Methodology**:
  - `listen_from_microphone()`: Activates the system's microphone. It specifically implements `adjust_for_ambient_noise` to filter static, then listens for up to 8 seconds (`timeout`).
  - `speech_to_text()`: Sends the captured audio bytes to Google's free recognition API along with the target dialect code (`en`, `hi`, `te`) and returns the translated text sequence.
  - `text_to_speech()`: Translates text strings into native dialect audio formats mapping to `.mp3` files in a temporary directory (`tempfile`), yielding the file paths back to the Flask app to stream to the browser.

### 2.5 Language Module (`language_module.py`)
A lightweight state manager handling language codes and dictionaries across modules.

---

## 3. Utility Modules (`utils/`)

### 3.1 Dataset Loader (`dataset_loader.py`)
This script provisions the AI. Since Neural networks or NLP engines are blank slates, they require data to learn logic.
- **Methodology**: It attempts to load custom `.csv` dictionaries from `dataset/english_data.csv`, etc., using the `pandas` library.
- **Fallback Mechanism**: If the CSVs do not exist, it automatically falls back to hardcoded arrays of conversational examples (e.g., "Hello, how are you? -> I am doing great"). There is a separate data array configured for English, Hindi, and Telugu.

### 3.2 Preprocessor (`preprocessing.py`)
This is an underlying text cleaning suite utilizing the famous `NLTK` (Natural Language Toolkit) package.
- **Techniques**:
  1. `clean_text()` Removes all special characters and numbers mathematically using Regular Expressions (`re`).
  2. `tokenize()` Splits paragraphs into arrays of standard words.
  3. `remove_stopwords()` Extracts filler words (is, an, the, of) to prevent the AI models from giving false positive similarity scores to generic connecting grammar.
  4. `lemmatize()` Simplifies words down to their root context (e.g., "running", "ran", "runs" all become "run") using `WordNetLemmatizer`.

*(Note: While built out robustly, it acts as a foundation helper for the main engines).*

---

## 4. Frontend Interface (`frontend/`)

### 4.1 Layout & Structure (`index.html`)
The frontend is built with an enterprise SaaS dashboard aesthetic utilizing **Bootstrap 5 grid frameworks**.
- **Navigation (nav)**: Contains the central logo and language toggles.
- **Split Layout**:
  - `Left Sidebar (col-lg-3)`: Provides system context, including a "System Status" card outlining API node endpoints, module liveliness, and action buttons to clear sessions.
  - `Right Chat Interface (col-lg-9)`: The core interactive domain composed of the scrollable chat display, the input text fields, and the absolutely positioned Floating Prediction panel.

### 4.2 Styling (`style.css`)
- **Theme Concept**: Implements "Glassmorphism" visually by using `backdrop-filter: blur()`, giving semi-transparent white backgrounds layered on top of a dynamic purple "mesh" radial-gradient.
- **Variables**: Employs CSS roots (`:root`) enabling unified variable management for exact shade matching (`--primary-color`, `--bot-msg-bg`, etc.).
- The CSS dictates smart hovering effects on prediction chips and an infinite pulse (`pulseRecording`) CSS animation alerting users exactly when their microphone is live.

### 4.3 Logic (`script.js`)
The JS handles user DOM manipulation, event throttling, and AJAX REST calls (`fetch()`) to the `Flask` server.
- **Debouncing**: `handleInputChange()` utilizes `setTimeout` overrides (`predictionTimeout`) to prevent the application from spamming the backend API for predictions on every single keystroke. It waits until the user pauses typing for 300ms before querying the server.
- **DOM Injection**: Responses are actively parsed and appended as `div` strings into inner HTML hierarchies. Auto-scroll logic (`chatWindow.scrollTop = chatWindow.scrollHeight;`) snaps the view automatically down to the most recent message.
- **Voice Interactivity**: Clicking the Voice button locks the UI state, shows a spinner, hits the `/voice-to-text` Python endpoint, waits for speech translation, handles/silences timeout errors gracefully, auto-fills the typing box, and triggers auto-send.
- **Audio Output**: Uses JavaScript `Audio` API coupled with `URL.createObjectURL(blob)` to turn the backend's `.mp3` bytes into a native streaming format without requiring page reloads or local downloads.

---

## 5. Technology Stack Summary

1. **Python 3.8+**: Application Language.
2. **Flask & Flask-CORS**: Highly extensible microscopic web application/socket server.
3. **NLTK, Scikit-Learn (TF-IDF), Numpy**: Mathematical modeling utilities defining the internal NLP algorithms.
4. **SpeechRecognition & Google gTTS**: Hardware microphone interfacing alongside the Google Voice synthesis array.
5. **Pandas**: Structured dataset ingestion.
6. **Bootstrap 5 / Vanilla JavaScript**: Modular, ultra-responsive frontend framework operating in decoupled asynchronous patterns.
