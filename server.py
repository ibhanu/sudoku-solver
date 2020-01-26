import cv2 
from main_img import main_process_img
from tensorflow.keras.models import load_model
import os
from flask import Flask, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'images_test'
SAVE_FOLDER = 'images_save'
ALLOWED_EXTENSIONS = set(['jpeg', 'bmp', 'png', 'jpg', 'ash'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def process(filename):
    im_path = 'images_test/'+filename
    model = load_model('model/my_model.h5')
    try:
        main_process_img(im_path, model, save=True, display=False)
    except:
        return(0)
    return(1)

@app.route('/solve', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        #if file and allowed_file(file.filename):
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            status = process(filename)
            if(status):    
                savedfilename = filename[:-4] + '_solved.jpg'
                savedfile = 'images_save/' + savedfilename
                return send_file(savedfile, mimetype='image/jpeg')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8123, debug=True)


