# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import random

class SnakeLadder:
    
    def __init__(self):
        self.players={1:{"name":1,"dices":[],"positions":[],"current":0,},
        2:{"name":2,"dices":[],"positions":[],"current":0},
        3:{"name":3,"dices":[],"positions":[],"current":0}}
        
        self.total=0
        
    def printing(self):
        
        for name,obj in self.players.items():
                
          
            positions =obj.get("positions")
            dices =obj.get("dices")
            current =obj.get("current")
            
            print ("player         Dice role history        position history      winner status")
            
            winner="Winner" if current ==self.total else ""
            
            print(name ,"           ", dices,"     ",  positions ,winner)
            
        
     
        
    def check_for_players(self,player,pos):
        
        for name,obj in self.players.items():
                
            if name ==player:
                continue
          
            positions =obj.get("positions")
            dices =obj.get("dices")
            current =obj.get("current")
            
            
            
            if pos==current:
                positions.append(0)
                self.players[name]={"name":name,"dices":dices,"positions":positions,"current":0}
                break
    
    def update(self,player,dice):
        
            
        for name,obj in self.players.items():
   
            positions =obj.get("positions")
            dices =obj.get("dices",)
          
            
            current =obj.get("current")
            
            now=current+dice
            
            if name ==player:
              
                positions.append(now)
                dices.append(dice)
           
                self.players[name]={"name":name,"dices":dices,"positions":positions,"current":now}
             
                
                if now==self.total:
                    return True
                break    
    
        return False
    def start_game(self):
        check=False
        
        
        while True:
        
            for name,obj in self.players.items():

          
  
                positions =obj.get("positions")
                dices =obj.get("dices")
                current =obj.get("current")
                
                dice= random.randint(1,6)
            
                
                if current+dice>self.total:
                    dices.append(dice)
                    
                    self.players[name]={"name":name,"dices":dices,"positions":positions,"current":current}
                    
                    
                    continue
                
                self.check_for_players(name,current+dice)
                
                
                check =self.update(name,dice)
                
                if check:
                    print("completed")
                    
                    break
            if check:
                self.printing()
                break
            
            
        
    
    def start(self):
        
        while True:
        
            grid=input("enter ur grid : ")
            
            try:
                total=int(grid)*int(grid)
            except Exception as e:
                print("enter the grid in no")
                continue
                
            self.total=total
            
            self.start_game()
            print(" game complted")
            break
            

game=SnakeLadder()
game.start()
        
        
