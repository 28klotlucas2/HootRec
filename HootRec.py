import time
import sys
from time import sleep
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
kahootWWWkama = "'"
def HootRecmenu():
    print('''
██╗░░██╗░█████╗░░█████╗░████████╗██████╗░███████╗░█████╗░
██║░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██╔══██╗
███████║██║░░██║██║░░██║░░░██║░░░██████╔╝█████╗░░██║░░╚═╝
██╔══██║██║░░██║██║░░██║░░░██║░░░██╔══██╗██╔══╝░░██║░░██╗
██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║███████╗╚█████╔╝
╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚════╝░
🇧​​​​​🇾​​​​​ 🇳​​​​​🇪​​​​​🇹​​​​​🇷​​​​​🇪​​​​​🇨​​​​​
-----------------------------------------------------------------''')
    Kahootid = input('Kahoot id:')
    kahootbotname = input('Botnames:')
    sys.stdout.write('\rLoading.')
    time.sleep(0.1)
    sys.stdout.write('\rLoading..')
    time.sleep(0.5)
    sys.stdout.write('\rLoading...')
    print()
    Botgathing = print("Gathing 'Bots' ")
    if False:
        print("Failed to gather 'Bots'")
    sys.stdout.write('\r.')
    time.sleep(0.1)
    sys.stdout.write('\r..')
    time.sleep(0.5)
    sys.stdout.write('\r...')
    print("'Bots' gathered✓")
    Botnameing = print("Naming 'Bots'")
    if False:
        print("Failed to name Bots'")
    sys.stdout.write('\r.')
    time.sleep(0.1)
    sys.stdout.write('\r..')
    time.sleep(0.5)
    sys.stdout.write('\r...')
    print("'Bots' named✓")
    sys.stdout.write('\r.')
    time.sleep(0.1)
    sys.stdout.write('\r..')
    time.sleep(0.5)
    sys.stdout.write('\r...')
    botsending = print("Sending 'Bots'")
    if False:
        print("Failed to send 'Bots'")
    sys.stdout.write('\r.')
    time.sleep(0.1)
    sys.stdout.write('\r..')
    time.sleep(0.5)
    sys.stdout.write('\r...')
    numberOfBots = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    delayBeforeLeaving = 20
    delayBetweenActions = 2.5
    def createBot(Kahootid, Kahootbotname):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("test-type")
        options.add_argument("--js-flags=--expose-gc")
        options.add_argument("--enable-precise-memory-info")
        options.add_argument("--disable-default-apps")
        browser = webdriver.Chrome(options = options)
        browser.get("http://kahoot.it")
        sleep(delayBetweenActions)
        browser.find_element_by_css_selector('#inputSession').send_keys()
        browser.find_element_by_css_selector('.btn-greyscale').click()
        sleep(delayBetweenActions)
        browser.find_element_by_css_selector('#username').send_keys((u'\u200b').join(Kahootbotname))
        browser.find_element_by_css_selector('.btn-greyscale').click()
        sleep(delayBeforeLeaving)
        browser.close()
        for i in range(numberOfBots):
            Thread(target = lambda : createBot(Kahootid, kahootbotname + str(i))).start()
    print("'Bots' Sent!")
    sys.stdout.write('\r.')
    time.sleep(0.1)
    sys.stdout.write('\r..')
    time.sleep(0.5)
    sys.stdout.write('\r...')
    print("'Bots' Sent to 'www.kahoot.it/play/"+Kahootid+kahootWWWkama)
HootRecmenu()
if False:
    print('!⚠Unable to launch HootRec⚠!')

else:
    print('!⚠HootRec did not launch try again or fix the code⚠!')