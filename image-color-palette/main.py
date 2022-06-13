import os

from flask import *
import numpy as np
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.getcwd()) + '\\static\\files\\'

ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("/index.html",img="",colors=[],uploaded=False)


@app.route("/upload",methods=["GET","POST"])
def upload_file():
    if request.method=="POST":
        print(request.files)
        if 'file-upload' not in request.files:
            print('No file has been uploaded')
            return redirect(url_for("home"))
        files = request.files['file-upload']
        if files.filename=='':
            print('No file has been selected')
            return redirect(url_for("home"))
        if files and allowed_file(files.filename):
            filename = secure_filename(files.filename)
            files.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            img_arr =  np.array(img)
            img_arr.reshape(-1,3)
            unique_colors,freq = np.unique(img_arr.reshape(-1,3),axis = 0,return_counts=True)
            sorted_index = np.argsort(freq)
            print(sorted_index)
            most_common =  unique_colors[sorted_index][:10]
            return render_template("/index.html", img=filename, colors=most_common, uploaded=True)


if __name__=='__main__':
    app.run(debug = True)