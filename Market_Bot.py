import time
import cv2
import mss
import numpy
import pytesseract
import pyautogui


pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'


time.sleep(5)
pyautogui.moveTo(1113,26)
pyautogui.scroll(2)
pyautogui.mouseDown(1113, 26, button='left')
pyautogui.mouseUp(1113, 26, button='left')
time.sleep(2)
pyautogui.moveTo(221,490)
pyautogui.scroll(2) 
pyautogui.mouseDown(221, 490, button='left')
pyautogui.mouseUp(221, 490, button='left')
while 1: 
    """Hero Weapon"""
    pyautogui.moveTo(218,534)
    pyautogui.scroll(2)
    pyautogui.mouseDown(218, 534, button='left')
    pyautogui.mouseUp(218, 534, button='left')
    """Hero Weapon"""
    """Choose a weapon"""
    pyautogui.moveTo(587,210)
    pyautogui.scroll(2)
    pyautogui.mouseDown(587, 210, button='left')
    pyautogui.mouseUp(587, 210, button='left')
    """Choose a weapon"""
    """ShortSword"""
    
    pyautogui.moveTo(530,275)
    pyautogui.scroll(2)
    pyautogui.mouseDown(530, 275, button='left')
    pyautogui.mouseUp(530, 275, button='left')
    time.sleep(0.5)
    mon = {'top': 270, 'left': 1397, 'width': 330, 'height': 80}

    with mss.mss() as sct:
        while 1:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            sayı = pytesseract.image_to_string(im)
            a = len(sayı)
            if (sayı == "STAY)\n" or sayı =="ANT)\n" or sayı == "24444,\n" or sayı =="AN)\n" or sayı =="PESUTY)\n" or sayı == "18888,\n" or sayı =="Et)\n" or sayı =="PAT)\n" or sayı =="PAX)\n" or sayı =="SU PLYA\n" or sayı == "19264,\n" or sayı =="28285.71\n" or sayı =="600000\n\n6\n" or sayı =="\n" or sayı =="Pt)\n" or sayı =="STATON\n"  or sayı =="14995,\n" or sayı =="16666.50\n" or sayı =="28285.71\n"  or sayı == "27333.33\n" or sayı =="184,00\n" or sayı =="STAC)\n" or sayı =="16666.67\n" or sayı =="164,00\n" or sayı =="SUA)\n" or sayı =="19444,\n" or sayı == "STAAL\n" or sayı =="17997-75\n" or sayı =="STATON\n" or sayı =="16888.\n" or sayı =="11666.67\n" or sayı =="STAY\n" or sayı =="26595,\n" or sayı =="PATI)\n" or sayı =="164,00\n" or sayı =="VEL)\n" or sayı =="17654,\n" or sayı =="AL)\n" or sayı =="PAL)\n" or sayı =="PAN)\n" or sayı == "AAI)\n" or sayı =="34995,\n" or sayı =="34954.50\n" or sayı =="33333,\n" or sayı =="33333.33\n\n1\n" or sayı =="34.000\n" or sayı =="PAL)\n" or sayı =="PLA)\n" or sayı =="BA)\n"  or sayı =="PA)\n" or sayı =="PLAN)\n"  or sayı =="Ee)\n" or sayı =="A)\n" or sayı =="YAN)\n" or sayı=="Ey)\n" or "," in sayı or "." in sayı or ")" in sayı or sayı =="STATO\n" or sayı =="VAT\n"):
                break
            if(a < 18 and a>3  and int(sayı) <= 7000):
                sayı = int(pytesseract.image_to_string(im))
                pyautogui.moveTo(x=849, y=316)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=849, y=316, button='left')
                pyautogui.mouseUp(x=849, y=316, button='left') 
                pyautogui.moveTo(x=1713, y=977)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=1713, y=977, button='left')
                pyautogui.mouseUp(x=1713, y=977, button='left')
                pyautogui.moveTo(x=842, y=634)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=842, y=634, button='left')
                pyautogui.mouseUp(x=842, y=634, button='left')
                cv2.imshow('Image', im)
                break
                
            else:
                break
            
    """ShortSword"""
    """Choose a weapon"""
    
    pyautogui.moveTo(587,210)
    pyautogui.scroll(2)
    pyautogui.mouseDown(587, 210, button='left')
    pyautogui.mouseUp(587, 210, button='left')
    """Choose a weapon"""
    """Glaive"""
    pyautogui.moveTo(491,317)
    pyautogui.scroll(2)
    pyautogui.mouseDown(491, 317, button='left')
    pyautogui.mouseUp(491, 317, button='left')
    time.sleep(0.5)
    mon = {'top': 270, 'left': 1397, 'width': 330, 'height': 80}

    with mss.mss() as sct:
        while 1:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            sayı = pytesseract.image_to_string(im)
            a = len(sayı)
            if (sayı == "STAY)\n" or sayı =="ANT)\n" or sayı == "24444,\n" or sayı =="AN)\n" or sayı =="PESUTY)\n" or sayı == "18888,\n" or sayı =="Et)\n" or sayı =="PAT)\n" or sayı =="PAX)\n" or sayı =="SU PLYA\n" or sayı == "19264,\n" or sayı =="28285.71\n" or sayı =="600000\n\n6\n" or sayı =="\n" or sayı =="Pt)\n" or sayı =="STATON\n"  or sayı =="14995,\n" or sayı =="16666.50\n" or sayı =="28285.71\n"  or sayı == "27333.33\n" or sayı =="184,00\n" or sayı =="STAC)\n" or sayı =="16666.67\n" or sayı =="164,00\n" or sayı =="SUA)\n" or sayı =="19444,\n" or sayı == "STAAL\n" or sayı =="17997-75\n" or sayı =="STATON\n" or sayı =="16888.\n" or sayı =="11666.67\n" or sayı =="STAY\n" or sayı =="26595,\n" or sayı =="PATI)\n" or sayı =="164,00\n" or sayı =="VEL)\n" or sayı =="17654,\n" or sayı =="AL)\n" or sayı =="PAL)\n" or sayı =="PAN)\n" or sayı == "AAI)\n" or sayı =="34995,\n" or sayı =="34954.50\n" or sayı =="33333,\n" or sayı =="33333.33\n\n1\n" or sayı =="34.000\n" or sayı =="PAL)\n" or sayı =="PLA)\n" or sayı =="BA)\n"  or sayı =="PA)\n" or sayı =="PLAN)\n"  or sayı =="Ee)\n" or sayı =="A)\n" or sayı =="YAN)\n" or sayı=="Ey)\n" or "," in sayı or "." in sayı or ")" in sayı or sayı =="STATO\n" or sayı =="VAT\n"):
                break
            if(a < 18 and a>3  and int(sayı) <= 8000):
                sayı = int(pytesseract.image_to_string(im))
                pyautogui.moveTo(x=849, y=316)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=849, y=316, button='left')
                pyautogui.mouseUp(x=849, y=316, button='left') 
                pyautogui.moveTo(x=1713, y=977)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=1713, y=977, button='left')
                pyautogui.mouseUp(x=1713, y=977, button='left')
                pyautogui.moveTo(x=842, y=634)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=842, y=634, button='left')
                pyautogui.mouseUp(x=842, y=634, button='left')
                cv2.imshow('Image', im)
                break
                
            else:
                break
    
    """Glaive"""
    
    """Choose a weapon"""
    
    pyautogui.moveTo(587,210)
    pyautogui.scroll(2)
    pyautogui.mouseDown(587, 210, button='left')
    pyautogui.mouseUp(587, 210, button='left')
    """Choose a weapon"""
    """LongSword Shield"""
    
    pyautogui.moveTo(493,359)
    pyautogui.scroll(2)
    pyautogui.mouseDown(493, 359, button='left')
    pyautogui.mouseUp(493, 359, button='left')
    time.sleep(0.5)
    mon = {'top': 270, 'left': 1397, 'width': 330, 'height': 80}

    with mss.mss() as sct:
        while 1:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            sayı = pytesseract.image_to_string(im)
            a = len(sayı)
            if (sayı == "STAY)\n" or sayı =="ANT)\n" or sayı == "24444,\n" or sayı =="AN)\n" or sayı =="PESUTY)\n" or sayı == "18888,\n" or sayı =="Et)\n" or sayı =="PAT)\n" or sayı =="PAX)\n" or sayı =="SU PLYA\n" or sayı == "19264,\n" or sayı =="28285.71\n" or sayı =="600000\n\n6\n" or sayı =="\n" or sayı =="Pt)\n" or sayı =="STATON\n"  or sayı =="14995,\n" or sayı =="16666.50\n" or sayı =="28285.71\n"  or sayı == "27333.33\n" or sayı =="184,00\n" or sayı =="STAC)\n" or sayı =="16666.67\n" or sayı =="164,00\n" or sayı =="SUA)\n" or sayı =="19444,\n" or sayı == "STAAL\n" or sayı =="17997-75\n" or sayı =="STATON\n" or sayı =="16888.\n" or sayı =="11666.67\n" or sayı =="STAY\n" or sayı =="26595,\n" or sayı =="PATI)\n" or sayı =="164,00\n" or sayı =="VEL)\n" or sayı =="17654,\n" or sayı =="AL)\n" or sayı =="PAL)\n" or sayı =="PAN)\n" or sayı == "AAI)\n" or sayı =="34995,\n" or sayı =="34954.50\n" or sayı =="33333,\n" or sayı =="33333.33\n\n1\n" or sayı =="34.000\n" or sayı =="PAL)\n" or sayı =="PLA)\n" or sayı =="BA)\n"  or sayı =="PA)\n" or sayı =="PLAN)\n"  or sayı =="Ee)\n" or sayı =="A)\n" or sayı =="YAN)\n" or sayı=="Ey)\n" or "," in sayı or "." in sayı or ")" in sayı or sayı =="STATO\n" or sayı =="VAT\n"):
                break
            if(a < 18 and a>1 and int(sayı) <= 7000):
                sayı = int(pytesseract.image_to_string(im))
                pyautogui.moveTo(x=849, y=316)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=849, y=316, button='left')
                pyautogui.mouseUp(x=849, y=316, button='left') 
                pyautogui.moveTo(x=1713, y=977)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=1713, y=977, button='left')
                pyautogui.mouseUp(x=1713, y=977, button='left')
                pyautogui.moveTo(x=842, y=634)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=842, y=634, button='left')
                pyautogui.mouseUp(x=842, y=634, button='left')
                cv2.imshow('Image', im)
                break
                
            else:
                break
    """LongSword Shield"""
    """Choose a weapon"""
    pyautogui.moveTo(587,210)
    pyautogui.scroll(2)
    pyautogui.mouseDown(587, 210, button='left')
    pyautogui.mouseUp(587, 210, button='left')
    """Choose a weapon"""
    """Poleaxe"""
    
    pyautogui.moveTo(510,398)
    pyautogui.scroll(2)
    pyautogui.mouseDown(510, 398, button='left')
    pyautogui.mouseUp(510, 398, button='left')
    time.sleep(0.5)
    mon = {'top': 270, 'left': 1397, 'width': 330, 'height': 80}

    with mss.mss() as sct:
        while 1:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            sayı = pytesseract.image_to_string(im)
            a = len(sayı)
            if (sayı == "STAY)\n" or sayı =="ANT)\n" or sayı == "24444,\n" or sayı =="AN)\n" or sayı =="PESUTY)\n" or sayı == "18888,\n" or sayı =="Et)\n" or sayı =="PAT)\n" or sayı =="PAX)\n" or sayı =="SU PLYA\n" or sayı == "19264,\n" or sayı =="28285.71\n" or sayı =="600000\n\n6\n" or sayı =="\n" or sayı =="Pt)\n" or sayı =="STATON\n"  or sayı =="14995,\n" or sayı =="16666.50\n" or sayı =="28285.71\n"  or sayı == "27333.33\n" or sayı =="184,00\n" or sayı =="STAC)\n" or sayı =="16666.67\n" or sayı =="164,00\n" or sayı =="SUA)\n" or sayı =="19444,\n" or sayı == "STAAL\n" or sayı =="17997-75\n" or sayı =="STATON\n" or sayı =="16888.\n" or sayı =="11666.67\n" or sayı =="STAY\n" or sayı =="26595,\n" or sayı =="PATI)\n" or sayı =="164,00\n" or sayı =="VEL)\n" or sayı =="17654,\n" or sayı =="AL)\n" or sayı =="PAL)\n" or sayı =="PAN)\n" or sayı == "AAI)\n" or sayı =="34995,\n" or sayı =="34954.50\n" or sayı =="33333,\n" or sayı =="33333.33\n\n1\n" or sayı =="34.000\n" or sayı =="PAL)\n" or sayı =="PLA)\n" or sayı =="BA)\n"  or sayı =="PA)\n" or sayı =="PLAN)\n"  or sayı =="Ee)\n" or sayı =="A)\n" or sayı =="YAN)\n" or sayı=="Ey)\n" or "," in sayı or "." in sayı or ")" in sayı or sayı =="STATO\n" or sayı =="VAT\n"):
                break
            if(a < 18 and a>3  and int(sayı) <= 7200):
                sayı = int(pytesseract.image_to_string(im))
                pyautogui.moveTo(x=849, y=316)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=849, y=316, button='left')
                pyautogui.mouseUp(x=849, y=316, button='left') 
                pyautogui.moveTo(x=1713, y=977)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=1713, y=977, button='left')
                pyautogui.mouseUp(x=1713, y=977, button='left')
                pyautogui.moveTo(x=842, y=634)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=842, y=634, button='left')
                pyautogui.mouseUp(x=842, y=634, button='left')
                cv2.imshow('Image', im)
                break
                
            else:
                break
    """Poleaxe"""
    """Choose a weapon"""
    
    pyautogui.moveTo(587,210)
    pyautogui.scroll(2)
    pyautogui.mouseDown(587, 210, button='left')
    pyautogui.mouseUp(587, 210, button='left')
    """Choose a weapon"""
    """Spear"""
    
    pyautogui.moveTo(484,447)
    pyautogui.scroll(2)
    pyautogui.mouseDown(484, 447, button='left')
    pyautogui.mouseUp(484, 447, button='left')
    time.sleep(0.5)
    mon = {'top': 270, 'left': 1397, 'width': 330, 'height': 80}

    with mss.mss() as sct:
        while 1:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            sayı = pytesseract.image_to_string(im)
            a = len(sayı)
            if (sayı == "STAY)\n" or sayı =="ANT)\n" or sayı == "24444,\n" or sayı =="AN)\n" or sayı =="PESUTY)\n" or sayı == "18888,\n" or sayı =="Et)\n" or sayı =="PAT)\n" or sayı =="PAX)\n" or sayı =="SU PLYA\n" or sayı == "19264,\n" or sayı =="28285.71\n" or sayı =="600000\n\n6\n" or sayı =="\n" or sayı =="Pt)\n" or sayı =="STATON\n"  or sayı =="14995,\n" or sayı =="16666.50\n" or sayı =="28285.71\n"  or sayı == "27333.33\n" or sayı =="184,00\n" or sayı =="STAC)\n" or sayı =="16666.67\n" or sayı =="164,00\n" or sayı =="SUA)\n" or sayı =="19444,\n" or sayı == "STAAL\n" or sayı =="17997-75\n" or sayı =="STATON\n" or sayı =="16888.\n" or sayı =="11666.67\n" or sayı =="STAY\n" or sayı =="26595,\n" or sayı =="PATI)\n" or sayı =="164,00\n" or sayı =="VEL)\n" or sayı =="17654,\n" or sayı =="AL)\n" or sayı =="PAL)\n" or sayı =="PAN)\n" or sayı == "AAI)\n" or sayı =="34995,\n" or sayı =="34954.50\n" or sayı =="33333,\n" or sayı =="33333.33\n\n1\n" or sayı =="34.000\n" or sayı =="PAL)\n" or sayı =="PLA)\n" or sayı =="BA)\n" or sayı =="PA)\n" or sayı =="PLAN)\n"  or sayı =="Ee)\n" or sayı =="A)\n" or sayı =="YAN)\n" or sayı=="Ey)\n" or "," in sayı or "." in sayı or ")" in sayı or sayı =="STATO\n" or sayı =="VAT\n"):
                break
            if(a < 18 and a>3  and int(sayı) <= 6500):
                sayı = int(pytesseract.image_to_string(im))
                pyautogui.moveTo(x=849, y=316)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=849, y=316, button='left')
                pyautogui.mouseUp(x=849, y=316, button='left') 
                pyautogui.moveTo(x=1713, y=977)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=1713, y=977, button='left')
                pyautogui.mouseUp(x=1713, y=977, button='left')
                pyautogui.moveTo(x=842, y=634)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=842, y=634, button='left')
                pyautogui.mouseUp(x=842, y=634, button='left')
                cv2.imshow('Image', im)
                break
                
            else:
                break
    """Spear"""
    """Choose a weapon"""
    
    pyautogui.moveTo(587,210)
    pyautogui.scroll(2)
    pyautogui.mouseDown(587, 210, button='left')
    pyautogui.mouseUp(587, 210, button='left')
    """Choose a weapon"""
    """Nodachi"""
    
    pyautogui.moveTo(493,486)
    pyautogui.scroll(2)
    pyautogui.mouseDown(493, 486, button='left')
    pyautogui.mouseUp(493, 486, button='left')
    time.sleep(0.5)
    mon = {'top': 270, 'left': 1397, 'width': 330, 'height': 80}

    with mss.mss() as sct:
        while 1:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            sayı = pytesseract.image_to_string(im)
            a = len(sayı)
            if (sayı == "STAY)\n" or sayı =="ANT)\n" or sayı == "24444,\n" or sayı =="AN)\n" or sayı =="PESUTY)\n" or sayı == "18888,\n" or sayı =="Et)\n" or sayı =="PAT)\n" or sayı =="PAX)\n" or sayı =="SU PLYA\n" or sayı == "19264,\n" or sayı =="28285.71\n" or sayı =="600000\n\n6\n" or sayı =="\n" or sayı =="Pt)\n" or sayı =="STATON\n"  or sayı =="14995,\n" or sayı =="16666.50\n" or sayı =="28285.71\n"  or sayı == "27333.33\n" or sayı =="184,00\n" or sayı =="STAC)\n" or sayı =="16666.67\n" or sayı =="164,00\n" or sayı =="SUA)\n" or sayı =="19444,\n" or sayı == "STAAL\n" or sayı =="17997-75\n" or sayı =="STATON\n" or sayı =="16888.\n" or sayı =="11666.67\n" or sayı =="STAY\n" or sayı =="26595,\n" or sayı =="PATI)\n" or sayı =="164,00\n" or sayı =="VEL)\n" or sayı =="17654,\n" or sayı =="AL)\n" or sayı =="PAL)\n" or sayı =="PAN)\n" or sayı == "AAI)\n" or sayı =="34995,\n" or sayı =="34954.50\n" or sayı =="33333,\n" or sayı =="33333.33\n\n1\n" or sayı =="34.000\n" or sayı =="PAL)\n" or sayı =="PLA)\n" or sayı =="BA)\n"  or sayı =="PA)\n" or sayı =="PLAN)\n"  or sayı =="Ee)\n" or sayı =="A)\n" or sayı =="YAN)\n" or sayı=="Ey)\n" or "," in sayı or "." in sayı or ")" in sayı or sayı =="STATO\n" or sayı =="VAT\n"):
                break
            if(a < 18 and a>3  and int(sayı) <= 6000):
                sayı = int(pytesseract.image_to_string(im))
                pyautogui.moveTo(x=849, y=316)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=849, y=316, button='left')
                pyautogui.mouseUp(x=849, y=316, button='left') 
                pyautogui.moveTo(x=1713, y=977)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=1713, y=977, button='left')
                pyautogui.mouseUp(x=1713, y=977, button='left')
                pyautogui.moveTo(x=842, y=634)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=842, y=634, button='left')
                pyautogui.mouseUp(x=842, y=634, button='left')
                cv2.imshow('Image', im)
                break
                
            else:
                break
    """Nodachi"""
    """Choose a weapon"""
    
    pyautogui.moveTo(587,210)
    pyautogui.scroll(2)
    pyautogui.mouseDown(587, 210, button='left')
    pyautogui.mouseUp(587, 210, button='left')
    """Choose a weapon"""
    """Musket"""
    
    pyautogui.moveTo(494,529)
    pyautogui.scroll(2)
    pyautogui.mouseDown(494, 529, button='left')
    pyautogui.mouseUp(494, 529, button='left')
    time.sleep(0.5)
    mon = {'top': 270, 'left': 1397, 'width': 330, 'height': 80}

    with mss.mss() as sct:
        while 1:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            sayı = pytesseract.image_to_string(im)
            a = len(sayı)
            if (sayı == "STAY)\n" or sayı =="ANT)\n" or sayı == "24444,\n" or sayı =="AN)\n" or sayı =="PESUTY)\n" or sayı == "18888,\n" or sayı =="Et)\n" or sayı =="PAT)\n" or sayı =="PAX)\n" or sayı =="SU PLYA\n" or sayı == "19264,\n" or sayı =="28285.71\n" or sayı =="600000\n\n6\n" or sayı =="\n" or sayı =="Pt)\n" or sayı =="STATON\n"  or sayı =="14995,\n" or sayı =="16666.50\n" or sayı =="28285.71\n"  or sayı == "27333.33\n" or sayı =="184,00\n" or sayı =="STAC)\n" or sayı =="16666.67\n" or sayı =="164,00\n" or sayı =="SUA)\n" or sayı =="19444,\n" or sayı == "STAAL\n" or sayı =="17997-75\n" or sayı =="STATON\n" or sayı =="16888.\n" or sayı =="11666.67\n" or sayı =="STAY\n" or sayı =="26595,\n" or sayı =="PATI)\n" or sayı =="164,00\n" or sayı =="VEL)\n" or sayı =="17654,\n" or sayı =="AL)\n" or sayı =="PAL)\n" or sayı =="PAN)\n" or sayı == "AAI)\n" or sayı =="34995,\n" or sayı =="34954.50\n" or sayı =="33333,\n" or sayı =="33333.33\n\n1\n" or sayı =="34.000\n" or sayı =="PAL)\n" or sayı =="PLA)\n" or sayı =="BA)\n"  or sayı =="PA)\n" or sayı =="PLAN)\n"  or sayı =="Ee)\n" or sayı =="A)\n" or sayı =="YAN)\n" or sayı=="Ey)\n" or "," in sayı or "." in sayı or ")" in sayı or sayı =="STATO\n" or sayı =="VAT\n"):
                break
            if(a < 18 and a>3  and int(sayı) <= 10000):
                sayı = int(pytesseract.image_to_string(im))
                pyautogui.moveTo(x=849, y=316)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=849, y=316, button='left')
                pyautogui.mouseUp(x=849, y=316, button='left') 
                pyautogui.moveTo(x=1713, y=977)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=1713, y=977, button='left')
                pyautogui.mouseUp(x=1713, y=977, button='left')
                pyautogui.moveTo(x=842, y=634)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=842, y=634, button='left')
                pyautogui.mouseUp(x=842, y=634, button='left')
                cv2.imshow('Image', im)
                break
                
            else:
                break
    """Musket"""
    """Choose a weapon"""
    
    pyautogui.moveTo(587,210)
    pyautogui.scroll(2)
    pyautogui.mouseDown(587, 210, button='left')
    pyautogui.mouseUp(587, 210, button='left')
    """Choose a weapon"""
    """Bow"""
    
    pyautogui.moveTo(514,559)
    pyautogui.scroll(2)
    pyautogui.mouseDown(514, 559, button='left')
    pyautogui.mouseUp(514, 559, button='left')
    time.sleep(0.5)
    mon = {'top': 270, 'left': 1397, 'width': 330, 'height': 80}

    with mss.mss() as sct:
        while 1:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            sayı = pytesseract.image_to_string(im)
            a = len(sayı)
            if (sayı == "STAY)\n" or sayı =="ANT)\n" or sayı == "24444,\n" or sayı =="AN)\n" or sayı =="PESUTY)\n" or sayı == "18888,\n" or sayı =="Et)\n" or sayı =="PAT)\n" or sayı =="PAX)\n" or sayı =="SU PLYA\n" or sayı == "19264,\n" or sayı =="28285.71\n" or sayı =="600000\n\n6\n" or sayı =="\n" or sayı =="Pt)\n" or sayı =="STATON\n"  or sayı =="14995,\n" or sayı =="16666.50\n" or sayı =="28285.71\n"  or sayı == "27333.33\n" or sayı =="184,00\n" or sayı =="STAC)\n" or sayı =="16666.67\n" or sayı =="164,00\n" or sayı =="SUA)\n" or sayı =="19444,\n" or sayı == "STAAL\n" or sayı =="17997-75\n" or sayı =="STATON\n" or sayı =="16888.\n" or sayı =="11666.67\n" or sayı =="STAY\n" or sayı =="26595,\n" or sayı =="PATI)\n" or sayı =="164,00\n" or sayı =="VEL)\n" or sayı =="17654,\n" or sayı =="AL)\n" or sayı =="PAL)\n" or sayı =="PAN)\n" or sayı == "AAI)\n" or sayı =="34995,\n" or sayı =="34954.50\n" or sayı =="33333,\n" or sayı =="33333.33\n\n1\n" or sayı =="34.000\n" or sayı =="PAL)\n" or sayı =="PLA)\n" or sayı =="BA)\n"  or sayı =="PA)\n" or sayı =="PLAN)\n"  or sayı =="Ee)\n" or sayı =="A)\n" or sayı =="YAN)\n" or sayı=="Ey)\n" or "," in sayı or "." in sayı or ")" in sayı or sayı =="STATO\n" or sayı =="VAT\n"):
                break
            if(a < 18 and a>3  and int(sayı) <= 7000):
                sayı = int(pytesseract.image_to_string(im))
                pyautogui.moveTo(x=849, y=316)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=849, y=316, button='left')
                pyautogui.mouseUp(x=849, y=316, button='left') 
                pyautogui.moveTo(x=1713, y=977)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=1713, y=977, button='left')
                pyautogui.mouseUp(x=1713, y=977, button='left')
                pyautogui.moveTo(x=842, y=634)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=842, y=634, button='left')
                pyautogui.mouseUp(x=842, y=634, button='left')
                cv2.imshow('Image', im)
                break
                
            else:
                break
    """Bow"""
    """Choose a weapon"""
    
    pyautogui.moveTo(587,210)
    pyautogui.scroll(2)
    pyautogui.mouseDown(587, 210, button='left')
    pyautogui.mouseUp(587, 210, button='left')
    """Choose a weapon"""
    """Short Bow"""
    
    pyautogui.moveTo(516,600)
    pyautogui.scroll(2)
    pyautogui.mouseDown(516, 600, button='left')
    pyautogui.mouseUp(516, 600, button='left')
    time.sleep(0.5)
    mon = {'top': 270, 'left': 1397, 'width': 330, 'height': 80}

    with mss.mss() as sct:
        while 1:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            sayı = pytesseract.image_to_string(im)
            a = len(sayı)
            if (sayı == "STAY)\n" or sayı =="ANT)\n" or sayı == "24444,\n" or sayı =="AN)\n" or sayı =="PESUTY)\n" or sayı == "18888,\n" or sayı =="Et)\n" or sayı =="PAT)\n" or sayı =="PAX)\n" or sayı =="SU PLYA\n" or sayı == "19264,\n" or sayı =="28285.71\n" or sayı =="600000\n\n6\n" or sayı =="\n" or sayı =="Pt)\n" or sayı =="STATON\n"  or sayı =="14995,\n" or sayı =="16666.50\n" or sayı =="28285.71\n"  or sayı == "27333.33\n" or sayı =="184,00\n" or sayı =="STAC)\n" or sayı =="16666.67\n" or sayı =="164,00\n" or sayı =="SUA)\n" or sayı =="19444,\n" or sayı == "STAAL\n" or sayı =="17997-75\n" or sayı =="STATON\n" or sayı =="16888.\n" or sayı =="11666.67\n" or sayı =="STAY\n" or sayı =="26595,\n" or sayı =="PATI)\n" or sayı =="164,00\n" or sayı =="VEL)\n" or sayı =="17654,\n" or sayı =="AL)\n" or sayı =="PAL)\n" or sayı =="PAN)\n" or sayı == "AAI)\n" or sayı =="34995,\n" or sayı =="34954.50\n" or sayı =="33333,\n" or sayı =="33333.33\n\n1\n" or sayı =="34.000\n" or sayı =="PAL)\n" or sayı =="PLA)\n" or sayı =="BA)\n"  or sayı =="PA)\n" or sayı =="PLAN)\n"  or sayı =="Ee)\n" or sayı =="A)\n" or sayı =="YAN)\n" or sayı=="Ey)\n" or "," in sayı or "." in sayı or ")" in sayı or sayı =="STATO\n" or sayı =="VAT\n"):
                break
            if(a < 18 and a>3  and int(sayı) <= 6500):
                sayı = int(pytesseract.image_to_string(im))
                pyautogui.moveTo(x=849, y=316)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=849, y=316, button='left')
                pyautogui.mouseUp(x=849, y=316, button='left') 
                pyautogui.moveTo(x=1713, y=977)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=1713, y=977, button='left')
                pyautogui.mouseUp(x=1713, y=977, button='left')
                pyautogui.moveTo(x=842, y=634)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=842, y=634, button='left')
                pyautogui.mouseUp(x=842, y=634, button='left')
                cv2.imshow('Image', im)
                break
                
            else:
                break
    """Short Bow"""
    """Choose a weapon"""
   
    pyautogui.moveTo(587,210)
    pyautogui.scroll(2)
    pyautogui.mouseDown(587, 210, button='left')
    pyautogui.mouseUp(587, 210, button='left')
    """Choose a weapon"""
    """Dual Blades"""
    
    pyautogui.moveTo(515,636)
    pyautogui.scroll(2)
    pyautogui.mouseDown(515,636, button='left')
    pyautogui.mouseUp(515,636, button='left')
    time.sleep(0.5)
    mon = {'top': 270, 'left': 1397, 'width': 330, 'height': 80}

    with mss.mss() as sct:
        while 1:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            sayı = pytesseract.image_to_string(im)
            a = len(sayı)
            if (sayı == "STAY)\n" or sayı =="ANT)\n" or sayı == "24444,\n" or sayı =="AN)\n" or sayı =="PESUTY)\n" or sayı == "18888,\n" or sayı =="Et)\n" or sayı =="PAT)\n" or sayı =="PAX)\n" or sayı =="SU PLYA\n" or sayı == "19264,\n" or sayı =="28285.71\n" or sayı =="600000\n\n6\n" or sayı =="\n" or sayı =="Pt)\n" or sayı =="STATON\n"  or sayı =="14995,\n" or sayı =="16666.50\n" or sayı =="28285.71\n"  or sayı == "27333.33\n" or sayı =="184,00\n" or sayı =="STAC)\n" or sayı =="16666.67\n" or sayı =="164,00\n" or sayı =="SUA)\n" or sayı =="19444,\n" or sayı == "STAAL\n" or sayı =="17997-75\n" or sayı =="STATON\n" or sayı =="16888.\n" or sayı =="11666.67\n" or sayı =="STAY\n" or sayı =="26595,\n" or sayı =="PATI)\n" or sayı =="164,00\n" or sayı =="VEL)\n" or sayı =="17654,\n" or sayı =="AL)\n" or sayı =="PAL)\n" or sayı =="PAN)\n" or sayı == "AAI)\n" or sayı =="34995,\n" or sayı =="34954.50\n" or sayı =="33333,\n" or sayı =="33333.33\n\n1\n" or sayı =="34.000\n" or sayı =="PAL)\n" or sayı =="PLA)\n" or sayı =="BA)\n"  or sayı =="PA)\n" or sayı =="PLAN)\n"  or sayı =="Ee)\n" or sayı =="A)\n" or sayı =="YAN)\n" or sayı=="Ey)\n" or "," in sayı or "." in sayı or ")" in sayı or sayı =="STATO\n" or sayı =="VAT\n"):
                break
            if(a < 18 and a>3  and int(sayı) <= 8000):
                sayı = int(pytesseract.image_to_string(im))
                pyautogui.moveTo(x=849, y=316)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=849, y=316, button='left')
                pyautogui.mouseUp(x=849, y=316, button='left') 
                pyautogui.moveTo(x=1713, y=977)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=1713, y=977, button='left')
                pyautogui.mouseUp(x=1713, y=977, button='left')
                pyautogui.moveTo(x=842, y=634)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=842, y=634, button='left')
                pyautogui.mouseUp(x=842, y=634, button='left')
                cv2.imshow('Image', im)
                break
                
            else:
                break
    """Dual Blades"""
    """Choose a weapon"""
    
    pyautogui.moveTo(587,210)
    pyautogui.scroll(2)
    pyautogui.mouseDown(587, 210, button='left')
    pyautogui.mouseUp(587, 210, button='left')
    """Choose a weapon"""
    """Maul"""
    
    pyautogui.moveTo(495,679)
    pyautogui.scroll(2)
    pyautogui.mouseDown(495, 679, button='left')
    pyautogui.mouseUp(495, 679, button='left')
    time.sleep(0.5)
    mon = {'top': 270, 'left': 1397, 'width': 330, 'height': 80}

    with mss.mss() as sct:
        while 1:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            sayı = pytesseract.image_to_string(im)
            a = len(sayı)
            if (sayı == "STAY)\n" or sayı =="ANT)\n" or sayı == "24444,\n" or sayı =="AN)\n" or sayı =="PESUTY)\n" or sayı == "18888,\n" or sayı =="Et)\n" or sayı =="PAT)\n" or sayı =="PAX)\n" or sayı =="SU PLYA\n" or sayı == "19264,\n" or sayı =="28285.71\n" or sayı =="600000\n\n6\n" or sayı =="\n" or sayı =="Pt)\n" or sayı =="STATON\n"  or sayı =="14995,\n" or sayı =="16666.50\n" or sayı =="28285.71\n"  or sayı == "27333.33\n" or sayı =="184,00\n" or sayı =="STAC)\n" or sayı =="16666.67\n" or sayı =="164,00\n" or sayı =="SUA)\n" or sayı =="19444,\n" or sayı == "STAAL\n" or sayı =="17997-75\n" or sayı =="STATON\n" or sayı =="16888.\n" or sayı =="11666.67\n" or sayı =="STAY\n" or sayı =="26595,\n" or sayı =="PATI)\n" or sayı =="164,00\n" or sayı =="VEL)\n" or sayı =="17654,\n" or sayı =="AL)\n" or sayı =="PAL)\n" or sayı =="PAN)\n" or sayı == "AAI)\n" or sayı =="34995,\n" or sayı =="34954.50\n" or sayı =="33333,\n" or sayı =="33333.33\n\n1\n" or sayı =="34.000\n" or sayı =="PAL)\n" or sayı =="PLA)\n" or sayı =="BA)\n"  or sayı =="PA)\n" or sayı =="PLAN)\n"  or sayı =="Ee)\n" or sayı =="A)\n" or sayı =="YAN)\n" or sayı=="Ey)\n" or "," in sayı or "." in sayı or ")" in sayı or sayı =="STATO\n" or "i" in sayı or sayı =="VAT\n"):
                break
            if(a < 18 and a>3  and int(sayı) <= 8000):
                sayı = int(pytesseract.image_to_string(im))
                pyautogui.moveTo(x=849, y=316)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=849, y=316, button='left')
                pyautogui.mouseUp(x=849, y=316, button='left') 
                pyautogui.moveTo(x=1713, y=977)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=1713, y=977, button='left')
                pyautogui.mouseUp(x=1713, y=977, button='left')
                pyautogui.moveTo(x=842, y=634)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=842, y=634, button='left')
                pyautogui.mouseUp(x=842, y=634, button='left')
                cv2.imshow('Image', im)
                break
                
            else:
                break
    """Choose a weapon"""
    pyautogui.moveTo(587,210)
    pyautogui.scroll(2)
    pyautogui.mouseDown(587, 210, button='left')
    pyautogui.mouseUp(587, 210, button='left')
    """Choose a weapon"""
    """PİKE"""
    pyautogui.moveTo(496,717)
    pyautogui.scroll(2)
    pyautogui.mouseDown(496,717, button='left')
    pyautogui.mouseUp(496,717, button='left')
    time.sleep(0.5)
    mon = {'top': 270, 'left': 1397, 'width': 330, 'height': 80}

    with mss.mss() as sct:
        while 1:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            sayı = pytesseract.image_to_string(im)
            a = len(sayı)
            if (sayı == "STAY)\n" or sayı =="ANT)\n" or sayı == "24444,\n" or sayı =="AN)\n" or sayı =="PESUTY)\n" or sayı == "18888,\n" or sayı =="Et)\n" or sayı =="PAT)\n" or sayı =="PAX)\n" or sayı =="SU PLYA\n" or sayı == "19264,\n" or sayı =="28285.71\n" or sayı =="600000\n\n6\n" or sayı =="\n" or sayı =="Pt)\n" or sayı =="STATON\n"  or sayı =="14995,\n" or sayı =="16666.50\n" or sayı =="28285.71\n"  or sayı == "27333.33\n" or sayı =="184,00\n" or sayı =="STAC)\n" or sayı =="16666.67\n" or sayı =="164,00\n" or sayı =="SUA)\n" or sayı =="19444,\n" or sayı == "STAAL\n" or sayı =="17997-75\n" or sayı =="STATON\n" or sayı =="16888.\n" or sayı =="11666.67\n" or sayı =="STAY\n" or sayı =="26595,\n" or sayı =="PATI)\n" or sayı =="164,00\n" or sayı =="VEL)\n" or sayı =="17654,\n" or sayı =="AL)\n" or sayı =="PAL)\n" or sayı =="PAN)\n" or sayı == "AAI)\n" or sayı =="34995,\n" or sayı =="34954.50\n" or sayı =="33333,\n" or sayı =="33333.33\n\n1\n" or sayı =="34.000\n" or sayı =="PAL)\n" or sayı =="PLA)\n" or sayı =="BA)\n"  or sayı =="PA)\n" or sayı =="PLAN)\n"  or sayı =="Ee)\n" or sayı =="A)\n" or sayı =="YAN)\n" or sayı=="Ey)\n" or "," in sayı or "." in sayı or ")" in sayı or sayı =="STATO\n" or "i" in sayı or sayı =="VAT\n"):
                break
            if(a < 18 and a>3  and int(sayı) <= 9000):
                sayı = int(pytesseract.image_to_string(im))
                pyautogui.moveTo(x=849, y=316)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=849, y=316, button='left')
                pyautogui.mouseUp(x=849, y=316, button='left') 
                pyautogui.moveTo(x=1713, y=977)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=1713, y=977, button='left')
                pyautogui.mouseUp(x=1713, y=977, button='left')
                pyautogui.moveTo(x=842, y=634)
                pyautogui.scroll(2)
                pyautogui.mouseDown(x=842, y=634, button='left')
                pyautogui.mouseUp(x=842, y=634, button='left')
                cv2.imshow('Image', im)
                break
                
            else:
                break
    
