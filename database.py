import sqlite3
# databasmotror som ligger redan inbyggdd i python, gör det möjligt att skriva sql kommandon i terminalen 

def init_db():
    try: # försöker köra koden 
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
        
     #fångar alla SQLlite- relaterade fel, "e" innehåller felmedelandet
    except sqlite3.Error as e:
        print(f" Database initialization error: {e}")


def save_weather (city, temperature, date):
    try: #försöker köra datan
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
        print(f" Error while saving: {e}")  # print - visar output 
        return False
 
    # return true/false = retunerar om det gick bra eller ej 
 
def get_all_weather(): 
    try: #försöker köra datan 
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
    # return [] = retunerar tom lista om fel uppstår 
    # förhindrar att programmet krachar 
  

if __name__ == "__main__": # kontrollerar om denna fil körs dirket (inte importerad från annan fil)
    init_db() # funktionen skapar databasen och tabellen 
    print("Database initialized") # skriver uti terminalen 