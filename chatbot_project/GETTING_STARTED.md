# 🚀 Getting Started - 5 Minute Guide

## Welcome to the Multilingual Chatbot! 🤖

This guide will get you up and running in 5 minutes.

---

## Step 1: Install Dependencies (2 minutes)

Open terminal/command prompt in the `chatbot_project` folder:

```bash
pip install -r requirements.txt
```

Wait for installation to complete...

---

## Step 2: Download NLTK Data (1 minute)

Run this command:

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

---

## Step 3: Start the Server (30 seconds)

```bash
cd backend
python app.py
```

You should see:
```
Starting Multilingual Chatbot Server...
Open http://localhost:5000 in your browser
```

---

## Step 4: Open Browser (30 seconds)

Open your web browser and go to:
```
http://localhost:5000
```

---

## Step 5: Start Chatting! (1 minute)

### Try These Examples:

1. **Type**: "How are"
   - Watch predictions appear!
   - Click on "you" to complete

2. **Send**: "Hello"
   - See the bot respond

3. **Change Language**: Select "Hindi" from dropdown
   - Type in Hindi or English

4. **Voice Input**: Click microphone button 🎤
   - Speak your message
   - (Works best in Chrome/Edge)

5. **Voice Output**: Click "Speak Response" 🔊
   - Hear the bot's voice

---

## 🎯 Quick Tips

✅ **Predictions appear as you type** - Click them to auto-complete  
✅ **Orange chips** = Next words  
✅ **Green chips** = Complete phrases  
✅ **Switch languages anytime** - No restart needed  
✅ **Use voice** - Click mic button and speak  

---

## 🎨 Interface Overview

```
┌─────────────────────────────────────┐
│  Multilingual AI Chatbot           │
│  Word Prediction & Voice Assistant  │
├─────────────────────────────────────┤
│  Language: [English ▼]              │
├─────────────────────────────────────┤
│  ┌───────────────────────────────┐ │
│  │ Chat Window                   │ │
│  │                               │ │
│  │ Bot: Hello! How can I help?   │ │
│  │                               │ │
│  │ You: How are you?             │ │
│  │                               │ │
│  │ Bot: I am doing great!        │ │
│  └───────────────────────────────┘ │
├─────────────────────────────────────┤
│  ┌───────────────────────────────┐ │
│  │ 💡 Predictions                │ │
│  │                               │ │
│  │ [you] [they] [things]         │ │
│  │                               │ │
│  │ Suggested Phrases:            │ │
│  │ [How are you]                 │ │
│  │ [How are they]                │ │
│  └───────────────────────────────┘ │
├─────────────────────────────────────┤
│  Type message: ________________    │
│  [🎤] [Send]                        │
│                                     │
│  [Clear Chat] [Speak Response]      │
└─────────────────────────────────────┘
```

---

## 📝 Example Conversation

```
You: Hello
Bot: Hello! How can I help you?

You: Tell me about AI
Bot: Artificial Intelligence is fascinating!

You: What is machine learning
Bot: Machine learning is a subset of AI.

You: Thank you
Bot: You are welcome!
```

---

## 🌐 Try Different Languages

### English
```
You: How are you?
Bot: I am doing great!
```

### Hindi (हिंदी)
```
You: नमस्ते
Bot: नमस्ते! मैं आपकी कैसे मदद कर सकता हूं?
```

### Telugu (తెలుగు)
```
You: నమస్కారం
Bot: నమస్కారం! నేను మీకు ఎలా సహాయం చేయగలను?
```

---

## 🎤 Voice Features

### Voice Input
1. Click microphone button 🎤
2. Allow microphone access (first time)
3. Speak clearly: "Hello, how are you?"
4. Text appears in input box
5. Click Send

### Voice Output
1. Receive a bot response
2. Click "Speak Response" button 🔊
3. Listen to the bot speak
4. Works in all 3 languages!

---

## ⚡ Keyboard Shortcuts

- **Enter** - Send message
- **Ctrl+R** - Refresh page
- **Esc** - Clear input (browser default)

---

## 🐛 Quick Troubleshooting

### Server won't start?
```bash
# Check if port 5000 is free
# Or change port in backend/app.py
```

### Predictions not showing?
- Wait 2-3 seconds after typing
- Models need time to train on first run

### Voice not working?
- Use Chrome or Edge browser
- Allow microphone permissions
- Check microphone is connected

### Module not found?
```bash
pip install -r requirements.txt
```

---

## 📚 Learn More

- **Full Documentation**: README.md
- **User Manual**: USER_GUIDE.md
- **Quick Reference**: QUICK_REFERENCE.md
- **All Docs**: INDEX.md

---

## 🎉 You're Ready!

That's it! You're now ready to use the chatbot.

### What to Try Next:

1. ✅ Test word predictions
2. ✅ Try all 3 languages
3. ✅ Use voice features
4. ✅ Explore the UI
5. ✅ Read full documentation

---

## 💡 Pro Tips

🔥 **Type partial sentences** for better predictions  
🔥 **Click predictions** instead of typing  
🔥 **Switch languages** to test translation  
🔥 **Use voice** for hands-free interaction  
🔥 **Clear chat** to start fresh  

---

## 🆘 Need Help?

1. Check **USER_GUIDE.md** for detailed help
2. Check **README.md** for technical info
3. Run `python test_system.py` to verify setup

---

## 🎊 Enjoy Your Chatbot!

**You're all set! Start chatting now! 🚀**

---

*Time to complete: ~5 minutes*  
*Difficulty: Easy*  
*Requirements: Python 3.8+, Web Browser*
