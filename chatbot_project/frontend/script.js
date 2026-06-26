// Global variables
let currentLanguage = 'english';
let lastBotResponse = '';
let isListening = false;

// DOM Elements
const chatWindow = document.getElementById('chatWindow');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const voiceBtn = document.getElementById('voiceBtn');
const clearBtn = document.getElementById('clearBtn');
const speakBtn = document.getElementById('speakBtn');
const languageSelect = document.getElementById('languageSelect');
const predictionsPanel = document.getElementById('predictionsPanel');
const predictionsContent = document.getElementById('predictionsContent');
const loadingIndicator = document.getElementById('loadingIndicator');

// API Base URL
const API_URL = 'http://localhost:5000';

// Event Listeners
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});
userInput.addEventListener('input', handleInputChange);
voiceBtn.addEventListener('click', startVoiceInput);
clearBtn.addEventListener('click', clearChat);
speakBtn.addEventListener('click', speakLastResponse);
languageSelect.addEventListener('change', changeLanguage);

// Send message function
async function sendMessage() {
    const message = userInput.value.trim();

    if (!message) return;

    // Add user message to chat
    addMessage(message, 'user');
    userInput.value = '';
    predictionsContent.innerHTML = '';
    predictionsPanel.classList.remove('active');

    // Show loading
    showLoading();

    try {
        // Get chatbot response
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                language: currentLanguage
            })
        });

        const data = await response.json();

        // Hide loading
        hideLoading();

        // Add bot response
        if (data.response) {
            lastBotResponse = data.response;
            addMessage(data.response, 'bot');
        } else if (data.error) {
            addMessage('Sorry, I encountered an error.', 'bot');
        }
    } catch (error) {
        hideLoading();
        addMessage('Sorry, I could not connect to the server.', 'bot');
        console.error('Error:', error);
    }
}

// Add message to chat window
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;

    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content shadow-sm';
    contentDiv.textContent = text;

    messageDiv.appendChild(contentDiv);
    chatWindow.appendChild(messageDiv);

    // Scroll to bottom
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

// Handle input change for predictions
let predictionTimeout;
async function handleInputChange() {
    const text = userInput.value.trim();

    // Clear previous timeout
    clearTimeout(predictionTimeout);

    if (!text) {
        predictionsContent.innerHTML = '';
        predictionsPanel.classList.remove('active');
        return;
    }

    // Debounce predictions
    predictionTimeout = setTimeout(async () => {
        try {
            const response = await fetch(`${API_URL}/predict`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    text: text,
                    language: currentLanguage
                })
            });

            const data = await response.json();
            displayPredictions(data);
        } catch (error) {
            console.error('Prediction error:', error);
        }
    }, 300);
}

// Display predictions
function displayPredictions(data) {
    predictionsContent.innerHTML = '';

    if (data.predictions && data.predictions.length > 0) {
        // Add word predictions
        const wordsHeader = document.createElement('div');
        wordsHeader.className = 'section-label';
        wordsHeader.textContent = 'Next Words';
        predictionsContent.appendChild(wordsHeader);

        data.predictions.forEach(pred => {
            const chip = document.createElement('span');
            chip.className = 'prediction-chip';
            chip.textContent = pred;
            chip.onclick = () => appendPrediction(pred);
            predictionsContent.appendChild(chip);
        });
    }

    if (data.sequences && data.sequences.length > 0) {
        // Add sequence predictions
        const seqHeader = document.createElement('div');
        seqHeader.className = 'section-label mt-2';
        seqHeader.textContent = 'Suggested Phrases';
        predictionsContent.appendChild(seqHeader);

        data.sequences.forEach(seq => {
            const chip = document.createElement('span');
            chip.className = 'sequence-chip';
            chip.textContent = seq;
            chip.onclick = () => replacePrediction(seq);
            predictionsContent.appendChild(chip);
        });
    }

    if ((!data.predictions || data.predictions.length === 0) &&
        (!data.sequences || data.sequences.length === 0)) {
        predictionsPanel.classList.remove('active');
    } else {
        predictionsPanel.classList.add('active');
    }
}

// Append prediction to input
function appendPrediction(word) {
    userInput.value += ' ' + word;
    userInput.focus();
    handleInputChange();
}

// Replace input with prediction
function replacePrediction(text) {
    userInput.value = text;
    userInput.focus();
    handleInputChange();
}

// Voice input using Backend API
async function startVoiceInput() {
    if (isListening) return;

    voiceBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
    voiceBtn.classList.add('recording');
    isListening = true;

    try {
        const response = await fetch(`${API_URL}/voice-to-text`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                language: currentLanguage
            })
        });

        const data = await response.json();

        if (data.error) {
            console.warn('Voice recognition:', data.error);
            const originalPlaceholder = userInput.placeholder;
            userInput.placeholder = "Didn't catch that...";
            setTimeout(() => { userInput.placeholder = originalPlaceholder; }, 2000);
        } else if (data.text) {
            userInput.value = data.text;
            handleInputChange();
            // Automatically send the message after a brief pause
            setTimeout(sendMessage, 500);
        }
    } catch (error) {
        console.error('Voice input error:', error);
        const originalPlaceholder = userInput.placeholder;
        userInput.placeholder = "Voice server disconnected...";
        setTimeout(() => { userInput.placeholder = originalPlaceholder; }, 2000);
    } finally {
        voiceBtn.innerHTML = '<i class="fas fa-microphone"></i>';
        voiceBtn.classList.remove('recording');
        isListening = false;
    }
}

// Speak last bot response via Backend API
async function speakLastResponse() {
    if (!lastBotResponse) {
        alert('No response to speak!');
        return;
    }

    const speakIcon = speakBtn.innerHTML;
    speakBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
    speakBtn.disabled = true;

    try {
        const response = await fetch(`${API_URL}/text-to-speech`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: lastBotResponse,
                language: currentLanguage
            })
        });

        if (!response.ok) throw new Error('Network response was not ok');

        const blob = await response.blob();
        const audioUrl = URL.createObjectURL(blob);
        const audio = new Audio(audioUrl);

        audio.onended = () => {
            speakBtn.innerHTML = speakIcon;
            speakBtn.disabled = false;
        };

        await audio.play();
    } catch (error) {
        console.error('Text-to-speech error:', error);

        // Fallback to browser TTS
        if ('speechSynthesis' in window) {
            const utterance = new SpeechSynthesisUtterance(lastBotResponse);
            const langCodes = { 'english': 'en-US', 'hindi': 'hi-IN', 'telugu': 'te-IN' };
            utterance.lang = langCodes[currentLanguage] || 'en-US';
            window.speechSynthesis.speak(utterance);
        } else {
            alert('Text-to-speech failed or is not supported.');
        }

        speakBtn.innerHTML = speakIcon;
        speakBtn.disabled = false;
    }
}

// Clear chat
async function clearChat() {
    if (confirm('Are you sure you want to clear the chat?')) {
        chatWindow.innerHTML = `
            <div class="message bot-message">
                <div class="message-content shadow-sm">
                    Hello! I'm your Multilingual AI companion. How can I help you today?
                </div>
            </div>
        `;

        try {
            await fetch(`${API_URL}/clear-history`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            });
        } catch (error) {
            console.error('Error clearing history:', error);
        }
    }
}

// Change language
async function changeLanguage() {
    currentLanguage = languageSelect.value;

    try {
        await fetch(`${API_URL}/change-language`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                language: currentLanguage
            })
        });

        // Update UI message
        const langNames = {
            'english': 'English',
            'hindi': 'Hindi',
            'telugu': 'Telugu'
        };

        addMessage(`Language changed to ${langNames[currentLanguage]}`, 'bot');
    } catch (error) {
        console.error('Error changing language:', error);
    }
}

// Show/hide loading indicator
function showLoading() {
    loadingIndicator.classList.add('show');
}

function hideLoading() {
    loadingIndicator.classList.remove('show');
}

// Initialize
console.log('Multilingual Chatbot initialized!');
