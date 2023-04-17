from abc import ABC, abstractmethod


class CalculationMark(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calc_ave_mark(self):
        pass
