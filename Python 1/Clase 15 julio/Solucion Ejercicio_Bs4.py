import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
from urllib.request import urlopen

#Este es un pequeño ejemplo de como pudo ser elaborado el problema aplicando lo 
#Aprendio en clase

def getData(url):
  return requests.get(url)

class Publicaciones(ABC):

  def __init__(self, name, description, identify, category, url):
      self.__name = name
      self.__description = description
      self.__identify = identify
      self.__category = category
      self.url = url

  @abstractmethod
  def save_method_search(self):
      file = open("file_search.txt","w")
      file.write('Lista De Url Validas')
      file.write("\n" + self.url)
      file.close()

  def save_bs4_elements(self,elements):
    print("Guardando...")
    file = open("Elementos_recuperados.txt","w")
    file.write("\n" + self.url + " " + str(element))
    file.close()
    print("Guardado")

class Promociones(Publicaciones):
  def __init__(self, name, description, identify, category, url):
    super().__init__(name, description, identify, category, url)

  @property
  def save_method_search(self):
    print("Guardando...")
    super().save_method_search()
    print("Guardado")

  def read_method_file(self):
      file = open("file_search.txt","r")
      print(file.read())
      file.close()

   

def getInfo(self):
   return self.url
   
search = str(input('Valor a buscar: '))
url = 'http://alicorp-staging.phantasia.pe/search/pe/es/'+search+'/all'
response = getData(url)

if response.status_code == 200:
 results = response.json()
 jsons = results[1]
 for json in jsons:
    promo = Promociones(json['name'], json['description'], json['identify'], json['category'],json['url'])
    url = 'http://alicorp-staging.phantasia.pe/' + json['url']
    response = getData(url)
    if response.status_code == 200:
        try:
          promo.save_method_search()
        except:
          print ('Error code')
        print(url)
        url = urlopen(url)
        soup = BeautifulSoup(url, 'html5lib')
        element = soup.findAll("div", {"class": "img-banner-lg"})
        try:
          if element != None:
            promo.save_bs4_elements(element)
        except:
          print ('Error code')

        isTrue = True
        while isTrue:
            try: 
              isTrue = bool(int(input("Visualizar resultados? 1 : si - 0 : no : ")))
              print(isTrue)
              if isTrue == True:
                promo.read_method_file()
            except:
              print("Ingrese dato correcto")
    else:
        print('Status error %s.' % response.status_code)
    
else:
 print ('Error code')


