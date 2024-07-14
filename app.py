from flask import Flask, request, jsonify
from flask_cors import CORS
import jamspell

app = Flask(__name__)

CORS(app)

@app.route('/get_answer', methods=['GET'])
def get_answer():
    return jsonify({"answer": 'amogus'})

@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    corrector = jamspell.TSpellCorrector()
    corrector.LoadLangModel('wiki+text/model_twiki.bin')
    
    text = corrector.FixFragment('Цвæр царæгай кæнæ зæйæгой нæ зæронт кæны')
    changed_text = text

    return jsonify({'changed_text': changed_text})

if __name__ == '__main__':
    app.run(debug=True)