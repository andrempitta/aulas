import pygame
pygame.mixer.init()
# windowSize = 600, 400
# pygame.display.set_mode(windowSize)
pygame.mixer.music.load('GoodTimes.mp3')
pygame.mixer.music.play()
pygame.event.wait()
# pygame.quit()
