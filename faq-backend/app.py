from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample FAQ data
faqs = [
    {"id": 1, "question": "How to reset password?", "answer": "Use the IT portal."},
    {"id": 2, "question": "How to apply for leave?", "answer": "Go to HR portal."}
]

@app.route('/api/faqs', methods=['GET'])
def get_faqs():
    return jsonify(faqs)

@app.route('/api/faqs', methods=['POST'])
def add_faq():
    data = request.get_json()
    new_faq = {
        "id": len(faqs) + 1,
        "question": data["question"],
        "answer": data["answer"]
    }
    faqs.append(new_faq)
    return jsonify(new_faq), 201

@app.route('/api/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    global faqs
    faqs = [f for f in faqs if f["id"] != faq_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
