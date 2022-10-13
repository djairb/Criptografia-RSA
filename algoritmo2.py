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


mensagemM = input("Digite a mensagem aqui: ")
chaveN = int(input("Digite a chave N: "))
chaveE = int(input("Digite a chave E: "))

mensagemCod = criptografiaASC(mensagemM)
listaASC = retornaListaString(mensagemCod)
listaCodRSA = []
#c é o resto que m^e apresenta ao ser divido por n
for m in listaASC:
  mElevadoaE = m**chaveE
  c = mElevadoaE%chaveN
  listaCodRSA.append(c)
print("A mensagem cifrada pelo sistema RSA é igual a: ")
print(listaCodRSA)

