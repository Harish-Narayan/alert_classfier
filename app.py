from flask import Flask, request, jsonify, render_template
import json
from gemini import generate_context
from summarize_text import summarize_alert
from RAG_fusion import alert_retriever

# Placeholder for your imported functions
# from gemini import generate_context
# from summarize_text import summarize_alert
# from RAG_fusion import alert_retriever

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_alert', methods=['POST'])
def process_alert():
    data = request.data.decode('utf-8')  
    print(data)# Get the raw string data
          # Parse the string into a JSON dictionary
    
    # Example implementations for your functions
    alert_context = summarize_alert(data)  # Replace with your actual function
    similar_alerts = alert_retriever(alert_context)  # Replace with your actual function
    result = generate_context(similar_alerts, alert_context)  # Replace with your actual function
    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
