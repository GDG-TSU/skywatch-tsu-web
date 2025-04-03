from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__, template_folder='templates')

@app.route('/', methods = ['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        api_key = '7----1'
        data = get_weather(city, state, country)
        return render_template('index.html', weather_data=weather_data)
    return render_template('index.html')


    if __name__ == '__main__':
        app.run(debug=True)
