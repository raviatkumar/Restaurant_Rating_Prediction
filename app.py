from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Load the fitted LabelEncoders
le_location = pickle.load(open('label_encoder_location.pkl', 'rb'))
le_rest_type = pickle.load(open('label_encoder_rest_type.pkl', 'rb'))
le_cuisines = pickle.load(open('label_encoder_cuisines.pkl', 'rb'))
le_type = pickle.load(open('label_encoder_type.pkl', 'rb'))

# Define dropdown values
online_order_values = ['Yes', 'No']
book_table_values = ['Yes', 'No']
location_values = le_location.classes_.tolist()
rest_type_values = le_rest_type.classes_.tolist()
approx_cost_values = [200, 300, 400, 500, 600]  # Modify as needed
cuisines_values = le_cuisines.classes_.tolist()
type_values = le_type.classes_.tolist()

# Hardcoded credentials
USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('show_predictor'))
        else:
            return render_template('login.html', error='Invalid credentials! Please try again.')
    return render_template('login.html')

@app.route('/predict')
def show_predictor():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    return render_template('predictor.html',
                           online_order_values=online_order_values,
                           book_table_values=book_table_values,
                           location_values=location_values,
                           rest_type_values=rest_type_values,
                           approx_cost_values=approx_cost_values,
                           cuisines_values=cuisines_values,
                           type_values=type_values)

@app.route('/predict', methods=['POST'])
def predict():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    online_order = request.form['online_order']
    book_table = request.form['book_table']
    votes = request.form['votes']
    location = request.form['location']
    rest_type = request.form['rest_type']
    cuisines = request.form['cuisines']
    cost_for_two_people = request.form['cost_for_two_people']
    type = request.form['type']
    
    input_data = pd.DataFrame([[online_order, book_table, votes, location, rest_type, cuisines, 
                                 cost_for_two_people, type]],
                              columns=['online_order', 'book_table', 'votes', 'location', 
                                       'rest_type', 'cuisines', 'cost_for_two_people', 
                                        'type'])

    input_data['cost_for_two_people'] = pd.to_numeric(input_data['cost_for_two_people'], errors='coerce')
    input_data['votes'] = pd.to_numeric(input_data['votes'], errors='coerce')

    input_data['location'] = le_location.transform(input_data['location'])
    input_data['rest_type'] = le_rest_type.transform(input_data['rest_type'])
    input_data['cuisines'] = le_cuisines.transform(input_data['cuisines'])
    input_data['type'] = le_type.transform(input_data['type'])

    input_data['online_order'] = input_data['online_order'].map({'Yes': 1, 'No': 0})
    input_data['book_table'] = input_data['book_table'].map({'Yes': 1, 'No': 0})

    prediction = model.predict(input_data)

    return render_template('predictor.html', prediction=prediction[0],
                           online_order_values=online_order_values,
                           book_table_values=book_table_values,
                           location_values=location_values,
                           rest_type_values=rest_type_values,
                           approx_cost_values=approx_cost_values,
                           cuisines_values=cuisines_values,
                           type_values=type_values)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
