import requests 
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
response = requests.get(url)
texto = response.text
soup = BeautifulSoup(texto, 'html.parser')

preguntas = soup.select('.question-summary')
print(preguntas[0])

for pregunta in preguntas:
  titulo = pregunta.select_one('.question-hyperlink').getText()