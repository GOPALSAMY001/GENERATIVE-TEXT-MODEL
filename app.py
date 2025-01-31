from flask import Flask, request, jsonify
from generate_text import generate_text

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        if data is None:
            raise ValueError("Invalid JSON")
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid or missing JSON in request'}), 400
    
    prompt = data.get('prompt', '')
    max_length = data.get('max_length', 100)
    
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    
    generated_text = generate_text(prompt, max_length)
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
