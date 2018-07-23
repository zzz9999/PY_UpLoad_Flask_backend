from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import *
from werkzeug.utils import secure_filename
import os
import csv
import json
import time
import base64

app = Flask(__name__)
CORS(app, supports_credentials = True)

ALLOWED_EXTENSIONS = set(['csv'])
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        if f and allowed_file(f.filename):
            basepath = os.path.dirname(__file__)  # 当前文件所在路径
            upload_path = os.path.join(basepath, 'static/uploads', secure_filename(f.filename))  # 注意：要先创建该文件夹，不然会提示没有该路径
            f.save(upload_path)
            t = date_work('C:\\Users\\zou\\PycharmProjects\\Web_backend\\static\\uploads\\' + f.filename) # 静态库绝对路径+文件名

            return t
        else:
            return jsonify({"errno": 1001, "errmsg": u"failed"})

    """
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['file']  # 从表单的file字段获取文件，file为该表单的name值

    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname = secure_filename(f.filename)
        print(fname)
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = 'test' + '.' + ext  # 修改了上传的文件名
        f.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录
        token = base64.b64encode(new_filename)
        print(token)
        t = date_work('/upload/' + new_filename)

        return t
    else:
        return jsonify({"errno": 1001, "errmsg": u"failed"})
    """


@app.route('/')
def hello_world(): 
    return 'Hello World!'
"""
@app.route('/users/<id>')
def hello_users(id):
    return "users: " + id

@app.route('/query_user')
def query_user():
    id = request.args.get(id)
    return "query_user: id" + id
"""


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def date_work(filename):
    csv_file = csv.reader(open(filename, 'r'))
    column = [row[51] for row in csv_file]
    print(column)
    X1 = 0  # 0-20
    X2 = 0  # 20-40
    X3 = 0  # 40-60
    X4 = 0  # 60-80
    for a in column:
        a = int(a)
        if a >= 0 and a < 20:
            X1 = X1 + 1
        elif a >= 20 and a < 40:
            X2 = X2 + 1
        elif a >= 40 and a < 60:
            X3 = X3 + 1
        elif a >= 60 and a < 80:
            X4 = X4 + 1
        else:
            pass
    print(X1, X2, X3, X4)
    back = [
        {
        'distance':'0-20',
        'count':X1
        },
        {'distance':'20-40',
         'count':X2
        },
        {'distance':'40-60',
         'count':X3
        },
        {'distance':'60-80',
         'count':X4
        }
    ]
    return json.dumps(back)


if __name__ == '__main__':
    #print(date_work('C:/Users/zou/PycharmProjects/Web_backend/sc1.csv'))
    app.run(host='0.0.0.0', port=5000)
