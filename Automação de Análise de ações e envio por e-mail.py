#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Buscando a cotações da Ação selecionada

import yfinance
print("MagicAnalizer&Send - developed by: Mathäus H.")
print ("---*---" * 6)

ticker = str(input("Digite o código da ação: ")).upper().strip()
dados = yfinance.Ticker(ticker)
dados.history()
    
#Configuração do período de análise
tabela = dados.history("6mo")
tabela


# In[3]:


#Selecionando apenas a coluna de fechamento do histórico gerado
fechamento = tabela.Close
fechamento


# In[4]:


#Geração de gráfico simples de linha
grafico = fechamento.plot()


# In[5]:


#Gerar as estatísticas
maxima = fechamento.max()
minima = fechamento.min ()
atual = fechamento [-1]

print (maxima)
print (minima)
print (atual)


# In[26]:


import pyautogui
import pyperclip


# In[12]:


#Código que irá gerar o e-mail que enviaremos para o "chefe"

destinatario = "don.canoas@hotmail.com"
assunto = "Análise Diária"

mensagem = f"""
Bom dia,

Segue abaixo as análises da ação {ticker} dos últimos seis meses:

Cotação máxima: R$ {round (maxima,2) }
Cotação mínima: R$ {round (minima,2) }
Cotação atual: R$ {round (atual,2) }

Atenciosamente,
Mathäus Hamermüller
"""


# In[13]:


#E-mail gerado através do código acima
print (destinatario)
print (assunto)
print (mensagem)


# In[28]:


#Automatizando teclado e mouse para enviar o e-mail

#Tempo de pausa entre as ações do pyautogui
pyautogui.PAUSE = 5

#abrir uma nova guia do navegador
pyautogui.hotkey("ctrl" , "t")

#escrever o site do e-mail e dar um Enter
pyautogui.write("www.gmail.com")
pyautogui.press("enter")

#Posição que o mouse vai ir e clicar para escrever o e-mail
pyautogui.click(x=36, y=170)

#preencher o destinatário
pyperclip.copy(destinatario)
pyautogui.hotkey ("ctrl", "v")
pyautogui.press ("tab")

#Preencher o assunto
pyperclip.copy (assunto)
pyautogui.hotkey ("ctrl" , "v")
pyautogui.press ("tab")

#Preencher o corpo do e-mail
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

#Clicar no "Enviar"
pyautogui.hotkey("ctrl", "enter")

#fechar a aba do e-mail
pyautogui.hotkey("ctrl", "w")

#Mensagem de sucesso do envio
print ("E-mail enviado com sucesso")


# In[27]:





# In[ ]:





# In[ ]:




