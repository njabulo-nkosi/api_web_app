from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from api_data_manager import APIDataManager
from dotenv import load_dotenv
import datetime
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
Bootstrap5(app)
api_data_manager = APIDataManager()


@app.route('/')
def homepage():
    current_year = datetime.datetime.now().year

    title, explanation, media_type, image_url = api_data_manager.get_picture_of_the_day()

    return render_template('index.html', title=title, explanation=explanation,
                           media_type=media_type, image_url=image_url, current_year=current_year)


@app.route('/about')
def about():
    current_year = datetime.datetime.now().year
    return render_template('about.html', current_year=current_year)


@app.route('/picture-of-the-day')
def show_picture_of_the_day():
    current_year = datetime.datetime.now().year

    title, explanation, media_type, image_url = api_data_manager.get_picture_of_the_day()

    return render_template('display_picture.html', title=title, explanation=explanation,
                           media_type=media_type, image_url=image_url, current_year=current_year)


@app.route('/mars-weather')
def get_mars_weather():
    current_year = datetime.datetime.now().year

    average_temp, min_temp, max_temp, first_utc_date_collection = api_data_manager.get_mars_weather()

    return render_template('mars_weather.html', average_temp=average_temp,
                           min_temp=min_temp, max_temp=max_temp,
                           first_utc_date=first_utc_date_collection, current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
