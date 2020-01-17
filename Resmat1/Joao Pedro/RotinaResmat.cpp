//Bibliotecas
#include <iostream> //biblioteca padrao c++
#include <cmath> //biblioteca matemática
#include <fstream> //biblioteca de arquivo
#include <string> //biblioteca tipo texto

using namespace std;

int main ()
{
	/*ABRIR ARQUIVO PARA LEITURA*/
	//Entradas de dados
	string nome, leituranome,salvarnome, medida;
	cout << "Digite o nome do arquivo que sera aberto: ";
	cin >> nome;
	
	leituranome = nome+".DAT"; //concatenar nome do arquivo com extensao
	ifstream leitura(leituranome.c_str(),ios::binary); //nome passado do arquivo
	
	if(!leitura.is_open( ))  // * verifica se o programa conseguiu abrir o arquivo de nome informado pelo usuario *
    {
		cout<<"Não foi possível abrir arquivo!\n";
        leitura.clear( ); //reseta o objeto leitura
    }
	
	//lendo os elementos no arquivo
	int pontos = 0, figuras;
	/* LEITURA DAS LINHAS DO ARQUIVO PASSADO */
	leitura >> figuras;
	
	double arestas[figuras];
	int i,j,k, aux, prox;
	/*LOOP PARA LER OS PONTOS DE CADA FIGURA*/
	for (i=0; i<figuras; i++)
	{
		leitura >> arestas[i];
		pontos = arestas[i] + pontos;
	}
	double x[pontos], y[pontos];
	/*LOOP PARA LER COORDENADAS*/
	for (i=0; i<pontos; i++)
	{
		leitura >> x[i];
		leitura >> y[i];
	}
	leitura >> medida;
	leitura.close();//fecha arquivo
	
	/*------------Area e Perimetro-------*/
	double area[figuras], tarea, perimetro[figuras], tperimetro;
	
	//Inicializa a variavel em 0 para ser feito o somatório e não pegar lixo
	tarea = 0; //total da area
	tperimetro = 0; //total do perimetro
	
	k=0; //variavel k utilizada para percorrer o vetor das coordenadas x e y
	aux=0; //variavel utilizada para identificar quando a figura fecha
	prox=0; //variavel que é responsavel por aderir a posição do começo da figura para poder fechar ela
	
	for (i=0; i<figuras; i++) //percorre a quantidade de figuras digitadas 
	{
		//inicializamos em 0 para somatorio
		area[i] = 0; 
		perimetro[i] = 0;		
		for (j=0; j<arestas[i]; j++) //percorremos a quantidade de aresta de cada figura
		{
			if (aux==(arestas[i]-1)) //if que identifica se chegou no final da figura para fechar com o inicio
			{
				//prox identifica a coordenada inicial para fechar a figura
				//equações para calculos
				perimetro[i] = perimetro[i] + sqrt(pow((x[prox]-x[k]),2) + pow((y[prox]-y[k]),2)); 
				area[i] = area[i] + (x[k]*y[prox]-x[prox]*y[k]);
			}else
			{
				//k e k+1 percorrer as coordenadas
				perimetro[i] = perimetro[i] + sqrt(pow((x[k+1]-x[k]),2) + pow((y[k+1]-y[k]),2));
				area[i] = area[i] + (x[k]*y[k+1]-x[k+1]*y[k]);
			}
			k++; //incrementa para percorrer coordenada
			aux++; //incrementa para chegar no final da figura
		}
		aux = 0; //zera para poder começar outra figura
		prox = arestas[i]+prox; //pega o ponto inicial da proxima figura
		
		//somatorio das equações
		tperimetro = tperimetro + perimetro[i];
		tarea = tarea + area[i];
	}
	tarea = 0.5*tarea; //calculo area

	
	/*----------Centro de Gravidade-----------*/
	//declaração de variaveis
	double CGx[figuras], tCGx, CGy[figuras], tCGy;
	
	//inicialização em 0 para somatorio
	tCGx = 0;
	tCGy = 0;
	
	k=0; //variavel k utilizada para percorrer o vetor das coordenadas x e y
	aux=0; //variavel utilizada para identificar quando a figura fecha
	prox=0; //variavel que é responsavel por aderir a posição do começo da figura para poder fechar ela
	
	for (i=0; i<figuras; i++) //percorre a quantidade de figuras digitadas 
	{
		//inicializamos em 0 para somatorio
		CGx[i] = 0;
		CGy[i] = 0;
		for (j=0; j<arestas[i]; j++) //percorremos a quantidade de aresta de cada figura
		{
			if (aux==(arestas[i]-1)) //if que identifica se chegou no final da figura para fechar com o inicio
			{
				//prox identifica a coordenada inicial para fechar a figura
				//equações para calculos
				CGx[i] = CGx[i] + ((x[k]+x[prox])*(x[k]*y[prox]-x[prox]*y[k]));
				CGy[i] = CGy[i] + ((y[k]+y[prox])*(x[k]*y[prox]-x[prox]*y[k]));
			}else
			{
				//k e k+1 percorrer as coordenadas
				CGx[i] = CGx[i] + ((x[k]+x[k+1])*(x[k]*y[k+1]-x[k+1]*y[k]));
				CGy[i] = CGy[i] + ((y[k]+y[k+1])*(x[k]*y[k+1]-x[k+1]*y[k]));
			}
			k++; //incrementa para percorrer coordenada
			aux++; //incrementa para chegar no final da figura
		}
		aux = 0; //zera para poder começar outra figura
		prox = arestas[i]+prox; //pega o ponto inicial da proxima figura
		
		//somatorio das equações
		tCGx = tCGx + CGx[i];
		tCGy = tCGy + CGy[i];
	}
	//calculo final do somatorio da equação
	tCGx = tCGx/(6*tarea); 
	tCGy = tCGy/(6*tarea);



	/*-----------Momento de Inércia--------------*/
	//Subtração das coordenas dos seus centro de gravidades para o calculo da Inercia
	for (i=0; i<pontos; i++)
	{
		x[i] = x[i] - tCGx;
		y[i] = y[i] - tCGy;
	}
	
	//declaração de variaveis
	double Ix[figuras], tIx, Iy[figuras], tIy, Ixy[figuras], tIxy, a[pontos], somaix, somaiy, somaixy, ax, pI;
	//inicialização em 0 para somatorio
	tIx = 0;
	tIy = 0;
	tIxy = 0;
	somaix = 0;
	somaiy = 0;
	somaixy = 0;
	ax = 0;
	k=0; //variavel k utilizada para percorrer o vetor das coordenadas x e y
	aux=0; //variavel utilizada para identificar quando a figura fecha
	prox=0; //variavel que é responsavel por aderir a posição do começo da figura para poder fechar ela
	
	for (i=0; i<figuras; i++) //percorre a quantidade de figuras digitadas 
	{
		for (j=0; j<arestas[i]; j++) //percorremos a quantidade de aresta de cada figura
		{
			if (aux==(arestas[i]-1)) //if que identifica se chegou no final da figura para fechar com o inicio
			{
				//prox identifica a coordenada inicial para fechar a figura
				//equações para calculos
				ax = ((x[k]*y[prox])-(x[prox]*y[k]));
				a[k] = ax;
				somaix = somaix + a[k]*(pow(y[k],2)+y[k]*y[prox]+pow(y[prox],2));
				somaiy = somaiy + a[k]*(pow(x[k],2)+x[k]*x[prox]+pow(x[prox],2));
				somaixy = somaixy + a[k]*(x[k]*y[prox]+2*(x[k]*y[k])+2*(x[prox]*y[prox])+x[prox]*y[k]);
			}else
			{
				//k e k+1 percorrer as coordenadas
				ax = ((x[k]*y[k+1])-(x[k+1]*y[k]));
				a[k] = ax;
				somaix = somaix + a[k]*(pow(y[k],2)+y[k]*y[k+1]+pow(y[k+1],2));
				somaiy = somaiy + a[k]*(pow(x[k],2)+x[k]*x[k+1]+pow(x[k+1],2));
				somaixy = somaixy + a[k]*(x[k]*y[k+1]+2*(x[k]*y[k])+2*(x[k+1]*y[k+1])+x[k+1]*y[k]);
			}
			k++; //incrementa para percorrer coordenada
			aux++; //incrementa para chegar no final da figura
		}
		aux = 0; //zera para poder começar outra figura
		prox = arestas[i]+prox; //pega o ponto inicial da proxima figura
		
		//somatorio das equações
		Ix[i] = somaix;
		Iy[i] = somaiy;
		Ixy[i] = somaixy;
		somaix=0;
		somaiy=0;
		somaixy=0;
	}
	
	for (i=0; i<figuras; i++) //percorre a quantidade de figuras digitadas 
	{
		//somatorio
		tIx = tIx + Ix[i];
		tIy = tIy + Iy[i];
		tIxy = tIxy +Ixy[i];
	}
	//calculo final da equação
	tIx = tIx/12;
	tIy = tIy/12;
	tIxy = tIxy/24;
	pI = tIx + tIy;

	//Abaixo só o uso de equações
	/*------Momento de Inercia Minimo e Maximo------*/
	double Imax, Imin;
	
	Imax = (tIx+tIy)/2 + sqrt(pow(((tIx-tIy)/2),2)+pow(tIxy,2));
	Imin = (tIx+tIy)/2 - sqrt(pow(((tIx-tIy)/2),2)+pow(tIxy,2));
	
	
	/*-------TetaP--------*/
	double tetap1, tetap2;
	
	tetap1 = (atan(-tIxy/((tIx-tIy)/2)))/2;
	tetap1 = tetap1*180/M_PI;
	tetap2 = tetap1 + 90;
	
	
	/*--------Raio de giração------------*/
	double Kx, Ky;
	
	Kx = sqrt(Imax/tarea);
	Ky = sqrt(Imin/tarea);
	
	salvarnome = nome + ".OUT"; //concatenar nome para salvar arquivo
	ofstream salvar(salvarnome.c_str(),ios::binary);
	
	/*DEFINIÇÃO DE PRECISÃO*/
	salvar << fixed;
	salvar.precision(6);
	
	if (salvar.is_open() ){
	
		//dados impressos
		salvar << "      **** PROPRIEDADES GEOMETRICAS DAS FIGURAS PLANAS ****"<<endl;
		salvar << "                    RESULTADOS OBTIDOS:"<<endl<<endl;	
		salvar << "	NUMERO DE CONTORNOS NA FIGURA:    	"<<figuras<<endl<<endl;
		salvar << "	NUMERO DE VERTICES NO CONTORNO:    	"<<pontos<<endl<<endl;
		salvar << "	AREA DA FIGURA:                             "<<tarea<<" "<<medida<<"²"<<endl; 
		salvar << "	PERIMETRO DA FIGURA:                        "<<tperimetro<<" "<<medida<<endl;  
		salvar <<endl;
		salvar <<"	COORDENADA X DO C. G.:                      "<<tCGx<<" "<<medida<<endl;  
		salvar <<"	COORDENADA Y DO C. G.:                      "<<tCGy<<" "<<medida<<endl;  
		salvar <<endl;
		salvar <<"	MOMENTO DE INERCIA, Ix:                     "<<tIx<<" "<<medida<<"4"<<endl; 
		salvar <<"	MOMENTO DE INERCIA, Iy:                     "<<tIy<<" "<<medida<<"4"<<endl;
		salvar <<"	PRODUTO DE INERCIA, Ixy:                    "<<tIxy<<" "<<medida<<"4"<<endl;
		salvar <<"	MOMENTO POLAR DE INÉRCIA, Ip:				"<<pI<<" "<<medida<<"4"<<endl;
		salvar <<endl;
		salvar <<"	MOMENTO DE INERCIA MINIMO, Imn:             "<<Imin<<" "<<medida<<"4"<<endl;
		salvar <<"	MOMENTO DE INERCIA MAXIMO, Imx:             "<<Imax<<" "<<medida<<"4"<<endl;
		salvar <<endl;
		salvar <<"	ANG. INCL. EIXO PRINC. - Teta1:             "<<tetap1<<"°   "<<endl;
		salvar <<"	ANG. INCL. EIXO PRINC. - Teta2:             "<<tetap2<<"°   "<<endl;
		salvar <<endl;
		salvar <<"	RAIO DE GIRACAO, Rmin.:                     "<<Ky<<" "<<medida<<endl;
		salvar <<"	RAIO DE GIRACAO, RmAx:			    		"<<Kx<<" "<<medida<<endl;
	 }
	 salvar.close();
}
