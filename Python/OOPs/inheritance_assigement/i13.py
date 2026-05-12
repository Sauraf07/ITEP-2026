'''
13. Smart Device System
Device
SmartDevice(Device)
SmartTV(SmartDevice)
Add WiFi support.
'''
class Device:
    def wifi(self):
        print("Wifi Supported")

class SmartDevice(Device):
    def wifi(self):
        return super().wifi()
class SmartTv(Device):
    def wifi(self):
        return super().wifi()
d = Device()
d.wifi()
sd = SmartDevice()
sd.wifi()
st = SmartTv()
st.wifi()