from abc import ABC, abstractmethod


class BaseOrder(ABC):

    @abstractmethod
    def __init__(self):
        super().__init__()

    @abstractmethod
    def __str__(self):
        pass
