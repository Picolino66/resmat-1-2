from math import atan,sin,cos,radians, degrees , acos , pi ,sqrt
import datetime
now = datetime.datetime.now()
nomeArq = input("digite nome do arquivo: ") 
carregar = open(nomeArq + ".dat", 'r') 

dim = int(carregar.readline())
tt = int(carregar.readline())
ep = int(carregar.readline())
td = int(carregar.readline())
mat = [[0,0,0],[0,0,0],[0,0,0]]
matrizAux = []
mat_def = [[0,0,0],[0,0,0],[0,0,0]]
mat_tensao = [[0,0,0],[0,0,0],[0,0,0]]
mat_dev = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(dim):
	aux = list(map(float, carregar.readline().split()))
	matrizAux.append(aux)
for i in range(dim):
	for j in range(dim):
		mat[i][j] = matrizAux[i][j]
fy = float(carregar.readline())
E = float(carregar.readline())
ni = float(carregar.readline())
gama = float(carregar.readline())
unidade = str(carregar.readline())

G = E/(2*(1+ni))

if (dim == 3): #3d
	mat_cron = [[1,0,0],[0,1,0],[0,0,1]]
	if (tt == 1): #tensao
		# TENSOR TENSAO
		mat_tensao = [[0,0,0],[0,0,0],[0,0,0]]
		mat_tensao = mat
		#TENSOR DE DEFORMAÇÃO 
		mat_def[0][0] = (1/E)*(mat_tensao[0][0] - ni*(mat_tensao[1][1]+mat_tensao[2][2]))
		mat_def[1][1] = (1/E)*(mat_tensao[1][1] - ni*(mat_tensao[0][0]+mat_tensao[2][2]))
		mat_def[2][2] = (1/E)*(mat_tensao[2][2] - ni*(mat_tensao[1][1]+mat_tensao[0][0]))
		
		if (td == 1): #angular
			mat_def[0][1] = mat_tensao[0][1]/G
			mat_def[0][2] = mat_tensao[0][2]/G
			mat_def[1][2] = mat_tensao[1][2]/G
		elif (td == 2): #linear
			mat_def[0][1] = mat_tensao[0][1]/(2*G)
			mat_def[0][2] = mat_tensao[0][2]/(2*G)
			mat_def[1][2] = mat_tensao[1][2]/(2*G)
		mat_def[1][0] = mat_def[0][1]
		mat_def[2][0] = mat_def[0][2]
		mat_def[2][1] = mat_def[1][2]
		
	if (tt == 2):
		#TENSOR DE DEFORMAÇÃO 
		mat_def = [[0,0,0],[0,0,0],[0,0,0]]
		mat_def = mat
		
		#TENSOR TENSAO
		mat_tensao[0][0] = (E/((1+ni)*(1-2*ni)))*(((1-ni)*mat_def[0][0])+(ni*(mat_def[1][1]+mat_def[2][2])))
		mat_tensao[1][1] = (E/((1+ni)*(1-2*ni)))*(((1-ni)*mat_def[1][1])+(ni*(mat_def[0][0]+mat_def[2][2])))
		mat_tensao[2][2] = (E/((1+ni)*(1-2*ni)))*(((1-ni)*mat_def[2][2])+(ni*(mat_def[1][1]+mat_def[0][0])))
		
		if (td == 1): #angular
			mat_tensao[0][1] = mat_def[0][1]*G
			mat_tensao[0][2] = mat_def[0][2]*G
			mat_tensao[1][2] = mat_def[1][2]*G
		elif (td == 2): #linear
			mat_tensao[0][1] = 2*mat_def[0][1]*G
			mat_tensao[0][2] = 2*mat_def[0][2]*G
			mat_tensao[1][2] = 2*mat_def[1][2]*G
		mat_tensao[1][0] = mat_tensao[0][1]
		mat_tensao[2][0] = mat_tensao[0][2]
		mat_tensao[2][1] = mat_tensao[1][2]
		
	
	# INVARIANTES DE Sigma_ij:
	I1 = mat_tensao[0][0] + mat_tensao[1][1] + mat_tensao[2][2]
	I2 = (mat_tensao[0][0]*mat_tensao[1][1]-pow(mat_tensao[0][1],2)) + (mat_tensao[0][0]*mat_tensao[2][2]-pow(mat_tensao[0][2],2)) + (mat_tensao[1][1]*mat_tensao[2][2]-pow(mat_tensao[1][2],2))
	I3 = (mat_tensao[0][0]*mat_tensao[1][1]*mat_tensao[2][2] + mat_tensao[0][1]*mat_tensao[1][2]*mat_tensao[2][0] + mat_tensao[0][2]*mat_tensao[1][0]*mat_tensao[2][1]) - (mat_tensao[2][0]*mat_tensao[1][1]*mat_tensao[0][2] + mat_tensao[2][1]*mat_tensao[1][2]*mat_tensao[0][0] + mat_tensao[2][2]*mat_tensao[1][0]*mat_tensao[0][1])
	
	#TENSOR DEVITÓRICO S_ij:
	sig_n = I1/3
	for i in range (3):
		for j in range (3):
			mat_dev[i][j] = mat_tensao[i][j] - sig_n*mat_cron[i][j]
	
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

if (dim==2):
	mat_cron = [[1,0,0],[0,1,0],[0,0,1]]
	if (ep==1): #EPT
		if (tt==1): #TENSAO
			#TENSOR DE TENSÃO
			for i in range (3):
				for j in range (3):
					mat_tensao[i][j] = mat[i][j]
			
			#TENSOR DE DEFORMAÇÃO
			mat_def[0][0] = (1/E)*(mat_tensao[0][0] - ni*mat_tensao[1][1])
			mat_def[1][1] = (1/E)*(mat_tensao[1][1] - ni*mat_tensao[0][0])
			
			if (td==1):
				mat_def[0][1] = mat_tensao[0][1]/G
			
			if (td==2):
				mat_def[0][1] = mat_tensao[0][1]/(2*G)
				
			mat_def[1][0] = mat_def[0][1]
			mat_def[2][2] = (-ni/E)*(mat_tensao[0][0] + mat_tensao[1][1])

		if (tt==2): #DEFORMAÇÃO
			#TENSOR DE DEFORMAÇÃO
			for i in range (3):
				for j in range (3):
					mat_def[i][j] = mat[i][j]
			
			#TENSOR DE TENSÃO
			mat_tensao[0][0] = (E/pow((1-ni),2))*(mat_def[0][0] + ni*mat_def[1][1])
			mat_tensao[1][1] = (E/pow((1-ni),2))*(mat_def[1][1] + ni*mat_def[0][0])
			
			if (td==1):
				mat_tensao[0][1] = G*mat_def[0][1]
			
			if (td==2):
				mat_tensao[0][1] = G*mat_def[0][1]*2
			
			mat_tensao[1][0] = mat_tensao[0][1]
		
		#INVARIANTES TENSAO 
		I1 = mat_tensao[0][0] + mat_tensao[1][1]
		I2 = (mat_tensao[0][0]*mat_tensao[1][1]-pow(mat_tensao[0][1],2)) + (mat_tensao[0][0]*mat_tensao[2][2]-pow(mat_tensao[0][2],2)) + (mat_tensao[1][1]*mat_tensao[2][2]-pow(mat_tensao[1][2],2))
		I3 = (mat_tensao[0][0]*mat_tensao[1][1]*mat_tensao[2][2] + mat_tensao[0][1]*mat_tensao[1][2]*mat_tensao[2][0] + mat_tensao[0][2]*mat_tensao[1][0]*mat_tensao[2][1]) - (mat_tensao[2][0]*mat_tensao[1][1]*mat_tensao[0][2] + mat_tensao[2][1]*mat_tensao[1][2]*mat_tensao[0][0] + mat_tensao[2][2]*mat_tensao[1][0]*mat_tensao[0][1])

		#TENSOR DEVITÓRICO
		sig_n = I1/2
		for i in range (3):
			for j in range (3):
				mat_dev[i][j] = mat_tensao[i][j] - sig_n*mat_cron[i][j]
		
		#IVARIANTES DEVITORICO
		J2 = 1/3 * (pow(I1,2) - 3*I2)
		J3 = 1/27 * (2*pow(I1,3) - 9*I1*I2 + 27*I3)
		
		# INVARIANTE DE COS
		cos3teta = ((3*sqrt(3))/2)*(J3/(sqrt(pow(J2,3))))
		teta3 = acos(cos3teta) #guarda variavel
		teta = teta3 / 3
		
		#TENSÕES PRINCIPAIS
		sig1 = ((mat_tensao[0][0] + mat_tensao[1][1])/2) + sqrt(pow(((mat_tensao[0][0] - mat_tensao[1][1])/2),2) + pow(mat_tensao[0][1],2))
		sig2 = ((mat_tensao[0][0] + mat_tensao[1][1])/2) - sqrt(pow(((mat_tensao[0][0] - mat_tensao[1][1])/2),2) + pow(mat_tensao[0][1],2))
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
			for i in range (dim):
				for j in range (dim):
					mat_tensao[i][j] = mat[i][j]
			mat_tensao[2][2] = ni*(mat_tensao[0][0] + mat_tensao[1][1])
			#TENSOR DE DEFORMAÇÃO
			mat_def[0][0] = (1/E)*(mat_tensao[0][0] - ni*(mat_tensao[1][1] + mat_tensao[2][2]))
			mat_def[1][1] = (1/E)*(mat_tensao[1][1] - ni*(mat_tensao[0][0] + mat_tensao[2][2]))
			
			if (td==1):
				mat_def[0][1] = mat_tensao[0][1]/G
			
			if (td==2):
				mat_def[0][1] = mat_tensao[0][1]/(2*G)
				
			mat_def[1][0] = mat_def[0][1]

		if (tt==2): #DEFORMAÇÃO
			#TENSOR DE DEFORMAÇÃO
			for i in range (dim):
				for j in range (dim):
					mat_def[i][j] = mat[i][j]
			#TENSOR DE TENSÃO
			mat_tensao[0][0] = (E/((1+ni)*(1-2*ni)))*((1-ni)*mat_def[0][0] + ni*mat_def[1][1])
			mat_tensao[1][1] = (E/((1+ni)*(1-2*ni)))*((1-ni)*mat_def[1][1] + ni*mat_def[0][0])
			mat_tensao[2][2] = ni*(mat_tensao[0][0] + mat_tensao[1][1])
			
			if (td==1):
				mat_tensao[0][1] = G*mat_def[0][1]
			
			if (td==2):
				mat_tensao[0][1] = G*mat_def[0][1]*2
			
			mat_tensao[1][0] = mat_tensao[0][1]
		
		#INVARIANTES TENSAO 
		I1 = mat_tensao[0][0] + mat_tensao[1][1] + mat_tensao[2][2]
		I2 = (mat_tensao[0][0]*mat_tensao[1][1]-pow(mat_tensao[0][1],2)) + (mat_tensao[0][0]*mat_tensao[2][2]-pow(mat_tensao[0][2],2)) + (mat_tensao[1][1]*mat_tensao[2][2]-pow(mat_tensao[1][2],2))
		I3 = (mat_tensao[0][0]*mat_tensao[1][1]*mat_tensao[2][2] + mat_tensao[0][1]*mat_tensao[1][2]*mat_tensao[2][0] + mat_tensao[0][2]*mat_tensao[1][0]*mat_tensao[2][1]) - (mat_tensao[2][0]*mat_tensao[1][1]*mat_tensao[0][2] + mat_tensao[2][1]*mat_tensao[1][2]*mat_tensao[0][0] + mat_tensao[2][2]*mat_tensao[1][0]*mat_tensao[0][1])

		#TENSOR DEVITÓRICO
		sig_n = I1/3
		for i in range (3):
			for j in range (3):
				mat_dev[i][j] = mat_tensao[i][j] - sig_n*mat_cron[i][j]

		#IVARIANTES DEVITORICO
		J2 = (pow(I1,2) - 3*I2)/3
		J3 = (2*pow(I1,3) - 9*I1*I2 + 27*I3)/27
		
		#TENSÕES PRINCIPAIS
		sig1 = ((mat_tensao[0][0] + mat_tensao[1][1])/2) + sqrt(pow(((mat_tensao[0][0] - mat_tensao[1][1])/2),2) + pow(mat_tensao[0][1],2))
		sig2 = ((mat_tensao[0][0] + mat_tensao[1][1])/2) - sqrt(pow(((mat_tensao[0][0] - mat_tensao[1][1])/2),2) + pow(mat_tensao[0][1],2))
		sig3 = mat_tensao[2][2]
	
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
		
salvar = open(nomeArq + ".out", 'w') # abre arq 

#f = open("arq2.txt", 'w')
salvar.write("    \n")
salvar.write("                      **** ANÁLISE DO TENSOR DE TENSÃO E CRITÉRIOS DE ESCOAMENTO **** \n")
salvar.write("    \n")
salvar.write("    \n")
salvar.write("			ARQUIVOS DE DADOS :				" + nomeArq + ".out" '\n\n')
salvar.write("    \n")
salvar.write("			Data do processamento :			" + str(now) +'\n')
salvar.write("    \n")
salvar.write("Tensor de Tensão Sigma_ij:                " + '\n')
salvar.write("			|  " +'{:e}'.format( mat_tensao[0][0])+"  " +'{:e}'.format( mat_tensao[0][1]) +"  " +'{:e}'.format( mat_tensao[0][2]) +"|" + '\n')
salvar.write("	       Sig_ij = |  " +'{:e}'.format( mat_tensao[1][0])+"  " +'{:e}'.format( mat_tensao[1][1]) +"  " +'{:e}'.format( mat_tensao[1][2]) +"|" + '\n')
salvar.write("			|  " +'{:e}'.format( mat_tensao[2][0])+"  " +'{:e}'.format( mat_tensao[2][1]) +"  " +'{:e}'.format( mat_tensao[2][2]) +"|" + unidade+ '\n')
salvar.write("    \n")
salvar.write("Tensor Desviatório S_ij :                    " +'\n')
salvar.write("			|  " +'{:e}'.format( mat_dev[0][0])+"  " +'{:e}'.format( mat_dev[0][1]) +"  " +'{:e}'.format( mat_dev[0][2]) +"|" '\n')
salvar.write("		S_ij =	|  " +'{:e}'.format( mat_dev[1][0])+"  " +'{:e}'.format( mat_dev[1][1]) +"  " +'{:e}'.format( mat_dev[1][2]) +"|" +'\n')
salvar.write("			|  " +'{:e}'.format( mat_dev[2][0])+"  " +'{:e}'.format( mat_dev[2][1]) +"  " +'{:e}'.format( mat_dev[2][2]) +"|" +  unidade+ '\n')
salvar.write("    \n")
salvar.write("			Invariantes de Sigma_ij              " '\n')
salvar.write("    \n")
salvar.write("			i1:                " +'{:e}'.format(I1 )+ unidade+ '\n')
salvar.write("			i2:                " +'{:e}'.format(I2 )+ unidade+ "²"'\n')
salvar.write("			i3:                " +'{:e}'.format(I3 )+ unidade+ "³"'\n')
salvar.write("    \n")
salvar.write("			Invariantes de S_ij              " '\n')
salvar.write("    \n")
salvar.write("			J2:                " +'{:e}'.format(J2 )+ unidade+ "²"'\n')
salvar.write("			J3:                " +'{:e}'.format(J3 )+ unidade+ "³"'\n')
salvar.write("    \n")
salvar.write("			Invariante COS(3Teta)             " '\n')
salvar.write("			cos(3teta)=              " +'{:e}'.format(cos3teta)+'\n')
salvar.write("    \n")
salvar.write("			Tensões Principais             " '\n')
salvar.write("			Sig1=            " +'{:e}'.format(s1 )+ unidade+ '\n')
salvar.write("			Sig2=             " +'{:e}'.format(s2) + unidade+ '\n')
salvar.write("			Sig3=            " +'{:e}'.format(s3) + unidade+ '\n')
salvar.write("			TauMx=            " +'{:e}'.format(tau_max) + unidade+ '\n')
salvar.write("    \n")
salvar.write("			Parâmetros do Material           " '\n')
salvar.write("    \n")
salvar.write("			fy=            " +'{:e}'.format(fy )+ unidade+ '\n')
salvar.write("			Gama_mat=             " +'{:e}'.format(gama) + '\n')
salvar.write("			Rel.Poisson        " +'{:e}'.format(ni) + '\n')
salvar.write("			Mód.Young           " +'{:e}'.format(E) + unidade+ '\n')
salvar.write("    \n")
salvar.write("Tensor de deformação Epsilon_ij           " '\n')
salvar.write("		   |  " +'{:e}'.format( mat_def[0][0])+"  " +'{:e}'.format( mat_def[0][1]) +"  " +'{:e}'.format( mat_def[0][2]) +"|" + '\n')
salvar.write("	  Eps_ij = |  " +'{:e}'.format( mat_def[1][0])+"  " +'{:e}'.format( mat_def[1][1]) +"  " +'{:e}'.format( mat_def[1][2]) +"|" +  '\n')
salvar.write("		   |  " +'{:e}'.format( mat_def[2][0])+"  " +'{:e}'.format( mat_def[2][1]) +"  " +'{:e}'.format( mat_def[2][2]) +"|" +  '\n')
salvar.write("    \n")
salvar.write("			Deformações Principais             " '\n')
salvar.write("			Eps1=            " +'{:e}'.format(def1 )+  '\n')
salvar.write("			Eps2=             " +'{:e}'.format(def2) + '\n')
salvar.write("			Eps3=            " +'{:e}'.format(def3) + '\n')
salvar.write("			Gama_Mx=            " +'{:e}'.format(gamamax) + '\n')
salvar.write("    \n")
salvar.write("			Tensão Equivalente de tresca            " '\n')
salvar.write("			2 Tau_mx=       " +'{:e}'.format(tresca) + unidade+ '\n')
salvar.write("    \n")
salvar.write("			Tensão Equivalente de Von Mises           " '\n')
salvar.write("			Sig_Eq=       " +'{:e}'.format(mises) + unidade+ '\n')
salvar.write("    \n")
#ESCOOU
if (tresca <= fy):
	salvar.write("		Critério de Tresca: Estavel, nao ha escoamento")	
	salvar.write("    \n")
elif (tresca > fy):
	salvar.write("		Critério de Tresca: Instavel, ha escoamento")
	salvar.write("    \n")
if (mises <= fy):
	salvar.write("		Critério de von Mises: Estavel, nao ha escoamento")
	salvar.write("    \n")
elif (mises > fy):
	salvar.write("		Critério de von Mises: Instavel, ha escoamento")
	salvar.write("    \n")

				
