from functions_file import *

grid = []

for i in range(2, h-7, 1):
  down = i*w
  left = down + 2
  right = down + w-1
  

  # l = [x for x in range(left, right, 1)]
  # grid.append(l)
  grid += list(range(left, right, 1))
  # .append(list(range(left, right, 1)))


for x in grid:
   print(x)


def animate():
  screen = screen_calibrate()



  # gen objects
  grant = Man(750)
  jen = Man(900)
  grant_staring = Man(3400)

  st = []
  for i in range(1,8,1): # adjust position and move amount so that no static goes off screen but the whole screen is taken over, need a list of available functions
    st.append(Static(110,i))

  # ----------------------------

  # title sequence

  # sceen 1 - meet cute

  for i in range(10):
    screen = grant.walk1(screen)
    screen = jen.walk1(screen)
    
    
    print(screen)

    screen = grant.move(screen, 1)
    screen = jen.move(screen, 1)
    
    
    sleep(sleep_inc)
    screen = grant.walk2(screen)
    screen = jen.walk2(screen)
    print(screen)

    screen = grant.move(screen, 1)
    screen = jen.move(screen, 1)

    sleep(sleep_inc)


  # sceen _ - watching the static
  screen = screen_calibrate()

  

  for i in range(8):
    screen = st[5].flow(screen)
    screen = grant_staring.walk2(screen)
    print(screen)

    screen = st[5].move(screen, 5)

    sleep(sleep_inc)

  for x in grid:
    screen = screen[:i] + '.' + screen[i + 1:]
  print('!!!')
  print(screen)

  # print(st[5].flow(screen))



  
  # screen = test(screen)
  


# ------------------------------------------------------------------------  






# def gen_static(screen):
#   st1 = Static(180,5)
#   screen = st1.flow(screen)
#   print(screen)

#   return(screen)
  


# def test(screen):
#   # title sequence
  
#   # sceen 1 - meet cute
#   grant = Man(750)
#   jen = Man(900)
#   for i in range(20):
#     screen = grant.walk1(screen)
#     screen = jen.walk1(screen)
    
#     print(screen)

#     screen = grant.move(screen, 1)
#     screen = jen.move(screen, 1)
    
#     sleep(sleep_inc)
#     screen = grant.walk2(screen)
#     screen = jen.walk2(screen)
#     print(screen)

#     screen = grant.move(screen, 1)
#     screen = jen.move(screen, 1)

#     # screen = screen_calibrate()
#     sleep(sleep_inc)

#     return(screen)