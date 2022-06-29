from flask import Flask, render_template, request, jsonify, json
import os
app = Flask(__name__)

@app.route('/data')
def webapi():
    return render_template('data.html')

@app.route('/data/message', methods=['GET'])
def getDataMessage():
    if request.method == "GET":
        print('Austin ' + os.path.dirname(os.path.abspath(__file__)))
        # with open('static/data/message.json', 'r') as f:
        with open('./message.json', 'r') as f:
        # with open('D:\\Austin\\00.Personal\\devWorkSpace\\PythonWithFlask_WorkSpace\\static\\data\\message.json', 'r') as f:
            data = json.load(f)
            print("text : ", data)
        f.close
        return jsonify(data)  # 直接回傳 data 也可以，都是 json 格式

@app.route('/data/message', methods=['POST'])
def setDataMessage():
    if request.method == "POST":
        data = {
            'appInfo': {
                'id': request.form['app_id'],
                'name': request.form['app_name'],
                'version': request.form['app_version'],
                'author': request.form['app_author'],
                'remark': request.form['app_remark']
            }
        }
        print(type(data))
        # with open('static/data/input.json', 'w') as f:
        with open('D:\\Austin\\00.Personal\\devWorkSpace\\PythonWithFlask_WorkSpace\\static\\data\\input.json', 'w') as f:
            json.dump(data, f)
        f.close
        return jsonify(result='OK')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)