import os, random
from datetime import datetime
from flask import jsonify
from werkzeug.utils import secure_filename
from PIL import Image


# ----------------------------------------------------------------------------

class imageThumbnail:

    def __init__(self):
        self.UPLOAD_FOLDER = 'image'
        self.ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
        self.IMAGE_SIZE = 925, 617 # W | H
        self.THUMBNAIL_SIZE = 260, 195 # W | H

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def get_unique_filename(self):
        random_int = random.randint(0, 99999999)
        datetime_now = datetime.now()
        return datetime_now.strftime('%m%d%Y-%H%M%S-{}'.format(random_int))

    def upload(self, file):
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(self.UPLOAD_FOLDER, filename))
            return self.thumbnail(filename)
        else:
            return jsonify({
                'success' : False,
                'message' : 'File type not allowed, the allowed file types are: png, jpg, jpeg.'
            }), 400

    def thumbnail(self, filename):
        source_path = '{}/{}'.format(self.UPLOAD_FOLDER, filename)
        dest_path = '{}/{}'.format(self.UPLOAD_FOLDER, self.get_unique_filename())

        image = Image.open(source_path)
        image_rgb = image.convert('RGB')

        image_rgb.thumbnail(self.IMAGE_SIZE, Image.ANTIALIAS)
        image_rgb.save(dest_path+'.jpg', 'JPEG', quality=95)

        image_rgb.thumbnail(self.THUMBNAIL_SIZE, Image.ANTIALIAS)
        image_rgb.save(dest_path+'_ico.jpg', 'JPEG', quality=95)

        try:
            os.remove('{}/{}'.format(self.UPLOAD_FOLDER, filename))
            return jsonify({
                'success':  True,
                'message' : 'The required image has been upload and resize - operation successfully completed'
            }), 200
        except OSError as e:
            return jsonify({
                'success':  False,
                'message' : 'Error: {} - {}'.format(e.filename, e.strerror)
            }), 500

# ----------------------------------------------------------------------------
