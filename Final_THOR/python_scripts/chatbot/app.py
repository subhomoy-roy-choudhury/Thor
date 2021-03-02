from flask import Flask,render_template, jsonify, request
from flask_cors import CORS
import chat_API
import pywhatkit
app = Flask(__name__)
CORS(app)

# @app.route('/predict',methods=['POST'])
# def index():
#     user_input = request.args.get('user_input')
#     return jsonify({'user_input':str(chat_API.brain(user_input))})

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('user_input')
    if "search" in userText:
        userText = userText.replace('search', '')  
        pywhatkit.search(userText) 
        return "searched"+str(userText)
    return str(chat_API.brain(userText))



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)