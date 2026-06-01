
import entity
from entity.structure import entityStructure






class userStruc():
    # super().__init__()
    health:int = 100



NTTSYS = entity.entitySys(userStruc)







ntt1:entityStructure = NTTSYS.new()

ntt2 = NTTSYS.new()



print(vars(ntt1.user))