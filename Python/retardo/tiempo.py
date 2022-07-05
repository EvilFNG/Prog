def CalculoCM(F,t):
    tCM = 4/(F*(10**6))
    #print(tCM)
    return int((t*(10**(-3))) / tCM)
    #print(CM)

def Var1porM1(N,cm):
    MaxCM1 = 5 + (256 * (N + 3))
    #print(MaxCM1)
    Var11D = (cm-5) / (N + 3) 
    #print(Var11D)
    Nopsres1 = cm - (5 + (int(Var11D) * (N + 3)))
    if (cm <= MaxCM1):
        return f"Var1 = {int(Var11D)} Nops = {Nopsres1}"
    else:
        return "No se puede obtener el tiempo solicitado por este metodo"

def VarMetodo2(N,cm):
    nopsres = 10
    Var22 = 256
    Var21 = 256
    MaxCM2 = 7 + (4 * Var22) + ((3+N) * Var21 * Var22)
    #print(MaxCM2)
    if (cm > MaxCM2):
        return "No se puede obtener el tiempo solicitado por este metodo"
    Var22p = 1 
    Var21p = 2
    while (Var22p<=256 and Var21p >= 1):
        Var21p = (cm - 7 - (4 * Var22p))/((N+3) * Var22p)
        Cmp = 7 + (4 * Var22p) + ((N+3) * int(Var21p) * Var22p)
        resnop = cm - Cmp
        if (resnop< nopsres and int(Var21p)< 257 and int(Var22p) < 257):
            nopsres = resnop
            Var21 = int(Var21p)
            Var22 = Var22p
            if (nopsres == 0):
                return f'Var1 = {Var21}  Var2 = {Var22} Nops =  {nopsres} '
        Var22p = Var22p + 1
    return f'Var1 = {Var21}  Var2 = {Var22} Nops =  {nopsres} '
    
def VarMetodo3(N,cm):
    nopsres = 10
    Var31 = 256
    Var32 = 256
    Var33 = 256
    MaxCM3 = 9 + (4*Var31) + (4 * Var31 * Var33) +((3+N) * Var31 * Var32 * Var33)
    if (cm > MaxCM3): 
        return "No se puede obtener el tiempo solicitado por este metodo"
    Var31p = 2
    Var32p = 1
    Var33p = 1
    while (Var33p < 257):
        while (Var32p < 257 and Var31p >= 1):
            Var31p = (cm - 9)/(4 + (4 * Var33p) + ((3+N)*Var32p * Var33p))
            Cmp = 9 + (4*int(Var31p)) + (4*int(Var31p)*Var33p) + ((3+N)* int(Var31p) * Var32p * Var33p)
            resnop = cm - Cmp
            #print(f'{Var31p}  {Var32p}  {Var33p}  {resnop}')
            if (resnop< nopsres and int(Var31p)< 257 and int(Var32p) < 257 and int(Var33p) < 257):
                nopsres = resnop
                Var31 = int(Var31p)
                Var32 = Var32p
                Var33 = Var33p
                if (nopsres == 0):
                    return f'Var1 = {Var31}  Var2 = {Var32}  Var3 = {Var33}  Nops =  {nopsres} '
            Var32p = Var32p + 1
        Var31p = 2
        Var32p = 1
        Var33p = Var33p + 1
    return f'Var1 = {Var31}  Var2 = {Var32}  Var3 = {Var33}  Nops =  {nopsres} '
            
       #INICIA PROGRAMA         
Fosc = int(input("Fosc(en Mhz): "))
Nops = int(input("Numero de Nops: "))
tiempo = float(input("Periodo de tiempo (ms): "))
CM = CalculoCM(Fosc,tiempo)
Res1 = Var1porM1(Nops,CM)
print("Por metodo 1: ")
print(Res1)
Res2 = VarMetodo2(Nops,CM)
print("Por Metodo 2: ")
print(Res2)
Res3 = VarMetodo3(Nops, CM)
print("Por Metodo 3: ")
print(Res3)

