import os
import json
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")

connection = psycopg2.connect(url)

@app.route("/", methods=['GET'])
def get_all_cars():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("Select * From Cars;")
            cars = cursor.fetchall()
    # with connection:
    #     with connection.cursor() as cursor:
    #         cursor.execute("Select taxi_name, tarif_name, price from taxi, Сhoice, cars where cars.car_id = 1 AND taxi.taxi_id = Сhoice.tarif_id AND Cars.car_id = Сhoice.car_id;")
    #         cars = cursor.fetchall()
    return render_template('index.html', cars=cars)

@app.route("/api/car/<int:n>", methods=['GET'])
def get_info_taxi(n):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('Select taxi_name, tarif_name, price from taxi, Сhoice, cars where cars.car_id = {0} AND taxi.taxi_id = Сhoice.tarif_id AND Cars.car_id = Сhoice.car_id;'.format(n))
            data = cursor.fetchall()
    

    return render_template('data.html', data=data)
