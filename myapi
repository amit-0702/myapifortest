from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return "welcome to the api"


response = [
    {'is_seccess': 'true',
     'user_id': 'amit_kumar_07022002',
     'count': 0,
     'email': '1905559@kiit.ac.in',
     'roll_number': 1905559,
     'numbers': [],
     'alphabets': []
     }
]


@app.route('/challenge', methods=['GET'])
def get():
    return jsonify({'Response': response})


@app.route('/challenge/')
def post():



if __name__ == "__main__":
    app.run(debug=True)
