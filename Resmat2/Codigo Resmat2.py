import datetime
from math import atan,sin,cos,radians, degrees , acos , pi ,sqrt
now = datetime.datetime.now()
#entrada

nomeArq = input("digite nome do arquivo: ") 
dados = open(nomeArq + ".dat", 'r') 
f = dados.read().split() 
dados.close()
dim=int(f[0]) # dado normal
tt= int(f[1])
ep= int(f[2])
td= int(f[3])

tensao=[]
defor=[]
deforaux=[]

if dim == 3:
		if tt==1:	
			tensao=[0]*3
			tensao[0] = [float(f[4]),float(f[5]),float(f[6])]
			tensao[1] = [float(f[7]),float(f[8]),float(f[9])]
			tensao[2] = [float(f[10]),float(f[11]),float(f[12])]
			defor=[[0,0,0],[0,0,0],[0,0,0]]
			deforaux=[[0,0,0],[0,0,0],[0,0,0]]

			
		else:
			if td==1:
				defor=[0]*3
				defor[0] = [float(f[4]),float(f[5]),float(f[6])]
				defor[1] = [float(f[7]),float(f[8]),float(f[9])]
				defor[2] = [float(f[10]),float(f[11]),float(f[12])]
				tensao=[[0,0,0],[0,0,0],[0,0,0]]
				deforaux=[[0,0,0],[0,0,0],[0,0,0]]
			else:
				deforaux=[0]*3
				deforaux[0] = [float(f[4]),float(f[5]),float(f[6])]
				deforaux[1] = [float(f[7]),float(f[8]),float(f[9])]
				deforaux[2] = [float(f[10]),float(f[11]),float(f[12])]
				tensao=[[0,0,0],[0,0,0],[0,0,0]]
				defor=[[0,0,0],[0,0,0],[0,0,0]]
		fy= float(f[13])
		E= float(f[14])
		NI= float(f[15])
		gama= float(f[16])
		unidade= str(f[17]) 
		
else:
		if tt==1:	
			tensao=[0]*3
			tensao[0] = [float(f[4]),float(f[5]),0]
			tensao[1] = [float(f[6]),float(f[7]),0]
			tensao[2] = [0,0,0]
			defor=[[0,0,0],[0,0,0],[0,0,0]]
			deforaux=[[0,0,0],[0,0,0],[0,0,0]]
		else:
			if td==1:
				defor=[0]*3
				defor[0] = [float(f[4]),float(f[5]),0]
				defor[1] = [float(f[6]),float(f[7]),0]
				defor[2] = [0,0,0]
				tensao=[[0,0,0],[0,0,0],[0,0,0]]
				deforaux=[[0,0,0],[0,0,0],[0,0,0]]
			else:
				deforaux=[0]*3
				deforaux[0] = [float(f[4]),float(f[5]),0]
				deforaux[1] = [float(f[6]),float(f[7]),0]
				deforaux[2] = [0,0,0]
				tensao=[[0,0,0],[0,0,0],[0,0,0]]
				defor=[[0,0,0],[0,0,0],[0,0,0]]
		fy= float(f[8])
		E= float(f[9])
		NI= float(f[10])
		gama= float(f[11])
		unidade= str(f[12]) 
				
if td==2 and tt==2:
	if dim==3:
		defor=[[deforaux[0][0],deforaux[0][1]/2,deforaux[0][2]/2],[deforaux[1][0]/2,deforaux[1][1],deforaux[1][2]/2],[deforaux[2][0]/2,deforaux[2][1]/2,deforaux[2][2]]]	
	if dim==2:
		defor=[[deforaux[0][0],deforaux[0][1]/2,0],[deforaux[1][0]/2,deforaux[1][1],0],[0,0,0]]
	
G=E/(2*(1+NI))
#calculando componentes anti-planas

	
if dim == 3 or dim==2 :
	dd = (E/((1+NI) *(1 - 2*NI)))
	cc=1/E
	if dim==3:
		if tt==1:
				defor[0][0]=cc*(tensao[0][0] - NI*(tensao[1][1]+tensao[2][2]))
				defor[1][1]=cc*(tensao[1][1] - NI*(tensao[0][0]+tensao[2][2]))
				defor[2][2]=cc*(tensao[2][2] - NI*(tensao[1][1]+tensao[0][0]))
				defor[0][1]=tensao[0][1]/(G)
				defor[0][2]=tensao[0][2]/(G)
				defor[1][0]=tensao[1][0]/(G)
				defor[1][2]=tensao[1][2]/(G)
				defor[2][0]=tensao[2][0]/(G)
				defor[2][1]=tensao[2][1]/(G)
			
		else:
				tensao[0][0]=dd*((1-NI)*(defor[0][0] + NI*(defor[1][1]+defor[2][2])))
				tensao[1][1]=dd*((1-NI)*(defor[1][1] + NI*(defor[0][0]+defor[2][2])))
				tensao[2][2]=dd*((1-NI)*(defor[2][2] + NI*(defor[1][1]+defor[0][0])))
				tensao[0][1]=G*(2*defor[0][1])
				tensao[0][2]=G*(2*defor[0][2])
				tensao[1][0]=G*(2*defor[1][0])
				tensao[1][2]=G*(2*defor[1][2])
				tensao[2][0]=G*(2*defor[2][0])
				tensao[2][1]=G*(2*defor[2][1])
	if dim==2:
		if tt==1:
				szz = NI*(tensao[0][0]+tensao[1][1])
				ezz=(-NI/E)*(tensao[0][0]+tensao[1][1])
				exx=(1/E)*(tensao[0][0] - NI*(tensao[1][1]+szz))
				eyy=(1/E)*(tensao[1][1] - NI*(tensao[0][0]+szz))
				tauxy=tensao[0][1]/(G*2)
				tauyx=tensao[1][0]/(G*2)
				defor=[[exx,tauxy,0],[tauyx,eyy,0],[0,0,ezz]]
		if tt==2:
				sxx=2*G*defor[0][0] + ((NI*E)/((1+NI)*(1-2*NI)))*(defor[0][0]+defor[1][1])
				syy=2*G*defor[1][1] + ((NI*E)/((1+NI)*(1-2*NI)))*(defor[0][0]+defor[1][1])
				szz=NI*(sxx+syy)
				tauxy = G*defor[0][1]
				tauyx = tauxy
				tensao=[[sxx,tauxy,0],[tauyx,syy,0],[0,0,szz]]
		
					#calculando componentes antiplanas
	#calculando o tensor desviatório
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
			s1=sigma1aux
			s2=sigma2aux
			s3=sigma3aux
		else:
			s1=sigma1aux
			s2=sigma3aux
			s3=sigma2aux
	if sigma2aux>= sigma1aux and sigma2aux>=sigma3aux:
		if sigma1aux>=sigma3aux:
			s1=sigma2aux
			s2=sigma1aux
			s3=sigma3aux
		else:
			s1=sigma2aux
			s2=sigma3aux
			s3=sigma1aux
	if sigma3aux>= sigma2aux and sigma3aux>=sigma1aux:
		if sigma2aux>=sigma1aux:
			s1=sigma3aux
			s2=sigma2aux
			s3=sigma1aux
		else:
			s1=sigma3aux
			s2=sigma1aux
			s3=sigma2aux
			
	taumax=(s1- s3)/2
	
	#deformações principais e gama max
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
			s2=tau2aux
			tau3=tau1aux
		else:
			tau1=tau3aux
			tau2=tau1aux
			tau3=tau2aux
	tauemax=(tau1-tau3)


	#Direções Principais
	cof_a1 = ((tensao[1][1] - s1)*(tensao[2][2] - s1)) - (tensao[2][1]*tensao[1][2]);
	cof_b1 = -((tensao[0][1]*(tensao[2][2] - s1)) - (tensao[1][2]*tensao[0][2]));
	cof_c1 = (tensao[0][1]*tensao[1][2]) - ((tensao[1][1] - s1)*tensao[0][2]);
	k1 = 1/sqrt(cof_a1*cof_a1 + cof_b1*cof_b1 + cof_c1*cof_c1);
	ni1 = k1*cof_a1;
	nj1 = k1*cof_b1;
	nk1 = k1*cof_c1;
	cof_a2 = ((tensao[1][1] - s2)*(tensao[2][2] - s2)) - (tensao[2][1]*tensao[1][2]);
	cof_b2 = -((tensao[0][1]*(tensao[2][2] - s2)) - (tensao[1][2]*tensao[0][2]));
	cof_c2 = (tensao[0][1]*tensao[1][2]) - ((tensao[1][1] - s2)*tensao[0][2]);
	k2 = 1/sqrt(cof_a2*cof_a2 + cof_b2*cof_b2 + cof_c2*cof_c2);
	ni2 = k2*cof_a2;
	nj2 = k2*cof_b2;
	nk2 = k2*cof_c2;
	if dim==3:
		cof_a3 = ((tensao[1][1] - s3)*(tensao[2][2] - s3)) - (tensao[2][1]*tensao[1][2]);
		cof_b3 = -((tensao[0][1]*(tensao[2][2] - s3)) - (tensao[1][2]*tensao[0][2]));
		cof_c3 = (tensao[0][1]*tensao[1][2]) - ((tensao[1][1] - s3)*tensao[0][2]);
		k3 = 1/sqrt(cof_a3*cof_a3 + cof_b3*cof_b3 + cof_c3*cof_c3);
		ni3 = k3*cof_a3;
		nj3 = k3*cof_b3;
		nk3 = k3*cof_c3;
	else:
		ni3 = 0
		nj3 = 0
		nk3 = 0
		
		
	#critérios de estabilidade
	teqt= 2*taumax
	teqv=sqrt(3*j2)
	if teqt<=(fy/gama):
		saida=str("Critério de Tresca : ESTÁVEL, NÃO HÁ ESCOAMENTO.")
	else:
		saida=str("Critério de Tresca : INSTÁVEL,  HÁ ESCOAMENTO.")
	if teqv<=(fy/gama):
		saida1=str("Critério de von Mises : ESTÁVEL, NÃO HÁ ESCOAMENTO.")
	else:
		saida1=str("Critério de von Mises : INSTÁVEL,  HÁ ESCOAMENTO.")
	teta1=0.5*atan((2*tensao[0][1])/(tensao[0][0]-tensao[1][1]))
	teta2=teta1+90
	tetas=0.5*atan(-(tensao[0][0]-tensao[1][1])/(2*tensao[1][0]))


if td==2 and tt==2:
	if dim==3:
		deforaux3=defor
		defor=[[deforaux3[0][0],deforaux3[0][1]*2,deforaux3[0][2]*2],[deforaux3[1][0]*2,deforaux3[1][1],deforaux3[1][2]*2],[deforaux3[2][0]*2,deforaux3[2][1]*2,deforaux3[2][2]]]	
	if dim==2:
		deforaux3=defor
		defor=[[deforaux3[0][0],deforaux3[0][1]*2,0],[deforaux3[1][0]*2,deforaux3[1][1],0],[0,0,0]]
if dim==2 or dim==3:
	#editando a saida 
	f = open(nomeArq + ".out", 'w') # abre arq 

	#f = open("arq2.txt", 'w')
	f.write("    \n")
	f.write("                      **** ANÁLISE DO TENSOR DE TENSÃO E CRITÉRIOS DE ESCOAMENTO **** \n")
	f.write("    \n")
	f.write("    \n")
	f.write("arquivo de dados :            " + nomeArq + ".out" '\n')
	f.write("Data do processamento :                  " + str(now) +'\n')
	f.write("    \n")
	f.write("    \n")

	f.write("Tensor de Tensão Sigma_ij:                " + '\n')
	f.write("|  " +str( "%.9f" % tensao[0][0])+"  "+str( "%.9f" % tensao[0][1]) +"  "+str( "%.9f" % tensao[0][2]) +"|" + '\n')
	f.write("|  " +str( "%.9f" % tensao[1][0])+"  "+str( "%.9f" % tensao[1][1]) +"  "+str( "%.9f" % tensao[1][2]) +"|" + unidade+ '\n')
	f.write("|  " +str( "%.9f" % tensao[2][0])+"  "+str( "%.9f" % tensao[2][1]) +"  "+str( "%.9f" % tensao[2][2]) +"|" +  '\n')
	f.write("    \n")
	f.write("Tensor Desviatório S_ij :                    " +'\n')
	f.write("|  " +str( "%.9f" % desvij[0][0])+"  "+str( "%.9f" % desvij[0][1]) +"  "+str( "%.9f" % desvij[0][2]) +"|" '\n')
	f.write("|  " +str( "%.9f" % desvij[1][0])+"  "+str( "%.9f" % desvij[1][1]) +"  "+str( "%.9f" % desvij[1][2]) +"|" + unidade+ '\n')
	f.write("|  " +str( "%.9f" % desvij[2][0])+"  "+str( "%.9f" % desvij[2][1]) +"  "+str( "%.9f" % desvij[2][2]) +"|" +  '\n')
	f.write("    \n")
	f.write("Invariantes de Sigma_ij              " '\n')
	f.write("    \n")
	f.write("i1:                " +str( "%.9f" %i1 )+ unidade+ '\n')
	f.write("    \n")
	f.write("i2:                " +str( "%.9f" %i2 )+ unidade+ "²"'\n')
	f.write("    \n")
	f.write("i3:                " +str( "%.9f" %i3 )+ unidade+ "³"'\n')
	f.write("    \n")
	f.write("    \n")
	f.write("Invariantes de S_ij              " '\n')
	f.write("    \n")
	f.write("J2:                " +str( "%.9f" %j2 )+ unidade+ "²"'\n')
	f.write("    \n")
	f.write("J3:                " +str( "%.9f" %j3 )+ unidade+ "³"'\n')
	f.write("    \n")
	f.write("Ângulo de similaridade           " '\n')
	f.write("teta=              " +str( "%.9f" %tetasi)+'\n')
	f.write("    \n")
	f.write("Invariante COS(3Teta)             " '\n')
	f.write("cos(3teta)=              " +str( "%.9f" %teta)+'\n')
	f.write("    \n")
	f.write("    \n")
	f.write("Tensões Principais             " '\n')
	f.write("Sig1=            " +str( "%.9f" %s1 )+ unidade+ '\n')
	f.write("Sig2=             " +str( "%.9f" %s2) + unidade+ '\n')
	f.write("Sig3=            "+ str("%.9f" %s3) + unidade+ '\n')
	f.write("TauMx=            "+ str("%.9f" %taumax) + unidade+ '\n')
	f.write("    \n")
	f.write("    \n")
	f.write("Parâmetros do Material           " '\n')
	f.write("    \n")
	f.write("fy=            " +str( "%.9f" %fy )+ unidade+ '\n')
	f.write("Gama_mat=             " +str( "%.9f" %gama) + '\n')
	f.write("Rel.Poisson        "+ str("%.9f" %NI) + '\n')
	f.write("Mód.Young           "+ str("%.9f" %E) + unidade+ '\n')
	f.write("    \n")
	f.write("    \n")
	f.write("    \n")
	f.write("Tensor de deformação Epsilon_ij           " '\n')
	f.write("|  " +str( "%.9f" % defor[0][0])+"  "+str( "%.9f" % defor[0][1]) +"  "+str( "%.9f" % defor[0][2]) +"|" + '\n')
	f.write("|  " +str( "%.9f" % defor[1][0])+"  "+str( "%.9f" % defor[1][1]) +"  "+str( "%.9f" % defor[1][2]) +"|" +  '\n')
	f.write("|  " +str( "%.9f" % defor[2][0])+"  "+str( "%.9f" % defor[2][1]) +"  "+str( "%.9f" % defor[2][2]) +"|" +  '\n')
	f.write("    \n")
	f.write("Deformações Principais             " '\n')
	f.write("Eps1=            " +str( "%.9f" %tau1 )+  '\n')
	f.write("Eps2=             " +str( "%.9f" %tau2) + '\n')
	f.write("Eps3=            "+ str("%.9f" %tau3) + '\n')
	f.write("Gama_Mx=            "+ str("%.9f" %tauemax) + '\n')
	if (dim == 3):
		f.write("Direções Principais             " '\n')
		f.write("N1=            " +str( "%.9f" %ni1 )+"  i  "+ str( "%.9f" %nj1 )+"  j  "+str( "%.9f" %nk1 )+"  k" '\n')
		f.write("N2=            " +str( "%.9f" %ni2 )+"  i  "+ str( "%.9f" %nj2 )+"  j  "+str( "%.9f" %nk2 )+"  k" '\n')
		f.write("N3=            "+str( "%.9f" %ni3 )+"  i  "+ str( "%.9f" %nj3 )+"  j  "+str( "%.9f" %nk3 )+"  k" '\n')
	f.write("Angulos Principais             " '\n')
	f.write("teta1=            " +str( "%.9f" %teta1 )+'\n')
	f.write("teta2=             " +str( "%.9f" %teta2 )+ '\n')
	f.write("tetas=             " +str( "%.9f" %tetas )+ '\n')
	f.write("    \n")
	f.write("    \n")
	f.write("Tensão Equivalente de tresca            " '\n')
	f.write("2 Tau_mx=       " + str("%.9f" %teqt) + unidade+ '\n')
	f.write("    \n")
	f.write("Tensão Equivalente de Von Mises           " '\n')
	f.write("Sig_Eq=       " + str("%.9f" %teqv) + unidade+ '\n')
	f.write("    \n")

	f.write("Verificação da estabilidade:          " '\n')
	f.write("    \n")
	f.write("Critério de Tresca      " + saida+ '\n')
	f.write("    \n")
	f.write("Critério de Von Mises      " + saida1 + '\n')

	


