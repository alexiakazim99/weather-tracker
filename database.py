import sqlite3
# databasmotror som ligger redan inbyggdd i python, gör det möjligt att jobba med databasen 

def init_db():
    try:
        # Anslut till databasen (skapar weather.db om den inte finns)
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        
        # Skapar tabell för väderdata
        # execute = man aktiverar cursor för användning 
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                temperature REAL NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        
        # Spara ändringarna
        conn.commit()
        conn.close()
        print(" Database initalized")
        
    except sqlite3.Error as e:
        print(f" Database initialization error: {e}")


def save_weather (city, temperature, date):
    try: 
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
         #sparar det jag har skrivit 
        conn.close() 
        # stäng dörren 
        print(f" Saved weather for {city}: {temperature}°C")
        return True

    except sqlite3.Error as e:
        print(f" Error while saving: {e}")
        return False

 
def get_all_wather(): 
    try:
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
        print (f"retrieved {len(rows)} rows from database") 
    #retunerar data 
        return rows 
    except sqlite3.Error as e: 
       print (f" Error while saving: {e}")
       return []
  