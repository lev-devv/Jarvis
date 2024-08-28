import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyCtGPb45Td-dEiTuMT2InJFp7sIoPLaTcI")

# Initialize the GenerativeModel
model = genai.GenerativeModel("gemini-1.5-flash")

# Start a chat session
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "You are a virtual assistant named jarvis skilled in general tasks like alexa and chatgpt"},
        {"role": "model", "parts": "What is Coding"},
    ]

        
)

# Send a message and get the response

# Send another message and get the response
response = chat.send_message("Who is Subhash CHandra Bose")
print(response.text)

# api key = AIzaSyCtGPb45Td-dEiTuMT2InJFp7sIoPLaTcI
