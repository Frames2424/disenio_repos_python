from abc import ABC, abstractmethod

class AbstractProduct_A(ABC):
    @abstractmethod
    def operation_A(self):
        pass

class AbstractProduct_B(ABC):
    @abstractmethod
    def operation_B(self):
        pass