import sys
import argparse
from yolo import YOLO, detect_video, run_on_video
from PIL import Image
import cv2


if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    
    #parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    yolo = YOLO()

    img = 'test/2.jpg'
    draw_img = cv2.imread(img)
    image = Image.open(img)
    #c1, c0 = yolo.detect_image(draw_img, image)
    #c1, c0 = yolo.detect_image('test/3.jpg')
    #c1, c0 = yolo.detect_image('test/4.jpg')
    run_on_video(yolo, 1)
    '''
    f = open('result.csv','w')
    for i in range(1592):
        print ("-------------------------------------")
        print(i)
        print ("-------------------------------------")
        img = 'test/{}.jpg'.format(i)
        image = Image.open(img)
        c1,c0 = yolo.detect_image(image)
        f.write('{},{},{}\n'.format(i,c1,c0))
    f.close()
    '''