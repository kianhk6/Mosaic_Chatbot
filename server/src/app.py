from flask import Flask, request, jsonify
from flask_cors import CORS  
from dotenv import load_dotenv
import os
from chatservice import ChatService

load_dotenv()
app = Flask(__name__)
CORS(app)  # Initialize CORS with the Flask app

api_key = os.getenv('OPENAI_API_KEY')
chat_service = ChatService(api_key=api_key)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    response_content = chat_service.get_response(user_message)
    return jsonify({'response': response_content})

@app.route('/api-check', methods=['GET'])
def api_check():
    try:
        # This is a simplified check. Consider a more specific test for API connectivity if necessary.
        response = chat_service.get_response("Hello")
        if response:
            return jsonify({'status': 'success', 'message': 'API connection is working.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
