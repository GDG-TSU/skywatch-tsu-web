from flask import Flask, render_template, request, flash
from weather import main as get_weather

app = Flask(__name__, template_folder='templates')
app.secret_key = 'skywatch_secret_key'  # Add a secret key for flash messages

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        
        # Check if the user provided the required information
        if not city or not country:
            flash("Please enter at least city and country", "error")
            return render_template('index.html', weather=None)
            
        data = get_weather(city, state, country)
        
        # Check if weather data was successfully fetched
        if data is None:
            flash("Couldn't fetch weather data. Please check your location details and try again.", "error")
            
    return render_template('index.html', weather=data)

if __name__ == '__main__':
    app.run(debug=True)