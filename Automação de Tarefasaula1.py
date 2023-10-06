# #Passo a passo do projeto
# #Passo 1: Entrar no sistema da empresa
#     #https://dlp.hashtagtreinamentos.com/python/intensivao/login
#instalar pyautogui pip install  pyautogui

import pyautogui
import time

# #pyautogui.click -> clicar com o mouse
# #pyautogui.write -> escrever um texto
# #pyautogui.press -> apertar uma tecla
# #pyautogui.hotkey -> atalho (ctrl+C)

pyautogui.PAUSE = 0.5

#abrir o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press("enter")

#entrar no link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

# #esperar o site carregar
time.sleep(3)

#Passo 2: Fazer login
#como falar para o python onde clicar? abrir um arquivo auxiliar para pegar a posicao
# '''import pyautogui
# import time
# time.sleep(5)
# print(pyautogui.position())'''

pyautogui.click(x=904, y=818)
pyautogui.write('saboechat@gmail.com')
pyautogui.press('tab') #passar para o campo senha
pyautogui.write('123456')
pyautogui.press('tab') # passar para o botao logar
pyautogui.press('enter')

time.sleep (3)

#Passo 3: Importar a base de dados
#instalar pandas terminal pip install pandas numpy empyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print (tabela)

for linha in tabela.index:
    #Passo 4: Cadastrar um produto
    pyautogui.click(x=719, y=547)

    #criando variaveis para receber o valor
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]


    #chamando a funcao direto

    #preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    pyautogui.write(str(marca))
    pyautogui.press('tab')

    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs): #se o campo obs nao for vazia preencha
        pyautogui.write(str (obs))

    #clicar no botao de enviar
    pyautogui.press('tab')
    pyautogui.press('enter')

    #Passo 5: Repetir o processo para todos os produtos
    #colocar tudo dentro do for

    #rolar a tela p cima numeros positivos
    #rolar a tela p baixo numeros negativos
    pyautogui.scroll(5000)

    #fim

    