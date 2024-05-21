from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
with open('model_nb.pkl', 'rb') as f:
  model_nb = pickle.load(f)

@app.route('/')
def index():
    return 'Hey Golie'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Assuming JSON input
    text = data['text']

    prediction = model_nb.predict([text])

    class_names = ['Common Cold', 'Dengue', 'Malaria', 'Typhoid']
    
    prediction = class_names[prediction[0]]
    
    
    return jsonify(prediction)