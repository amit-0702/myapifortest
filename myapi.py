from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return "welcome to the api"


response = [
    {'is_success': '',
     'user_id': 'amit_kumar_07022002',
     'count': 0,
     'email': '1905559@kiit.ac.in',
     'roll_number': 1905559,
     'numbers': [],
     'alphabets': []
     }
]


@app.route('/challenge', methods=['GET', 'POST'])
def get_response():
    return jsonify({'Response': response})


if __name__ == "__main__":
    app.run(debug=True)
