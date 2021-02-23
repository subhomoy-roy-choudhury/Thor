from flask import Flask, jsonify, request
from flask_cors import CORS
import chat_API
app = Flask(__name__)
CORS(app)

@app.route('/predict',methods=['POST'])
def index():
    user_input = request.args.get('user_input')
    return jsonify({'user_input':str(chat_API.brain(user_input))})

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)