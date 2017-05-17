from picamera import PiCamera
import os
import time
import subprocess

def tesseract(img, cleanup=True, options=''):
    
    subprocess.check_output('tesseract ' + img + ' ' +
                            img + ' ' + options, shell=True)
    text = ''
    with open(img + '.txt', 'r') as f:
        text = f.read().strip()
    if cleanup:
        os.remove(img + '.txt')
        os.remove(img)
    return text

def capture():
    camera=PiCamera()
    img=time.strftime("%Y%m%d%H%M%S")+'.jpg'
    try:
        camera.capture(img)
    finally:
        camera.close()
    return img

#img=capture()
##tesseract(img, False)
##text=tesseract(img, options='-psm 7')
#text=tesseract(img)
#if (text in ['forward', 'left', 'right', 'backward']):
#    print text
