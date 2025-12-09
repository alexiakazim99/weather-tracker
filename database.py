import sqlite3
# databasmotror som ligger redan inbyggdd i python, gör det möjligt att jobba med databasen 

def init_db()
    connection = sqlite3.connect("weather.db")
    # öppna en koppling till en databasfil som  då heter (weather.db)
    cursor = connection.cursor()
    # gör det möjligt att skriva sql här 

crete table if not exist weather (
    id integer primary key autoincrement, 
    city text not null, 
    temperatur real not null, 
    data text not null 
)

def save_weather (city, temperature, date):
    #funktion tar emot 3 parametrar (city, temprature, date)
    conn = sqlite3.connect('weather.db')
    #skapar en anslutning till databasfilen (wather.db)
    cursor = conn.cursor() 

    cursor.execute('''
        INSERT INTO weather (city, temperature, date)
        VALUES (?, ?, ?)
    ''', (city, temperature, date))
    # använder verktyget för att kunna skriva commits 

    conn.commit()
    #sparar det jag ahr skrivit 
    conn.close() 
    # stäng dörren 

def get_all_wather(): 
   #ansluter till databasen 
    conn = sqlite3.connect ('weather.db')
    cursor = conn.cursor()

    # hämtar all värder data från taballen 
    cursor.execute('SELECT * FROM weather')
    #hämtar alla rader från en lista 
    rows = cursor.fetchall()
    #stäng anslutning 
    conn.close()
    #retunerar datan 
    return rows 

