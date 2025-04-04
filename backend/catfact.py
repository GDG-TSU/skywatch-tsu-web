import requests

def get_joke():
    url = 'https://v2.jokeapi.dev/joke/Any?type=single'
    response = requests.get(url)
    data = response.json()
    
   
    return data 
print(get_joke())