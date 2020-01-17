from math import* #importa funções matemáticas
import math

import datetime #importa funções de hora
hora_exata = datetime.datetime.now() #assim que roda o código, pega a hora

print ("Digite o nome do arquivo: ")
nome=input() 

nomecompleto = nome + '.dat' #junção de string para ler o nome do escrita
leitura = open(nomecompleto, 'r')
 
#ler as entradas do escrita
figs = int(leitura.readline()) #le a quantidade de figura
pontos = 0
arestas=[]

#um embaixo do outro
for i in range(figs): #loop para ler a quantidade de pontos de cada figura
	auxcontorno = int(leitura.readline()) #le os pontos 
	arestas.append(auxcontorno) #adiciona a quantidade de ponto no vetor
	pontos = pontos + auxcontorno #soma total de pontas

cord_px=[]
cord_py=[]

for i in range(pontos):
	cordx, cordy = map(float, leitura.readline().split()) #le na mesma linha identificando os espaços em brancos
	cord_px.append(cordx) 
	cord_py.append(cordy)

uni = leitura.readline() #le a unidade

#fim da leitura do arquivo

saida = nome + '.out' #criar arquivo .out
escrita = open(saida,'w')#abrir para escrever no escrita
#escrita.write escreve no arquivo .out
escrita.write("**** PROPRIEDADES GEOMÉTRICAS DAS FIGURAS PLANAS ****")
escrita.write ("\n")
escrita.write("		Data do Processamento: ")
escrita.write(str(hora_exata.day))
escrita.write("/")
escrita.write(str(hora_exata.month))
escrita.write("/")
escrita.write(str(hora_exata.year))
escrita.write(" ")
escrita.write(str(hora_exata.hour))
escrita.write(":")
escrita.write(str(hora_exata.minute))
escrita.write(":")
escrita.write(str(hora_exata.second))
escrita.write ("\n")
escrita.write ("\n")
escrita.write("	Número de contorno na figura:		")
escrita.write(str(figs))
escrita.write("\n")
escrita.write("	Número Total de Vértices:		")
escrita.write(str(pontos))
escrita.write("\n")
escrita.write('\n')
##AREA E PERIMETRO
i=0 #percorre as figuras
j=0 #percorre as arestas de cada figura
k=0 #percorre todos os pontos
auxcontorno=0 #auxcontorno identifica quando a figura estiver na ultimo ponto para poder fechar com o primeiro ponto
inicio=0 #inicio armazena a posição inicial da figura
area=[] #vetor area
tarea=0.0 #total area
perimetro=[] #vetor perimetro
tperimetro=0.0 #total perimetro
area.append(0.0) #inicia vetor area
perimetro.append(0.0) #inicia vetor perimetro
sperimetro=0.0 #somatorio para somar a equação do perimetro
sarea=0.0 #somatorio para somar a equação do area
#laço para fazer as equações
for i in range(figs): #laço para percorrer as figuras
	for j in range(arestas[i]): #laço para percorrer as arestas (vértices)
		if(auxcontorno==(arestas[i]-1)):##Identifica final da figura
			sperimetro+=sqrt(((cord_px[inicio]-cord_px[k])**2)+((cord_py[inicio]-cord_py[k])**2))
			sarea+=cord_px[k]*cord_py[inicio]-cord_px[inicio]*cord_py[k]
		else:
			sperimetro+=sqrt(((cord_px[k+1]-cord_px[k])**2)+((cord_py[k+1]-cord_py[k])**2))
			sarea+=cord_px[k]*cord_py[k+1]-cord_px[k+1]*cord_py[k]
		k+=1
		auxcontorno+=1
	perimetro.append(sperimetro) ##armazena o soma perimetro no vetor perimetro
	area.append(sarea) ##msm coisa
	auxcontorno=0
	inicio=arestas[i]+inicio
	sarea=0
	sperimetro=0
for i in range(len(area)):#somar area,somar perimetro
	tarea+=area[i]
	tperimetro+=perimetro[i]
tarea*=0.5
escrita.write("A area da sua figura e: 		")
escrita.write("{:.6f}".format(tarea))
escrita.write(uni+"²") 
escrita.write('\n')	
escrita.write("O perimetro de sua figura e: 		")
escrita.write("{:.6f}".format(tperimetro))
escrita.write (uni) 
escrita.write('\n')

#cálculo centro de gravidade cord_px,cord_py
cgx=[]
tcgx=0.0
cgy=[]
tcgy=0.0
k=0
auxcontorno=0
inicio=0
cgx.append(0.0)
cgy.append(0.0)
somax=0
somay=0
for i in range(figs):
	for j in range(arestas[i]):
		if(auxcontorno==(arestas[i]-1)):
			somax+=((cord_px[k]+cord_px[inicio])*(cord_px[k]*cord_py[inicio]-cord_px[inicio]*cord_py[k]))
			somay+=((cord_py[k]+cord_py[inicio])*(cord_px[k]*cord_py[inicio]-cord_px[inicio]*cord_py[k]))
		else:
			somax+=((cord_px[k]+cord_px[k+1])*(cord_px[k]*cord_py[k+1]-cord_px[k+1]*cord_py[k]))
			somay+=((cord_py[k]+cord_py[k+1])*(cord_px[k]*cord_py[k+1]-cord_px[k+1]*cord_py[k]))
		k+=1
		auxcontorno+=1
	cgx.append(somax)
	cgy.append(somay)
	auxcontorno=0
	inicio+=arestas[i]
	somax=0
	somay=0

for i in range(len(cgx)):
	tcgx+=cgx[i]
	tcgy+=cgy[i]

tcgx/=(6*tarea)
tcgy/=(6*tarea)
escrita.write("Coordenada do CG no eixo x: 		")
escrita.write("{:.6f}".format(tcgx))
escrita.write (uni)
escrita.write('\n')
escrita.write("Coordenada do CG no eixo y: 		")
escrita.write("{:.6f}".format(tcgy))
escrita.write (uni)
escrita.write('\n')
escrita.write('\n')

#momento inercia
for i in range(pontos): #atualiza as coordenadas subtraindo os centros de gravidades
	cord_px[i] = cord_px[i] - tcgx
	cord_py[i] = cord_py[i] - tcgy
inerciaX=[]
totalinerciaX=0.0
inerciaY=[]
totalinerciaY=0.0
produtoinercia=[]
totalprodutoinercia=0.0
a=[]
k=0
auxcontorno=0
inicio=0
inerciaX.append(0.0)
inerciaY.append(0.0)
produtoinercia.append(0.0)
somaix=0
somaiy=0
somaixy=0
ax=0
for i in range(figs):
	for j in range(arestas[i]):
		
		if(auxcontorno==(arestas[i]-1)):
			ax=((cord_px[k]*cord_py[inicio])-(cord_px[inicio]*cord_py[k]))
			a.append(ax)
			somaix+=a[k]*(pow(cord_py[k],2)+cord_py[k]*cord_py[inicio]+pow(cord_py[inicio],2))
			somaiy+=a[k]*(pow(cord_px[k],2)+cord_px[k]*cord_px[inicio]+pow(cord_px[inicio],2))
			somaixy+=a[k]*(cord_px[inicio]*cord_py[inicio]+2*cord_px[k]*cord_py[k]+2*cord_px[inicio]*cord_py[inicio]+cord_px[k]*cord_py[k])
		else:
			ax=((cord_px[k]*cord_py[k+1])-(cord_px[k+1]*cord_py[k]))
			a.append(ax)
			somaix+=a[k]*(pow(cord_py[k],2)+cord_py[k]*cord_py[k+1]+pow(cord_py[k+1],2))
			somaiy+=a[k]*(pow(cord_px[k],2)+cord_px[k]*cord_px[k+1]+pow(cord_px[k+1],2))
			somaixy+=a[k]*(cord_px[k+1]*cord_py[k+1]+2*cord_px[k]*cord_py[k]+2*cord_px[k+1]*cord_py[k+1]+cord_px[k]*cord_py[k])
		k+=1
		auxcontorno+=1
	auxcontorno=0
	inicio=arestas[i]+inicio
	inerciaX.append(somaix)
	inerciaY.append(somaiy)
	produtoinercia.append(somaixy)
	somaix=0
	somaiy=0
	somaixy=0
		
for i in range(len(inerciaX)):
	totalinerciaX+=inerciaX[i]
	totalinerciaY+=inerciaY[i]
	totalprodutoinercia+=produtoinercia[i]

totalinerciaX = totalinerciaX/12
totalinerciaY = totalinerciaY/12
totalprodutoinercia = totalprodutoinercia/24
momentoinercia = totalinerciaY + totalinerciaX

escrita.write("Momento de inercia em Ix: 		")
escrita.write("{:.6f}".format(totalinerciaX))
escrita.write (uni+'4')
escrita.write('\n')
escrita.write("Momento de inercia em Iy: 		")
escrita.write("{:.6f}".format(totalinerciaY))
escrita.write (uni+'4')
escrita.write('\n')
escrita.write("Produto de inercia em Ixy: 		")
escrita.write("{:.6f}".format(totalprodutoinercia))
escrita.write (uni+'4')
escrita.write('\n')
escrita.write("Momento Polar de Inercia: 		")
escrita.write("{:.6f}".format(momentoinercia))
escrita.write (uni+'4')
escrita.write('\n')
escrita.write('\n')


#inicio das equações sem precisar usar o laço (for)

inerciamax = (totalinerciaX+totalinerciaY)/2 + sqrt(((totalinerciaX-totalinerciaY)/2)**2+(totalprodutoinercia**2))

inerciamin = (totalinerciaX+totalinerciaY)/2 - sqrt(((totalinerciaX-totalinerciaY)/2)**2+totalprodutoinercia**2)


escrita.write("Momento Inercia Min de sua figura é: 	")
escrita.write("{:.6f}".format(inerciamin))
escrita.write (uni+'4')
escrita.write('\n')
escrita.write("Momento Inercia Max de sua figura é: 	")
escrita.write("{:.6f}".format(inerciamax))
escrita.write (uni+'4')
escrita.write('\n')
escrita.write('\n')


teta1 = (math.atan(-totalprodutoinercia/((totalinerciaX-totalinerciaY)/2)))/2 #math.atan arco tangente 
teta1 = teta1*180/math.pi #math.pi numero de pi

teta2 = teta1 + 90

escrita.write("O Teta1 de sua figura é:		")
escrita.write("{:.6f}".format(teta1))
escrita.write("º")
escrita.write('\n')
escrita.write("O Teta2 de sua figura é:		")
escrita.write("{:.6f}".format(teta2))
escrita.write("º")
escrita.write('\n')

raiomin = sqrt(inerciamin/tarea)
raiomax = sqrt(inerciamax/tarea)

escrita.write("O Raio de Giracao Min de sua figura: 	")
escrita.write("{:.6f}".format(raiomin))
escrita.write (uni)
escrita.write('\n')
escrita.write("O Raio de Giracao Max de sua figura: 	")
escrita.write("{:.6f}".format(raiomax))
escrita.write (uni)
escrita.write('\n')
escrita.close()

print ("Arquivo salvo.")
