import sqlite3


def init_db():
    try: 
       
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                temperature REAL NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        print(" Database initalized")
        
    except sqlite3.Error as e:
        print(f" Database initialization error: {e}")


def save_weather (city, temperature, date):
    try:
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor() 
        cursor.execute('''
            INSERT INTO weather (city, temperature, date)
             VALUES (?, ?, ?)
         ''', (city, temperature, date))

        conn.commit()
        conn.close() 
        print(f" Saved weather for {city}: {temperature}°C")
        return True

    except sqlite3.Error as e:
        print(f" Error while saving: {e}")  
        return False
 
  
 
def get_all_weather(): 
    try: 
        conn = sqlite3.connect ('weather.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM weather')
        rows = cursor.fetchall()
        conn.close()
        print (f"retrieved {len(rows)} rows from database") 
    
        return rows 
    except sqlite3.Error as e: 
       print (f" Error while saving: {e}")
       return []
   
  

if __name__ == "__main__":
    init_db() 
    print("Database initialized") 