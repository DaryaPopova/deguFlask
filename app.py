from flask import Flask


app = Flask(__name__)


@app.route('/user/<int:user_id>')
def index(user_id):
    return f'Дегу номер {user_id}'


@app.route('/')
def root():
    return "Hi Degu"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
