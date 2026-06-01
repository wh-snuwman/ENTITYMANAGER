import entity
from entity.structure import entityStructure
from entity.structure import userStructure

class test(userStructure):
    def __init__(self):
        super().__init__()
        self.health:int = 100
    



NTTSYS = entity.entitySys(test)

ntt1:entityStructure = NTTSYS.new()
ntt2:entityStructure = NTTSYS.new()

NTTSYS.remove(ntt1)


print(ntt1.tag.isCollide(ntt2))