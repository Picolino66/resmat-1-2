from math import atan,sin,cos,radians, degrees , acos , pi ,sqrt
import datetime #biblioteca de hora e data

def salvar(Arquivo,matT,matDev,I1,I2,I3,J2,J3,cos3teta,s1,s2,s3,tau_max,fy,gama,ni,E,matDef,def1,def2,def3,gamamax,tresca,mises,fraset,frasem,unidade):
	data_atual = datetime.datetime.now() #pega hora e data
	salvar = open(Arquivo + ".out", 'w') # abre arq 
	#salvar = open("arq2.txt", 'w')
	salvar.write("    \n")
	salvar.write("                      **** ANÁLISE DO TENSOR DE TENSÃO E CRITÉRIOS DE ESCOAMENTO **** \n")
	salvar.write("    \n")
	salvar.write ("\n")
	salvar.write ("		Data do Processamento:		")
	salvar.write(str(data_atual.day))
	salvar.write("/")
	salvar.write(str(data_atual.month))
	salvar.write("/")
	salvar.write(str(data_atual.year))
	salvar.write(" ")
	salvar.write(str(data_atual.hour))
	salvar.write(":")
	salvar.write(str(data_atual.minute))
	salvar.write(":")
	salvar.write(str(data_atual.second))
	salvar.write ("\n")
	salvar.write("    \n")
	salvar.write("arquivo de dados :            " + Arquivo + ".out" '\n')
	salvar.write("    \n")
	salvar.write("    \n")
	salvar.write("Tensor de Tensão Sigma_ij:                " + '\n')
	salvar.write("|  " +'{:e}'.format(matT[0][0])+"  "+'{:e}'.format(matT[0][1]) +"  "+'{:e}'.format(matT[0][2]) +"|" + '\n')
	salvar.write("|  " +'{:e}'.format(matT[1][0])+"  "+'{:e}'.format(matT[1][1]) +"  "+'{:e}'.format(matT[1][2]) +"|" + unidade+ '\n')
	salvar.write("|  " +'{:e}'.format(matT[2][0])+"  "+'{:e}'.format(matT[2][1]) +"  "+'{:e}'.format(matT[2][2]) +"|" +  '\n')
	salvar.write("    \n")
	salvar.write("Tensor Desviatório S_ij :                    " +'\n')
	salvar.write("|  " +'{:e}'.format(matDev[0][0])+"  "+'{:e}'.format(matDev[0][1]) +"  "+'{:e}'.format(matDev[0][2]) +"|" '\n')
	salvar.write("|  " +'{:e}'.format(matDev[1][0])+"  "+'{:e}'.format(matDev[1][1]) +"  "+'{:e}'.format(matDev[1][2]) +"|" + unidade+ '\n')
	salvar.write("|  " +'{:e}'.format(matDev[2][0])+"  "+'{:e}'.format(matDev[2][1]) +"  "+'{:e}'.format(matDev[2][2]) +"|" +  '\n')
	salvar.write("    \n")
	salvar.write("Invariantes de Sigma_ij              " '\n')
	salvar.write("    \n")
	salvar.write("i1:                " +'{:e}'.format(I1 )+ unidade+ '\n')
	salvar.write("    \n")
	salvar.write("i2:                " +'{:e}'.format(I2 )+ unidade+ "²"'\n')
	salvar.write("    \n")
	salvar.write("i3:                " +'{:e}'.format(I3 )+ unidade+ "³"'\n')
	salvar.write("    \n")
	salvar.write("    \n")
	salvar.write("Invariantes de S_ij              " '\n')
	salvar.write("    \n")
	salvar.write("J2:                " +'{:e}'.format(J2 )+ unidade+ "²"'\n')
	salvar.write("    \n")
	salvar.write("J3:                " +'{:e}'.format(J3 )+ unidade+ "³"'\n')
	salvar.write("    \n")
	salvar.write("Invariante COS(3Teta)             " '\n')
	salvar.write("cos(3teta)=              " +'{:e}'.format(cos3teta)+'\n')
	salvar.write("    \n")
	salvar.write("    \n")
	salvar.write("Tensões Principais             " '\n')
	salvar.write("Sig1=            " +'{:e}'.format(s1 )+ unidade+ '\n')
	salvar.write("Sig2=             " +'{:e}'.format(s2) + unidade+ '\n')
	salvar.write("Sig3=            "+'{:e}'.format(s3) + unidade+ '\n')
	salvar.write("TauMx=            "+'{:e}'.format(tau_max) + unidade+ '\n')
	salvar.write("    \n")
	salvar.write("    \n")
	salvar.write("Parâmetros do Material           " '\n')
	salvar.write("    \n")
	salvar.write("fy=            " +'{:e}'.format(fy)+ unidade+ '\n')
	salvar.write("Gama_mat=             " +'{:e}'.format(gama) + '\n')
	salvar.write("Rel.Poisson        "+'{:e}'.format(ni) + '\n')
	salvar.write("Mód.Young           "+'{:e}'.format(E) + unidade+ '\n')
	salvar.write("    \n")
	salvar.write("    \n")
	salvar.write("    \n")
	salvar.write("Tensor de deformação estadoPlanosilon_ij           " '\n')
	salvar.write("|  " +'{:e}'.format(matDef[0][0])+"  "+'{:e}'.format(matDef[0][1]) +"  "+'{:e}'.format(matDef[0][2]) +"|" + '\n')
	salvar.write("|  " +'{:e}'.format(matDef[1][0])+"  "+'{:e}'.format(matDef[1][1]) +"  "+'{:e}'.format(matDef[1][2]) +"|" +  '\n')
	salvar.write("|  " +'{:e}'.format(matDef[2][0])+"  "+'{:e}'.format(matDef[2][1]) +"  "+'{:e}'.format(matDef[2][2]) +"|" +  '\n')
	salvar.write("    \n")
	salvar.write("Deformações Principais             " '\n')
	salvar.write("estadoPlanos1=            " +'{:e}'.format(def1 )+  '\n')
	salvar.write("estadoPlanos2=             " +'{:e}'.format(def2) + '\n')
	salvar.write("estadoPlanos3=            "+'{:e}'.format(def3) + '\n')
	salvar.write("Gama_Mx=            "+'{:e}'.format(gamamax) + '\n')
	salvar.write("Tensão Equivalente de tresca            " '\n')
	salvar.write("2 Tau_mx=       " +'{:e}'.format(tresca) + unidade+ '\n')
	salvar.write("    \n")
	salvar.write("Tensão Equivalente de Von Mises           " '\n')
	salvar.write("Sig_Eq=       " +'{:e}'.format(mises) + unidade+ '\n')
	salvar.write("    \n")
	salvar.write("Verificação da estabilidade:          " '\n')
	salvar.write("    \n")
	salvar.write("Critério de Tresca      " + fraset+ '\n')
	salvar.write("    \n")
	salvar.write("Critério de Von Mises      " + frasem + '\n')


def principal():
	Arquivo = input("digite nome do arquivo: ") 
	ler = open(Arquivo + ".dat", 'r') 
	Dimensao = int(ler.readline())
	tipoTensor = int(ler.readline())
	estadoPlano = int(ler.readline())
	tipoDeformacao = int(ler.readline())
	matriz = [[0,0,0],[0,0,0],[0,0,0]]
	matrizAux = []
	matDef = [[0,0,0],[0,0,0],[0,0,0]]
	matT = [[0,0,0],[0,0,0],[0,0,0]]
	matDev = [[0,0,0],[0,0,0],[0,0,0]]
	for i in range(Dimensao):
		aux = list(map(float, ler.readline().split()))
		matrizAux.append(aux)
	for i in range(Dimensao):
		for j in range(Dimensao):
			matriz[i][j] = matrizAux[i][j]
	fy = float(ler.readline())
	E = float(ler.readline())
	ni = float(ler.readline())
	gama = float(ler.readline())
	unidade = str(ler.readline())
	G = E/(2*(1+ni))
	mat_cron = [[1,0,0],[0,1,0],[0,0,1]]
	if (Dimensao == 3): #3d
		if (tipoTensor == 1): #tensao
			# TENSOR TENSAO
			matT = [[0,0,0],[0,0,0],[0,0,0]]
			matT = matriz
			#TENSOR DE DEFORMAÇÃO 
			matDef[0][0] = (1/E)*(matT[0][0] - ni*(matT[1][1]+matT[2][2]))
			matDef[1][1] = (1/E)*(matT[1][1] - ni*(matT[0][0]+matT[2][2]))
			matDef[2][2] = (1/E)*(matT[2][2] - ni*(matT[1][1]+matT[0][0]))
			
			if (tipoDeformacao == 1): #angular
				matDef[0][1] = matT[0][1]/G
				matDef[0][2] = matT[0][2]/G
				matDef[1][2] = matT[1][2]/G
			elif (tipoDeformacao == 2): #linear
				matDef[0][1] = matT[0][1]/(2*G)
				matDef[0][2] = matT[0][2]/(2*G)
				matDef[1][2] = matT[1][2]/(2*G)
			matDef[1][0] = matDef[0][1]
			matDef[2][0] = matDef[0][2]
			matDef[2][1] = matDef[1][2]
			
		if (tipoTensor == 2):
			#TENSOR DE DEFORMAÇÃO 
			matDef = [[0,0,0],[0,0,0],[0,0,0]]
			matDef = matriz
			
			#TENSOR TENSAO
			matT[0][0] = (E/((1+ni)*(1-2*ni)))*(((1-ni)*matDef[0][0])+(ni*(matDef[1][1]+matDef[2][2])))
			matT[1][1] = (E/((1+ni)*(1-2*ni)))*(((1-ni)*matDef[1][1])+(ni*(matDef[0][0]+matDef[2][2])))
			matT[2][2] = (E/((1+ni)*(1-2*ni)))*(((1-ni)*matDef[2][2])+(ni*(matDef[1][1]+matDef[0][0])))
			
			if (tipoDeformacao == 1): #angular
				matT[0][1] = matDef[0][1]*G
				matT[0][2] = matDef[0][2]*G
				matT[1][2] = matDef[1][2]*G
			elif (tipoDeformacao == 2): #linear
				matT[0][1] = 2*matDef[0][1]*G
				matT[0][2] = 2*matDef[0][2]*G
				matT[1][2] = 2*matDef[1][2]*G
			matT[1][0] = matT[0][1]
			matT[2][0] = matT[0][2]
			matT[2][1] = matT[1][2]
			
		
		# INVARIANTES DE Sigma_ij:
		I1 = matT[0][0] + matT[1][1] + matT[2][2]
		I2 = (matT[0][0]*matT[1][1]-pow(matT[0][1],2)) + (matT[0][0]*matT[2][2]-pow(matT[0][2],2)) + (matT[1][1]*matT[2][2]-pow(matT[1][2],2))
		I3 = (matT[0][0]*matT[1][1]*matT[2][2] + matT[0][1]*matT[1][2]*matT[2][0] + matT[0][2]*matT[1][0]*matT[2][1]) - (matT[2][0]*matT[1][1]*matT[0][2] + matT[2][1]*matT[1][2]*matT[0][0] + matT[2][2]*matT[1][0]*matT[0][1])
		
		#TENSOR DEVITÓRICO S_ij:
		sig_n = I1/3
		for i in range (3):
			for j in range (3):
				matDev[i][j] = matT[i][j] - sig_n*mat_cron[i][j]
		
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
						matT[i][j] = matriz[i][j]
				
				#TENSOR DE DEFORMAÇÃO
				matDef[0][0] = (1/E)*(matT[0][0] - ni*matT[1][1])
				matDef[1][1] = (1/E)*(matT[1][1] - ni*matT[0][0])
				
				if (tipoDeformacao==1):
					matDef[0][1] = matT[0][1]/G
				
				if (tipoDeformacao==2):
					matDef[0][1] = matT[0][1]/(2*G)
					
				matDef[1][0] = matDef[0][1]
				matDef[2][2] = (-ni/E)*(matT[0][0] + matT[1][1])

			if (tipoTensor==2): #DEFORMAÇÃO
				#TENSOR DE DEFORMAÇÃO
				for i in range (3):
					for j in range (3):
						matDef[i][j] = matriz[i][j]
				
				#TENSOR DE TENSÃO
				matT[0][0] = (E/pow((1-ni),2))*(matDef[0][0] + ni*matDef[1][1])
				matT[1][1] = (E/pow((1-ni),2))*(matDef[1][1] + ni*matDef[0][0])
				
				if (tipoDeformacao==1):
					matT[0][1] = G*matDef[0][1]
				
				if (tipoDeformacao==2):
					matT[0][1] = G*matDef[0][1]*2
				
				matT[1][0] = matT[0][1]
			
			#INVARIANTES TENSAO 
			I1 = matT[0][0] + matT[1][1]
			I2 = (matT[0][0]*matT[1][1]-pow(matT[0][1],2)) + (matT[0][0]*matT[2][2]-pow(matT[0][2],2)) + (matT[1][1]*matT[2][2]-pow(matT[1][2],2))
			I3 = (matT[0][0]*matT[1][1]*matT[2][2] + matT[0][1]*matT[1][2]*matT[2][0] + matT[0][2]*matT[1][0]*matT[2][1]) - (matT[2][0]*matT[1][1]*matT[0][2] + matT[2][1]*matT[1][2]*matT[0][0] + matT[2][2]*matT[1][0]*matT[0][1])

			#TENSOR DEVITÓRICO
			sig_n = I1/2
			for i in range (3):
				for j in range (3):
					matDev[i][j] = matT[i][j] - sig_n*mat_cron[i][j]
			
			#IVARIANTES DEVITORICO
			J2 = 1/3 * (pow(I1,2) - 3*I2)
			J3 = 1/27 * (2*pow(I1,3) - 9*I1*I2 + 27*I3)
			
			# INVARIANTE DE COS
			cos3teta = ((3*sqrt(3))/2)*(J3/(sqrt(pow(J2,3))))
			teta3 = acos(cos3teta) #guarda variavel
			teta = teta3 / 3
			
			#TENSÕES PRINCIPAIS
			sig1 = ((matT[0][0] + matT[1][1])/2) + sqrt(pow(((matT[0][0] - matT[1][1])/2),2) + pow(matT[0][1],2))
			sig2 = ((matT[0][0] + matT[1][1])/2) - sqrt(pow(((matT[0][0] - matT[1][1])/2),2) + pow(matT[0][1],2))
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
						matT[i][j] = matriz[i][j]
				matT[2][2] = ni*(matT[0][0] + matT[1][1])
				#TENSOR DE DEFORMAÇÃO
				matDef[0][0] = (1/E)*(matT[0][0] - ni*(matT[1][1] + matT[2][2]))
				matDef[1][1] = (1/E)*(matT[1][1] - ni*(matT[0][0] + matT[2][2]))
				
				if (tipoDeformacao==1):
					matDef[0][1] = matT[0][1]/G
				
				if (tipoDeformacao==2):
					matDef[0][1] = matT[0][1]/(2*G)
					
				matDef[1][0] = matDef[0][1]

			if (tipoTensor==2): #DEFORMAÇÃO
				#TENSOR DE DEFORMAÇÃO
				for i in range (Dimensao):
					for j in range (Dimensao):
						matDef[i][j] = matriz[i][j]
				#TENSOR DE TENSÃO
				matT[0][0] = (E/((1+ni)*(1-2*ni)))*((1-ni)*matDef[0][0] + ni*matDef[1][1])
				matT[1][1] = (E/((1+ni)*(1-2*ni)))*((1-ni)*matDef[1][1] + ni*matDef[0][0])
				matT[2][2] = ni*(matT[0][0] + matT[1][1])
				
				if (tipoDeformacao==1):
					matT[0][1] = G*matDef[0][1]
				
				if (tipoDeformacao==2):
					matT[0][1] = G*matDef[0][1]*2
				
				matT[1][0] = matT[0][1]
			
			#INVARIANTES TENSAO 
			I1 = matT[0][0] + matT[1][1] + matT[2][2]
			I2 = (matT[0][0]*matT[1][1]-pow(matT[0][1],2)) + (matT[0][0]*matT[2][2]-pow(matT[0][2],2)) + (matT[1][1]*matT[2][2]-pow(matT[1][2],2))
			I3 = (matT[0][0]*matT[1][1]*matT[2][2] + matT[0][1]*matT[1][2]*matT[2][0] + matT[0][2]*matT[1][0]*matT[2][1]) - (matT[2][0]*matT[1][1]*matT[0][2] + matT[2][1]*matT[1][2]*matT[0][0] + matT[2][2]*matT[1][0]*matT[0][1])

			#TENSOR DEVITÓRICO
			sig_n = I1/3
			for i in range (3):
				for j in range (3):
					matDev[i][j] = matT[i][j] - sig_n*mat_cron[i][j]

			#IVARIANTES DEVITORICO
			J2 = (pow(I1,2) - 3*I2)/3
			J3 = (2*pow(I1,3) - 9*I1*I2 + 27*I3)/27
			
			#TENSÕES PRINCIPAIS
			sig1 = ((matT[0][0] + matT[1][1])/2) + sqrt(pow(((matT[0][0] - matT[1][1])/2),2) + pow(matT[0][1],2))
			sig2 = ((matT[0][0] + matT[1][1])/2) - sqrt(pow(((matT[0][0] - matT[1][1])/2),2) + pow(matT[0][1],2))
			sig3 = matT[2][2]
		
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

	salvar(Arquivo,matT,matDev,I1,I2,I3,J2,J3,cos3teta,s1,s2,s3,tau_max,fy,gama,ni,E,matDef,def1,def2,def3,gamamax,tresca,mises,fraset,frasem,unidade)

principal()
