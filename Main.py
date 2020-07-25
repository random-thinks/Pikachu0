#! encoding: utf-8

import time
from DartCCD import DartDev, DartMod

DartDev.init()
DartDev.SwitchMode(DartMod.Manual)
DartDev.ReadOnce()
DartDev.ReadCMD()
DartDev.ReadOnce()


while True:
    try:
        print (time.strftime("%Y-%m-%d %H:%M:%S %A"), end='\t')
        # Get HCHO
        DartDev.ReadCMD()
        hcho = DartDev.ReadOnce()
        if hcho < 0:
            print ("Err failed to get HCHO")
        else:
            print (f'Get HCHO = {hcho} mg/m3 ({hcho/1.2258} ppm)')
    except Exception as ex:
        print (ex)
        continue
    finally:
        time.sleep(30*60)


DartDev.dest()
