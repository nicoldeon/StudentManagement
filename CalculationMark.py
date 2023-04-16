from abc import ABC, abstractmethod


class CalculationMark(ABC):

    @abstractmethod
    def calc_ave_mark(self):
        pass
