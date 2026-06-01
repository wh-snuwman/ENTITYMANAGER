from .structure import entityStructure
from .id import entityId

class entitySys():
    def __init__(self,struc):
        self._ALL = {}
        self._newEntity_reserve = []
        self._removeEntity_reserve = []
        self._entityCount = 0
        self._userStructure = struc
    

    def All(self):
        return self._ALL


    def get(self,id:str,type='obj') -> entityStructure|dict:
        result = self._ALL.get(id)
        if result is not None:
            if type == 'obj':
                return result
            elif type == 'dict':
                # print(vars(result))
                return vars(result)
        
        for i in self._newEntity_reserve:
            if i.id == id:
                if type == 'obj':
                    return self._newEntity_reserve[self._newEntity_reserve.index(i)]
                elif type == 'dict':
                    return vars(self._newEntity_reserve[self._newEntity_reserve.index(i)])

        return None                


    def getTypeCollide(self,ntt:entityStructure,Ntttype:str) -> list[entityStructure]:
        collideEntityArr = []
        for other_ntt in self.getAll():
            other_ntt : entityStructure = self.get(other_ntt)
            if other_ntt.type == Ntttype and self.isCollide(ntt,other_ntt):
                collideEntityArr.append(other_ntt)
        return collideEntityArr


    def getTypeFilter(self,type:str) -> list[entityStructure]:
        EntityArr = []
        for ntt_ in self.getAll():
            ntt_ = self.get(ntt_)
            if ntt_.type == type:
                EntityArr.append(ntt_)
        return EntityArr


    def getAllCollide(self,ntt:entityStructure) -> list[entityStructure]:
        collideEntityArr = []
        for other_ntt in self.getAll():
            if self.isCollide(ntt,other_ntt):
                collideEntityArr.append(other_ntt)
        return collideEntityArr


    def clear(self) -> None: # 취급주의
        self._ALL = {}
        self._newEntity_reserve = []
        self._removeEntity_reserve = []
        self._entityCount = 0


    def count(self) -> int:
        return self._entityCount


    def new(self):
        ntt = entityStructure(self._userStructure)
        self._newEntity_reserve.append(ntt)
        self._entityCount += 1
        return ntt


    def remove(self,_id=str) -> bool:
        self._removeEntity_reserve.append(_id)
        self._entityCount -= 1
        return True


    def goto(self,_id:str,pos:list) -> None:
        self.get(_id).pos = pos

    
    def move(self,_id:str,pos:list[float|int,float|int]) -> None:
        self.get(_id).pos[0] += pos[0]
        self.get(_id).pos[1] += pos[1]


    def isCollide(self,ntt1:entityStructure,ntt2:entityStructure) -> bool:
        return (
        ntt1.pos[0] < ntt2.pos[0] + ntt2.size[0] and
        ntt1.pos[0] + ntt1.size[0] > ntt2.pos[0] and
        ntt1.pos[1] < ntt2.pos[1] + ntt2.size[1] and
        ntt1.pos[1] + ntt1.size[1] > ntt2.pos[1]
    )





    def run(self):
        for Rid in self._removeEntity_reserve:
            if Rid in list(self._ALL.keys()):
                del self._ALL[Rid]
        self._removeEntity_reserve = []
        

        for Rntt in self._newEntity_reserve:
            self._ALL[Rntt.id] = Rntt
        self._newEntity_reserve = []