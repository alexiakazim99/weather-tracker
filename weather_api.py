import requests 
#Hämtar ett verktyg/biblioteket 
# requests låter dig prata med internet (api) anrop
def get_weather (city)
    api_key = "67ca9a0af0e84854903142852252911"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

# skapat en funktion med namnet get_weather 
# (city) = funktionen tar emot en paramenter (stadens namn)
# api_key = din personliga nyckel 
# url = adressen till Api:et 
# f-string =  låter dig sätta in variabler inuti texten
#{api_key} = sätter in din nyckel i URL:en
#{city} = sätter in staden ("Stockholm")



