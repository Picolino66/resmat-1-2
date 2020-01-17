#include <iostream>
#include <cmath>
#include <fstream>
#include <string>

using namespace std;

int main ()
{
	//Entradas de dados
	string arquivo, nome, nome2;
	cout << "Digite: ";
	cin >> arquivo;
	
	nome = arquivo+".DAT"; //concatenar arquivo do arquivo com extensao
	ifstream leitura(nome.c_str(),ios::binary); //arquivo passado do arquivo
	
	if(!leitura.is_open( ))  // * verifica se o programa conseguiu abrir o arquivo de arquivo informado pelo usuario *
    {
		cout<<"Não foi possível abrir arquivo!\n";
        leitura.clear( ); //reseta o objeto leitura
    }
	
	//lendo os elementos no arquivo
	int contornos, figuras;
	leitura >> figuras;
	leitura >> contornos;
	
	double x[contornos], y[contornos], arestas[figuras];
	int i,j,k, aux, prox;
	
	i=0;
	while (i<figuras)
	{
		leitura >> arestas[i];
		i++;
	}
	i=0;
	while (i<contornos)
	{
		leitura >> x[i];
		leitura >> y[i]; 
		i++;
	}
	
	leitura.close();//fecha arquivo
	
	/*------------Area e Perimetro-------*/
	double area[figuras], tarea, perimetro[figuras], tperimetro;
	
	//Inicializa a variavel em 0 para ser feito o somatório e não pegar lixo
	tarea = 0; //total da area
	tperimetro = 0; //total do perimetro
	
	k=0; //variavel k utilizada para percorrer o vetor das coordenadas x e y
	aux=0; //variavel utilizada para identificar quando a figura fecha
	prox=0; //variavel que é responsavel por aderir a posição do começo da figura para poder fechar ela
	
	i=0;
	while (i<figuras) //percorre a quantidade de figuras digitadas 
	{
		//inicializamos em 0 para somatorio
		area[i] = 0; 
		perimetro[i] = 0;
		
		j=0;
		while(j<arestas[i]) //percorremos a quantidade de aresta de cada figura
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
			j++;
		}
		aux = 0; //zera para poder começar outra figura
		prox = arestas[i]+prox; //pega o ponto inicial da proxima figura
		
		//somatorio das equações
		tperimetro = tperimetro + perimetro[i];
		tarea = tarea + area[i];
		i++;
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
	
	i=0;
	while (i<figuras) //percorre a quantidade de figuras digitadas 
	{
		//inicializamos em 0 para somatorio
		CGx[i] = 0;
		CGy[i] = 0;
		j=0;
		while(j<arestas[i]) //percorremos a quantidade de aresta de cada figura
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
			j++;
		}
		aux = 0; //zera para poder começar outra figura
		prox = arestas[i]+prox; //pega o ponto inicial da proxima figura
		
		//somatorio das equações
		tCGx = tCGx + CGx[i];
		tCGy = tCGy + CGy[i];
		i++;
	}
	//calculo final do somatorio da equação
	tCGx = tCGx/(6*tarea); 
	tCGy = tCGy/(6*tarea);



	/*-----------Momento de Inércia--------------*/
	//Subtração das coordenas dos seus centro de gravidades para o calculo da Inercia
	i=0;
	while (i<contornos)
	{
		x[i] = x[i] - tCGx;
		y[i] = y[i] - tCGy;
		i++;
	}
	
	//declaração de variaveis
	double Ix[figuras], tIx, Iy[figuras], tIy, Ixy[figuras], tIxy, mpIxy, a[contornos], somaix, somaiy, somaixy, ax;
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
	
	i=0;
	while (i<figuras) //percorre a quantidade de figuras digitadas 
	{
		j=0;
		while(j<arestas[i]) //percorremos a quantidade de aresta de cada figura
		{
			if (aux==(arestas[i]-1)) //if que identifica se chegou no final da figura para fechar com o inicio
			{
				//prox identifica a coordenada inicial para fechar a figura
				//equações para calculos
				ax = ((x[k]*y[prox])-(x[prox]*y[k]));
				a[k] = ax;
				somaix = somaix + a[k]*(pow(y[k],2)+y[k]*y[prox]+pow(y[prox],2));
				somaiy = somaiy + a[k]*(pow(x[k],2)+x[k]*x[prox]+pow(x[prox],2));
				somaixy = somaixy + a[k]*(x[prox]*y[prox]+2*(x[k]*y[k])+2*(x[prox]*y[prox])+x[k]*y[k]);
			}else
			{
				//k e k+1 percorrer as coordenadas
				ax = ((x[k]*y[k+1])-(x[k+1]*y[k]));
				a[k] = ax;
				somaix = somaix + a[k]*(pow(y[k],2)+y[k]*y[k+1]+pow(y[k+1],2));
				somaiy = somaiy + a[k]*(pow(x[k],2)+x[k]*x[k+1]+pow(x[k+1],2));
				somaixy = somaixy + a[k]*(x[k+1]*y[k+1]+2*(x[k]*y[k])+2*(x[k+1]*y[k+1])+x[k]*y[k]);
			}
			k++; //incrementa para percorrer coordenada
			aux++; //incrementa para chegar no final da figura
			j++;
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
		i++;
	}
	
	i=0;
	while (i<figuras) //percorre a quantidade de figuras digitadas 
	{
		//somatorio
		tIx = tIx + Ix[i];
		tIy = tIy + Iy[i];
		tIxy = tIxy +Ixy[i];
		i++;
	}
	//calculo final da equação
	tIx = tIx/12;
	tIy = tIy/12;
	tIxy = tIxy/24;
	mpIxy = tIx + tIy;

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
	
	Kx = sqrt(tIx/tarea);
	Ky = sqrt(tIy/tarea);
	
	nome2 = arquivo + ".OUT"; //concatenar arquivo para salvar arquivo
	ofstream escrita(nome2.c_str(),ios::binary);
	if (escrita.is_open() ){
	
		//dados impressos
		escrita << fixed;
		escrita.precision(6);
		escrita << "      **** PROPRIEDADES GEOMETRICAS DAS FIGURAS PLANAS ****"<<endl;
		escrita << "                    RESULTADOS OBTIDOS:"<<endl<<endl;
		escrita << "	NUMERO DE VERTICES NO CONTORNO:    	"<<contornos<<endl<<endl;
		escrita << "	AREA DA FIGURA:                             "<<tarea<<" cm2"<<endl; 
		escrita << "	PERIMETRO DA FIGURA:                        "<<tperimetro<<" cm"<<endl;  
		escrita <<endl;
		escrita <<"	COORDENADA X DO C. G.:                      "<<tCGx<<" cm"<<endl;  
		escrita <<"	COORDENADA Y DO C. G.:                      "<<tCGy<<" cm"<<endl;  
		escrita <<endl;
		escrita <<"	MOMENTO DE INERCIA, Ix:                     "<<tIx<<" cm4"<<endl; 
		escrita <<"	MOMENTO DE INERCIA, Iy:                     "<<tIy<<" cm4 "<<endl;
		escrita <<"	PRODUTO DE INERCIA, Ixy:                    "<<tIxy<<" cm4 "<<endl;
		escrita <<"	MOMENTO POLAR DE INERCIA, Ixy:                    "<<mpIxy<<" cm4 "<<endl;
		escrita <<endl;
		escrita <<"	MOMENTO DE INERCIA MINIMO, Imn:             "<<Imin<<" cm4 "<<endl;
		escrita <<"	MOMENTO DE INERCIA MAXIMO, Imx:             "<<Imax<<" cm4 "<<endl;
		escrita <<endl;
		escrita <<"	ANG. INCL. EIXO PRINC. - Teta1:             "<<tetap1<<"°   "<<endl;
		escrita <<"	ANG. INCL. EIXO PRINC. - Teta2:             "<<tetap2<<"°   "<<endl;
		escrita <<endl;
		escrita <<"	RAIO DE GIRACAO, Rmin.:                     "<<Kx<<" cm  "<<endl;
		escrita <<"	RAIO DE GIRACAO, RmAx:			    "<<Ky<<" cm "<<endl;
	 }
	 escrita.close();
}
