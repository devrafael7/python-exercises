import requests
from config import API_KEY

def get_city(city):
    
    if not city:
        print("Cidade invlida")
        return

    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br&units=metric"
    requisition = requests.get(link)
    
    if requisition.status_code == 200:
        requisition_dic = requisition.json()
        
        sky_description = requisition_dic['weather'][0]['description']
        temp = requisition_dic['main']['temp']
        
        print(sky_description)
        print(f"Temperatura: {temp:.2f}°C")
    else:
        print(f"Erro: {requisition.status_code}")

get_city("Rio de Janeiro")