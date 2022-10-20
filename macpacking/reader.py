from abc import ABC, abstractmethod
from os import path
from random import shuffle, seed
from . import WeightSet, WeightStream


class DatasetReader(ABC):

    def offline(self) -> WeightSet:
        '''Return a WeightSet to support an offline algorithm'''
        (capacity, weights) = self._load_data_from_disk()
        seed(42)          # always produce the same shuffled result
        shuffle(weights)  # side effect shuffling
        return (capacity, weights)

    def online(self) -> WeightStream:
        '''Return a WeighStream, to support an online algorithm'''
        (capacity, weights) = self.offline()

        def iterator():  # Wrapping the contents into an iterator
            for w in weights:
                yield w  # yields the current value and moves to the next one

        return (capacity, iterator())

    @abstractmethod
    def _load_data_from_disk(self) -> WeightSet:
        '''Method that read the data from disk, depending on the file format'''
        pass


class BinppReader(DatasetReader):
    '''Read problem description according to the BinPP format'''

    def __init__(self, filename: str) -> None:
        if not path.exists(filename):
            raise ValueError(f'Unkown file [{filename}]')
        self.__filename = filename

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__filename, 'r') as reader:
            nb_objects: int = int(reader.readline())
            capacity: int = int(reader.readline())
            weights = []
            for _ in range(nb_objects):
                weights.append(int(reader.readline()))
            return (capacity, weights)


class JburkardtReader(DatasetReader):
    '''Read problem description according to the Jburkardt format'''

    def __init__(self, c_filename: str, w_filename: str) -> None:
        if not path.exists(c_filename):
            raise ValueError(f'Unkown capacity file [{c_filename}]')
        if not path.exists(w_filename):
            raise ValueError(f'Unkown weights file [{w_filename}]')
        self.__c_filename = c_filename
        self.__w_filename = w_filename

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__c_filename, 'r') as r1:
            capacity: int = int(r1.readline())

        with open(self.__w_filename, 'r') as r2:
            lines = r2.readlines()
            
            weights = []
            for i in range(len(lines)-1):
                weights.append(int(lines[i].strip()))
    
            return (capacity, weights)
