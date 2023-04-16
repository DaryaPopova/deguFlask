from flask import Flask


app = Flask(__name__)


@app.route('/user/<int:user_id>')
def index(user_id):
    return f'Дегу номер {user_id}'


if __name__ == '__main__':
    app.run(debug=True)
