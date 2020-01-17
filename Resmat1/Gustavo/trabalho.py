from math import* #importa funções matemáticas
import math

def ler():
	print ("Arquivo: ")
	arquivos=input() 
	nomeAbertura = arquivos + '.dat' #junção de string para ler o arquivos
	leitura = open(nomeAbertura, 'r') #abrir para leitura
	
	#ler as entradas do escrita
	N = int(leitura.readline()) ##qnt de figuras
	NC = 0
	NVC=[] #arestas de cada figura
	#um em baixo do outro
	for i in range(N):
		auxiliar = int(leitura.readline())
		NVC.append(auxiliar)
		NC = NC + auxiliar
	#na mesma linha
	#NVC = list(map(int, leitura.readline().split()))
	Xi=[] #x
	Yi=[] #y

	for i in range(NC):
		ptx, pty = map(float, leitura.readline().split())
		Xi.append(ptx)
		Yi.append(pty)
	extensao(leitura.readline())
	leitura.close()
	return arquivos, N, NC, NVC, Xi, Yi, extensao

def salvar(arquivos, respPerimetro, respArea, respGravidadeX, respGravidadeY, respInerciaX, respInerciaY, respInerciaXY, respMomentoInercia, respImax, respImin, respTeta1, respTeta2, respRaioMin, respRaioMax, NC, extensao):
	nomeFechar = arquivos + '.out'
	escrita = open(nomeFechar,'w')#abrir para escrever no escrita
	##escrita.write salva no arquivo
	escrita.write("**** PROPRIEDADES GEOMÉTRICAS DAS FIGURAS PLANAS ****")
	escrita.write ("\n")
	escrita.write("ARQUIVOS DE DADOS: 	")
	escrita.write(str(nomeFechar))
	escrita.write ("\n")
	escrita.write("RESULTADOS OBTIDOS: 	")
	escrita.write ("\n")
	escrita.write("NÚMERO DE VERTICES NO CONTORNO:	")
	escrita.write(str(NC))
	escrita.write ("\n")
	escrita.write("ÁREA DA FIGURA: ")
	escrita.write("{:.6f}".format(respArea))
	escrita.write(extensao+'²')
	escrita.write("\n")
	escrita.write("PERÍMETRO DA FIGURA: ")
	escrita.write("{:.6f}".format(respPerimetro))
	escrita.write(extensao)
	escrita.write("\n")
	escrita.write("COORDENADA X DO C. G.: ")
	escrita.write("{:.6f}".format(respGravidadeX))
	escrita.write(extensao)
	escrita.write("\n")
	escrita.write("COORDENADA Y DO C. G.: ")
	escrita.write("{:.6f}".format(respGravidadeY))
	escrita.write(extensao)
	escrita.write("\n")
	escrita.write("MOMENTO DE INÉRCIA, Ix: ")
	escrita.write("{:.6f}".format(respInerciaX))
	escrita.write(extensao+'4')
	escrita.write("\n")
	escrita.write("MOMENTO DE INÉRCIA, Iy: ")
	escrita.write("{:.6f}".format(respInerciaY))
	escrita.write(extensao+'4')
	escrita.write("\n")
	escrita.write("PRODUTO DE INÉRCIA, Ixy:  ")
	escrita.write("{:.6f}".format(respInerciaXY))
	escrita.write(extensao+'4')
	escrita.write("\n")
	escrita.write("MOMENTO POLAR DE INÉRCIA, Ip: ")
	escrita.write("{:.6f}".format(respMomentoInercia))
	escrita.write(extensao+'4')
	escrita.write("\n")
	escrita.write("MOMENTO DE INÉRCIA MÍNIMO, Imn: ")
	escrita.write("{:.6f}".format(respImin))
	escrita.write(extensao+'4')
	escrita.write("\n")
	escrita.write("MOMENTO DE INÉRCIA MÁXIMO, Imx: ")
	escrita.write("{:.6f}".format(respImax))
	escrita.write(extensao+'4')
	escrita.write("\n")
	escrita.write("ANG. INCL. EIXO PRINC. - respTeta1: ")
	escrita.write("{:.6f}".format(respTeta1))
	escrita.write("º")
	escrita.write("\n")
	escrita.write("ANG. INCL. EIXO PRINC. - respTeta2: ")
	escrita.write("{:.6f}".format(respTeta2))
	escrita.write("º")
	escrita.write("\n")
	escrita.write("RAIO DE GIRAÇÃO, Rmin.:  ")
	escrita.write("{:.6f}".format(respRaioMin))
	escrita.write(extensao)
	escrita.write("\n")
	escrita.write("RAIO DE GIRAÇÃO, Rmáx: ")
	escrita.write("{:.6f}".format(respRaioMax))
	escrita.write(extensao)
	escrita.write ("\n")
	escrita.write("			CÁLCULOS EFETUADOS COM DUPLA PRECISÃO. 		")
	escrita.write("\n")
	print ("Salvo.")
	escrita.close()

def calculoAreaPerimetro(N, NC, NVC, Xi, Yi):
	i=0 #percorrer a quantidade de figuras
	j=0 #percorrer a  quantidade de pontos
	anda=0 #percorre todos os pontos
	identificador=0 #identificador identifica quando a figura estiver na ultimo ponto para poder fechar com o primeiro ponto
	comeco=0 #comeco armazena a posição inicial da figura
	area=[]
	respArea=0.0
	perimetro=[]
	respPerimetro=0.0
	area.append(0.0)
	perimetro.append(0.0)
	somatoriop=0.0
	somatorioa=0.0
	#laço para fazer as equações
	for i in range(N):
		for j in range(NVC[i]):
			if(identificador==(NVC[i]-1)): #identifica o final
				somatoriop+=sqrt(((Xi[comeco]-Xi[anda])**2)+((Yi[comeco]-Yi[anda])**2))
				somatorioa+=Xi[anda]*Yi[comeco]-Xi[comeco]*Yi[anda]
			else:
				somatoriop+=sqrt(((Xi[anda+1]-Xi[anda])**2)+((Yi[anda+1]-Yi[anda])**2))
				somatorioa+=Xi[anda]*Yi[anda+1]-Xi[anda+1]*Yi[anda]
			anda+=1
			identificador+=1
		perimetro.append(somatoriop)
		area.append(somatorioa)
		identificador=0
		comeco=NVC[i]+comeco
		somatorioa=0
		somatoriop=0
	for i in range(len(area)):#somar area,somar perimetro
		respArea+=area[i]
		respPerimetro+=perimetro[i]
	respArea*=0.5	
	return respArea, respPerimetro

def calculoCentroGravidade(N, NC, NVC, Xi, Yi, respArea):
	#cacluco centro de gravidade Xi,Yi
	i=0
	j=0
	cgx=[]
	respGravidadeX=0.0
	cgy=[]
	respGravidadeY=0.0
	anda=0
	identificador=0
	comeco=0
	cgx.append(0.0)
	cgy.append(0.0)
	somagravx=0
	somagravy=0
	for i in range(N):
		for j in range(NVC[i]):
			if(identificador==(NVC[i]-1)):
				somagravx+=((Xi[anda]+Xi[comeco])*(Xi[anda]*Yi[comeco]-Xi[comeco]*Yi[anda]))
				somagravy+=((Yi[anda]+Yi[comeco])*(Xi[anda]*Yi[comeco]-Xi[comeco]*Yi[anda]))
			else:
				somagravx+=((Xi[anda]+Xi[anda+1])*(Xi[anda]*Yi[anda+1]-Xi[anda+1]*Yi[anda]))
				somagravy+=((Yi[anda]+Yi[anda+1])*(Xi[anda]*Yi[anda+1]-Xi[anda+1]*Yi[anda]))
			anda+=1
			identificador+=1
		cgx.append(somagravx)
		cgy.append(somagravy)
		identificador=0
		comeco+=NVC[i]
		somagravx=0
		somagravy=0

	for i in range(len(cgx)):
		respGravidadeX+=cgx[i]
		respGravidadeY+=cgy[i]
	respGravidadeX/=(6*respArea)
	respGravidadeY/=(6*respArea)
	return respGravidadeX, respGravidadeY

def CalculoInercia(N, NC, NVC, Xi, Yi, respGravidadeX, respGravidadeY):
	#momento CalculoInercia
	for i in range(NC): ##atualiza o ponto x e y para calculo de inercia
		Xi[i] = Xi[i] - respGravidadeX
		Yi[i] = Yi[i] - respGravidadeY
	i=0
	j=0
	inerciaX=[]
	respInerciaX=0.0
	inerciaY=[]
	respInerciaY=0.0
	produtoinercia=[]
	respInerciaXY=0.0
	a=[]
	anda=0
	identificador=0
	comeco=0
	inerciaX.append(0.0)
	inerciaY.append(0.0)
	produtoinercia.append(0.0)
	somatorioix=0
	somatoriaiy=0
	somatorioprodutoi=0
	ax=0
	for i in range(N):
		for j in range(NVC[i]):
			if(identificador==(NVC[i]-1)):
				ax=((Xi[anda]*Yi[comeco])-(Xi[comeco]*Yi[anda]))
				a.append(ax)
				somatorioix+=a[anda]*(pow(Yi[anda],2)+Yi[anda]*Yi[comeco]+pow(Yi[comeco],2))
				somatoriaiy+=a[anda]*(pow(Xi[anda],2)+Xi[anda]*Xi[comeco]+pow(Xi[comeco],2))
				somatorioprodutoi+=a[anda]*(Xi[comeco]*Yi[comeco]+2*Xi[anda]*Yi[anda]+2*Xi[comeco]*Yi[comeco]+Xi[anda]*Yi[anda])
			else:
				ax=((Xi[anda]*Yi[anda+1])-(Xi[anda+1]*Yi[anda]))
				a.append(ax)
				somatorioix+=a[anda]*(pow(Yi[anda],2)+Yi[anda]*Yi[anda+1]+pow(Yi[anda+1],2))
				somatoriaiy+=a[anda]*(pow(Xi[anda],2)+Xi[anda]*Xi[anda+1]+pow(Xi[anda+1],2))
				somatorioprodutoi+=a[anda]*(Xi[anda+1]*Yi[anda+1]+2*Xi[anda]*Yi[anda]+2*Xi[anda+1]*Yi[anda+1]+Xi[anda]*Yi[anda])
			anda+=1
			identificador+=1
		identificador=0
		comeco=NVC[i]+comeco
		inerciaX.append(somatorioix)
		inerciaY.append(somatoriaiy)
		produtoinercia.append(somatorioprodutoi)
		somatorioix=0
		somatoriaiy=0
		somatorioprodutoi=0	
	for i in range(len(inerciaX)):
		respInerciaX+=inerciaX[i]
		respInerciaY+=inerciaY[i]
		respInerciaXY+=produtoinercia[i]
	
	##Inercia em X, Y, XY e Momento de Inercia
	respInerciaX = respInerciaX/12
	respInerciaY = respInerciaY/12
	respInerciaXY = respInerciaXY/24
	respMomentoInercia = respInerciaY + respInerciaX
	
	##CalculoInercia maximo e minimo##
	respImax = (respInerciaX+respInerciaY)/2 + sqrt(((respInerciaX-respInerciaY)/2)**2+(respInerciaXY**2))
	respImin = (respInerciaX+respInerciaY)/2 - sqrt(((respInerciaX-respInerciaY)/2)**2+respInerciaXY**2)

	return respInerciaX, respInerciaY, respInerciaXY, respMomentoInercia, respImax, respImin

def CalculoAnguloRaio(respInerciaXY, respInerciaX, respInerciaY, respImin, respImax, respArea):
	#teta 1 e Teta2
	respTeta1 = (math.atan(-respInerciaXY/((respInerciaX-respInerciaY)/2)))/2
	respTeta1 = respTeta1*180/math.pi
	respTeta2 = respTeta1 + 90

	#raio de giro minimo e maxio
	respRaioMin = sqrt(respImin/respArea)
	respRaioMax = sqrt(respImax/respArea)

	return respTeta1, respTeta2, respRaioMin, respRaioMax 

def principal():
	arquivos, N, NC, NVC, Xi, Yi, extensao = ler()
	respArea, respPerimetro = calculoAreaPerimetro(N, NC, NVC, Xi, Yi)
	respGravidadeX, respGravidadeY = calculoCentroGravidade(N, NC, NVC, Xi, Yi, respArea)
	respInerciaX, respInerciaY, respInerciaXY, respMomentoInercia, respImax, respImin = CalculoInercia(N, NC, NVC, Xi, Yi, respGravidadeX, respGravidadeY)
	respTeta1, respTeta2, respRaioMin, respRaioMax = CalculoAnguloRaio(respInerciaXY, respInerciaX, respInerciaY, respImin, respImax, respArea)
	salvar(arquivos, respPerimetro, respArea, respGravidadeX, respGravidadeY, respInerciaX, respInerciaY, respInerciaXY, respMomentoInercia, respImax, respImin, respTeta1, respTeta2, respRaioMin, respRaioMax, NC, extensao)

principal()
