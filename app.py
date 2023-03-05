from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # Show content of index.html

@app.route('/submit', methods=['POST'])
def submit(name=None):
    submit_data = request.get_json()   # Receive JSON format data
    user_input = submit_data['input']  # Retrieve input
    result = f"You sent: {user_input}" # Prepare response data
    return jsonify({"result": result}) # Return data in JSON format
