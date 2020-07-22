
#Retirado e adaptado do livro Foundations of network python programming
#Salvar como location.py para poder funcionar
#Se salvar com outro nome esse nome deve ser colocado na linha 11 na variável user_agent

from geopy.geocoders import Nominatim

#Informe um logradouro e recebe a latitude e longitude aproximada
if __name__ == '__main__':
    #address = 'Rua Poti Fortaleza Ceará'
    address = input("Digite logradouro, cidade e estado para obter a localização em latitude e longitude:\n")
    user_agent = 'location.py'
    location = Nominatim(user_agent=user_agent).geocode(address)
    print(location.latitude, location.longitude)
