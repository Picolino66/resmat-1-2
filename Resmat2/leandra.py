from math import atan,sin,cos,radians, degrees , acos , pi ,sqrt

nomeArq = input("Digite o nome do arquivo de entrada: ") 
entrada = open(nomeArq + ".dat", 'r') 

dimensao = int(entrada.readline())
tt = int(entrada.readline())
ep = int(entrada.readline())
td = int(entrada.readline())
mat = [[0,0,0],[0,0,0],[0,0,0]]
matrizAux = []
matDefor = [[0,0,0],[0,0,0],[0,0,0]]
matTensao = [[0,0,0],[0,0,0],[0,0,0]]
matDevi = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(dimensao):
	aux = list(map(float, entrada.readline().split()))
	matrizAux.append(aux)
for i in range(dimensao):
	for j in range(dimensao):
		mat[i][j] = matrizAux[i][j]
fy = float(entrada.readline())
E = float(entrada.readline())
ni = float(entrada.readline())
gama = float(entrada.readline())
unidade = str(entrada.readline())

G = E/(2*(1+ni))
if (dimensao==2):
	matPrincipal = [[1,0,0],[0,1,0],[0,0,1]]
	if (ep==1): #EPT
		if (tt==1): #TENSAO
			#TENSOR DE TENSÃO
			for i in range (3):
				for j in range (3):
					matTensao[i][j] = mat[i][j]
			
			#TENSOR DE DEFORMAÇÃO
			matDefor[0][0] = (1/E)*(matTensao[0][0] - ni*matTensao[1][1])
			matDefor[1][1] = (1/E)*(matTensao[1][1] - ni*matTensao[0][0])
			
			if (td==1):
				matDefor[0][1] = matTensao[0][1]/G
			
			if (td==2):
				matDefor[0][1] = matTensao[0][1]/(2*G)
				
			matDefor[1][0] = matDefor[0][1]
			matDefor[2][2] = (-ni/E)*(matTensao[0][0] + matTensao[1][1])

		if (tt==2): #DEFORMAÇÃO
			#TENSOR DE DEFORMAÇÃO
			for i in range (3):
				for j in range (3):
					matDefor[i][j] = mat[i][j]
			
			#TENSOR DE TENSÃO
			matTensao[0][0] = (E/pow((1-ni),2))*(matDefor[0][0] + ni*matDefor[1][1])
			matTensao[1][1] = (E/pow((1-ni),2))*(matDefor[1][1] + ni*matDefor[0][0])
			
			if (td==1):
				matTensao[0][1] = G*matDefor[0][1]
			
			if (td==2):
				matTensao[0][1] = G*matDefor[0][1]*2
			
			matTensao[1][0] = matTensao[0][1]
		
		#INVARIANTES TENSAO 
		I1 = matTensao[0][0] + matTensao[1][1]
		I2 = (matTensao[0][0]*matTensao[1][1]-pow(matTensao[0][1],2)) + (matTensao[0][0]*matTensao[2][2]-pow(matTensao[0][2],2)) + (matTensao[1][1]*matTensao[2][2]-pow(matTensao[1][2],2))
		I3 = (matTensao[0][0]*matTensao[1][1]*matTensao[2][2] + matTensao[0][1]*matTensao[1][2]*matTensao[2][0] + matTensao[0][2]*matTensao[1][0]*matTensao[2][1]) - (matTensao[2][0]*matTensao[1][1]*matTensao[0][2] + matTensao[2][1]*matTensao[1][2]*matTensao[0][0] + matTensao[2][2]*matTensao[1][0]*matTensao[0][1])

		#TENSOR DEVITÓRICO
		sig_n = I1/2
		for i in range (3):
			for j in range (3):
				matDevi[i][j] = matTensao[i][j] - sig_n*matPrincipal[i][j]
		
		#IVARIANTES DEVITORICO
		J2 = 1/3 * (pow(I1,2) - 3*I2)
		J3 = 1/27 * (2*pow(I1,3) - 9*I1*I2 + 27*I3)
		
		# INVARIANTE DE COS
		cos3teta = ((3*sqrt(3))/2)*(J3/(sqrt(pow(J2,3))))
		teta3 = acos(cos3teta) #guarda variavel
		teta = teta3 / 3
		
		#TENSÕES PRINCIPAIS
		sig1 = ((matTensao[0][0] + matTensao[1][1])/2) + sqrt(pow(((matTensao[0][0] - matTensao[1][1])/2),2) + pow(matTensao[0][1],2))
		sig2 = ((matTensao[0][0] + matTensao[1][1])/2) - sqrt(pow(((matTensao[0][0] - matTensao[1][1])/2),2) + pow(matTensao[0][1],2))
		sig3 = 0
		
		#DEFORMAÇÕES PRINCIPAIS
		def1 = (1/E)*(sig1 - ni*(sig2+sig3))
		def2 = (1/E)*(sig2 - ni*(sig1+sig3))
		def3 = (1/E)*(sig3 - ni*(sig2+sig1))
		
		#GAMA_MAX
		gamamax = def1 - def3
	if (ep==2): #EPD
		if (tt==1): #TENSAO
			#TENSOR DE TENSÃO
			for i in range (dimensao):
				for j in range (dimensao):
					matTensao[i][j] = mat[i][j]
			matTensao[2][2] = ni*(matTensao[0][0] + matTensao[1][1])
			#TENSOR DE DEFORMAÇÃO
			matDefor[0][0] = (1/E)*(matTensao[0][0] - ni*(matTensao[1][1] + matTensao[2][2]))
			matDefor[1][1] = (1/E)*(matTensao[1][1] - ni*(matTensao[0][0] + matTensao[2][2]))
			
			if (td==1):
				matDefor[0][1] = matTensao[0][1]/G
			
			if (td==2):
				matDefor[0][1] = matTensao[0][1]/(2*G)
				
			matDefor[1][0] = matDefor[0][1]

		if (tt==2): #DEFORMAÇÃO
			#TENSOR DE DEFORMAÇÃO
			for i in range (dimensao):
				for j in range (dimensao):
					matDefor[i][j] = mat[i][j]
			#TENSOR DE TENSÃO
			matTensao[0][0] = (E/((1+ni)*(1-2*ni)))*((1-ni)*matDefor[0][0] + ni*matDefor[1][1])
			matTensao[1][1] = (E/((1+ni)*(1-2*ni)))*((1-ni)*matDefor[1][1] + ni*matDefor[0][0])
			matTensao[2][2] = ni*(matTensao[0][0] + matTensao[1][1])
			
			if (td==1):
				matTensao[0][1] = G*matDefor[0][1]
			
			if (td==2):
				matTensao[0][1] = G*matDefor[0][1]*2
			
			matTensao[1][0] = matTensao[0][1]
		
		#INVARIANTES TENSAO 
		I1 = matTensao[0][0] + matTensao[1][1] + matTensao[2][2]
		I2 = (matTensao[0][0]*matTensao[1][1]-pow(matTensao[0][1],2)) + (matTensao[0][0]*matTensao[2][2]-pow(matTensao[0][2],2)) + (matTensao[1][1]*matTensao[2][2]-pow(matTensao[1][2],2))
		I3 = (matTensao[0][0]*matTensao[1][1]*matTensao[2][2] + matTensao[0][1]*matTensao[1][2]*matTensao[2][0] + matTensao[0][2]*matTensao[1][0]*matTensao[2][1]) - (matTensao[2][0]*matTensao[1][1]*matTensao[0][2] + matTensao[2][1]*matTensao[1][2]*matTensao[0][0] + matTensao[2][2]*matTensao[1][0]*matTensao[0][1])

		#TENSOR DEVITÓRICO
		sig_n = I1/3
		for i in range (3):
			for j in range (3):
				matDevi[i][j] = matTensao[i][j] - sig_n*matPrincipal[i][j]

		#IVARIANTES DEVITORICO
		J2 = (pow(I1,2) - 3*I2)/3
		J3 = (2*pow(I1,3) - 9*I1*I2 + 27*I3)/27
		
		#TENSÕES PRINCIPAIS
		sig1 = ((matTensao[0][0] + matTensao[1][1])/2) + sqrt(pow(((matTensao[0][0] - matTensao[1][1])/2),2) + pow(matTensao[0][1],2))
		sig2 = ((matTensao[0][0] + matTensao[1][1])/2) - sqrt(pow(((matTensao[0][0] - matTensao[1][1])/2),2) + pow(matTensao[0][1],2))
		sig3 = matTensao[2][2]
	
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

if (dimensao == 3): #3d
	matPrincipal = [[1,0,0],[0,1,0],[0,0,1]]
	if (tt == 1): #tensao
		# TENSOR TENSAO
		matTensao = [[0,0,0],[0,0,0],[0,0,0]]
		matTensao = mat
		#TENSOR DE DEFORMAÇÃO 
		matDefor[0][0] = (1/E)*(matTensao[0][0] - ni*(matTensao[1][1]+matTensao[2][2]))
		matDefor[1][1] = (1/E)*(matTensao[1][1] - ni*(matTensao[0][0]+matTensao[2][2]))
		matDefor[2][2] = (1/E)*(matTensao[2][2] - ni*(matTensao[1][1]+matTensao[0][0]))
		
		if (td == 1): #angular
			matDefor[0][1] = matTensao[0][1]/G
			matDefor[0][2] = matTensao[0][2]/G
			matDefor[1][2] = matTensao[1][2]/G
		elif (td == 2): #linear
			matDefor[0][1] = matTensao[0][1]/(2*G)
			matDefor[0][2] = matTensao[0][2]/(2*G)
			matDefor[1][2] = matTensao[1][2]/(2*G)
		matDefor[1][0] = matDefor[0][1]
		matDefor[2][0] = matDefor[0][2]
		matDefor[2][1] = matDefor[1][2]
		
	if (tt == 2):
		#TENSOR DE DEFORMAÇÃO 
		matDefor = [[0,0,0],[0,0,0],[0,0,0]]
		matDefor = mat
		
		#TENSOR TENSAO
		matTensao[0][0] = (E/((1+ni)*(1-2*ni)))*(((1-ni)*matDefor[0][0])+(ni*(matDefor[1][1]+matDefor[2][2])))
		matTensao[1][1] = (E/((1+ni)*(1-2*ni)))*(((1-ni)*matDefor[1][1])+(ni*(matDefor[0][0]+matDefor[2][2])))
		matTensao[2][2] = (E/((1+ni)*(1-2*ni)))*(((1-ni)*matDefor[2][2])+(ni*(matDefor[1][1]+matDefor[0][0])))
		
		if (td == 1): #angular
			matTensao[0][1] = matDefor[0][1]*G
			matTensao[0][2] = matDefor[0][2]*G
			matTensao[1][2] = matDefor[1][2]*G
		elif (td == 2): #linear
			matTensao[0][1] = 2*matDefor[0][1]*G
			matTensao[0][2] = 2*matDefor[0][2]*G
			matTensao[1][2] = 2*matDefor[1][2]*G
		matTensao[1][0] = matTensao[0][1]
		matTensao[2][0] = matTensao[0][2]
		matTensao[2][1] = matTensao[1][2]
		
	
	# INVARIANTES DE Sigma_ij:
	I1 = matTensao[0][0] + matTensao[1][1] + matTensao[2][2]
	I2 = (matTensao[0][0]*matTensao[1][1]-pow(matTensao[0][1],2)) + (matTensao[0][0]*matTensao[2][2]-pow(matTensao[0][2],2)) + (matTensao[1][1]*matTensao[2][2]-pow(matTensao[1][2],2))
	I3 = (matTensao[0][0]*matTensao[1][1]*matTensao[2][2] + matTensao[0][1]*matTensao[1][2]*matTensao[2][0] + matTensao[0][2]*matTensao[1][0]*matTensao[2][1]) - (matTensao[2][0]*matTensao[1][1]*matTensao[0][2] + matTensao[2][1]*matTensao[1][2]*matTensao[0][0] + matTensao[2][2]*matTensao[1][0]*matTensao[0][1])
	
	#TENSOR DEVITÓRICO S_ij:
	sig_n = I1/3
	for i in range (3):
		for j in range (3):
			matDevi[i][j] = matTensao[i][j] - sig_n*matPrincipal[i][j]
	
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
		
saida = open(nomeArq + ".out", 'w') # abre arq 

#f = open("arq2.txt", 'w')
saida.write("    \n")
saida.write("                      **** ANÁLISE DO TENSOR DE TENSÃO E CRITÉRIOS DE ESCOAMENTO **** \n")
saida.write("    \n")
saida.write("    \n")
saida.write("arquivo de dados :            " + nomeArq + ".out" '\n')
saida.write("    \n")
saida.write("    \n")
saida.write("Tensor de Tensão Sigma_ij:                " + '\n')
saida.write("|  " +'{:e}'.format( matTensao[0][0])+"  " +'{:e}'.format( matTensao[0][1]) +"  " +'{:e}'.format( matTensao[0][2]) +"|" + '\n')
saida.write("|  " +'{:e}'.format( matTensao[1][0])+"  " +'{:e}'.format( matTensao[1][1]) +"  " +'{:e}'.format( matTensao[1][2]) +"|" + unidade+ '\n')
saida.write("|  " +'{:e}'.format( matTensao[2][0])+"  " +'{:e}'.format( matTensao[2][1]) +"  " +'{:e}'.format( matTensao[2][2]) +"|" +  '\n')
saida.write("    \n")
saida.write("Tensor Desviatório S_ij :                    " +'\n')
saida.write("|  " +'{:e}'.format( matDevi[0][0])+"  " +'{:e}'.format( matDevi[0][1]) +"  " +'{:e}'.format( matDevi[0][2]) +"|" '\n')
saida.write("|  " +'{:e}'.format( matDevi[1][0])+"  " +'{:e}'.format( matDevi[1][1]) +"  " +'{:e}'.format( matDevi[1][2]) +"|" + unidade+ '\n')
saida.write("|  " +'{:e}'.format( matDevi[2][0])+"  " +'{:e}'.format( matDevi[2][1]) +"  " +'{:e}'.format( matDevi[2][2]) +"|" +  '\n')
saida.write("    \n")
saida.write("Invariantes de Sigma_ij              " '\n')
saida.write("    \n")
saida.write("i1:                " +'{:e}'.format(I1 )+ unidade+ '\n')
saida.write("    \n")
saida.write("i2:                " +'{:e}'.format(I2 )+ unidade+ "²"'\n')
saida.write("    \n")
saida.write("i3:                " +'{:e}'.format(I3 )+ unidade+ "³"'\n')
saida.write("    \n")
saida.write("    \n")
saida.write("Invariantes de S_ij              " '\n')
saida.write("    \n")
saida.write("J2:                " +'{:e}'.format(J2 )+ unidade+ "²"'\n')
saida.write("    \n")
saida.write("J3:                " +'{:e}'.format(J3 )+ unidade+ "³"'\n')
saida.write("    \n")
saida.write("Invariante COS(3Teta)             " '\n')
saida.write("cos(3teta)=              " +'{:e}'.format(cos3teta)+'\n')
saida.write("    \n")
saida.write("    \n")
saida.write("Tensões Principais             " '\n')
saida.write("Sig1=            " +'{:e}'.format(s1 )+ unidade+ '\n')
saida.write("Sig2=             " +'{:e}'.format(s2) + unidade+ '\n')
saida.write("Sig3=            " +'{:e}'.format(s3) + unidade+ '\n')
saida.write("TauMx=            " +'{:e}'.format(tau_max) + unidade+ '\n')
saida.write("    \n")
saida.write("    \n")
saida.write("Parâmetros do Material           " '\n')
saida.write("    \n")
saida.write("fy=            " +'{:e}'.format(fy )+ unidade+ '\n')
saida.write("Gama_mat=             " +'{:e}'.format(gama) + '\n')
saida.write("Rel.Poisson        " +'{:e}'.format(ni) + '\n')
saida.write("Mód.Young           " +'{:e}'.format(E) + unidade+ '\n')
saida.write("    \n")
saida.write("    \n")
saida.write("    \n")
saida.write("Tensor de deformação Epsilon_ij           " '\n')
saida.write("|  " +'{:e}'.format( matDefor[0][0])+"  " +'{:e}'.format( matDefor[0][1]) +"  " +'{:e}'.format( matDefor[0][2]) +"|" + '\n')
saida.write("|  " +'{:e}'.format( matDefor[1][0])+"  " +'{:e}'.format( matDefor[1][1]) +"  " +'{:e}'.format( matDefor[1][2]) +"|" +  '\n')
saida.write("|  " +'{:e}'.format( matDefor[2][0])+"  " +'{:e}'.format( matDefor[2][1]) +"  " +'{:e}'.format( matDefor[2][2]) +"|" +  '\n')
saida.write("    \n")
saida.write("Deformações Principais             " '\n')
saida.write("Eps1=            " +'{:e}'.format(def1 )+  '\n')
saida.write("Eps2=             " +'{:e}'.format(def2) + '\n')
saida.write("Eps3=            " +'{:e}'.format(def3) + '\n')
saida.write("Gama_Mx=            " +'{:e}'.format(gamamax) + '\n')
saida.write("Tensão Equivalente de tresca            " '\n')
saida.write("2 Tau_mx=       " +'{:e}'.format(tresca) + unidade+ '\n')
saida.write("    \n")
saida.write("Tensão Equivalente de Von Mises           " '\n')
saida.write("Sig_Eq=       " +'{:e}'.format(mises) + unidade+ '\n')
saida.write("    \n")
#ESCOOU
if (tresca <= fy):
	saida.write("Estavel, nao ha escoamento")
elif (tresca > fy):
	saida.write("Instavel, ha escoamento")
if (mises <= fy):
	saida.write("Estavel, nao ha escoamento")
elif (mises > fy):
	saida.write("Instavel, ha escoamento")

				
