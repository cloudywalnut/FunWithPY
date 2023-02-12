class balloon:

    #PRIVATE Health : INTEGER
    #PRIVATE Colour : INTEGER
    #PRIVATE DefenceItem : INTEGER

    def __init__(self,Colour,DefenceItem):
        self.__Health=100
        self.__Colour=Colour
        self.__DefenceItem=DefenceItem

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self,value):
        self.__Health+=value

    def CheckHealth(self):
        if self.__Health<=0:
            return True
        else:
            return False


Colour=str(input("enter the color: "))
DefenceItem=str(input("enter the defence item: "))
Balloon1=balloon(Colour, DefenceItem)

def Defend(Balloon1):
    strength=int(input("enter the strength of the opponent: "))
    Balloon1.ChangeHealth(-1*strength)
    print(Balloon1.GetDefenceItem())
    if Balloon1.CheckHealth():
        print("No health remaining")
    else:
        print("Health Stil remaining")
    
    return Balloon1

Defend(Balloon1)
