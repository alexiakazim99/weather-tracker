import requests 
from datetime import datetime 
from database import save_weather

def get_weather (city):
    api_key = "67ca9a0af0e84854903142852252911" 
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}" ""  

    response = requests.get(url)

    try:
        response = requests.get(url)
        
        if response.status_code == 200: 
            data = response.json() 
            temperature = data['current']['temp_c'] 
            city_name =  data['location']['name'] 
            date = datetime.now().strftime("%Y-%m-%d")
            save_weather (city_name, temperature, date) 
            
            return temperature, city_name, date
        
        else: 
            print(f"Error: Invalid response status {response.status_code}") 
            return None 
    
    except Exception as e: 
        print(f"Error fetching weather data: {e}") 
        return None

def fetch_multiple_cities(cities_list): 
    try:
        all_weather = [] 
        
        for city in cities_list: 
            result = get_weather(city)  
            if result: 
                all_weather.append(result) 
        
        return all_weather 
    
    except Exception as e: 
        print(f"Error fetching multiple cities: {e}")
        return [] 
    

if __name__ == "__main__":  
    result = get_weather("Stockholm")
    print (result)

    cities = ["Stockholm", "Göteborg", "Malmö"]
    results = fetch_multiple_cities(cities)
    print(results)