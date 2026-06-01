from time import time

class entityStructure():
    def __init__(self,userStructure):
        self.startTime = time()
        self.id:str = ''
        self.tag = userStructure # 유저커스텀 정보

class userStructure():
    def __init__(self):
        # 기본적으로 제공하는 것들
        self.tag:dict = {}
        self.name:str = ''
        self.pos:list = [0,0]
        self.size:list = [0,0]
        self.startPos:list = [0,0]
        self.type:str = ''
        self.inventory:list[int] = [None,None,None,None,None,None,None,None,None,None]

    def isCollide(self,ntt1:entityStructure) -> bool:
        return (
            ntt1.tag.pos[0] < self.pos[0] + self.size[0] and
            ntt1.tag.pos[0] + ntt1.tag.size[0] > self.pos[0] and
            ntt1.tag.pos[1] < self.pos[1] + self.size[1] and
            ntt1.tag.pos[1] + ntt1.tag.size[1] > self.pos[1]
        )
    

    def goto(self,pos:list[int,int]) -> None:
        self.pos = [round(pos[0]),round(pos[1])]

    
    def move(self,pos:list[int,int]) -> None:
        self.pos[0] += round(pos[0])
        self.pos[1] += round(pos[1])
