from math import* #importa funções matemáticas
import math
#Função para pegar os valores do arquivo
def criar_arq(): #funcao para ler os dados dos arquivos
	print ("Digite o nome do arquivo: ")
	arq=input() 
	arqentrada = arq + '.dat' #junção de string para ler o nome do arquivo
	f = open(arqentrada, 'r') #abrir arquivo para leitura
	#ler as entradas do arquivo
	NC = int(f.readline())
	a = []
	NCV = 0
	#caso for um em baixo do outro
	for i in range(NC):
		aaux = int(f.readline())
		a.append(aaux)
		NCV = aaux + NCV
	px=[]
	py=[]
	for i in range(NCV):
		x, y = map(float, f.readline().split())
		px.append(x)
		py.append(y)
	unidade = f.readline()
	return NC,NCV,a,px,py,arq, unidade

def principal():
	figuras,NCV,arestas,x,y,arqsaida, unidade = criar_arq()
	arqsaida = arqsaida + '.out'
	arquivo = open(arqsaida,'w')#abrir para escrever no arquivo
	arquivo.write("**** PROPRIEDADES GEOMÉTRICAS DAS FIGURAS PLANAS ****")
	arquivo.write ("\n")
	tam=NCV+1
	i=0
	j=0
	k=0
	aux=0 #aux identifica quando a figura estiver na ultimo ponto para poder fechar com o primeiro ponto
	prox=0 #prox armazena a posição inicial da figura
	
	###AREA E PERIMETRO####
	area=[]
	tarea=0.0
	perimetro=[]
	tperimetro=0.0
	area.append(0.0)
	perimetro.append(0.0)
	somap=0
	somaa=0
	#laço para fazer as equações
	for i in range(figuras):
		for j in range(arestas[i]):
			if(aux==(arestas[i]-1)):
				somap+=sqrt(((x[prox]-x[k])**2)+((y[prox]-y[k])**2))
				somaa+=x[k]*y[prox]-x[prox]*y[k]
			else:
				somap+=sqrt(((x[k+1]-x[k])**2)+((y[k+1]-y[k])**2))
				somaa+=x[k]*y[k+1]-x[k+1]*y[k]
			k+=1
			aux+=1
		perimetro.append(somap)
		area.append(somaa)
		aux=0
		prox=arestas[i]+prox
		somaa=0	
		somap=0

	for i in range(len(area)):#somar area,somar perimetro
		tarea+=area[i]
		tperimetro+=perimetro[i]
	tarea*=0.5	
	arquivo.write("A area da sua figura e: ")
	arquivo.write("{:.6f}".format(tarea))
	arquivo.write(unidade+'²')
	arquivo.write('\n')
	arquivo.write("O perimetro de sua figura e: ")
	arquivo.write("{:.6f}".format(tperimetro))
	arquivo.write(unidade)
	arquivo.write('\n')
	
	
	##cacluco centro de gravidade x,y
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
	arquivo.write("Coordenada do CG no eixo x: ")
	arquivo.write("{:.6f}".format(tcgx))
	arquivo.write(unidade)
	arquivo.write('\n')
	arquivo.write("Coordenada do CG no eixo y: ")
	arquivo.write("{:.6f}".format(tcgy))
	arquivo.write(unidade)
	arquivo.write('\n')


	##momento inercia
	for i in range(NCV):
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
				somaixy+=a[k]*(x[prox]*y[prox]+2*x[k]*y[k]+2*x[prox]*y[prox]+x[k]*y[k])
			else:
				ax=((x[k]*y[k+1])-(x[k+1]*y[k]))
				a.append(ax)
				somaix+=a[k]*(pow(y[k],2)+y[k]*y[k+1]+pow(y[k+1],2))
				somaiy+=a[k]*(pow(x[k],2)+x[k]*x[k+1]+pow(x[k+1],2))
				somaixy+=a[k]*(x[k+1]*y[k+1]+2*x[k]*y[k]+2*x[k+1]*y[k+1]+x[k]*y[k])
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

	arquivo.write("Momento de inercia em x: ")
	arquivo.write("{:.6f}".format(tIx))
	arquivo.write(unidade+'4')
	arquivo.write('\n')
	arquivo.write("Momento de inercia em y: ")
	arquivo.write("{:.6f}".format(tIy))
	arquivo.write(unidade+'4')
	arquivo.write('\n')
	arquivo.write("Produto de inercia em xy: ")
	arquivo.write("{:.6f}".format(tIxy))
	arquivo.write(unidade+'4')
	arquivo.write('\n')
	arquivo.write("Momento polar de Inercia: ")
	arquivo.write("{:.6f}".format(tIx+tIy))
	arquivo.write(unidade+'4')
	arquivo.write('\n')

	
	##MOMENTO DE INERCIA MAXIMO E MINIMO
	Imax = (tIx+tIy)/2 + sqrt(((tIx-tIy)/2)**2+(tIxy**2))
	Imin = (tIx+tIy)/2 - sqrt(((tIx-tIy)/2)**2+tIxy**2)
	arquivo.write("O Imin de sua figura é: ")
	arquivo.write("{:.6f}".format(Imin))
	arquivo.write(unidade+'4')
	arquivo.write('\n')
	arquivo.write("O Imax de sua figura é: ")
	arquivo.write("{:.6f}".format(Imax))
	arquivo.write(unidade+'4')
	arquivo.write('\n')

	##ANGULO PRINCIPAL TETA 1 E TETA 2
	tetap1 = (math.atan(-tIxy/((tIx-tIy)/2)))/2
	tetap1 = tetap1*180/math.pi
	tetap2 = tetap1 + 90
	arquivo.write("O Tetap1 de sua figura é: ")
	arquivo.write(str(tetap1))
	arquivo.write("º")
	arquivo.write('\n')
	arquivo.write("O Tetap2 de sua figura é: ")
	arquivo.write(str(tetap2))
	arquivo.write("º")
	arquivo.write('\n')

	#RAIO DE GIRAÇÃO
	Kx = sqrt(Imax/tarea)
	Ky = sqrt(Imin/tarea)
	
	arquivo.write("O Rmin de sua figura: ")
	arquivo.write("{:.6f}".format(Ky))
	arquivo.write(unidade)
	arquivo.write('\n')
	arquivo.write("O Rmax de sua figura: ")
	arquivo.write("{:.6f}".format(Kx))
	arquivo.write(unidade)
	arquivo.write('\n')
	arquivo.close()
	
	print ("Arquivo salvo.")
principal()




	
		
