from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/secretpage')
def secret_page():
    flag = os.environ.get('CTF_FLAG', 'Флаг не найден')
    return render_template('secretpage.html', flag=flag)

if __name__ == '__main__':
    app.run(debug=True)
