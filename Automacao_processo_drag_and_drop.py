#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pyautogui

pyautogui.alert("O programa DRAG_AND_DROP será sendo executado.")
pyautogui.PAUSE = 1
# Entrar no meu google drive
pyautogui.press('winleft')
pyautogui.write('Chrome')
pyautogui.press('enter')
pyautogui.write('https://drive.google.com/')
pyautogui.press('enter')

# Entrar na área de trabalho
pyautogui.hotkey('winleft', 'd')
# Clicar no arquivo e arrasta-lo para o google drive
pyautogui.moveTo(1856, 220)
pyautogui.mouseDown()
pyautogui.moveTo(1047, 778)
pyautogui.hotkey('alt', 'tab')
pyautogui.mouseUp()

time.spleep(5)
pyautogui.alert("O programa DRAG_AND_DROP foi executado com sucesso.")


# In[15]:


pyautogui.position()

