from flask import Flask, render_template

app = Flask(__name__)


@app.route('/static')
def staticPage():
    return render_template('static.html')

if __name__ == '__main__': 
    app.run(debug=True)
