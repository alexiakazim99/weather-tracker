import requests 
#Hämtar ett verktyg/biblioteket 
# requests låter dig prata med internet (api) anrop
def get_weather (city): #funktion 
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

#kontollerar ett vilkor och kör kod endast om vilkoret stämmer 
if response.status_code == 200:  #kontrollerar serves svar om allt är ok
    data = response.json () # konverterar servers svar från json till dic, sparar variabeln till data 
    temperature = data ['current']['temp_c'] # hämtar temperaturen i data 
    city_name = data['location']['name'] # hämtar stad namnet från data 

    from datetime import datetime # får dagens datum och tid 
    date = datetime.now().strftime("%Y-%m-%d") # sparar i data 
        