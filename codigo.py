import pyautogui 
import pandas 
import time 

pyautogui.PAUSE = 1.5 

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter") 
pyautogui.click(x=169, y=63)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(8) 

pyautogui.click(x=403, y=409)
pyautogui.write("devhyuuga@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(8)

import pandas as pd 

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: 

    pyautogui.click(x=406, y=294)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
        pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(8)
    pyautogui.scroll(5000)
