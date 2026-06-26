import speech_recognition as sr
from gtts import gTTS
import os
import tempfile

class VoiceModule:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.language_codes = {
            'english': 'en',
            'hindi': 'hi',
            'telugu': 'te'
        }
    
    def speech_to_text(self, audio_data, language='english'):
        """Convert speech to text"""
        try:
            lang_code = self.language_codes.get(language, 'en')
            
            # Recognize speech
            text = self.recognizer.recognize_google(audio_data, language=lang_code)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError:
            return "Could not request results"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def text_to_speech(self, text, language='english'):
        """Convert text to speech and return audio file path"""
        try:
            lang_code = self.language_codes.get(language, 'en')
            
            # Create temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
            temp_path = temp_file.name
            temp_file.close()
            
            # Generate speech
            tts = gTTS(text=text, lang=lang_code, slow=False)
            tts.save(temp_path)
            
            return temp_path
        except Exception as e:
            return None
    
    def listen_from_microphone(self, language='english'):
        """Listen to microphone and convert to text"""
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                try:
                    audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=15)
                    text = self.speech_to_text(audio, language)
                    return text
                except sr.WaitTimeoutError:
                    return ""
        except Exception as e:
            if "listening timed out" in str(e).lower():
                return ""
            return f"Error: {str(e)}"
