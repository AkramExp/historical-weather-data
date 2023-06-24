from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data/stations.txt", skiprows=17)


@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def one_data(station, date):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df = df.loc[df['    DATE'] == date]
    df['   TG'] = df['   TG'] / 10
    return render_template("page1.html", data=df.to_html(), station=station, date=date)


@app.route("/api/v1/<station>")
def one_station(station):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df['   TG'] = df['   TG'] / 10
    return render_template("page2.html", data=df.to_html(), station=station)


@app.route("/api/v1/<station>/yearly/<year>")
def one_year(station, year):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    df = df[df["    DATE"].str.startswith(str(year))]
    df['   TG'] = df['   TG'] / 10
    return render_template("page3.html", data=df.to_html(), year=year)


if __name__ == '__main__':
    app.run(debug=True)
