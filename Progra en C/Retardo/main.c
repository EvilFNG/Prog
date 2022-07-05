#include <stdio.h>
#include <stdlib.h>
#include <math.h>
float Var1,Var2,Var3;
int Fosc,Periodo,Nops,CM,ST,IVar1,IVar2,IVar3,NopsF,NopsR;
int Metodo1(int,int);
int Metodo2(int,int);
int Metodo3(int,int);
int ST1V(int,int);
int ST2V(int,int,int);
int ST3V(int,int,int,int);
int main()
{
    printf("Fosc(en Mhz):");
    scanf("%d",&Fosc);
    printf("Ciclos de Maquina:");
    scanf("%d",&Periodo);
    printf("Numero de Nops:");
    scanf("%d",&Nops);
    CM      =   4/Fosc;
    Metodo1(Periodo,Nops);
    Metodo2(Periodo,Nops);
    return 0;
}
ST1V(V1,N){
    ST = 5 + V1 * (N + 3);
    return ST;
}
ST2V(V1,V2,N){
    ST = 7 + 4 * V2 + ((N + 3) * V1 * V2);
    return ST;
}
ST3V(V1,V2,V3,N){
    ST = 9 + (4 * V1 * (1 + V3)) + (V1 * V2 * V3 * (N + 3));
    return ST;
}
Metodo1(T,N){
    Var1    =   (T-5) / (N + 3);
    IVar1 = floor(Var1);
    NopsF   =   T - (5 + (IVar1 * (N + 3)));
    printf("Metodo 1: ");
    if (T <= ST1V(256,N))
    {
        printf("Var1 = %d restan %d ciclos de maquina.",IVar1,NopsF);
    }
    else{
        printf("no se puede obtener el tiempo solicitado por medio de solo una variable");
    }
}
Metodo2(T,N){
    NopsF = 10;
    if (T > ST2V(256,256,N))
    {
        printf("No se puede obtener el tiempo solicitado por medio del metodo 2.");
    }
    Var1 = 1;
    Var2 = 2;
    while (Var2 <= 256 && Var1 >= 1)
    {
        Var1    =   (T - 7 - 4 * Var2) / ((N+3) * Var2);
        IVar1   =   floor(Var1);
        NopsR   =   T - ST2V(IVar1,IVar2,N);
        if (NopsR < NopsF && IVar1 <= 256 && IVar2 <= 256)
        {
            NopsF = NopsR;
            if (NopsR == 0)
            {
                printf("El valor de la variable 1 es %d, de la variable 2 es %d y el numerp de ciclos faltantes es %d",IVar1,IVar2,NopsF);
            }

        }
        Var2++;
    }
    printf("El valor de la variable 1 es %d, de la variable 2 es %d y el numerp de ciclos faltantes es %d",IVar1,IVar2,NopsF);

}
