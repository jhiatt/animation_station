from functions_file import *

def animate():
  screen = screen_calibrate()

  # title sequence

  # sceen 1 - meet cute

  screen = gen_static(screen)
  screen = test(screen)
  


# ------------------------------------------------------------------------  

def gen_static(screen):
  st1 = Static(180,5)
  screen = st1.flow(screen)
  print(screen)

  return(screen)
  


def test(screen):
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

    return(screen)