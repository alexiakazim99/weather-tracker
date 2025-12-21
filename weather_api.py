import requests 
from datetime import datetime # en modul for time and date
from database import save_weather # hämtar från filen bd, hämtar funktioneen från save_weather 
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
            save_weather (city_name, temperature, date) # sparar väder i databsen
            
            return temperature, city_name, date # retunerar alla tre värden 
        
        else: # om status ej är 200 
            print(f"Error: Invalid response status {response.status_code}") # skriv fel medelande 
            return None # retunerar inget 
    
    except Exception as e: # om något går fel i try - blocket
        print(f"Error fetching weather data: {e}") # skriv fel meddelande 
        return None # retunerar inget 

def fetch_multiple_cities(cities_list): # funktion för alla städer (lista)
    try:
        all_weather = [] # tom lista för att samla alla resultat 
        
        for city in cities_list: # loopa genom varje stad 
            result = get_weather(city)  # anropar get_weather (sparar automatiskt)
            if result: # om det går bra 
                all_weather.append(result) # lägg till i listan 
        
        return all_weather #retunerar alla värden - restultat 
    
    except Exception as e: # fångar felet #errorhantering
        print(f"Error fetching multiple cities: {e}") #visar vad felet är 
        return [] #retuneratr en tom lista, istället för att kracha 
    

# Error hanterining i funktionerna: 
# get weather hämtar data för en stad, om de misslyckas så får vi None
# fetch multipe citys hämtar väder för många städer, om de misslyckas så får vi en  tom lista
#skillnaden är då att fetch skapar en lista och därför vill vi retunera en lista 


if __name__ == "__main__": 
    result = get_weather("Stockholm")
    print (result)

    cities = ["Stockholm", "Göteborg", "Malmö"]
    results = fetch_multiple_cities(cities)
    print(results)