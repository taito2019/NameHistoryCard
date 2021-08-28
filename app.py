import os
from flask import Flask, request
from flask import *
import random
import string
import pathlib
import taito_blau_bot



UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'Please upload a File'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        file_extension = pathlib.Path(path).suffix
        print(get_random_string(5))
        new_file_name = (get_random_string(5) + file_extension)
        new_path = (app.config['UPLOAD_FOLDER'] + "/" + new_file_name)
        os.rename(path,new_path)
        return ("files.vollkorn.me/dl/?fl=" + new_file_name)

        return 'ok'
    return render_template("upload.html")

@app.route('/dl/', methods=['GET'])
def request_page():
    file_query = str(request.args.get('fl')) #/dl/?flr=
    print(file_query)
    return send_file(app.config['UPLOAD_FOLDER'] + "/" + file_query)

#TestRequest
@app.route('/TaitoNameHistory/', methods=['GET'])
def taito_request():
    try:
        user_query = str(request.args.get('user')) #/Test/?user=
        print(user_query)
        response = taito_blau_bot.getHistory(user_query)
        print("senden! :D")
        return send_file("result.png", mimetype='image/gif')
    except:
        return send_file("nop.png")
        




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
