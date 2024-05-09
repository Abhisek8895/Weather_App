from flask import Flask,render_template,request
from get_data import get_info

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    city = "Bhubaneswar"
    if request.method == 'POST':
        city = request.form.get('location')
        data = get_info(city)
        weather ={
            'name' :city,
            'temp' : data[0],
            'desc' : data[1],
            'date' : data[2],
            'time' : data[3],
            'day'  : data[4],
            'pressure' : data[5],
            'humidity' : data[6],
            'wind' : data[7],
            'cloud' : data[8],
            'icon' : data[9] 
        }
        weather_icon = weather['icon']
        weather_icon_url = f"http://openweathermap.org/img/wn/{weather_icon}.png"
        return render_template("index.html", weather = weather, weather_icon_url = weather_icon_url)
        # return render_template("index.html")
    else:
        data = get_info(city)
        weather ={
            'name' :city,
            'temp' : data[0],
            'desc' : data[1],
            'date' : data[2],
            'time' : data[3],
            'day'  : data[4],
            'pressure' : data[5],
            'humidity' : data[6],
            'wind' : data[7],
            'cloud' : data[8],
            'icon' : data[9] 
        }
        weather_icon = weather['icon']
        weather_icon_url = f"http://openweathermap.org/img/wn/{weather_icon}.png"
        return render_template("index.html", weather = weather, weather_icon_url = weather_icon_url)
    # return render_template("index.html")
# @app.route("/get_data")
# def get_data():


app.run(debug=True)