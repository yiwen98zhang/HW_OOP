from abc import ABC,abstractmethod

class ReadGeneral(ABC):
    @abstractmethod
    def read_all(self,dirname):
        pass



