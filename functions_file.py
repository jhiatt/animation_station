from time import sleep

w=105 # width
h = 35 # height
sleep_inc = .1


# def __init__(self) -> None:
#       pass


class Asset:
  def __init__(self,pos,connections=None):
      self.pos = pos
      if connections == None:
         connections = []
      self.connections = connections

  def move(self,string,spaces):
       new_pos = self.pos + spaces
       
       
       for i in self.connections:
          string = string[:i] + ' ' + string[i + 1:]

       self.connections = []

       self.pos = new_pos

       return(string)

class Static(Asset):
   def __init__(self,pos,length,connections=None):
      super().__init__(pos, connections)
      self.length = length
   
   def flow(self,string):
      # ~~~~~~~~~~~
      # ͡
      # ͝

      # only one line
      pos = self.pos
      s = string[:pos] + '~'*self.length + string[pos + self.length:]

      for l in range(self.length):
        self.connections.append(pos + l)
      
      return(s)

      
      

        
class Man(Asset):

    def __init__(self,pos,connections=None):
      super().__init__(pos, connections)


    def walk1(self,string): # move position to the self object

          # o
          #'|,
          # ʌ
          # first line
          pos = self.pos
          s = string[:pos] + 'o' + string[pos + 1:]

          self.connections.append(pos)

          # second line
          pos_l2 = pos + w + 1
          s = s[:pos_l2 - 1] + "'|," + s[pos_l2 + 2:]

          self.connections.append(pos_l2 -1)
          self.connections.append(pos_l2 + 0)
          self.connections.append(pos_l2 + 1)

          # third line
          pos_l3 = pos_l2 + w + 1
          s = s[:pos_l3] + "7" + s[pos_l3 + 1:]

          self.connections.append(pos_l3)

          return(s)
        
    
    def walk2(self,string):
        
          #  o
          # ,|'
          #  ㄱ
          # first line
          pos = self.pos
          s = string[:pos] + 'o' + string[pos + 1:]

          self.connections.append(pos)

          # second line
          pos_l2 = pos + w + 1
          s = s[:pos_l2 - 1] + ",|'" + s[pos_l2 + 2:]

          self.connections.append(pos_l2 - 1)
          self.connections.append(pos_l2)
          self.connections.append(pos_l2 + 1)

          # third line
          pos_l3 = pos_l2 + w + 1
          s = s[:pos_l3] + "λ" + s[pos_l3 + 1:]

          self.connections.append(pos_l3)

          return(s)
        



def screen_calibrate():
   w_2 = int(round((w-3)/2 ))
   # add top
   cal_string = '-'*w_2 + 'top' + '-'*w_2 + '\n'

   # create side peices
   sides =  '|' + ' '* (w-2) + '|'
   side_name = ''
   for l in 'side':
      side_name += l + ' '*(w-2) + l + '\n'
   
   # adding sides
   for i in range(int(round((h-5)/2))):
      cal_string += sides + '\n'

   cal_string += side_name
   
   for i in range(int(round((h-5)/2))):
    cal_string += sides + '\n'

   # add bottom
   cal_string += '|' + '-'*(w_2-1) + 'end' + '-'*(w_2-1) + '|'

   return(cal_string)
