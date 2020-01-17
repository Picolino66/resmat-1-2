from math import* #importa funções matemáticas
import math

print ("Digite o nome do arquivo: ")
nome=input() 

nomecompleto = nome + '.dat' #junção de string para ler o nome do escrita
leitura = open(nomecompleto, 'r') #abrir escrita para leitura

#ler as entradas do escrita
figs = int(leitura.readline())
pontos = 0
arestas=[]
#um embaixo do outro
for i in range(figs):
	auxcontorno = int(leitura.readline())
	arestas.append(auxcontorno)
	pontos = pontos + auxcontorno

cord_px=[]
cord_py=[]

for i in range(pontos):
	cordx, cordy = map(float, leitura.readline().split())
	cord_px.append(cordx)
	cord_py.append(cordy)

uni = leitura.readline()

saida = nome + '.out' #criar arquivo .out
escrita = open(saida,'w')#abrir para escrever no escrita
#escrita.write escreve no arquivo .out
escrita.write("**** PROPRIEDADES GEOMÉTRICAS DAS FIGURAS PLANAS ****")
escrita.write ("\n")
escrita.write("Número de Contorno na Figura: ")
escrita.write(str(figs))
escrita.write('\n')
escrita.write("Total de Vertices: ")
escrita.write(str(pontos))
escrita.write('\n')

##AREA E PERIMETRO
tam=pontos+1
i=0
j=0
k=0
auxcontorno=0 #auxcontorno identifica quando a figura estiver na ultimo ponto para poder fechar com o primeiro ponto
inicio=0 #inicio armazena a posição inicial da figura
area=[]
tarea=0.0
perimetro=[]
tperimetro=0.0
area.append(0.0)
perimetro.append(0.0)
sperimetro=0.0
sarea=0.0
#laço para fazer as equações
for i in range(figs):
	for j in range(arestas[i]):
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
escrita.write("O perimetro de sua figura e: ")
escrita.write("{:.6f}".format(tperimetro))
escrita.write (uni) 
escrita.write('\n')
escrita.write("A area da sua figura e: ")
escrita.write("{:.6f}".format(tarea))
escrita.write(uni+"²") 
escrita.write('\n')

#cacluco centro de gravidade cord_px,cord_py
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
escrita.write("Coordenada do CG no eixo cord_px: ")
escrita.write("{:.6f}".format(tcgx))
escrita.write (uni)
escrita.write('\n')
escrita.write("Coordenada do CG no eixo cord_py: ")
escrita.write("{:.6f}".format(tcgy))
escrita.write (uni)
escrita.write('\n')


#momento inercia
for i in range(pontos):
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

escrita.write("Momento de inercia em cord_px: ")
escrita.write("{:.6f}".format(totalinerciaX))
escrita.write (uni+'4')
escrita.write('\n')
escrita.write("Momento de inercia em cord_py: ")
escrita.write("{:.6f}".format(totalinerciaY))
escrita.write (uni+'4')
escrita.write('\n')
escrita.write("Produto de inercia em xy: ")
escrita.write("{:.6f}".format(totalprodutoinercia))
escrita.write (uni+'4')
escrita.write('\n')
escrita.write("Momento Polar de Inercia: ")
escrita.write("{:.6f}".format(momentoinercia))
escrita.write (uni+'4')
escrita.write('\n')


inerciamax = (totalinerciaX+totalinerciaY)/2 + sqrt(((totalinerciaX-totalinerciaY)/2)**2+(totalprodutoinercia**2))

inerciamin = (totalinerciaX+totalinerciaY)/2 - sqrt(((totalinerciaX-totalinerciaY)/2)**2+totalprodutoinercia**2)

escrita.write("O inerciamax de sua figura é: ")
escrita.write("{:.6f}".format(inerciamax))
escrita.write (uni+'4')
escrita.write('\n')
escrita.write("O inerciamin de sua figura é: ")
escrita.write("{:.6f}".format(inerciamin))
escrita.write (uni+'4')
escrita.write('\n')

teta1 = (math.atan(-totalprodutoinercia/((totalinerciaX-totalinerciaY)/2)))/2
teta1 = teta1*180/math.pi

teta2 = teta1 + 90

escrita.write("O Tetap1 de sua figura é: ")
escrita.write("{:.6f}".format(teta1))
escrita.write("º")
escrita.write('\n')
escrita.write("O Tetap2 de sua figura é: ")
escrita.write("{:.6f}".format(teta2))
escrita.write("º")
escrita.write('\n')

raiomin = sqrt(inerciamin /tarea)
raiomax = sqrt(inerciamax/tarea)
	
escrita.write("O raiomin de sua figura: ")
escrita.write("{:.6f}".format(raiomin))
escrita.write (uni)
escrita.write('\n')
escrita.write("O raiomax de sua figura: ")
escrita.write("{:.6f}".format(raiomax))
escrita.write (uni)
escrita.write('\n')
escrita.close()

print ("Arquivo salvo.")
