# Historical Weather Data



## Description
It is used to retrieve the historical temperature data of european stations over many years for a particular date.
I made it using **Python, Flask and Pandas**. 

Flask to connect with web pages and Pandas to retrieve data from csv files.

It can be build in a **Docker Image** with the Dockerfile in the repo.
- It has 3 formats of url
- Shows data in tabular format
- With the help of Pandas it makes easy to filter out the data and use it when comes to manupulating huge amount of data.


## Run Locally

Install Dependencies

```bash
  pip install --no-cache-dir -r requirements.txt
```

Run with python command

```bash
  python main.py
```
### Run with Docker
Build Docker Image
```bash
    docker build -t hist-data:1.0 .
```
Run Image
```bash
    docker run -p 5000:5000 hist-data:1.0
```
## Screenshots

![Screenshot1](https://github.com/AkramExp/historical-weather-data/blob/main/screenshots/Screenshot1.png)

![Screenshot2](https://github.com/AkramExp/historical-weather-data/blob/main/screenshots/Screenshot2.png)

![Screenshot3](https://github.com/AkramExp/historical-weather-data/blob/main/screenshots/Screenshot3.png)
