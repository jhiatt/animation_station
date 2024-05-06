from functions_file import *

def an():
    screen = screen_calibrate()
    
    # title sequence
    
    # sceen 1 - meet cute
    grant = Man(750)
    jen = Man(900)
    for i in range(20):
      screen = grant.walk1(screen)
      screen = jen.walk1(screen)
      
      print(screen)

      screen = grant.move(screen, 1)
      screen = jen.move(screen, 1)
      
      sleep(.1)
      screen = grant.walk2(screen)
      screen = jen.walk2(screen)
      print(screen)

      screen = grant.move(screen, 1)
      screen = jen.move(screen, 1)

      # screen = screen_calibrate()
      sleep(.1)
