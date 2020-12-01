from datetime import time
from tkinter import Button, Event
from typing import Text
import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Window
from first_page_crawl import FirstPageCrawl
import time

#Not working properly, neither is it complete

kommuner = [['ale-kommun'],['alingsas-kommun'],['alvesta-kommun'],['aneby-kommun'],['arboga-kommun'],['arjeplogs-kommun'],['arvidsjaurs-kommun'],
    ['arvika-kommun'],['askersunds-kommun'],['avesta-kommun'],['bengtsfors-kommun'],['bergs-kommun'],['bjurholms-kommun'],['bjuvs-kommun'],
    ['bodens-kommun'],['bollebygds-kommun'],['bollnas-kommun'],['borgholms-kommun'],['borlange-kommun'],['boras-kommun'],['botkyrka-kommun'],
    ['boxholms-kommun'],['bromolla-kommun'],['bracke-kommun'],['burlovs-kommun'],['bastads-kommun'],['dals-eds-kommun'],['danderyds-kommun'],
    ['degerfors-kommun'],['dorotea-kommun'],['eda-kommun'],['ekero-kommun'],['eksjo-kommun'],['emmaboda-kommun'],['enkopings-kommun'],
    ['eskilstuna-kommun'],['eslovs-kommun'],['essunga-kommun'],['fagersta-kommun'],['falkenbergs-kommun'],['falkopings-kommun'],['falu-kommun'],
    ['filipstads-kommun'],['finspangs-kommun'],['flens-kommun'],['forshaga-kommun'],['fargelanda-kommun'],['gagnefs-kommun'],['gislaveds-kommun'],
    ['gnesta-kommun'],['gnosjo-kommun'],['gotlands-kommun'],['grums-kommun'],['grastorps-kommun'],['gullspangs-kommun'],['gallivare-kommun'],
    ['gavle-kommun'],['goteborgs-kommun'],['gotene-kommun'],['habo-kommun'],['hagfors-kommun'],['hallsbergs-kommun'],['hallstahammars-kommun'],
    ['halmstads-kommun'],['hammaro-kommun'],['haninge-kommun'],['haparanda-kommun'],['heby-kommun'],['hedemora-kommun'],['helsingborgs-kommun'],
    ['herrljunga-kommun'],['hjo-kommun'],['hofors-kommun'],['huddinge-kommun'],['hudiksvalls-kommun'],['hultsfreds-kommun'],['hylte-kommun'],
    ['uppsala-habo-kommun'],['hallefors-kommun'],['harjedalens-kommun'],['harnosands-kommun'],['harryda-kommun'],['hassleholms-kommun'],
    ['hoganas-kommun'],['hogsby-kommun'],['horby-kommun'],['hoors-kommun'],['jokkmokks-kommun'],['jarfalla-kommun'],['jonkopings-kommun'],
    ['kalix-kommun'],['kalmar-kommun'],['karlsborgs-kommun'],['karlshamns-kommun'],['karlskoga-kommun'],['karlskrona-kommun'],['karlstads-kommun'],
    ['katrineholms-kommun'],['kils-kommun'],['kinda-kommun'],['kiruna-kommun'],['klippans-kommun'],['knivsta-kommun'],['kramfors-kommun'],
    ['kristianstads-kommun'],['kristinehamns-kommun'],['krokoms-kommun'],['kumla-kommun'],['kungsbacka-kommun'],['kungsors-kommun'],
    ['kungalvs-kommun'],['kavlinge-kommun'],['kopings-kommun'],['laholms-kommun'],['landskrona-kommun'],['laxa-kommun'],['lekebergs-kommun'],
    ['leksands-kommun'],['lerums-kommun'],['lessebo-kommun'],['lidingo-kommun'],['lidkopings-kommun'],['lilla-edets-kommun'],
    ['lindesbergs-kommun'],['linkopings-kommun'],['ljungby-kommun'],['ljusdals-kommun'],['ljusnarsbergs-kommun'],['lomma-kommun'],
    ['ludvika-kommun'],['lulea-kommun'],['lunds-kommun'],['lycksele-kommun'],['lysekils-kommun'],['malmo-kommun'],['malung-salens-kommun'],
    ['mala-kommun'],['mariestads-kommun'],['markaryds-kommun'],['marks-kommun'],['melleruds-kommun'],['mjolby-kommun'],['mora-kommun'],
    ['motala-kommun'],['mullsjo-kommun'],['munkedals-kommun'],['munkfors-kommun'],['molndals-kommun'],['monsteras-kommun'],['morbylanga-kommun'],
    ['nacka-kommun'],['nora-kommun'],['norbergs-kommun'],['nordanstigs-kommun'],['nordmalings-kommun'],['norrkopings-kommun'],['norrtalje-kommun'],
    ['norsjo-kommun'],['nybro-kommun'],['nykvarns-kommun'],['nykopings-kommun'],['nynashamns-kommun'],['nassjo-kommun'],['ockelbo-kommun'],
    ['olofstroms-kommun'],['orsa-kommun'],['orust-kommun'],['osby-kommun'],['oskarshamns-kommun'],['ovanakers-kommun'],['oxelosunds-kommun'],
    ['pajala-kommun'],['partille-kommun'],['perstorps-kommun'],['pitea-kommun'],['ragunda-kommun'],['robertsfors-kommun'],['ronneby-kommun'],
    ['rattviks-kommun'],['sala-kommun'],['salems-kommun'],['sandvikens-kommun'],['sigtuna-kommun'],['simrishamns-kommun'],['sjobo-kommun'],
    ['skara-kommun'],['skelleftea-kommun'],['skinnskattebergs-kommun'],['skurups-kommun'],['skovde-kommun'],['smedjebackens-kommun'],
    ['solleftea-kommun'],['sollentuna-kommun'],['solna-kommun'],['sorsele-kommun'],['sotenas-kommun'],['staffanstorps-kommun'],
    ['stenungsunds-kommun'],['stockholms-kommun'],['storfors-kommun'],['storumans-kommun'],['strangnas-kommun'],['stromstads-kommun'],
    ['stromsunds-kommun'],['sundbybergs-kommun'],['sundsvalls-kommun'],['sunne-kommun'],['surahammars-kommun'],['svalovs-kommun'],
    ['svedala-kommun'],['svenljunga-kommun'],['saffle-kommun'],['saters-kommun'],['savsjo-kommun'],['soderhamns-kommun'],['soderkopings-kommun'],
    ['sodertalje-kommun'],['solvesborgs-kommun'],['tanums-kommun'],['tibro-kommun'],['tidaholms-kommun'],['tierps-kommun'],['timra-kommun'],
    ['tingsryds-kommun'],['tjorns-kommun'],['tomelilla-kommun'],['torsby-kommun'],['torsas-kommun'],['tranemo-kommun'],['tranas-kommun'],
    ['trelleborgs-kommun'],['trollhattans-kommun'],['trosa-kommun'],['tyreso-kommun'],['taby-kommun'],['toreboda-kommun'],['uddevalla-kommun'],
    ['ulricehamns-kommun'],['umea-kommun'],['upplands-bro-kommun'],['upplands-vasby-kommun'],['uppsala-kommun'],['uppvidinge-kommun'],
    ['vadstena-kommun'],['vaggeryds-kommun'],['valdemarsviks-kommun'],['vallentuna-kommun'],['vansbro-kommun'],['vara-kommun'],['varbergs-kommun'],
    ['vaxholms-kommun'],['vellinge-kommun'],['vetlanda-kommun'],['vilhelmina-kommun'],['vimmerby-kommun'],['vindelns-kommun'],['vingakers-kommun'],
    ['vargarda-kommun'],['vanersborgs-kommun'],['vannas-kommun'],['varmdo-kommun'],['varnamo-kommun'],['vasterviks-kommun'],['vasteras-kommun'],
    ['vaxjo-kommun'],['ydre-kommun'],['ystads-kommun'],['amals-kommun'],['ange-kommun'],['are-kommun'],['arjangs-kommun'],['asele-kommun'],
    ['astorps-kommun'],['atvidabergs-kommun'],['almhults-kommun'],['alvdalens-kommun'],['alvkarleby-kommun'],['alvsbyns-kommun'],
    ['angelholms-kommun'],['ockero-kommun'],['odeshogs-kommun'],['orebro-kommun'],['orkelljunga-kommun'],['ornskoldsviks-kommun'],
    ['ostersunds-kommun'],['osterakers-kommun'],['osthammars-kommun'],['ostra-goinge-kommun'],['overkalix-kommun'],['overtornea-kommun']]


omraden_for_kommun = [[""],["ga"],["gsd"]]


layout = [  [psg.Text("Kommun"), psg.Text("                     "),psg.Text("Område")], 
            [psg.Listbox(kommuner, size=(20,10), enable_events=False, key='_KOMMUNER_'), psg.Listbox(omraden_for_kommun, size=(20,10), enable_events=False, key='_OMRADE_')], 
            [psg.Button("Start"), psg.Button("Stop"), psg.Button("Close")]  
        ]

Window = psg.Window("HemnetWatch", layout)

while True:
    event, values = Window.read()
    if event == "Close" or event == psg.WIN_CLOSED:
        break
    if event == "Start":
        fpc = FirstPageCrawl(str(values["_KOMMUNER_"])[3:-3], str(values["_OMRADE_"])[3:-3])
        while True:
            if event == "Stop": #crashes window, stopping loop not possible
                break
            fpc.initializeCrawl()
            fpc.runCrawl()
            time.sleep(5)
Window.close()