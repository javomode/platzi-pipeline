import requests

url = "https://api.escuelajs.co/api/v1/products"

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to retrieve data"}
    

