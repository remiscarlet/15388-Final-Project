from PIL import Image
import os
import pygame
import time

photo_folder = "female_portrait_medium"


pygame.init()
photos = os.listdir(photo_folder)

w = 640
h = 480
size=(w,h)
screen = pygame.display.set_mode(size) 
c = pygame.time.Clock() # create a clock object for timing

def save_photo(photo, filename, folder):
    if folder == "female":
        pygame.image.save(photo, photo_folder + "/female/"+filename)
    elif folder == "male":
        pygame.image.save(photo, photo_folder + "/male/"+filename)
    return
def main():
    counter = 0
    while True:
        photo_name = photos[counter]
        img=pygame.image.load(os.path.join(photo_folder, photo_name))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                print counter
                if keys[pygame.K_q]:
                    return
                #male
                elif keys[pygame.K_LEFT]:
                    save_photo(img, photo_name, "female")
                    counter += 1
                elif keys[pygame.K_RIGHT]:
                    save_photo(img, photo_name, "male")
                    counter += 1
                elif keys[pygame.K_UP]:
                    counter += 1
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        screen.blit(img,(0,0))
        pygame.display.flip() # update the display
        c.tick(20) # o
    


main()

