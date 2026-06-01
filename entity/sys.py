from .structure import entityStructure
from .id import entityId

class entitySys():
    def __init__(self,struc):
        self._all = []
        self._newEntity_reserve = []
        self._removeEntity_reserve = []
        self._entityCount = 0
        self._userStructure = struc
    
    def all(self):
        return self._all




    def clear(self) -> None: # 취급주의
        self._all = []
        self._newEntity_reserve = []
        self._removeEntity_reserve = []
        self._entityCount = 0


    def count(self) -> int:
        return self._entityCount


    def new(self):
        n = self._userStructure()
        ntt = entityStructure(n)
        self._all.append(ntt)
        self._entityCount += 1
        return ntt


    def remove(self,ntt:entityStructure) -> None:
        self._all.remove(ntt)
        self._entityCount -= 1


