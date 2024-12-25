import subprocess
import pygame
import os
import time
import json
from ultralytics import YOLO
from threading import Thread


class LostAndFoundGlasses:
    def __init__(self, model_path, image_path,imgsz=(320, 240)):
        self.model = YOLO(model_path)
        self.image_path = image_path
        self.imgsz = imgsz
        self.output_image_path = 'images/output'

    def run_detection(self):
        result = self.model(self.image_path,save_txt=True , save_conf=True)
        result[0].save()
        # result[0].save_txt("output.txt")


    def show(self):
        pygame.init()
        screen = pygame.display.set_mode(self.imgsz)
        pygame.display.set_caption("Lost And Found Glasses!")
        clock = pygame.time.Clock()

        running = True
        current_image = None

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            Thread(target=self.run_detection).start()
            screen.blit(pygame.image.load("results_piyan.jpg"), (0, 0))

            pygame.display.flip()
            clock.tick(1)
        os.system('rm -rf ./runs')
        pygame.quit()
        


if __name__ == '__main__':
    piyan = LostAndFoundGlasses('./models/ivan.pt', './images/input/piyan.jpg')
    piyan.show()

'''
python3 ./yolov9/detect.py --img 320 --conf 0.5 --source ./images/input/piyan.jpg --device 0 --weights ./models/best.pt --project ./images --name output --exist-ok
'''