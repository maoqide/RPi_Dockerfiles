from io import BytesIO
from picamera import PiCamera
from PIL import Image
import pytesseract
import time

def tesseract(imgBytes):
    # PIL.Image
    pilObj=Image.open(imgBytes)
    text=pytesseract.image_to_string(pilObj)
    return text

def capture():
    stream=BytesIO()
    camera=PiCamera()
    #img=time.strftime("%Y%m%d%H%M%S")+'.jpg'
    try:
        camera.capture(stream, format='jpeg')
        stream.seek(0)
    finally:
        camera.close()
    return stream

#t1=time.time()
#for num in range(0,20):
#    img=capture()
#    text=tesseract(img)
#    #print text
#t2=time.time()
#print t1, t2, (t2-t1)/20
