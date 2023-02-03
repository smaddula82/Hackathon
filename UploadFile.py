from flask import *
from werkzeug.utils import secure_filename
import os

app=Flask(__name__)
app.secret_key='fake_key'

UPLOAD_FOLDER='C:\\Users\\DELL\\PycharmProjects\\pythonProject\\HousePricePredict\\UploadedFile'
ALLOWED_EXTENSIONS={'csv'}
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

def allowed_filename(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload.file',methods=['GET','POST'])
def upload_file():
    if request.method=='POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file=request.files['file']
        print(file)
        if file.filename=='':
            return redirect(request.url)
        if file:
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return redirect(request.url)
        else:
            return redirect(request.url)
    return '''
    <!doctype html>
    <title>Upload New File</title>
    <h1>Upload new file</h1>
    <form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=Upload>
    </form>'''
if __name__=="__main__":
    app.run(debug=True)