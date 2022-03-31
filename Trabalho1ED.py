def deYodafy(listapal):
    pontuacao=listapal[-1][-1]
    listapal[-1]=listapal[-1].replace(pontuacao,"")
    listapal=list(reversed(listapal))
    frasenormal=""
    for i in listapal:
        if i is not listapal[-1]:
            frasenormal+=i + " "
        else:
            frasenormal+=i
    frasenormal+=pontuacao
    print(frasenormal)


def merge(string):
    lista=string.split(":")
    lista1=[]
    lista2=[]
    for i in lista:
        pal=i
        lista1=pal.strip("[]").split(", ")
        lista1=list(map(int,lista1))
        lista2.append(lista1)
    lista2=sorted(lista2)
    ind=len(lista2)
    ind2=0
    while ind > 0:
        for i in lista2[ind2+1:]:
            if lista2[ind2][1] >= lista2[lista2.index(i)][0]:
                lista2[ind2] =[lista2[ind2][0], max(lista2[ind2][1],lista2[lista2.index(i)][1])]
                lista2.pop(lista2.index(i))
            else:
                break
        ind2+=1
        ind-=1
    for i in lista2:
        print(i,end=" ")
    print("")


def crypto(string):
    id=len(string)
    lista=[]
    
    for i in range(id+1):
        lista.append(i+1)
    while True:
        mudanca=False
        ids=0
        for j in range(len(lista)-1):
            if string[ids]=="+":
                ids+=1
                if lista[j] < lista[j+1]:
                    continue
                else:
                    lista[j],lista[j+1]=lista[j+1],lista[j]
                    mudanca=True
            else:
                ids+=1
                if lista[j] > lista[j+1]:
                    continue
                else:
                    lista[j],lista[j+1]=lista[j+1],lista[j]
                    mudanca=True
        if mudanca==False:
            string2=""
            for i in lista:
                string2+=str(i)
            print(string2)
            break

listadeprocessos=[]
id=0
while True:
    instrucao=input().split()
    if id >= len(listadeprocessos):
        id=0
    if instrucao[0]=="add":
        bloco=[]
        id2=int(instrucao[1])
        while id2 > 0:
            comando=input()
            bloco.append(comando)
            id2-=1
        listadeprocessos.append(bloco)
    
    elif instrucao[0]=="process":
        if listadeprocessos == []:
            continue
        else:
            comando=listadeprocessos[id].pop(0)
            if listadeprocessos[id]==[]:
                listadeprocessos.pop(id)
            id+=1
            comando2=[]
            comando2=comando.split()
            if comando2[0]=="deYodafy":
                deYodafy(comando2[1:])
            elif comando2[0]=="merge":
                string=""
                for i in comando2[1:]:
                    if i is not comando2[-1]:
                        if "]" in i:
                            string+=i + ":"
                        else:
                            string+=i + " "
                    else:
                        string+=i
                merge(string)
            else:
                crypto(comando2[1])
    else:
        contproc=0
        for i in listadeprocessos:
            contproc+=len(i)
        print(f"{len(listadeprocessos)} processo(s) e {contproc} comando(s) órfão(s).")
        break
