
from Flask import Flask, render_template , requests
from weather import get_weather_data
app = Flask(__name__,template_folder = 'templates' )

@app.route('/', methods = ['GET', 'POST'])
def index():
    data = None
    if requests.method == 'POST':
        city = requests.form['cityName']
        state = requests.form['stateName']
        country = requests.form['countryName']
        data = get_weather_data(city, state, country)

    return render_template('index.html', weather = data)

if __name__ == '__main__' :
    app.run(debug = True)