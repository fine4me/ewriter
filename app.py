from flask_cors import CORS
from flask import Flask, render_template, request, jsonify



app = Flask(__name__)


CORS(app)
# Home route
@app.route('/')
def home():
    return render_template('home.html', page_title="Home")

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if data is None:
                return jsonify({'error': 'No JSON data provided'}), 400

            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return jsonify({'error': 'Email and password are required'}), 400

            return jsonify({'message': 'Login successful'}), 200

        except Exception as e:
            return jsonify({'error': 'Invalid request format'}), 400

    # GET request - render login page
    return render_template('login.html')
# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No JSON data provided'}), 400

            # Check required fields
            required = ['email', 'password', 'username', 'age']
            missing = [f for f in required if not data.get(f)]
            if missing:
                return jsonify({'error': f'Missing fields: {", ".join(missing)}'}), 400

            # Basic validations
            if '@' not in str(data['email']):
                return jsonify({'error': 'Invalid email format'}), 400

            try:
                age = int(data['age'])
                if not 0 <= age <= 150:
                    return jsonify({'error': 'Invalid age'}), 400
            except ValueError:
                return jsonify({'error': 'Age must be a number'}), 400

            if len(str(data['password'])) < 8:
                return jsonify({'error': 'Password must be 8+ characters'}), 400

            return jsonify({'message': 'Registration successful'}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 400

    return render_template('signup.html', page_title="Sign Up")
# About Us route
@app.route('/about')
def about():
    return render_template('about.html', page_title="About Us")

@app.route('/event')
def event():
    return render_template('event.html', page_title="Event")

@app.route('/community')
def community():
    return render_template('community.html', page_title="Community")

if __name__ == '__main__':
    app.run(debug=True)
