from tkinter import Event
from typing import Text
import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Window
from first_page_crawl import FirstPageCrawl

kommuner = [["taby-kommun"], ["asgasd"], ["jahsd"]]
omraden_for_kommun = [[""],["ga"],["gsd"]]


layout = [  [psg.Text("Kommun"), psg.Text("                     "),psg.Text("Område")], 
            [psg.Listbox(kommuner, size=(20,10), enable_events=False, key='_KOMMUNER_'), psg.Listbox(omraden_for_kommun, size=(20,10), enable_events=False, key='_OMRADE_')], 
            [psg.Button("Start"), psg.Button("Close")]  
        ]

Window = psg.Window("HemnetWatch", layout, margins=(200, 50))

while True:
    event, values = Window.read()
    if event == "Close" or event == psg.WIN_CLOSED:
        break
    print(str(values["_KOMMUNER_"])[3:-3], str(values["_OMRADE_"])[3:-3])
    fpc = FirstPageCrawl(str(values["_KOMMUNER_"])[3:-3], str(values["_OMRADE_"])[3:-3])
    fpc.initializeCrawl()
    fpc.runCrawl()

Window.close()