from config import app
from image_thumbnail import imageThumbnail
from flask import request, jsonify


# ----------------------------------------------------------------------------
# Upload
# ----------------------------------------------------------------------------

@app.route('/file-upload', methods=['POST'])
def upload_file():

    name = request.form.get('name', None)

    if 'file' not in request.files:
        return jsonify({
            'success':  False,
            'message' : 'No file part in the request'
        }), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({
            'success':  False,
            'message' : 'No file selected for uploading'
        }), 400

    return imageThumbnail().upload(file)

# ----------------------------------------------------------------------------

if __name__ == "__main__":
    app.run()
