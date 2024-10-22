from abc import ABC, abstractmethod


class BaseOrder(ABC):

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def __str__(self) -> str:
        pass
