from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import PyPDF2

app = Flask(__name__)

# Temporary folder to save PDFs
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    # Check if PDF file is part of the request
    if 'pdf' not in request.files:
        return jsonify({"error": "No PDF file uploaded"}), 400

    pdf_file = request.files['pdf']
    key1 = request.form.get('key1')
    key2 = request.form.get('key2')

    if pdf_file.filename == '':
        return jsonify({"error": "No selected PDF file"}), 400

    # Save the file securely
    filename = secure_filename(pdf_file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    pdf_file.save(file_path)

    try:
        # ---- Process PDF (example: extract text) ----
        reader = PyPDF2.PdfReader(file_path)
        extracted_text = ''
        for page in reader.pages:
            extracted_text += page.extract_text()

        # ---- After processing, delete the file ----
        os.remove(file_path)

        # ---- Return some result ----
        return jsonify({
            "message": "PDF processed successfully",
            "extracted_text": extracted_text,
            "received_keys": {"key1": key1, "key2": key2}
        })

    except Exception as e:
        # Make sure file is deleted even if an error happens
        if os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
