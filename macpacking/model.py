from abc import ABC, abstractmethod
from . import WeightStream, WeightIterator, WeightSet, WeightList, Solution


class BinPacker(ABC):
    pass


class Online(BinPacker):

    def __call__(self, ws: WeightStream):
        capacity, stream = ws
        return self._process(capacity, stream)

    @abstractmethod
    def _process(self, c: int, stream: WeightIterator) -> Solution:
        pass


class Offline(BinPacker):

    def __call__(self, ws: WeightSet):
        capacity, weights = ws
        return self._process(capacity, weights)

    @abstractmethod
    def _process(self, c: int, weights: WeightList) -> Solution:
        pass
