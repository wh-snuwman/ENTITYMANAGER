from time import time

class entityStructure():
    def __init__(self,):
        self.startTime = time()
        self.name:str = ''
        self.pos:list = [0,0]
        self.tag:dict = {}
        self.id:str = ''

        self.user = userStructure()

        # ===================
        self.size:list = []
        self.inventory:list[int] = [None,None,None,None,None,None,None,None,None,None]
        self.startPos:list = [0,0]
        self.type:str = ''


class userStructure():
    def __init__(self):pass