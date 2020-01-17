from math import atan,sin,cos,radians, degrees , acos , pi ,sqrt

#entrada

nome_entrada = input("Nome do arquivo a ser rodado: ") 
nome_completo = open(nome_entrada + ".dat", 'r') 
carregar = nome_completo.read().split() 
nome_completo.close()
dimensao=int(carregar[0]) # dado normal
tipo_T= int(carregar[1])
estado_P= int(carregar[2])
tipo_D= int(carregar[3])

tensao=[]
defor=[]
deforaux=[]

if dimensao == 2:
		if tipo_T==1:	
			tensao=[0]*3
			tensao[0] = [float(carregar[4]),float(carregar[5]),0]
			tensao[1] = [float(carregar[6]),float(carregar[7]),0]
			tensao[2] = [0,0,0]
			defor=[[0,0,0],[0,0,0],[0,0,0]]
			deforaux=[[0,0,0],[0,0,0],[0,0,0]]
		elif tipo_T==2:
			if tipo_D==1:
				defor=[0]*3
				defor[0] = [float(carregar[4]),float(carregar[5]),0]
				defor[1] = [float(carregar[6]),float(carregar[7]),0]
				defor[2] = [0,0,0]
				tensao=[[0,0,0],[0,0,0],[0,0,0]]
				deforaux=[[0,0,0],[0,0,0],[0,0,0]]
			elif tipo_D==2:
				deforaux=[0]*3
				deforaux[0] = [float(carregar[4]),float(carregar[5]),0]
				deforaux[1] = [float(carregar[6]),float(carregar[7]),0]
				deforaux[2] = [0,0,0]
				tensao=[[0,0,0],[0,0,0],[0,0,0]]
				defor=[[0,0,0],[0,0,0],[0,0,0]]
		fy= float(carregar[8])
		E= float(carregar[9])
		NI= float(carregar[10])
		gama= float(carregar[11])
		uni= str(carregar[12])
elif dimensao == 3:
		if tipo_T==1:	
			tensao=[0]*3
			tensao[0] = [float(carregar[4]),float(carregar[5]),float(carregar[6])]
			tensao[1] = [float(carregar[7]),float(carregar[8]),float(carregar[9])]
			tensao[2] = [float(carregar[10]),float(carregar[11]),float(carregar[12])]
			defor=[[0,0,0],[0,0,0],[0,0,0]]
			deforaux=[[0,0,0],[0,0,0],[0,0,0]]
		elif tipo_T==2:
			if tipo_D==1:
				defor=[0]*3
				defor[0] = [float(carregar[4]),float(carregar[5]),float(carregar[6])]
				defor[1] = [float(carregar[7]),float(carregar[8]),float(carregar[9])]
				defor[2] = [float(carregar[10]),float(carregar[11]),float(carregar[12])]
				tensao=[[0,0,0],[0,0,0],[0,0,0]]
				deforaux=[[0,0,0],[0,0,0],[0,0,0]]
			elif tipo_D==2:
				deforaux=[0]*3
				deforaux[0] = [float(carregar[4]),float(carregar[5]),float(carregar[6])]
				deforaux[1] = [float(carregar[7]),float(carregar[8]),float(carregar[9])]
				deforaux[2] = [float(carregar[10]),float(carregar[11]),float(carregar[12])]
				tensao=[[0,0,0],[0,0,0],[0,0,0]]
				defor=[[0,0,0],[0,0,0],[0,0,0]]
		fy= float(carregar[13])
		E= float(carregar[14])
		NI= float(carregar[15])
		gama= float(carregar[16])
		uni= str(carregar[17]) 
				
if tipo_D==2 and tipo_T==2:
	if dimensao==3:
		defor=[[deforaux[0][0],deforaux[0][1]/2,deforaux[0][2]/2],[deforaux[1][0]/2,deforaux[1][1],deforaux[1][2]/2],[deforaux[2][0]/2,deforaux[2][1]/2,deforaux[2][2]]]	
	if dimensao==2:
		defor=[[deforaux[0][0],deforaux[0][1]/2,0],[deforaux[1][0]/2,deforaux[1][1],0],[0,0,0]]
	
G=E/(2*(1+NI))
	
dd = (E/((1+NI) *(1 - 2*NI)))
cc=1/E

if dimensao==2:
	if tipo_T==1:
			szz = NI*(tensao[0][0]+tensao[1][1])
			ezz=(-NI/E)*(tensao[0][0]+tensao[1][1])
			exx=(1/E)*(tensao[0][0] - NI*(tensao[1][1]+szz))
			eyy=(1/E)*(tensao[1][1] - NI*(tensao[0][0]+szz))
			tauxy=tensao[0][1]/(G*2)
			tauyx=tensao[1][0]/(G*2)
			defor=[[exx,tauxy,0],[tauyx,eyy,0],[0,0,ezz]]
	if tipo_T==2:
			sxx=2*G*defor[0][0] + ((NI*E)/((1+NI)*(1-2*NI)))*(defor[0][0]+defor[1][1])
			syy=2*G*defor[1][1] + ((NI*E)/((1+NI)*(1-2*NI)))*(defor[0][0]+defor[1][1])
			szz=NI*(sxx+syy)
			tauxy = G*defor[0][1]
			tauyx = tauxy
			tensao=[[sxx,tauxy,0],[tauyx,syy,0],[0,0,szz]]
elif dimensao==3:
	if tipo_T==1:
			defor[0][0]=cc*(tensao[0][0] - NI*(tensao[1][1]+tensao[2][2]))
			defor[1][1]=cc*(tensao[1][1] - NI*(tensao[0][0]+tensao[2][2]))
			defor[2][2]=cc*(tensao[2][2] - NI*(tensao[1][1]+tensao[0][0]))
			defor[0][1]=tensao[0][1]/(G)
			defor[0][2]=tensao[0][2]/(G)
			defor[1][0]=tensao[1][0]/(G)
			defor[1][2]=tensao[1][2]/(G)
			defor[2][0]=tensao[2][0]/(G)
			defor[2][1]=tensao[2][1]/(G)
	elif tipo_T==2:
			tensao[0][0]=dd*((1-NI)*(defor[0][0] + NI*(defor[1][1]+defor[2][2])))
			tensao[1][1]=dd*((1-NI)*(defor[1][1] + NI*(defor[0][0]+defor[2][2])))
			tensao[2][2]=dd*((1-NI)*(defor[2][2] + NI*(defor[1][1]+defor[0][0])))
			tensao[0][1]=G*(2*defor[0][1])
			tensao[0][2]=G*(2*defor[0][2])
			tensao[1][0]=G*(2*defor[1][0])
			tensao[1][2]=G*(2*defor[1][2])
			tensao[2][0]=G*(2*defor[2][0])
			tensao[2][1]=G*(2*defor[2][1])
	
p=(tensao[0][0]+tensao[1][1]+tensao[2][2])/3
desvij=[[tensao[0][0]-p,tensao[0][1],tensao[0][2]],[tensao[1][0],tensao[1][1]-p,tensao[1][2]],[tensao[2][0],tensao[2][1],tensao[2][2]-p]]
i1=tensao[0][0] +tensao[1][1]+tensao[2][2]
i2=(tensao[0][0]*tensao[1][1] - (tensao[1][0]**2))+(tensao[0][0]*tensao[2][2] - (tensao[0][2]**2))+(tensao[2][2]*tensao[1][1] - (tensao[1][2]**2))
i3=(((tensao[0][0]*tensao[1][1]*tensao[2][2])+(tensao[0][1]*tensao[1][2]*tensao[2][0])+(tensao[0][2]*tensao[1][0]*tensao[2][1]))-((tensao[0][2]*tensao[1][1]*tensao[2][0])+(tensao[0][1]*tensao[1][0]*tensao[2][2])+(tensao[0][0]*tensao[1][2]*tensao[2][1])))
j1=0
j2=((i1**2 )-(3*i2))/3
j3=((2*i1**3)-(9*i1*i2)+(27*i3))/27
teta=((j3*3*(3**(1/2)))/(2*(j2**(3/2))))
tetau=acos(teta)/3
tetasi=(1/3)*acos((3*j3*sqrt(3))/(2*(j2**(3/2))))
sigmaoct=i1/3
sigma1aux=sigmaoct+(2*sqrt(j2/3))*cos(tetau)
sigma2aux=sigmaoct+(2*sqrt(j2/3))*cos(tetau -((2*pi)/3)) 
sigma3aux=sigmaoct+(2*sqrt(j2/3))*cos(tetau + ((2*pi)/3))
if sigma1aux>= sigma2aux and sigma1aux>=sigma3aux:
	if sigma2aux>=sigma3aux:
		sigma1=sigma1aux
		sigma2=sigma2aux
		sigma3=sigma3aux
	else:
		sigma1=sigma1aux
		sigma2=sigma3aux
		sigma3=sigma2aux
if sigma2aux>= sigma1aux and sigma2aux>=sigma3aux:
	if sigma1aux>=sigma3aux:
		sigma1=sigma2aux
		sigma2=sigma1aux
		sigma3=sigma3aux
	else:
		sigma1=sigma2aux
		sigma2=sigma3aux
		sigma3=sigma1aux
if sigma3aux>= sigma2aux and sigma3aux>=sigma1aux:
	if sigma2aux>=sigma1aux:
		sigma1=sigma3aux
		sigma2=sigma2aux
		sigma3=sigma1aux
	else:
		sigma1=sigma3aux
		sigma2=sigma1aux
		sigma3=sigma2aux
		
taumax=(sigma1- sigma3)/2

ie1=defor[0][0]+defor[1][1]+defor[2][2]
ie2=(defor[0][0]*defor[1][1] - ((defor[1][0]/2)**2))+(defor[0][0]*defor[2][2] - ((defor[0][2]/2)**2))+(defor[2][2]*defor[1][1] - ((defor[1][2]/2)**2))
deforaux2=[[defor[0][0],defor[0][1]/2,defor[0][2]/2],[defor[1][0]/2,defor[1][1],defor[1][2]/2],[defor[2][0]/2,defor[2][1]/2,defor[2][2]]]
ie3=(((deforaux2[0][0]*deforaux2[1][1]*deforaux2[2][2])+(deforaux2[0][1]*deforaux2[1][2]*deforaux2[2][0])+(deforaux2[0][2]*deforaux2[1][0]*deforaux2[2][1]))-((deforaux2[0][2]*deforaux2[1][1]*deforaux2[2][0])+(deforaux2[0][1]*deforaux2[1][0]*deforaux2[2][2])+(deforaux2[0][0]*deforaux2[1][2]*deforaux2[2][1])))
je1=0
je2=((ie1**2 )-(3*ie2))/3
je3=((2*ie1**3)-(9*ie1*ie2)+(27*ie3))/27
tetae=((je3*3*sqrt(3))/2)/(je2**(3/2))
tetaeu=acos(tetae)/3 
tauoct=ie1/3
tau1aux=tauoct+(2*sqrt(je2/3))*cos(tetaeu)
tau2aux=tauoct+(2*sqrt(je2/3))*cos(tetaeu - ((2*pi)/3)) 
tau3aux=tauoct+(2*sqrt(je2/3))*cos(tetaeu + ((2*pi)/3))
if tau1aux>= tau2aux and tau1aux>=tau3aux:
	if tau2aux>=tau3aux:
		tau1=tau1aux
		tau2=tau2aux
		tau3=tau3aux
	else:
		tau1=tau1aux
		tau2=tau3aux
		tau3=tau2aux
if tau2aux>= tau1aux and tau2aux>=tau3aux:
	if tau1aux>=tau3aux:
		tau1=tau2aux
		tau2=tau1aux
		tau3=tau3aux
	else:
		tau1=tau2aux
		tau2=tau3aux
		tau3=tau1aux
if tau3aux>= tau2aux and tau3aux>=tau1aux:
	if tau2aux>=tau1aux:
		tau1=tau3aux
		sigma2=tau2aux
		tau3=tau1aux
	else:
		tau1=tau3aux
		tau2=tau1aux
		tau3=tau2aux
tauemax=(tau1-tau3)

cofator_a1 = ((tensao[1][1] - sigma1)*(tensao[2][2] - sigma1)) - (tensao[2][1]*tensao[1][2]);
cofator_b1 = -((tensao[0][1]*(tensao[2][2] - sigma1)) - (tensao[1][2]*tensao[0][2]));
cofator_c1 = (tensao[0][1]*tensao[1][2]) - ((tensao[1][1] - sigma1)*tensao[0][2]);
k1 = 1/sqrt(cofator_a1*cofator_a1 + cofator_b1*cofator_b1 + cofator_c1*cofator_c1);
n1x = k1*cofator_a1;
n1y = k1*cofator_b1;
n1z = k1*cofator_c1;
cofator_a2 = ((tensao[1][1] - sigma2)*(tensao[2][2] - sigma2)) - (tensao[2][1]*tensao[1][2]);
cofator_b2 = -((tensao[0][1]*(tensao[2][2] - sigma2)) - (tensao[1][2]*tensao[0][2]));
cofator_c2 = (tensao[0][1]*tensao[1][2]) - ((tensao[1][1] - sigma2)*tensao[0][2]);
k2 = 1/sqrt(cofator_a2*cofator_a2 + cofator_b2*cofator_b2 + cofator_c2*cofator_c2);
n2x = k2*cofator_a2;
n2y = k2*cofator_b2;
n2z = k2*cofator_c2;

if dimensao==2:
	n3x = 0
	n3y = 0
	n3z = 0
elif dimensao==3:
	cofator_a3 = ((tensao[1][1] - sigma3)*(tensao[2][2] - sigma3)) - (tensao[2][1]*tensao[1][2]);
	cofator_b3 = -((tensao[0][1]*(tensao[2][2] - sigma3)) - (tensao[1][2]*tensao[0][2]));
	cofator_c3 = (tensao[0][1]*tensao[1][2]) - ((tensao[1][1] - sigma3)*tensao[0][2]);
	k3 = 1/sqrt(cofator_a3*cofator_a3 + cofator_b3*cofator_b3 + cofator_c3*cofator_c3);
	n3x = k3*cofator_a3;
	n3y = k3*cofator_b3;
	n3z = k3*cofator_c3;

criterio_tresca = 2*taumax
criterio_von_mises = sqrt(3*j2)

if criterio_tresca <= (fy/gama):
	saida_tresca=str("Critério de Tresca : ESTÁVEL, NÃO HÁ ESCOAMENTO.")
else:
	saida_tresca=str("Critério de Tresca : INSTÁVEL,  HÁ ESCOAMENTO.")
if criterio_von_mises<=(fy/gama):
	saida_von=str("Critério de von Mises : ESTÁVEL, NÃO HÁ ESCOAMENTO.")
else:
	saida_von=str("Critério de von Mises : INSTÁVEL,  HÁ ESCOAMENTO.")

teta1=0.5*atan((2*tensao[0][1])/(tensao[0][0]-tensao[1][1]))
teta2=teta1+90
tetas=0.5*atan(-(tensao[0][0]-tensao[1][1])/(2*tensao[1][0]))

if tipo_D==2 and tipo_T==2:
	if dimensao==3:
		new_matriz_deformacao=defor
		defor=[[new_matriz_deformacao[0][0],new_matriz_deformacao[0][1]*2,new_matriz_deformacao[0][2]*2],[new_matriz_deformacao[1][0]*2,new_matriz_deformacao[1][1],new_matriz_deformacao[1][2]*2],[new_matriz_deformacao[2][0]*2,new_matriz_deformacao[2][1]*2,new_matriz_deformacao[2][2]]]	
	if dimensao==2:
		new_matriz_deformacao=defor
		defor=[[new_matriz_deformacao[0][0],new_matriz_deformacao[0][1]*2,0],[new_matriz_deformacao[1][0]*2,new_matriz_deformacao[1][1],0],[0,0,0]]
carregar = open(nome_entrada + ".out", 'w') # abre arq 

carregar.write("\n")
carregar.write("                      **** ANÁLISE DO TENSOR DE TENSÃO E CRITÉRIOS DE ESCOAMENTO *\n")
carregar.write("\n")
carregar.write("\n")
carregar.write("		Tensor de Tensão Sigma_ij:	" + '\n')
carregar.write("|  " +str( "%.9f" % tensao[0][0])+"  "+str( "%.9f" % tensao[0][1]) +"  "+str( "%.9f" % tensao[0][2]) +"|" + '\n')
carregar.write("|  " +str( "%.9f" % tensao[1][0])+"  "+str( "%.9f" % tensao[1][1]) +"  "+str( "%.9f" % tensao[1][2]) +"|" + uni+ '\n')
carregar.write("|  " +str( "%.9f" % tensao[2][0])+"  "+str( "%.9f" % tensao[2][1]) +"  "+str( "%.9f" % tensao[2][2]) +"|" +  '\n')
carregar.write("\n")
carregar.write("		Tensor Desviatório S_ij :          " +'\n')
carregar.write("|  " +str( "%.9f" % desvij[0][0])+"  "+str( "%.9f" % desvij[0][1]) +"  "+str( "%.9f" % desvij[0][2]) +"|" '\n')
carregar.write("|  " +str( "%.9f" % desvij[1][0])+"  "+str( "%.9f" % desvij[1][1]) +"  "+str( "%.9f" % desvij[1][2]) +"|" + uni+ '\n')
carregar.write("|  " +str( "%.9f" % desvij[2][0])+"  "+str( "%.9f" % desvij[2][1]) +"  "+str( "%.9f" % desvij[2][2]) +"|" +  '\n')
carregar.write("\n")
carregar.write("		Invariantes de Sigma_ij    " '\n')
carregar.write("\n")
carregar.write("i1:	" +str( "%.9f" %i1 )+ uni+ '\n')
carregar.write("\n")
carregar.write("i2:	" +str( "%.9f" %i2 )+ uni+ "²"'\n')
carregar.write("\n")
carregar.write("i3:	" +str( "%.9f" %i3 )+ uni+ "³"'\n')
carregar.write("\n")
carregar.write("\n")
carregar.write("		Invariantes de S_ij    " '\n')
carregar.write("\n")
carregar.write("J2:	" +str( "%.9f" %j2 )+ uni+ "²"'\n')
carregar.write("\n")
carregar.write("J3:	" +str( "%.9f" %j3 )+ uni+ "³"'\n')
carregar.write("\n")
carregar.write("		Tensões Principais   " '\n')
carregar.write("Sig1=  " +str( "%.9f" %sigma1 )+ uni+ '\n')
carregar.write("Sig2=   " +str( "%.9f" %sigma2) + uni+ '\n')
carregar.write("Sig3=  "+ str("%.9f" %sigma3) + uni+ '\n')
carregar.write("TauMx=  "+ str("%.9f" %taumax) + uni+ '\n')
carregar.write("\n")
carregar.write("\n")
carregar.write("Ângulo de similaridade           " '\n')
carregar.write("teta=    " +str( "%.9f" %tetasi)+'\n')
carregar.write("\n")
carregar.write("Invariante COS(3Teta)   " '\n')
carregar.write("Cos(3teta)=    " +str( "%.9f" %teta)+'\n')
carregar.write("\n")
carregar.write("\n")
if (dimensao == 3):
	carregar.write("	Direções Principais   " '\n')
	carregar.write("N1=  " +str( "%.9f" %n1x )+"  i  "+ str( "%.9f" %n1y )+"  j  "+str( "%.9f" %n1z )+"  k" '\n')
	carregar.write("N2=  " +str( "%.9f" %n2x )+"  i  "+ str( "%.9f" %n2y )+"  j  "+str( "%.9f" %n2z )+"  k" '\n')
	carregar.write("N3=  "+str( "%.9f" %n3x )+"  i  "+ str( "%.9f" %n3y )+"  j  "+str( "%.9f" %n3z )+"  k" '\n')
carregar.write("	Angulos Principais   " '\n')
carregar.write("Teta1=  " +str( "%.9f" %teta1 )+'\n')
carregar.write("Teta2=   " +str( "%.9f" %teta2 )+ '\n')
carregar.write("Tetas=   " +str( "%.9f" %tetas )+ '\n')
carregar.write("\n")
carregar.write("\n")
carregar.write("		Tensor de Deformação Epsilon_ij           " '\n')
carregar.write("|  " +str( "%.9f" % defor[0][0])+"  "+str( "%.9f" % defor[0][1]) +"  "+str( "%.9f" % defor[0][2]) +"|" + '\n')
carregar.write("|  " +str( "%.9f" % defor[1][0])+"  "+str( "%.9f" % defor[1][1]) +"  "+str( "%.9f" % defor[1][2]) +"|" +  '\n')
carregar.write("|  " +str( "%.9f" % defor[2][0])+"  "+str( "%.9f" % defor[2][1]) +"  "+str( "%.9f" % defor[2][2]) +"|" +  '\n')
carregar.write("\n")
carregar.write("		Deformações Principais   " '\n')
carregar.write("Eps1=  " +str( "%.9f" %tau1 )+  '\n')
carregar.write("Eps2=   " +str( "%.9f" %tau2) + '\n')
carregar.write("Eps3=  "+ str("%.9f" %tau3) + '\n')
carregar.write("Gama_Mx=  "+ str("%.9f" %tauemax) + '\n')
carregar.write("		Parâmetros do Material           " '\n')
carregar.write("\n")
carregar.write("fy=  " +str( "%.9f" %fy )+ uni+ '\n')
carregar.write("Gama_mat=   " +str( "%.9f" %gama) + '\n')
carregar.write("Rel.Poisson        "+ str("%.9f" %NI) + '\n')
carregar.write("Mód.Young           "+ str("%.9f" %E) + uni+ '\n')
carregar.write("\n")
carregar.write("\n")
carregar.write("	Tensão Equivalente de tresca  " '\n')
carregar.write("2 Tau_mx=       " + str("%.9f" %criterio_tresca) + uni+ '\n')
carregar.write("\n")
carregar.write("	Tensão Equivalente de Von Mises           " '\n')
carregar.write("Sig_Eq=       " + str("%.9f" %criterio_von_mises) + uni+ '\n')
carregar.write("\n")
carregar.write("	Verificação da estabilidade:          " '\n')
carregar.write("\n")
carregar.write("Critério de Tresca      " + saida_tresca+ '\n')
carregar.write("\n")
carregar.write("Critério de Von Mises      " + saida_von + '\n')