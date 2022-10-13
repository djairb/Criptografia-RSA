def retornaListaString(texto):
  lista = []
  valor = 0
  texto = texto.split(" ")
  for i in texto:
    try:
      valor = int(i)
      lista.append(valor)
    except:
      pass
  return lista



def criptografiaASC(mensagem):
  mensagemCritografada = ""
  for letra in mensagem:
    mensagemCritografada += str(ord(letra)) + " "
  return mensagemCritografada

def descriptografiaASC(mensagemCifrada):
  mensagemDecifrada = ""
  listaCod = mensagemCifrada.split(" ")
  for codigo in listaCod:
    letraFormatada = chr(int(codigo))
    mensagemDecifrada += letraFormatada
  return mensagemDecifrada

def Eprimo(number):
  if number > 1:
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True

def gerarPeQ(numero):
  algorNum = numero
  listaPeQ = []
  for i in range(1000):
    if len(str(i)) == algorNum:
      if Eprimo(i):
        listaPeQ.append(i)
        if len(listaPeQ) == 2:
          break
  return listaPeQ

def retornaListaDivisores(numero):
  listaDivisores = []
  for i in range(1, numero+1):
    if numero%i == 0:
      if i != 1:
          listaDivisores.append(i)
  return listaDivisores

def comparaListaDivisores(lista1, lista2):
  for i in lista1:
    if i in lista2:
      #algum dos divisores sao comuns
      return True
  return False

def gerarChavesPublicas(p,q):#nEeEtotieneN
  n = p*q
  totieneN = (p-1)*(q-1)
  listaTotieneN = retornaListaDivisores(totieneN)
  global valorE
  for i in range(2, totieneN):
    listaE = retornaListaDivisores(i)
    if comparaListaDivisores(listaTotieneN, listaE):
      pass
    else:
      valorE = i
      break
  lista = [n,valorE, totieneN]
  return lista

def gerarD(valorE, totieneN):
  global ValorD
  for i in range(10000):
    #multiplicar x por e
    numero = i*valorE
    if numero%totieneN == 1:
      ValorD = i
      break
  return ValorD
#------- receber umvalor k e definir p e q
"""entrada = int(input("Defina o numero de algarismos que terao os primos"))
listapq = gerarPeQ(entrada)
p, q = listapq[0], listapq[1]"""
p = 17
q = 23
listaPublicas = gerarChavesPublicas(p, q)
n = listaPublicas[0]
e = listaPublicas[1]
totieneN = listaPublicas[2]
ValorD = gerarD(e, totieneN)

#definicaodeD
#um numero que multiplicado por E e dividido por TotientedeN apresente resto 1


print("\nAs chaves publicas são: n = %i,  e = %i\n" % (n, valorE))

print("As chaves privadas do sistema são: p = %i,  q = %i, d = %i\n" % (p, q, ValorD))

#ENCRIPTAÇÃO
#mensagempraASC
"""mensagemM = input("Digite a mensagem aqui: ")
chaveN = int(input("Digite a chave N: "))
chaveE = int(input("Digite a chave E: "))"""
n = 391
e = 3
mensagem = "morte ao miojo"
mensagemCod = criptografiaASC(mensagem)
listaASC = retornaListaString(mensagemCod)
listaCodRSA = []
#c é o resto que m^e apresenta ao ser divido por n
for m in listaASC:
  mElevadoaE = m**e
  c = mElevadoaE%n
  listaCodRSA.append(c)
print("A mensagem cifrada pelo sistema RSA é igual a: ")
print(listaCodRSA)

#assumindoDoisAlgarismosparaPeQ
#listapq = gerarPeQ(2)
#p, q = listapq[0], listapq[1]
#gerando os valores de n, e, e totieneN
p = 17
q = 23
listaPublicas = gerarChavesPublicas(p, q)
n = listaPublicas[0]
e = listaPublicas[1]
totieneN = listaPublicas[2]
#gerando o valor de d
ValorD = gerarD(e, totieneN)
#descriptografando
#c é o resto que m^e apresenta ao ser divido por n
print(ValorD)
listaDescRSA = []
for c in listaCodRSA:
  cElevadoad = c**ValorD
  m = cElevadoad%n
  listaDescRSA.append(m)
print(listaDescRSA)
print("mensagem Decifrada: ")
texto = ""
for i in listaDescRSA:
  texto += str(i) + " "
print(descriptografiaASC(texto[:-1]))




    



 

