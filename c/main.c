#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;
#define SCI_SPACE_CHAR ' '
#define SCI_NULL_CHAR '\0'
#define SCI_TAM_MAX_REG_ARQUIVO 90

int main()
{
	printf("\nHello Robot Friend\n");
	char fileName[90] = "XXX_COBILING_YYY_TEST.BMP";
	char* a;
	unsigned int uTamSrc;
	char pszTmp[SCI_TAM_MAX_REG_ARQUIVO];
	int iCont;
	char pszDest[SCI_TAM_MAX_REG_ARQUIVO];
	memset(pszTmp, '\0', SCI_TAM_MAX_REG_ARQUIVO);
	memset(pszDest, '\0', SCI_TAM_MAX_REG_ARQUIVO);
	a = (char *) fileName;

	printf("String: [%s]\n",a);
	uTamSrc = strlen((char*)a);

	printf("TamSrc: [%d]\n",uTamSrc);	
	
	strncpy(pszTmp, (char*) a, uTamSrc);

	printf("Copy: [%s]\n", pszTmp);
	
	pszTmp[uTamSrc]= SCI_NULL_CHAR;
		
	printf("Copy2: [%s]\n", pszTmp);
	
	for (iCont=(uTamSrc-1); iCont>=0; iCont--){
		if (pszTmp[iCont]!=SCI_SPACE_CHAR){
			pszTmp[iCont+1]=SCI_NULL_CHAR;
			break;
		}
	}
		
	printf("Copy2: [%s]\n", pszTmp);
	strcpy((char*)pszDest, pszTmp);
	printf("Final Dest: [%s]\n", pszDest);

	// ------------- Convert to strign END ----------
	char sLine[SCI_TAM_MAX_REG_ARQUIVO];
	memset(sLine, '\0', SCI_TAM_MAX_REG_ARQUIVO);
	
	char strSeparador[2];
	strSeparador[0] = ' ';
	strSeparador[1] = '\0';

	int iTamanho;
	
	strcat(sLine, pszDest);
	strcat(sLine, strSeparador);

	printf("Linha gerada:[%s]\n", sLine);
	iTamanho = strlen(sLine);
	sLine[iTamanho-1] = '\n';

	printf("Linha gerada:[%s]\n", sLine);

	return 0;
}
