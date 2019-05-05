import smbus 
import time 

bus = smbus.SMBus(1)
address = 0x48
def getR(delVol):
    if delVol == 5:
        return None
    else: 
        return delVol * (5000 / (5 - delVol)) 

def getV(port):
    return bus.read_byte_data(address, port) / 255 * 5

if __name__ == '__main__':
    while True:
        temp = getV(3)
        LSR = getR(getV(3))
        #print("Port2:%.2f:"%getV(2))
        #print("Port3:%.2f:"%getV(3))

        print("P3 %.2fVolt"%temp, end = ",")
        print("P2%.2fVolt"%getV(2))
        #print("%.2fOhm"%LSR)
        time.sleep(1)
