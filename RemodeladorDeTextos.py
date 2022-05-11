#!/usr/bin/env python
# coding: utf-8

# In[4]:


#IMPORTADO DEPENDENCIAS 
import nltk as nl
import pandas as pd
import random
nl.download('stopwords')
nl.download('punkt')
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords

#BASE DE DADOS DE SINONIMOS 
sinonimos="D:\BaseSinonimos.csv"
dicsin = pd.read_csv(sinonimos)

#CONTEUDO A SER PROCESSADO 
texto = "A partir do século XX, destacam-se as tecnologias de informação e comunicação através da evolução das telecomunicações, utilização dos computadores, desenvolvimento da internet e ainda, as tecnologias avançadas, que englobam a utilização de Energia Nuclear, Nanotecnologia, Biotecnologia, etc. Atualmente, a alta tecnologia, ou seja, a tecnologia mais avançada é conhecida como tecnologia de ponta"

#CODIGO RESPONSAVEL POR RESUMIR O TEXTO 

palavras = word_tokenize(texto)
palReservada = set(stopwords.words("portuguese"))
tablaFrec = dict()
for palavra in palavras:
    
    palavra = palavra.lower()
    
    if palavra in palReservada:
        continue
        
    if palavra in tablaFrec:
        
        tablaFrec[palavra] += 1
    else:
        
        tablaFrec[palavra] = 1

oracoes = sent_tokenize(texto)
valororacoes = dict()
sumaValores= int()
for oracao in oracoes:
    for palavra, frec in tablaFrec.items():
        if palavra in oracao.lower():
            if oracao in valororacoes:
                valororacoes[oracao] += frec
            else:
                valororacoes[oracao] = frec
for oracao in valororacoes:
    sumaValores += valororacoes[oracao]
promedio = int(sumaValores/(len(valororacoes)))
RESUMO = ''
for oracao in oracoes:    
    if (oracao in valororacoes) and (valororacoes[oracao] > (1.2 * promedio)):
        RESUMO += " " + oracao


#TROCA DE PALAVRAS POR SINONIMOS 
resumidoPalavras =word_tokenize(RESUMO)
resultsinonimCheck =[]
RESULTSinonimsCatalog =""
for databusca in resumidoPalavras:
    randontp = random.randint(0,10)
    if randontp == 1 :
            elemento_encontrado = None
            for s in dicsin["Palavras Similares"]:
                if databusca in s:
                    elemento_encontrado = s
                    break
            sinonimdata = elemento_encontrado
            if sinonimdata == None:
                sinonimossaida = databusca
            else :
                semelhantpalavras= sinonimdata.split(";")
                sinonimossaida=semelhantpalavras[random.randint(0,((len(semelhantpalavras))-1))]
    else:
        sinonimossaida = databusca
    resultsinonimCheck.append(sinonimossaida)
    RESULTSinonimsCatalog += " "+ sinonimossaida
print("RESUMO:\n\n", RESULTSinonimsCatalog)


# In[1]:


#import pandas as pd
#import random
#sinonimos="D:\BaseSinonimos.csv"
#databusca = "acl"
#dicsin = pd.read_csv(sinonimos)
#elemento_encontrado = None
#databusca = 'local'
#for s in dicsin["Palavras Similares"]:
#    if databusca in s:
#        elemento_encontrado = s
#        break
#sinonimdata = elemento_encontrado
#if sinonimdata == None:
#    print("Not foun sinonims")
#    sinonimossaida= databusca
#else :
#    print("Found Sinonims")
#    semelhantpalavras= sinonimdata.split(";")
#    sinonimossaida=semelhantpalavras[random.randint(0,((len(semelhantpalavras))-1))]
#print(sinonimossaida)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




