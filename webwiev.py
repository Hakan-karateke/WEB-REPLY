import webbrowser,time,os
for a in range(1):#burada belirteceğiniz kadar açılacaktır 
ad='www.google.com.tr'#açmak istediğiniz adresi paranteze yazın
time.sleep(30)
webbrowser.open_new(ad)
prg ="chrome.exe"
os.system("taskkill /f /im "+prg)