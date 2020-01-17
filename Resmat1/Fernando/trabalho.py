from math import* #importa funções matemáticas
import math
#Função para pegar os valores do arquivo
def criar(): #funcao para ler os dados dos arquivos
	print ("Digite o nome do arquivo: ")
	arq=input() #digitar nome do arquivo 
	arqentrada = arq + '.dat' #junção de string para ler o nome do arquivo
	f = open(arqentrada, 'r') #abrir arquivo para leitura
	#ler as entradas do arquivo
	figuras = int(f.readline())
	pontos = 0
	arestas=[]
	for i in range(figuras):
		aux = int(f.readline())
		pontos = pontos + aux
		arestas.append(aux)
	px=[] #vetor coordenada x
	py=[] #vetor coordenada y
	for i in range(pontos):
		x, y = map(float, f.readline().split())
		px.append(x)
		py.append(y)
	unidade = f.readline()
	return figuras,pontos,arestas,px,py,arq,unidade

def principal():
	figuras,pontos,arestas,x,y,arqsaida,unidade=criar()
	i=0 #laço pra percorrer as figuras 
	j=0 #laço pra percorrer as arestas de cada figura
	k=0 #variavel para andar nos pontos
	aux=0 #aux identifica quando a figura estiver na ultimo ponto para poder fechar com o primeiro ponto
	prox=0 #prox armazena a posição inicial da figura
	area=[]
	tarea=0.0
	perimetro=[]
	tperimetro=0.0
	area.append(0.0)
	perimetro.append(0.0)
	somap=0
	somaa=0
	
	#laço para fazer as equações
	#perimetro e area
	for i in range(figuras): #laço percorre as figuras 
		for j in range(arestas[i]): #laço percorre 
			if(aux==(arestas[i]-1)): #verifica final do arquivo
				somap+=sqrt(((x[prox]-x[k])**2)+((y[prox]-y[k])**2))
				somaa+=x[k]*y[prox]-x[prox]*y[k]
			else: 
				somap+=sqrt(((x[k+1]-x[k])**2)+((y[k+1]-y[k])**2))
				somaa+=x[k]*y[k+1]-x[k+1]*y[k]
			k+=1 #k percorre as figuras
			aux+=1 #aux anda até final da figura
		perimetro.append(somap) #armazena perimetro de cada figura no vetor
		area.append(somaa) #armazena area de cada figura no vetor
		aux=0 #zera aux pra proxima figura
		prox=arestas[i]+prox #prox é atualizado pra o novo inicio
		somaa=0 #zera variaveis
		somap=0

	for i in range(len(area)):#somar area,somar perimetro
		tarea+=area[i]
		tperimetro+=perimetro[i]
	tarea*=0.5
		
	#cacluco centro de gravidade x,y
	cgx=[]
	tcgx=0.0
	cgy=[]
	tcgy=0.0
	k=0
	aux=0
	prox=0
	cgx.append(0.0)
	cgy.append(0.0)
	somax=0
	somay=0
	for i in range(figuras):
		for j in range(arestas[i]):
			if(aux==(arestas[i]-1)):
				somax+=((x[k]+x[prox])*(x[k]*y[prox]-x[prox]*y[k]))
				somay+=((y[k]+y[prox])*(x[k]*y[prox]-x[prox]*y[k]))
			else:
				somax+=((x[k]+x[k+1])*(x[k]*y[k+1]-x[k+1]*y[k]))
				somay+=((y[k]+y[k+1])*(x[k]*y[k+1]-x[k+1]*y[k]))
			k+=1
			aux+=1
		cgx.append(somax)
		cgy.append(somay)
		aux=0
		prox+=arestas[i]
		somax=0
		somay=0

	for i in range(len(cgx)):
		tcgx+=cgx[i]
		tcgy+=cgy[i]

	tcgx/=(6*tarea)
	tcgy/=(6*tarea)

	#momento inercia
	for i in range(pontos): #atualiza os valores do x e y para calculo do momento de inercia
		x[i] = x[i] - tcgx
		y[i] = y[i] - tcgy
	Ix=[]
	tIx=0.0
	Iy=[]
	tIy=0.0
	Ixy=[]
	tIxy=0.0
	a=[]
	k=0
	aux=0
	prox=0
	Ix.append(0.0)
	Iy.append(0.0)
	Ixy.append(0.0)
	somaix=0
	somaiy=0
	somaixy=0
	ax=0
	for i in range(figuras):
		for j in range(arestas[i]):
			if(aux==(arestas[i]-1)):
				ax=((x[k]*y[prox])-(x[prox]*y[k]))
				a.append(ax)
				somaix+=a[k]*(pow(y[k],2)+y[k]*y[prox]+pow(y[prox],2))
				somaiy+=a[k]*(pow(x[k],2)+x[k]*x[prox]+pow(x[prox],2))
				somaixy+=a[k]*(x[prox]*y[k]+x[k]*y[prox]+2*x[k]*y[k]+2*x[prox]*y[prox])
			else:
				ax=((x[k]*y[k+1])-(x[k+1]*y[k]))
				a.append(ax)
				somaix+=a[k]*(pow(y[k],2)+y[k]*y[k+1]+pow(y[k+1],2))
				somaiy+=a[k]*(pow(x[k],2)+x[k]*x[k+1]+pow(x[k+1],2))
				somaixy+=a[k]*(x[k+1]*y[k]+x[k]*y[k+1]+2*x[k]*y[k]+2*x[k+1]*y[k+1])
			k+=1
			aux+=1
		aux=0
		prox=arestas[i]+prox
		Ix.append(somaix)
		Iy.append(somaiy)
		Ixy.append(somaixy)
		somaix=0
		somaiy=0
		somaixy=0
			
	for i in range(len(Ix)):
		tIx+=Ix[i]
		tIy+=Iy[i]
		tIxy+=Ixy[i]

	tIx = tIx/12
	tIy = tIy/12
	tIxy = tIxy/24
	poI = tIx + tIy


	#Momento de inercia maximo e minimo
	Imax = (tIx+tIy)/2 + sqrt(((tIx-tIy)/2)**2+(tIxy**2))

	Imin = (tIx+tIy)/2 - sqrt(((tIx-tIy)/2)**2+tIxy**2)

	#angulo de inclinacao x e y
	tetap1 = (math.atan(-tIxy/((tIx-tIy)/2)))/2 #math.atan arcotagente

	tetap1 = tetap1*180/math.pi #numero de pi

	tetap2 = tetap1 + 90
	
	#raio de giracao min e max
	Kx = sqrt(Imax/tarea)
	Ky = sqrt(Imin/tarea)


	#salvando o arquivo
	arqsaida = arqsaida + '.out'
	arquivo = open(arqsaida,'w')#abrir para escrever no arquivo
	arquivo.write("**** PROPRIEDADES GEOMÉTRICAS DAS FIGURAS PLANAS **** \n"
	"				RESULTADOS OBTIDOS: \n \n "
	"NUMERO DE CONTORNOS NA FIGURA:  "+str(figuras)+"\n \n"
	"NUMERO DE VERTICES NO CONTORNO: "+str(pontos)+"\n \n"
	"A area da sua figura e: 				{:.6f}".format(tarea)+"		"+str(unidade)+"² \n "
	"O perimetro de sua figura e: 			{:.6f}".format(tperimetro)+"		cm \n"
	"Coordenada do CG no eixo x: 			{:.6f}".format(tcgx)+"		"+str(unidade)+" \n"
	"Coordenada do CG no eixo y: 			{:.6f}".format(tcgy)+"		"+str(unidade)+" \n \n"
	"Momento de inercia em x: 				{:.6f}".format(tIx)+"		"+str(unidade)+"4  \n"
	"Momento de inercia em y: 				{:.6f}".format(tIy)+"		"+str(unidade)+"4  \n"
	"Produto de inercia em xy: 				{:.6f}".format(tIxy)+"		"+str(unidade)+"4  \n"
	"Momento polar de inercia, Ip: 			{:.6f}".format(poI)+"		"+str(unidade)+"4  \n \n"
	"Momento de inércia mínimo: 				{:.6f}".format(Imin)+"		"+str(unidade)+"4  \n"
	"Momento de inércia máximo: 				{:.6f}".format(Imax)+"		"+str(unidade)+"4  \n"
	"O Tetap1 de sua figura é: 				{:.9f}".format(tetap1)+"º \n"
	"O Tetap2 de sua figura é: 				{:.9f}".format(tetap2)+"º \n \n"
	"O Raio de giração, Rmin: 				{:.6f}".format(Ky)+"	"+str(unidade)+" \n"
	"O Raio de giração, Rmax: 				{:.6f}".format(Kx)+"	"+str(unidade)+" \n")
	arquivo.close()
	
	print ("Arquivo salvo.")
principal()




	
		
