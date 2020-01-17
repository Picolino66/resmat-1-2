from math import* #importa funções matemáticas
import math

import datetime #biblioteca de hora e data
data_atual = datetime.datetime.now() #pega hora e data

print ("Digite nome do arquivo: ")
name=input() 

arq = name + '.dat' #junção de string para ler o name do arquivo
carregar = open(arq, 'r') #abrir arquivo para carregar

#ler as entradas do arquivo
imagem = int(carregar.readline())
pts = 0 
linhas=[]
for i in range(imagem):
	alinhas = int(carregar.readline())
	pts = alinhas + pts 
	linhas.append(alinhas)
	
x_cord=[]
y_cord=[]

for i in range(pts):
	lx, ly = map(float, carregar.readline().split())
	x_cord.append(lx)
	y_cord.append(ly)
	
unidade = carregar.readline()

carregar.close()
##FIM DA LEITURA DO ARQUIVO##

i=0
j=0
proximo=0 #percorre a figura
acabou=0 #acabou identifica quando a figura estiver na ultimo ponto para poder fechar com o primeiro ponto
marco=0 #marco armazena a posição inicial da figura

area=[]
perimetro=[]
totala=0.0
totalp=0.0
area.append(0.0)
perimetro.append(0.0)
somaa=0.0
somap=0.0

#laço para fazer as equações
#dois for é para percorrer todas figuras
for i in range(imagem):
	for j in range(linhas[i]):
		#verificação se está no final da figura
		if(acabou==(linhas[i]-1)):
			somap+=sqrt(((x_cord[marco]-x_cord[proximo])**2)+((y_cord[marco]-y_cord[proximo])**2))
			somaa+=x_cord[proximo]*y_cord[marco]-x_cord[marco]*y_cord[proximo]
		else:
			somap+=sqrt(((x_cord[proximo+1]-x_cord[proximo])**2)+((y_cord[proximo+1]-y_cord[proximo])**2))
			somaa+=x_cord[proximo]*y_cord[proximo+1]-x_cord[proximo+1]*y_cord[proximo]
		proximo+=1
		acabou+=1
	perimetro.append(somap)
	area.append(somaa)
	acabou=0
	marco=linhas[i]+marco
	somaa=0
	somap=0

for i in range(len(area)):#somar area,somar perimetro
	totala+=area[i]
	totalp+=perimetro[i]
totala*=0.5

#cacluco centro de gravidade x_cord,y_cord
gravidadex=[]
totalgx=0.0
gravidadey=[]
totalgy=0.0
proximo=0
acabou=0
marco=0
gravidadex.append(0.0)
gravidadey.append(0.0)
somacgx=0
somacgy=0

for i in range(imagem):
	for j in range(linhas[i]):
		if(acabou==(linhas[i]-1)):
			somacgx+=((x_cord[proximo]+x_cord[marco])*(x_cord[proximo]*y_cord[marco]-x_cord[marco]*y_cord[proximo]))
			somacgy+=((y_cord[proximo]+y_cord[marco])*(x_cord[proximo]*y_cord[marco]-x_cord[marco]*y_cord[proximo]))
		else:
			somacgx+=((x_cord[proximo]+x_cord[proximo+1])*(x_cord[proximo]*y_cord[proximo+1]-x_cord[proximo+1]*y_cord[proximo]))
			somacgy+=((y_cord[proximo]+y_cord[proximo+1])*(x_cord[proximo]*y_cord[proximo+1]-x_cord[proximo+1]*y_cord[proximo]))
		proximo+=1
		acabou+=1
	gravidadex.append(somacgx)
	gravidadey.append(somacgy)
	acabou=0
	marco+=linhas[i]
	somacgx=0
	somacgy=0

for i in range(len(gravidadex)):
	totalgx+=gravidadex[i]
	totalgy+=gravidadey[i]
totalgx/=(6*totala)
totalgy/=(6*totala)

#momento inercia
for i in range(pts):
	x_cord[i] = x_cord[i] - totalgx
	y_cord[i] = y_cord[i] - totalgy
inerciax=[]
totalix=0.0
inerciay=[]
totaliy=0.0
produtoinercia=[]
totalpi=0.0
inerciax.append(0.0)
inerciay.append(0.0)
produtoinercia.append(0.0)
a=[]
ax=0
proximo=0
acabou=0
marco=0
somaix=0
somaiy=0
somaixy=0

for i in range(imagem):
	for j in range(linhas[i]):
		if(acabou==(linhas[i]-1)):
			ax=((x_cord[proximo]*y_cord[marco])-(x_cord[marco]*y_cord[proximo]))
			a.append(ax)
			somaix+=a[proximo]*(pow(y_cord[proximo],2)+y_cord[proximo]*y_cord[marco]+pow(y_cord[marco],2))
			somaiy+=a[proximo]*(pow(x_cord[proximo],2)+x_cord[proximo]*x_cord[marco]+pow(x_cord[marco],2))
			somaixy+=a[proximo]*(x_cord[marco]*y_cord[proximo]+x_cord[proximo]*y_cord[marco]+2*x_cord[proximo]*y_cord[proximo]+2*x_cord[marco]*y_cord[marco])
		else:
			ax=((x_cord[proximo]*y_cord[proximo+1])-(x_cord[proximo+1]*y_cord[proximo]))
			a.append(ax)
			somaix+=a[proximo]*(pow(y_cord[proximo],2)+y_cord[proximo]*y_cord[proximo+1]+pow(y_cord[proximo+1],2))
			somaiy+=a[proximo]*(pow(x_cord[proximo],2)+x_cord[proximo]*x_cord[proximo+1]+pow(x_cord[proximo+1],2))
			somaixy+=a[proximo]*(x_cord[proximo]*y_cord[proximo+1]+x_cord[proximo+1]*y_cord[proximo]+2*x_cord[proximo]*y_cord[proximo]+2*x_cord[proximo+1]*y_cord[proximo+1])
		proximo+=1
		acabou+=1
	acabou=0
	marco=linhas[i]+marco
	inerciax.append(somaix)
	inerciay.append(somaiy)
	produtoinercia.append(somaixy)
	somaix=0
	somaiy=0
	somaixy=0
		
for i in range(len(inerciax)):
	totalix+=inerciax[i]
	totaliy+=inerciay[i]
	totalpi+=produtoinercia[i]

totalix = totalix/12
totaliy = totaliy/12
totalpi = totalpi/24
momentoinercia = totaliy + totalix


#inercia maxima e minina

inerciamaxima = (totalix+totaliy)/2 + sqrt(((totalix-totaliy)/2)**2+(totalpi**2))
inerciaminima = (totalix+totaliy)/2 - sqrt(((totalix-totaliy)/2)**2+totalpi**2)

#teta1 e teta2
grau1 = (math.atan(-totalpi/((totalix-totaliy)/2)))/2
grau1 = grau1*180/math.pi
grau2 = grau1 + 90

#raio minimo e maximo
raiominimo = sqrt(inerciaminima/totala)
raiomaximo = sqrt(inerciamaxima/totala)

##FIM DOS CACLCULOS##

salvar = name + '.out'
salvando = open(salvar,'w')#abrir para escrever no salvando
salvando.write("				Propriedades Geométricas da Figuras Planas")
salvando.write ("\n")
salvando.write ("\n")
salvando.write ("			Arquivo de Dados:		")
salvando.write (salvar)
salvando.write ("\n")
salvando.write ("		Data do Processamento:		")
salvando.write(str(data_atual.day))
salvando.write("/")
salvando.write(str(data_atual.month))
salvando.write("/")
salvando.write(str(data_atual.year))
salvando.write(" ")
salvando.write(str(data_atual.hour))
salvando.write(":")
salvando.write(str(data_atual.minute))
salvando.write(":")
salvando.write(str(data_atual.second))
salvando.write ("\n")
salvando.write ("\n")
salvando.write ("			Resultado Obtidos				")
salvando.write ("\n")
salvando.write("	Número de contorno na figura:		")
salvando.write(str(imagem))
salvando.write("\n")
salvando.write("	Número Total de Vértices:			")
salvando.write(str(pts))
salvando.write("\n")
salvando.write('\n')
salvando.write("	A area da sua figura é:				")
salvando.write("{:.6f}".format(totala))
salvando.write(unidade+'²')
salvando.write('\n')
salvando.write("	O perimetro de sua figura é:		")
salvando.write("{:.6f}".format(totalp))
salvando.write(unidade)
salvando.write('\n')

salvando.write("	Coordenada X do CG:					")
salvando.write("{:.6f}".format(totalgx))
salvando.write(unidade)
salvando.write('\n')
salvando.write("	Coordenada Y do CG :				")
salvando.write("{:.6f}".format(totalgy))
salvando.write(unidade)
salvando.write('\n')

salvando.write("	Momento de inercia em Ix:			")
salvando.write("{:.6f}".format(totalix))
salvando.write(unidade+'4')
salvando.write('\n')
salvando.write("	Momento de inercia em Iy:			")
salvando.write("{:.6f}".format(totaliy))
salvando.write(unidade+'4')
salvando.write('\n')
salvando.write("	Produto de inercia em Ixy:			")
salvando.write("{:.6f}".format(totalpi))
salvando.write(unidade+'4')
salvando.write('\n')
salvando.write("	Momento Polar de Inercia:			")
salvando.write("{:.6f}".format(momentoinercia))
salvando.write(unidade+'4')
salvando.write('\n')

salvando.write("	O momento de inercia minimo:		")
salvando.write("{:.6f}".format(inerciaminima))
salvando.write(unidade+'4')
salvando.write('\n')
salvando.write("	O momento inercia maxima:			")
salvando.write("{:.6f}".format(inerciamaxima))
salvando.write(unidade+'4')
salvando.write('\n')

salvando.write("	Eixo Principal - Teta 1:			")
salvando.write("{:.9f}".format(grau1))
salvando.write("º")
salvando.write('\n')
salvando.write("	Eixo Principal - Teta 2:			")
salvando.write("{:.9f}".format(grau2))
salvando.write("º")
salvando.write('\n')
	
salvando.write("	Raio de giração min:				")
salvando.write("{:.6f}".format(raiominimo))
salvando.write(unidade)
salvando.write('\n')
salvando.write("	Raio de giração max:				")
salvando.write("{:.6f}".format(raiomaximo))
salvando.write(unidade)
salvando.write('\n')
salvando.close()
