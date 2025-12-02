import sqlite3
# databasmotror som ligger redan inbyggdd i python 

def init_db()
    connection = sqlite3.connect("weather.db")
    # öppna en koppling till en databasfil som  då heter (weather.db)
    cursor = connection.cursor()
    