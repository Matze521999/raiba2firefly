import os
import shutil
import tempfile
from flask import Flask, render_template, request, send_file, after_this_request
from werkzeug.utils import secure_filename
from processing import process_csv_files

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if not request.files:
        return 'Keine Dateien erhalten', 400

    files = request.files.getlist('files[]')
    if len(files) < 2:
        return 'Bitte mindestens zwei Dateien hochladen.', 400

    temp_dir = tempfile.mkdtemp()

    try:
        input_paths = []
        for f in files:
            filename = secure_filename(f.filename)
            file_path = os.path.join(temp_dir, filename)
            f.save(file_path)
            input_paths.append(file_path)

        output_path = os.path.join(temp_dir, 'bereinigt.csv')
        process_csv_files(input_paths, output_path)

        @after_this_request
        def cleanup(response):
            try:
                shutil.rmtree(temp_dir)
            except Exception:
                pass
            return response

        return send_file(output_path, as_attachment=True, download_name='bereinigt.csv')

    except Exception as e:
        try:
            shutil.rmtree(temp_dir)
        except Exception:
            pass
        return f'Fehler: {str(e)}', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
