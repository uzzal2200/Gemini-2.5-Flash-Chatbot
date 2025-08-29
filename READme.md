
# Gemini 2.5 Flash Streamlit Chatbot

This project is a simple chatbot web application built with Streamlit and Google's Gemini 2.5 Flash model. It allows users to interact with the Gemini AI model in a conversational interface.

## Features
- Chat with Gemini 2.5 Flash AI
- User-friendly Streamlit interface
- Maintains chat history in the session
- Error handling for API issues

## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/uzzal2200/Gemini-2.5-Flash-Chatbot.git
cd Gemni-Pro-Streamlit-Chatbot
```

### 2. Create and Activate Virtual Environment
```
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install Requirements
```
pip install -r requirement.txt
```

### 4. Set Up API Key
- Create a `.env` file in the project root.
- Add your Gemini API key:
```
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the Streamlit App
```
streamlit run main.py
```

### 6. Live link
```
https://gemini-25-flash-chatbot-khneq5py44c7strj5pnz72.streamlit.app
```

## File Structure
- `main.py` : Streamlit chatbot app using Gemini 2.5 Flash
- `demo.py` : Simple script to test Gemini API
- `requirement.txt` : Python dependencies
- `.env` : Environment file for API key

## Troubleshooting
- Make sure your API key is valid and has access to Gemini 2.5 Flash.
- Always run the app with `streamlit run main.py`.
- If you see errors, check your `.env` and dependencies.

## License

This project is for educational purposes.
