from lxml import html
from selenium import webdriver
import numpy
import warnings
warnings.filterwarnings("ignore") #Remover Deprecated alert do PhantomJS

name = input('Nome do invocador: ')
region = input('Servidor: ')
pagina = ("https://teemo.gg/player/active/"+region+"/"+name)
browser = webdriver.PhantomJS() #Define o navegador utilizado
browser.get(pagina)	#Baixa a pagina
page = browser.page_source #Adquire o source da pagina
tree = html.fromstring(page) #Transforma a pagina baixada em unit bytes

wins = tree.xpath('//span[@class="tm green"]/text()') #Procura toda tag span e extrai texto
#print('Vitorias: ',wins)

loses = tree.xpath('//span[@class="tm red"]/text()') #Procura toda tag span e extrai texto
#print('Derrotas: ',loses)

player = tree.xpath('//div[@class="summoner"]/a/text()') #Procura a div summoner e extrai texto do hyperlink
#print('Players: ',player)

champ = tree.xpath('//div[@class="champion champion-44x44"]/img/@alt') #Extrai texto alt da tag img
#print('Champions: ',champ)

winrate = numpy.zeros(10) #Completa a array com zeros
i=0
while (i<10):
	if (i<1):
		print("")
		print("Time Azul:")
		print("")
	elif (i==5):
		print("")
		print("Time Vermelho:")
		print("")
	try:
		winrate[i] = int((int(wins[i])/( int(loses[i])+int(wins[i]) ))*100) #Faz calculo do winrate, sendo: (Vitorias/Total de partidas)*100

	except ZeroDivisionError: #Caso não tenha partidas ranqueadas retorna 0%
		winrate[i] = 0
		
	print(champ[i],"/",player[i],":",winrate[i],"%")
	i=i+1
end = input()