#include <iostream>
#include <cmath>
#include <fstream>
#include <string>

using namespace std;

void salvarArquivo (int figuras, string nome, int nc, double totalArea, double totalPerimetro, double totalCentroX, double totalCentroY, double totalInerciaX, double totalInerciaY, 
					double totalInerciaXY, double totalInceriaPolar, double momentoInerciaMin, double momentoInceriaMax, double anguloTeta1, double anguloTeta2, double raioGiroMin, double raioGiroMax, string unidade) 
{
	
	
	string snome;
	snome = nome + ".OUT"; //concatenar nome para salvar arquivo
	ofstream escreverArq(snome.c_str(),ios::binary);
	if (escreverArq.is_open() ){
		escreverArq << fixed;
		escreverArq.precision(6);
		//dados impressos
		escreverArq << "      **** PROPRIEDADES GEOMETRICAS DAS FIGURAS PLANAS ****"<<endl;
		escreverArq << "                    RESULTADOS OBTIDOS:"<<endl<<endl;
		escreverArq << " NUMERO DE FIGURAS NO CONTORNO:    		"<<figuras<<endl;
		escreverArq << " NUMERO DE VERTICES NO CONTORNO:    	"<<nc<<endl<<endl;
		escreverArq << " AREA DA FIGURA:                     	"<<totalArea<<unidade<<"2"<<endl; 
		escreverArq << " PERIMETRO DA FIGURA:                   "<<totalPerimetro<<unidade<<""<<endl;  
		escreverArq <<endl;
		escreverArq <<"	COORDENADA X DO C. G.:                  "<<totalCentroX<<unidade<<""<<endl;  
		escreverArq <<"	COORDENADA Y DO C. G.:                  "<<totalCentroY<<unidade<<""<<endl;  
		escreverArq <<endl;
		escreverArq <<"	MOMENTO DE INERCIA, inerciaX:           "<<totalInerciaX<<unidade<<"4"<<endl; 
		escreverArq <<"	MOMENTO DE INERCIA, inerciaY:           "<<totalInerciaY<<unidade<<"4 "<<endl;
		escreverArq <<"	PRODUTO DE INERCIA, inerciaXY:          "<<totalInerciaXY<<unidade<<"4 "<<endl;
		escreverArq <<"	MOMENTO POLAR DE INERCIA, Ip:			"<<totalInceriaPolar<<unidade<<"4"<<endl;
		escreverArq <<endl;
		escreverArq <<"	MOMENTO DE INERCIA MINIMO, Imn:         "<<momentoInerciaMin<<unidade<<"4 "<<endl;
		escreverArq <<"	MOMENTO DE INERCIA MAXIMO, Imx:         "<<momentoInceriaMax<<unidade<<"4 "<<endl;
		escreverArq <<endl;
		escreverArq <<"	ANG. INCL. EIXO PRINC. - Teta1:         "<<anguloTeta1<<"°   "<<endl;
		escreverArq <<"	ANG. INCL. EIXO PRINC. - Teta2:         "<<anguloTeta2<<"°   "<<endl;
		escreverArq <<endl;
		escreverArq <<"	RAIO DE GIRACAO, Rmin.:                 "<<raioGiroMin<<unidade<<""<<endl;
		escreverArq <<"	RAIO DE GIRACAO, RmAx:			    	"<<raioGiroMax<<unidade<<""<<endl;
	 }
	 escreverArq.close();
}
int main ()
{
	//Entradas de dados
	string nome, lnome, unidade;
	cout << "Nome do arquivo: ";
	cin >> nome;
	
	lnome = nome+".DAT"; //concatenar nome do arquivo com extensao
	ifstream lerArq(lnome.c_str(),ios::binary); //nome passado do arquivo
	
	if(!lerArq.is_open( ))  //verifica se o programa conseguiu abrir o arquivo de nome informado pelo usuario *
    {
		cout<<"Não foi possível abrir arquivo!\n";
        lerArq.clear( ); //reseta o objeto lerArq
    }
	
	//lendo os elementos no arquivo
	int nc=0, figuras;
	lerArq >> figuras; //quantidade de figuras
	
	double nvc[figuras]; //coordenadas e numero de vertices de cada contorno
	int i,j,andar, identificador, inicioFigura;
	
	for (i=0; i<figuras; i++)
	{
		lerArq >> nvc[i];
		nc = nc + nvc[i];
	}
	double x[nc], y[nc];
	for (i=0; i<nc; i++)
	{
		lerArq >> x[i];
		lerArq >> y[i]; 
	}
	lerArq >> unidade;
	lerArq.close();//fecha arquivo
	
	/*------------Area e Perimetro-------*/
	double area[figuras], totalArea, perimetro[figuras], totalPerimetro;
	/*----------Centro de Gravidade-----------*/
	double centroGravidadeX[figuras], totalCentroX, centroGravidadeY[figuras], totalCentroY;
	
	
	//Inicializa a variavel em 0 para ser feito o somatório e não pegar lixo
	totalArea = 0; //total da area
	totalPerimetro = 0; //total do perimetro
	totalCentroX = 0; //total centro de gravidade em x
	totalCentroY = 0; //total centro de gravidade me y

	andar=0; //variavel andar utilizada para percorrer o vetor das coordenadas x e y
	identificador=0; //variavel utilizada para identificar quando a figura fecha
	inicioFigura=0; //variavel que é responsavel por aderir a posição do começo da figura para poder fechar ela
	
	for (i=0; i<figuras; i++) //percorre a quantidade de figuras digitadas 
	{
		//inicializamos em 0 para somatorio
		area[i] = 0; 
		perimetro[i] = 0;
		centroGravidadeX[i] = 0;
		centroGravidadeY[i] = 0;
		for (j=0; j<nvc[i]; j++) //percorremos a quantidade de aresta de cada figura
		{
			if (identificador==(nvc[i]-1)) //if que identifica se chegou no final da figura para fechar com o inicio
			{
				//inicioFigura identifica a coordenada inicial para fechar a figura
				//equações para calculos
				perimetro[i] = perimetro[i] + sqrt(pow((x[inicioFigura]-x[andar]),2) + pow((y[inicioFigura]-y[andar]),2)); 
				area[i] = area[i] + (x[andar]*y[inicioFigura]-x[inicioFigura]*y[andar]);
				centroGravidadeX[i] = centroGravidadeX[i] + ((x[andar]+x[inicioFigura])*(x[andar]*y[inicioFigura]-x[inicioFigura]*y[andar]));
				centroGravidadeY[i] = centroGravidadeY[i] + ((y[andar]+y[inicioFigura])*(x[andar]*y[inicioFigura]-x[inicioFigura]*y[andar]));
			}else
			{
				//andar e andar+1 percorrer as coordenadas
				perimetro[i] = perimetro[i] + sqrt(pow((x[andar+1]-x[andar]),2) + pow((y[andar+1]-y[andar]),2));
				area[i] = area[i] + (x[andar]*y[andar+1]-x[andar+1]*y[andar]);
				centroGravidadeX[i] = centroGravidadeX[i] + ((x[andar]+x[andar+1])*(x[andar]*y[andar+1]-x[andar+1]*y[andar]));
				centroGravidadeY[i] = centroGravidadeY[i] + ((y[andar]+y[andar+1])*(x[andar]*y[andar+1]-x[andar+1]*y[andar]));
			}
			andar++; //incrementa para percorrer coordenada
			identificador++; //incrementa para chegar no final da figura
		}
		identificador = 0; //zera para poder começar outra figura
		inicioFigura = nvc[i]+inicioFigura; //pega o ponto inicial da proxima figura
		
		//somatorio das equações
		totalPerimetro = totalPerimetro + perimetro[i];
		totalArea = totalArea + area[i];
		totalCentroX = totalCentroX + centroGravidadeX[i];
		totalCentroY = totalCentroY + centroGravidadeY[i];
	}
	totalArea = 0.5*totalArea; //calculo area
	totalCentroX = totalCentroX/(6*totalArea); //calculo centro de gravidade x 
	totalCentroY = totalCentroY/(6*totalArea); // calculo centro de gravidade y
	
	/*-----------Momento de Inércia--------------*/
	//Subtração das coordenas dos seus centro de gravidades para o calculo da Inercia
	for (i=0; i<nc; i++)
	{
		x[i] = x[i] - totalCentroX;
		y[i] = y[i] - totalCentroY;
	}
	
	//declaração de variaveis
	double inerciaX[figuras], totalInerciaX, inerciaY[figuras], totalInerciaY, inerciaXY[figuras], totalInerciaXY, totalInceriaPolar, a[nc], somaIX, somaIY, somaIXY, aCalc;
	//inicialização em 0 para somatorio
	totalInerciaX = 0;
	totalInerciaY = 0;
	totalInerciaXY = 0;
	somaIX = 0;
	somaIY = 0;
	somaIXY = 0;
	aCalc = 0;
	andar=0; //variavel andar utilizada para percorrer o vetor das coordenadas x e y
	identificador=0; //variavel utilizada para identificar quando a figura fecha
	inicioFigura=0; //variavel que é responsavel por aderir a posição do começo da figura para poder fechar ela
	
	for (i=0; i<figuras; i++) //percorre a quantidade de figuras digitadas 
	{
		for (j=0; j<nvc[i]; j++) //percorremos a quantidade de aresta de cada figura
		{
			if (identificador==(nvc[i]-1)) //if que identifica se chegou no final da figura para fechar com o inicio
			{
				//inicioFigura identifica a coordenada inicial para fechar a figura
				//equações para calculos
				aCalc = ((x[andar]*y[inicioFigura])-(x[inicioFigura]*y[andar]));
				a[andar] = aCalc;
				somaIX = somaIX + a[andar]*(pow(y[andar],2)+y[andar]*y[inicioFigura]+pow(y[inicioFigura],2));
				somaIY = somaIY + a[andar]*(pow(x[andar],2)+x[andar]*x[inicioFigura]+pow(x[inicioFigura],2));
				somaIXY = somaIXY + a[andar]*(x[andar]*y[inicioFigura]+2*(x[andar]*y[andar])+2*(x[inicioFigura]*y[inicioFigura])+x[inicioFigura]*y[andar]);
			}else
			{
				//andar e andar+1 percorrer as coordenadas
				aCalc = ((x[andar]*y[andar+1])-(x[andar+1]*y[andar]));
				a[andar] = aCalc;
				somaIX = somaIX + a[andar]*(pow(y[andar],2)+y[andar]*y[andar+1]+pow(y[andar+1],2));
				somaIY = somaIY + a[andar]*(pow(x[andar],2)+x[andar]*x[andar+1]+pow(x[andar+1],2));
				somaIXY = somaIXY + a[andar]*(x[andar]*y[andar+1]+2*(x[andar]*y[andar])+2*(x[andar+1]*y[andar+1])+x[andar+1]*y[andar]);
			}
			andar++; //incrementa para percorrer coordenada
			identificador++; //incrementa para chegar no final da figura
		}
		identificador = 0; //zera para poder começar outra figura
		inicioFigura = nvc[i]+inicioFigura; //pega o ponto inicial da proxima figura
		
		//somatorio das equações
		inerciaX[i] = somaIX;
		inerciaY[i] = somaIY;
		inerciaXY[i] = somaIXY;
		somaIX=0;
		somaIY=0;
		somaIXY=0;
	}
	
	for (i=0; i<figuras; i++) //percorre a quantidade de figuras digitadas 
	{
		//somatorio
		totalInerciaX = totalInerciaX + inerciaX[i];
		totalInerciaY = totalInerciaY + inerciaY[i];
		totalInerciaXY = totalInerciaXY +inerciaXY[i];
	}
	//calculo final da equação
	totalInerciaX = totalInerciaX/12;
	totalInerciaY = totalInerciaY/12;
	totalInerciaXY = totalInerciaXY/24;
	totalInceriaPolar = totalInerciaX + totalInerciaY;

	//Abaixo só o uso de equações
	/*------Momento de Inercia Minimo e Maximo------*/
	double momentoInceriaMax, momentoInerciaMin;
	
	momentoInceriaMax = (totalInerciaX+totalInerciaY)/2 + sqrt(pow(((totalInerciaX-totalInerciaY)/2),2)+pow(totalInerciaXY,2));
	momentoInerciaMin = (totalInerciaX+totalInerciaY)/2 - sqrt(pow(((totalInerciaX-totalInerciaY)/2),2)+pow(totalInerciaXY,2));
	
	
	/*-------TetaP--------*/
	double anguloTeta1, anguloTeta2;
	
	anguloTeta1 = (atan(-totalInerciaXY/((totalInerciaX-totalInerciaY)/2)))/2;
	anguloTeta1 = anguloTeta1*180/M_PI;
	anguloTeta2 = anguloTeta1 + 90;
	
	
	/*--------Raio de giração------------*/
	double raioGiroMin, raioGiroMax;
	
	raioGiroMin = sqrt(momentoInerciaMin/totalArea);
	raioGiroMax = sqrt(momentoInceriaMax/totalArea);
	
	//chama funcao que salva no arquivo
	salvarArquivo(figuras, nome, nc, totalArea, totalPerimetro, totalCentroX, totalCentroY, totalInerciaX, totalInerciaY, totalInerciaXY, 
				totalInceriaPolar, momentoInerciaMin, momentoInceriaMax, anguloTeta1, anguloTeta2, raioGiroMin, raioGiroMax, unidade);
}
