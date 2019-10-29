from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html")


@app.route('/alarm-clock')
def get_page_alarm_clock():
    return render_template("alarm-clock.html", title='Alarm clock', data=get_data())


@app.route('/headphones')
def get_page_headphones():
    return render_template("headphones.html", title='Headphones', data=get_data())


@app.route('/ipod')
def get_page_ipod():
    return render_template("ipod.html", title='iPod', data=get_data())


@app.route('/calculator')
def get_page_calculator():
    return render_template("calculator.html", title='Calculator', data=get_data())


@app.route('/coffeemaker')
def get_page_coffeemaker():
    return render_template("coffeemaker.html", title='Coffeemaker', data=get_data())


@app.route('/battery-charger')
def get_page_battery_charger():
    return render_template("battery-charger.html", title='Battery charger', data=get_data())


@app.route('/author')
def get_page_author():
    return render_template("author.html", title='Author')


if __name__ == "__main__":
    app.run(debug=True)
