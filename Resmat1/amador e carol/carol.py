from math import* #importa funções matemáticas
import math

print ("Digite o nome do arquivo: ")
nome_arq=input() 

arquivo = nome_arq + '.dat' #junção de string para ler o nome_arq do escrita
carregar = open(arquivo, 'r') #abrir escrita para carregar

#ler as entradas do escrita
figuras = int(carregar.readline())
arestas = 0
arestas_fig=[]
for i in range(figuras):
	aux = int(carregar.readline())
	arestas_fig.append(aux)
	arestas = arestas + arestas_fig[i]
ponto_x=[]
ponto_y=[]

for i in range(arestas):
	x, y = map(float, carregar.readline().split())
	ponto_x.append(x)
	ponto_y.append(y)
unidade = str(carregar.readline())
salvar = nome_arq + '.out'
escrita = open(salvar,'w')#abrir para escrever no escrita
escrita.write("Propriedades Geométricas da Figura")
escrita.write ("\n")
escrita.write(" NÚMERO DE CONTORNOS NA FIGURA: ") 
escrita.write(str(figuras))
escrita.write ("\n")
escrita.write(" NÚMERO TOTAL DE VÉRTICES: ") 
escrita.write(str(arestas))
escrita.write ("\n")
escrita.write ("\n")
i=0
j=0
percorre=0 #percorre a figura
fim=0 #fim identifica quando a figura estiver na ultimo ponto para poder fechar com o primeiro ponto
inicio=0 #inicio armazena a posição inicial da figura
area=[]
perimetro=[]
total_area=0.0
total_perimetro=0.0
area.append(0.0)
perimetro.append(0.0)
soma_area=0.0
soma_perimetro=0.0
#cacluco centro de gravidade ponto_x,ponto_y
centro_gravidade_x=[]
total_gravidade_x=0.0
centro_gravidade_y=[]
total_gravidade_y=0.0
centro_gravidade_x.append(0.0)
centro_gravidade_y.append(0.0)
soma_gravidade_x=0
soma_gravidade_y=0


#laço para fazer as equações
for i in range(figuras):
	for j in range(arestas_fig[i]):
		if(fim==(arestas_fig[i]-1)):
			soma_perimetro+=sqrt(((ponto_x[inicio]-ponto_x[percorre])**2)+((ponto_y[inicio]-ponto_y[percorre])**2))
			soma_area+=ponto_x[percorre]*ponto_y[inicio]-ponto_x[inicio]*ponto_y[percorre]
			soma_gravidade_x+=((ponto_x[percorre]+ponto_x[inicio])*(ponto_x[percorre]*ponto_y[inicio]-ponto_x[inicio]*ponto_y[percorre]))
			soma_gravidade_y+=((ponto_y[percorre]+ponto_y[inicio])*(ponto_x[percorre]*ponto_y[inicio]-ponto_x[inicio]*ponto_y[percorre]))
		else:
			soma_perimetro+=sqrt(((ponto_x[percorre+1]-ponto_x[percorre])**2)+((ponto_y[percorre+1]-ponto_y[percorre])**2))
			soma_area+=ponto_x[percorre]*ponto_y[percorre+1]-ponto_x[percorre+1]*ponto_y[percorre]
			soma_gravidade_x+=((ponto_x[percorre]+ponto_x[percorre+1])*(ponto_x[percorre]*ponto_y[percorre+1]-ponto_x[percorre+1]*ponto_y[percorre]))
			soma_gravidade_y+=((ponto_y[percorre]+ponto_y[percorre+1])*(ponto_x[percorre]*ponto_y[percorre+1]-ponto_x[percorre+1]*ponto_y[percorre]))
		percorre+=1
		fim+=1
	perimetro.append(soma_perimetro)
	area.append(soma_area)
	fim=0
	inicio=arestas_fig[i]+inicio
	soma_area=0
	soma_perimetro=0
	centro_gravidade_x.append(soma_gravidade_x)
	centro_gravidade_y.append(soma_gravidade_y)
	soma_gravidade_x=0
	soma_gravidade_y=0
for i in range(len(area)):#somar area,somar perimetro
	total_area+=area[i]
	total_perimetro+=perimetro[i]
	total_gravidade_x+=centro_gravidade_x[i]
	total_gravidade_y+=centro_gravidade_y[i]
total_area*=0.5
total_gravidade_x/=(6*total_area)
total_gravidade_y/=(6*total_area)

escrita.write("A area da sua figura e:						")
escrita.write("{:.6f}".format(total_area))
escrita.write(unidade+'² \n')
escrita.write("O perimetro de sua figura e:				")
escrita.write("{:.6f}".format(total_perimetro))
escrita.write(unidade+'\n')
escrita.write("Coordenada do CG no eixo ponto_x:			")
escrita.write("{:.6f}".format(total_gravidade_x))
escrita.write(unidade+' \n')
escrita.write("Coordenada do CG no eixo ponto_y:			")
escrita.write("{:.6f}".format(total_gravidade_y))
escrita.write(unidade+' \n')

#momento inercia

for i in range(arestas):
	ponto_x[i] = ponto_x[i] - total_gravidade_x
	ponto_y[i] = ponto_y[i] - total_gravidade_y
inerciaX=[]
totalinerciaX=0.0
inerciaY=[]
totalinerciaY=0.0
produtoinercia=[]
totalprodutoinercia=0.0
a=[]
percorre=0
fim=0
inicio=0
inerciaX.append(0.0)
inerciaY.append(0.0)
produtoinercia.append(0.0)
somaix=0
somaiy=0
somaixy=0
ax=0
for i in range(figuras):
	for j in range(arestas_fig[i]):
		
		if(fim==(arestas_fig[i]-1)):
			ax=((ponto_x[percorre]*ponto_y[inicio])-(ponto_x[inicio]*ponto_y[percorre]))
			a.append(ax)
			somaix+=a[percorre]*(pow(ponto_y[percorre],2)+ponto_y[percorre]*ponto_y[inicio]+pow(ponto_y[inicio],2))
			somaiy+=a[percorre]*(pow(ponto_x[percorre],2)+ponto_x[percorre]*ponto_x[inicio]+pow(ponto_x[inicio],2))
			somaixy+=a[percorre]*(ponto_x[percorre]*ponto_y[inicio]+2*ponto_x[percorre]*ponto_y[percorre]+2*ponto_x[inicio]*ponto_y[inicio]+ponto_x[inicio]*ponto_y[percorre])
		else:
			ax=((ponto_x[percorre]*ponto_y[percorre+1])-(ponto_x[percorre+1]*ponto_y[percorre]))
			a.append(ax)
			somaix+=a[percorre]*(pow(ponto_y[percorre],2)+ponto_y[percorre]*ponto_y[percorre+1]+pow(ponto_y[percorre+1],2))
			somaiy+=a[percorre]*(pow(ponto_x[percorre],2)+ponto_x[percorre]*ponto_x[percorre+1]+pow(ponto_x[percorre+1],2))
			somaixy+=a[percorre]*(ponto_x[percorre]*ponto_y[percorre+1]+2*ponto_x[percorre]*ponto_y[percorre]+2*ponto_x[percorre+1]*ponto_y[percorre+1]+ponto_x[percorre+1]*ponto_y[percorre])
		percorre+=1
		fim+=1
	fim=0
	inicio=arestas_fig[i]+inicio
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

escrita.write("Momento de inercia em ponto_x:				")
escrita.write("{:.6f}".format(totalinerciaX))
escrita.write(unidade+'4 \n')
escrita.write("Momento de inercia em ponto_y:				")
escrita.write("{:.6f}".format(totalinerciaY))
escrita.write(unidade+'4 \n')
escrita.write("Produto de inercia em xy:					")
escrita.write("{:.6f}".format(totalprodutoinercia))
escrita.write(unidade+'4 \n')
escrita.write("Momento Polar de Inercia:					")
escrita.write("{:.6f}".format(momentoinercia))
escrita.write(unidade+'4 \n')


inerciamax = (totalinerciaX+totalinerciaY)/2 + sqrt(((totalinerciaX-totalinerciaY)/2)**2+(totalprodutoinercia**2))

inerciamin = (totalinerciaX+totalinerciaY)/2 - sqrt(((totalinerciaX-totalinerciaY)/2)**2+totalprodutoinercia**2)

escrita.write("A inercia minima de sua figura é:			")
escrita.write("{:.6f}".format(inerciamin))
escrita.write(unidade+'4 \n')
escrita.write("A inercia maxima de sua figura é:			")
escrita.write("{:.6f}".format(inerciamax))
escrita.write(unidade+'4 \n')

teta1 = (math.atan(-totalprodutoinercia/((totalinerciaX-totalinerciaY)/2)))/2

teta1 = teta1*180/math.pi

teta2 = teta1 + 90
escrita.write("O Teta1 de sua figura é:					")
escrita.write("{:.6f}".format(teta1))
escrita.write("º")
escrita.write('\n')
escrita.write("O Teta2 de sua figura é:					")
escrita.write("{:.6f}".format(teta2))
escrita.write("º")
escrita.write('\n')

raiomin = sqrt(inerciamin/total_area)
raiomax = sqrt(inerciamax /total_area)
	
escrita.write("O raio minimo de giracao:					")
escrita.write("{:.6f}".format(raiomin))
escrita.write(unidade+' \n')
escrita.write("O raio maximo de giracao:					")
escrita.write("{:.6f}".format(raiomax))
escrita.write(unidade+' \n')
escrita.close()

print ("Arquivo salvo.")
