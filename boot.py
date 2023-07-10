import network
import time

class wifi:
    def __init__ (self, SSID, SSI_PASSWORD):
        self.SSID = SSID
        self.SSI_PASSWORD = SSI_PASSWORD

list = []
list.append(wifi("Hout", "Houthoung2261"))
list.append(wifi("Parzival", "jessuschrist"))

sta_if = network.WLAN(network.STA_IF)

print('starting connection to network...')
sta_if.active(False)
time.sleep(0.5)
sta_if.active(True)

t=0
for i in list :
    sta_if.connect(i.SSID, i.SSI_PASSWORD)
    print("- Connecting to <",i.SSID, ">")
    if not sta_if.isconnected():
        while (not sta_if.isconnected() and t<5):
            print(5-t)
            t = t+1
            time.sleep(1)
        
    if sta_if.isconnected():
        print('Connected! Network config:', sta_if.ifconfig())
        break
    sta_if.status()
    sta_if.disconnect()
    t=0