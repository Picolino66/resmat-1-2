from math import atan,sin,cos,radians, degrees , acos , pi ,sqrt
import datetime #biblioteca de hora e data

def ler():
	Arquivo = input("digite nome do arquivo: ") 
	leitura = open(Arquivo + ".dat", 'r') 
	Dimensao = int(leitura.readline())
	tipoTensor = int(leitura.readline())
	estadoPlano = int(leitura.readline())
	tipoDeformacao = int(leitura.readline())
	matriz = [[0,0,0],[0,0,0],[0,0,0]]
	matrizAux = []
	matrizDeformacao = [[0,0,0],[0,0,0],[0,0,0]]
	matrizTensao = [[0,0,0],[0,0,0],[0,0,0]]
	matrizDevitorico = [[0,0,0],[0,0,0],[0,0,0]]
	for i in range(Dimensao):
		aux = list(map(float, leitura.readline().split()))
		matrizAux.append(aux)
	for i in range(Dimensao):
		for j in range(Dimensao):
			matriz[i][j] = matrizAux[i][j]
	fy = float(leitura.readline())
	E = float(leitura.readline())
	ni = float(leitura.readline())
	gama = float(leitura.readline())
	unidade = str(leitura.readline())
	G = E/(2*(1+ni))
	mat_cron = [[1,0,0],[0,1,0],[0,0,1]]
	return Arquivo, Dimensao, tipoTensor, estadoPlano, tipoDeformacao, matriz, matrizDeformacao, matrizTensao, matrizDevitorico, fy, E, ni, gama, unidade, G, mat_cron

def salvar(Arquivo,matrizTensao,matrizDevitorico,I1,I2,I3,J2,J3,cos3teta,s1,s2,s3,tau_max,fy,gama,ni,E,matrizDeformacao,def1,def2,def3,gamamax,tresca,mises,fraset,frasem,unidade):
	data_atual = datetime.datetime.now() #pega hora e data
	escrita = open(Arquivo + ".out", 'w') # abre arq 
	#escrita = open("arq2.txt", 'w')
	escrita.write("    \n")
	escrita.write("                      **** ANÁLISE DO TENSOR DE TENSÃO E CRITÉRIOS DE ESCOAMENTO **** \n")
	escrita.write("    \n")
	escrita.write ("\n")
	escrita.write ("		Data do Processamento:		")
	escrita.write(str(data_atual.day))
	escrita.write("/")
	escrita.write(str(data_atual.month))
	escrita.write("/")
	escrita.write(str(data_atual.year))
	escrita.write(" ")
	escrita.write(str(data_atual.hour))
	escrita.write(":")
	escrita.write(str(data_atual.minute))
	escrita.write(":")
	escrita.write(str(data_atual.second))
	escrita.write ("\n")
	escrita.write("    \n")
	escrita.write("arquivo de dados :            " + Arquivo + ".out" '\n')
	escrita.write("    \n")
	escrita.write("    \n")
	escrita.write("Tensor de Tensão Sigma_ij:                " + '\n')
	escrita.write("|  " +'{:e}'.format(matrizTensao[0][0])+"  "+'{:e}'.format(matrizTensao[0][1]) +"  "+'{:e}'.format(matrizTensao[0][2]) +"|" + '\n')
	escrita.write("|  " +'{:e}'.format(matrizTensao[1][0])+"  "+'{:e}'.format(matrizTensao[1][1]) +"  "+'{:e}'.format(matrizTensao[1][2]) +"|" + unidade+ '\n')
	escrita.write("|  " +'{:e}'.format(matrizTensao[2][0])+"  "+'{:e}'.format(matrizTensao[2][1]) +"  "+'{:e}'.format(matrizTensao[2][2]) +"|" +  '\n')
	escrita.write("    \n")
	escrita.write("Tensor Desviatório S_ij :                    " +'\n')
	escrita.write("|  " +'{:e}'.format(matrizDevitorico[0][0])+"  "+'{:e}'.format(matrizDevitorico[0][1]) +"  "+'{:e}'.format(matrizDevitorico[0][2]) +"|" '\n')
	escrita.write("|  " +'{:e}'.format(matrizDevitorico[1][0])+"  "+'{:e}'.format(matrizDevitorico[1][1]) +"  "+'{:e}'.format(matrizDevitorico[1][2]) +"|" + unidade+ '\n')
	escrita.write("|  " +'{:e}'.format(matrizDevitorico[2][0])+"  "+'{:e}'.format(matrizDevitorico[2][1]) +"  "+'{:e}'.format(matrizDevitorico[2][2]) +"|" +  '\n')
	escrita.write("    \n")
	escrita.write("Invariantes de Sigma_ij              " '\n')
	escrita.write("    \n")
	escrita.write("i1:                " +'{:e}'.format(I1 )+ unidade+ '\n')
	escrita.write("    \n")
	escrita.write("i2:                " +'{:e}'.format(I2 )+ unidade+ "²"'\n')
	escrita.write("    \n")
	escrita.write("i3:                " +'{:e}'.format(I3 )+ unidade+ "³"'\n')
	escrita.write("    \n")
	escrita.write("    \n")
	escrita.write("Invariantes de S_ij              " '\n')
	escrita.write("    \n")
	escrita.write("J2:                " +'{:e}'.format(J2 )+ unidade+ "²"'\n')
	escrita.write("    \n")
	escrita.write("J3:                " +'{:e}'.format(J3 )+ unidade+ "³"'\n')
	escrita.write("    \n")
	escrita.write("Invariante COS(3Teta)             " '\n')
	escrita.write("cos(3teta)=              " +'{:e}'.format(cos3teta)+'\n')
	escrita.write("    \n")
	escrita.write("    \n")
	escrita.write("Tensões Principais             " '\n')
	escrita.write("Sig1=            " +'{:e}'.format(s1 )+ unidade+ '\n')
	escrita.write("Sig2=             " +'{:e}'.format(s2) + unidade+ '\n')
	escrita.write("Sig3=            "+'{:e}'.format(s3) + unidade+ '\n')
	escrita.write("TauMx=            "+'{:e}'.format(tau_max) + unidade+ '\n')
	escrita.write("    \n")
	escrita.write("    \n")
	escrita.write("Parâmetros do Material           " '\n')
	escrita.write("    \n")
	escrita.write("fy=            " +'{:e}'.format(fy)+ unidade+ '\n')
	escrita.write("Gama_mat=             " +'{:e}'.format(gama) + '\n')
	escrita.write("Rel.Poisson        "+'{:e}'.format(ni) + '\n')
	escrita.write("Mód.Young           "+'{:e}'.format(E) + unidade+ '\n')
	escrita.write("    \n")
	escrita.write("    \n")
	escrita.write("    \n")
	escrita.write("Tensor de deformação estadoPlanosilon_ij           " '\n')
	escrita.write("|  " +'{:e}'.format(matrizDeformacao[0][0])+"  "+'{:e}'.format(matrizDeformacao[0][1]) +"  "+'{:e}'.format(matrizDeformacao[0][2]) +"|" + '\n')
	escrita.write("|  " +'{:e}'.format(matrizDeformacao[1][0])+"  "+'{:e}'.format(matrizDeformacao[1][1]) +"  "+'{:e}'.format(matrizDeformacao[1][2]) +"|" +  '\n')
	escrita.write("|  " +'{:e}'.format(matrizDeformacao[2][0])+"  "+'{:e}'.format(matrizDeformacao[2][1]) +"  "+'{:e}'.format(matrizDeformacao[2][2]) +"|" +  '\n')
	escrita.write("    \n")
	escrita.write("Deformações Principais             " '\n')
	escrita.write("estadoPlanos1=            " +'{:e}'.format(def1 )+  '\n')
	escrita.write("estadoPlanos2=             " +'{:e}'.format(def2) + '\n')
	escrita.write("estadoPlanos3=            "+'{:e}'.format(def3) + '\n')
	escrita.write("Gama_Mx=            "+'{:e}'.format(gamamax) + '\n')
	escrita.write("Tensão Equivalente de tresca            " '\n')
	escrita.write("2 Tau_mx=       " +'{:e}'.format(tresca) + unidade+ '\n')
	escrita.write("    \n")
	escrita.write("Tensão Equivalente de Von Mises           " '\n')
	escrita.write("Sig_Eq=       " +'{:e}'.format(mises) + unidade+ '\n')
	escrita.write("    \n")
	escrita.write("Verificação da estabilidade:          " '\n')
	escrita.write("    \n")
	escrita.write("Critério de Tresca      " + fraset+ '\n')
	escrita.write("    \n")
	escrita.write("Critério de Von Mises      " + frasem + '\n')


def principal():
	Arquivo, Dimensao, tipoTensor, estadoPlano, tipoDeformacao, matriz, matrizDeformacao, matrizTensao, matrizDevitorico, fy, E, ni, gama, unidade, G, mat_cron = ler()
	if (Dimensao == 3): #3d
		if (tipoTensor == 1): #tensao
			# TENSOR TENSAO
			matrizTensao = [[0,0,0],[0,0,0],[0,0,0]]
			matrizTensao = matriz
			#TENSOR DE DEFORMAÇÃO 
			matrizDeformacao[0][0] = (1/E)*(matrizTensao[0][0] - ni*(matrizTensao[1][1]+matrizTensao[2][2]))
			matrizDeformacao[1][1] = (1/E)*(matrizTensao[1][1] - ni*(matrizTensao[0][0]+matrizTensao[2][2]))
			matrizDeformacao[2][2] = (1/E)*(matrizTensao[2][2] - ni*(matrizTensao[1][1]+matrizTensao[0][0]))
			
			if (tipoDeformacao == 1): #angular
				matrizDeformacao[0][1] = matrizTensao[0][1]/G
				matrizDeformacao[0][2] = matrizTensao[0][2]/G
				matrizDeformacao[1][2] = matrizTensao[1][2]/G
			elif (tipoDeformacao == 2): #linear
				matrizDeformacao[0][1] = matrizTensao[0][1]/(2*G)
				matrizDeformacao[0][2] = matrizTensao[0][2]/(2*G)
				matrizDeformacao[1][2] = matrizTensao[1][2]/(2*G)
			matrizDeformacao[1][0] = matrizDeformacao[0][1]
			matrizDeformacao[2][0] = matrizDeformacao[0][2]
			matrizDeformacao[2][1] = matrizDeformacao[1][2]
			
		if (tipoTensor == 2):
			#TENSOR DE DEFORMAÇÃO 
			matrizDeformacao = [[0,0,0],[0,0,0],[0,0,0]]
			matrizDeformacao = matriz
			
			#TENSOR TENSAO
			matrizTensao[0][0] = (E/((1+ni)*(1-2*ni)))*(((1-ni)*matrizDeformacao[0][0])+(ni*(matrizDeformacao[1][1]+matrizDeformacao[2][2])))
			matrizTensao[1][1] = (E/((1+ni)*(1-2*ni)))*(((1-ni)*matrizDeformacao[1][1])+(ni*(matrizDeformacao[0][0]+matrizDeformacao[2][2])))
			matrizTensao[2][2] = (E/((1+ni)*(1-2*ni)))*(((1-ni)*matrizDeformacao[2][2])+(ni*(matrizDeformacao[1][1]+matrizDeformacao[0][0])))
			
			if (tipoDeformacao == 1): #angular
				matrizTensao[0][1] = matrizDeformacao[0][1]*G
				matrizTensao[0][2] = matrizDeformacao[0][2]*G
				matrizTensao[1][2] = matrizDeformacao[1][2]*G
			elif (tipoDeformacao == 2): #linear
				matrizTensao[0][1] = 2*matrizDeformacao[0][1]*G
				matrizTensao[0][2] = 2*matrizDeformacao[0][2]*G
				matrizTensao[1][2] = 2*matrizDeformacao[1][2]*G
			matrizTensao[1][0] = matrizTensao[0][1]
			matrizTensao[2][0] = matrizTensao[0][2]
			matrizTensao[2][1] = matrizTensao[1][2]
			
		
		# INVARIANTES DE Sigma_ij:
		I1 = matrizTensao[0][0] + matrizTensao[1][1] + matrizTensao[2][2]
		I2 = (matrizTensao[0][0]*matrizTensao[1][1]-pow(matrizTensao[0][1],2)) + (matrizTensao[0][0]*matrizTensao[2][2]-pow(matrizTensao[0][2],2)) + (matrizTensao[1][1]*matrizTensao[2][2]-pow(matrizTensao[1][2],2))
		I3 = (matrizTensao[0][0]*matrizTensao[1][1]*matrizTensao[2][2] + matrizTensao[0][1]*matrizTensao[1][2]*matrizTensao[2][0] + matrizTensao[0][2]*matrizTensao[1][0]*matrizTensao[2][1]) - (matrizTensao[2][0]*matrizTensao[1][1]*matrizTensao[0][2] + matrizTensao[2][1]*matrizTensao[1][2]*matrizTensao[0][0] + matrizTensao[2][2]*matrizTensao[1][0]*matrizTensao[0][1])
		
		#TENSOR DEVITÓRICO S_ij:
		sig_n = I1/3
		for i in range (3):
			for j in range (3):
				matrizDevitorico[i][j] = matrizTensao[i][j] - sig_n*mat_cron[i][j]
		
		# INVARIANTES DE S_ij:
		J2 = (1/3) * (pow(I1,2)-3*I2) 
		J3 = (1/27) * (2*pow(I1,3)-9*I1*I2+27*I3)
		
		# INVARIANTE DE COS
		cos3teta = ((3*sqrt(3))/2)*(J3/(sqrt(pow(J2,3))))
		teta3 = acos(cos3teta) #guarda variavel
		teta = teta3 / 3
		
		#TENSÕES PRINCIPAIS:
		sig1 = sig_n + (2/sqrt(3))*sqrt(J2) * cos(teta)
		sig2 = sig_n + (2/sqrt(3))*sqrt(J2) * cos(teta-(2*pi)/3)
		sig3 = sig_n + (2/sqrt(3))*sqrt(J2) * cos(teta+(2*pi)/3)
					
		# DEFORMAÇÕES PRINCIPAIS
		def1 = (1/E)*(sig1 - ni*(sig2+sig3))
		def2 = (1/E)*(sig2 - ni*(sig1+sig3))
		def3 = (1/E)*(sig3 - ni*(sig2+sig1))
		gamamax = def1 - def3

	if (Dimensao==2):
		mat_cron = [[1,0,0],[0,1,0],[0,0,1]]
		if (estadoPlano==1): #estadoPlanoT
			if (tipoTensor==1): #TENSAO
				#TENSOR DE TENSÃO
				for i in range (3):
					for j in range (3):
						matrizTensao[i][j] = matriz[i][j]
				
				#TENSOR DE DEFORMAÇÃO
				matrizDeformacao[0][0] = (1/E)*(matrizTensao[0][0] - ni*matrizTensao[1][1])
				matrizDeformacao[1][1] = (1/E)*(matrizTensao[1][1] - ni*matrizTensao[0][0])
				
				if (tipoDeformacao==1):
					matrizDeformacao[0][1] = matrizTensao[0][1]/G
				
				if (tipoDeformacao==2):
					matrizDeformacao[0][1] = matrizTensao[0][1]/(2*G)
					
				matrizDeformacao[1][0] = matrizDeformacao[0][1]
				matrizDeformacao[2][2] = (-ni/E)*(matrizTensao[0][0] + matrizTensao[1][1])

			if (tipoTensor==2): #DEFORMAÇÃO
				#TENSOR DE DEFORMAÇÃO
				for i in range (3):
					for j in range (3):
						matrizDeformacao[i][j] = matriz[i][j]
				
				#TENSOR DE TENSÃO
				matrizTensao[0][0] = (E/pow((1-ni),2))*(matrizDeformacao[0][0] + ni*matrizDeformacao[1][1])
				matrizTensao[1][1] = (E/pow((1-ni),2))*(matrizDeformacao[1][1] + ni*matrizDeformacao[0][0])
				
				if (tipoDeformacao==1):
					matrizTensao[0][1] = G*matrizDeformacao[0][1]
				
				if (tipoDeformacao==2):
					matrizTensao[0][1] = G*matrizDeformacao[0][1]*2
				
				matrizTensao[1][0] = matrizTensao[0][1]
			
			#INVARIANTES TENSAO 
			I1 = matrizTensao[0][0] + matrizTensao[1][1]
			I2 = (matrizTensao[0][0]*matrizTensao[1][1]-pow(matrizTensao[0][1],2)) + (matrizTensao[0][0]*matrizTensao[2][2]-pow(matrizTensao[0][2],2)) + (matrizTensao[1][1]*matrizTensao[2][2]-pow(matrizTensao[1][2],2))
			I3 = (matrizTensao[0][0]*matrizTensao[1][1]*matrizTensao[2][2] + matrizTensao[0][1]*matrizTensao[1][2]*matrizTensao[2][0] + matrizTensao[0][2]*matrizTensao[1][0]*matrizTensao[2][1]) - (matrizTensao[2][0]*matrizTensao[1][1]*matrizTensao[0][2] + matrizTensao[2][1]*matrizTensao[1][2]*matrizTensao[0][0] + matrizTensao[2][2]*matrizTensao[1][0]*matrizTensao[0][1])

			#TENSOR DEVITÓRICO
			sig_n = I1/2
			for i in range (3):
				for j in range (3):
					matrizDevitorico[i][j] = matrizTensao[i][j] - sig_n*mat_cron[i][j]
			
			#IVARIANTES DEVITORICO
			J2 = 1/3 * (pow(I1,2) - 3*I2)
			J3 = 1/27 * (2*pow(I1,3) - 9*I1*I2 + 27*I3)
			
			# INVARIANTE DE COS
			cos3teta = ((3*sqrt(3))/2)*(J3/(sqrt(pow(J2,3))))
			teta3 = acos(cos3teta) #guarda variavel
			teta = teta3 / 3
			
			#TENSÕES PRINCIPAIS
			sig1 = ((matrizTensao[0][0] + matrizTensao[1][1])/2) + sqrt(pow(((matrizTensao[0][0] - matrizTensao[1][1])/2),2) + pow(matrizTensao[0][1],2))
			sig2 = ((matrizTensao[0][0] + matrizTensao[1][1])/2) - sqrt(pow(((matrizTensao[0][0] - matrizTensao[1][1])/2),2) + pow(matrizTensao[0][1],2))
			sig3 = 0
			
			#DEFORMAÇÕES PRINCIPAIS
			def1 = (1/E)*(sig1 - ni*(sig2+sig3))
			def2 = (1/E)*(sig2 - ni*(sig1+sig3))
			def3 = (1/E)*(sig3 - ni*(sig2+sig1))
			
			#GAMA_MAX
			gamamax = def1 - def3
		if (estadoPlano==2): #estadoPlanoD
			if (tipoTensor==1): #TENSAO
				#TENSOR DE TENSÃO
				for i in range (Dimensao):
					for j in range (Dimensao):
						matrizTensao[i][j] = matriz[i][j]
				matrizTensao[2][2] = ni*(matrizTensao[0][0] + matrizTensao[1][1])
				#TENSOR DE DEFORMAÇÃO
				matrizDeformacao[0][0] = (1/E)*(matrizTensao[0][0] - ni*(matrizTensao[1][1] + matrizTensao[2][2]))
				matrizDeformacao[1][1] = (1/E)*(matrizTensao[1][1] - ni*(matrizTensao[0][0] + matrizTensao[2][2]))
				
				if (tipoDeformacao==1):
					matrizDeformacao[0][1] = matrizTensao[0][1]/G
				
				if (tipoDeformacao==2):
					matrizDeformacao[0][1] = matrizTensao[0][1]/(2*G)
					
				matrizDeformacao[1][0] = matrizDeformacao[0][1]

			if (tipoTensor==2): #DEFORMAÇÃO
				#TENSOR DE DEFORMAÇÃO
				for i in range (Dimensao):
					for j in range (Dimensao):
						matrizDeformacao[i][j] = matriz[i][j]
				#TENSOR DE TENSÃO
				matrizTensao[0][0] = (E/((1+ni)*(1-2*ni)))*((1-ni)*matrizDeformacao[0][0] + ni*matrizDeformacao[1][1])
				matrizTensao[1][1] = (E/((1+ni)*(1-2*ni)))*((1-ni)*matrizDeformacao[1][1] + ni*matrizDeformacao[0][0])
				matrizTensao[2][2] = ni*(matrizTensao[0][0] + matrizTensao[1][1])
				
				if (tipoDeformacao==1):
					matrizTensao[0][1] = G*matrizDeformacao[0][1]
				
				if (tipoDeformacao==2):
					matrizTensao[0][1] = G*matrizDeformacao[0][1]*2
				
				matrizTensao[1][0] = matrizTensao[0][1]
			
			#INVARIANTES TENSAO 
			I1 = matrizTensao[0][0] + matrizTensao[1][1] + matrizTensao[2][2]
			I2 = (matrizTensao[0][0]*matrizTensao[1][1]-pow(matrizTensao[0][1],2)) + (matrizTensao[0][0]*matrizTensao[2][2]-pow(matrizTensao[0][2],2)) + (matrizTensao[1][1]*matrizTensao[2][2]-pow(matrizTensao[1][2],2))
			I3 = (matrizTensao[0][0]*matrizTensao[1][1]*matrizTensao[2][2] + matrizTensao[0][1]*matrizTensao[1][2]*matrizTensao[2][0] + matrizTensao[0][2]*matrizTensao[1][0]*matrizTensao[2][1]) - (matrizTensao[2][0]*matrizTensao[1][1]*matrizTensao[0][2] + matrizTensao[2][1]*matrizTensao[1][2]*matrizTensao[0][0] + matrizTensao[2][2]*matrizTensao[1][0]*matrizTensao[0][1])

			#TENSOR DEVITÓRICO
			sig_n = I1/3
			for i in range (3):
				for j in range (3):
					matrizDevitorico[i][j] = matrizTensao[i][j] - sig_n*mat_cron[i][j]

			#IVARIANTES DEVITORICO
			J2 = (pow(I1,2) - 3*I2)/3
			J3 = (2*pow(I1,3) - 9*I1*I2 + 27*I3)/27
			
			#TENSÕES PRINCIPAIS
			sig1 = ((matrizTensao[0][0] + matrizTensao[1][1])/2) + sqrt(pow(((matrizTensao[0][0] - matrizTensao[1][1])/2),2) + pow(matrizTensao[0][1],2))
			sig2 = ((matrizTensao[0][0] + matrizTensao[1][1])/2) - sqrt(pow(((matrizTensao[0][0] - matrizTensao[1][1])/2),2) + pow(matrizTensao[0][1],2))
			sig3 = matrizTensao[2][2]
		
			# INVARIANTE DE COS
			cos3teta = ((3*sqrt(3))/2)*(J3/(sqrt(pow(J2,3))))
			teta3 = acos(cos3teta) #guarda variavel
			teta = teta3 / 3
			
			#DEFORMAÇÕES PRINCIPAIS
			def1 = (1/E)*(sig1 - ni*(sig2+sig3))
			def2 = (1/E)*(sig2 - ni*(sig1+sig3))
			def3 = (1/E)*(sig3 - ni*(sig2+sig1))
			
			#GAMA_MAX
			gamamax = def1 - def2
	#Reposionar
	if sig1>= sig2 and sig1>=sig3:
		if sig2>=sig3:
			s1=sig1
			s2=sig2
			s3=sig3
		else:
			s1=sig1
			s2=sig3
			s3=sig2
	elif sig2>= sig1 and sig2>=sig3:
		if sig1>=sig3:
			s1=sig2
			s2=sig1
			s3=sig3
		else:
			s1=sig2
			s2=sig3
			s3=sig1
	elif sig3>= sig2 and sig3>=sig1:
		if sig2>=sig1:
			s1=sig3
			s2=sig2
			s3=sig1
		else:
			s1=sig3
			s2=sig1
			s3=sig2

	#TAU MAX
	tau_max = abs((s1 - s3)/2)
	# TENSÃO EQUIVALENTE DE TRESCA: 
	tresca = 2 * tau_max

	# TENSÃO EQUIV. DE von MISES: 
	mises = sqrt(3*J2)

	#ESCOOU
	if (tresca <= fy):
		fraset = str("Estavel, não há escoamento")
	elif (tresca > fy):
		fraset = str("Instavel, há escoamento")
	if (mises <= fy):
		frasem = str("Estavel, não há escoamento")
	elif (mises > fy):
		frasem = str("Instavel, há escoamento")

	salvar(Arquivo,matrizTensao,matrizDevitorico,I1,I2,I3,J2,J3,cos3teta,s1,s2,s3,tau_max,fy,gama,ni,E,matrizDeformacao,def1,def2,def3,gamamax,tresca,mises,fraset,frasem,unidade)

principal()
