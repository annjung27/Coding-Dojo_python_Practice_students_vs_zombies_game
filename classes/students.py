class Student:

    def __init__( self , name ):
        self.name = name
        self.energy = 10        
        self.health = 70
    
    def show_stats( self ):
        print(f"Name: {self.name}\nEnergy: {self.energy}\nHealth: {self.health}\n")

    def kick( self , zombie ):
        zombie.health -= 50
        print(f"{zombie.name} lost -50 health! Good Job!")
        print(f"{zombie.name}'s current health level: {zombie.health}")
        return self
    
    def shot_head(self, zombie): 
            zombie.health = 0
            zombie.energy = 0       
            print(f"{zombie.name} is Dead!")
            return self

    def heal(self):
        self.health += 100
        return self

    