import requests 
from datetime import datetime
#Hämtar ett verktyg/biblioteket 
# requests låter dig prata med internet (api) anrop
def get_weather (city): #funktion för att hämta 1 stad 
    api_key = "67ca9a0af0e84854903142852252911" # variabel #string 
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}" ""  

    response = requests.get(url)

# skapat en funktion med namnet get_weather 
# (city) = funktionen tar emot en paramenter (stadens namn)
# api_key = din personliga nyckel 
# url = adressen till Api:et  #variabel som lagrar värde
# f-string =  låter dig sätta in variabler inuti texten # string som innehåller variabel 
#{api_key} = sätter in din nyckel i URL:en
#{city} = sätter in staden ("Stockholm")
# response = skickar förfrågan till Api genom get - request  och får tillbaka svar i response  

    try: ## Försök köra denna kod
        response = requests.get(url)  # Skicka GET-request till WeatherAPI
        
        if response.status_code == 200: # Om serverns svar är OK (200)
            data = response.json() # Konvertera JSON till dictionary
            temperature = data['current']['temp_c'] #hämtar tempratur
            city_name = data['location']['name'] # hämtar stad 
            date = datetime.now().strftime("%Y-%m-%d") #hämtar dagens datum
            
            return temperature, city_name, date # retunerar alla tre värden 
        
        else: # om status ej är 200 
            print(f"Error: Invalid response status {response.status_code}") # skriv fel medelande 
            return None # retunerar inget 
    
    except Exception as e: # om något går fel i try - blocket
        print(f"Error fetching weather data: {e}") # skriv fel meddelande 
        return None # retunerar inget 

def fetch_multiple_cities(cities_list): # funktion för alla städer
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