from .. import Solution, WeightSet
from ..model import Offline
from .online import NextFit as Nf_online, FirstFit as Ff_online, BestFit as Bf_online, WorstFit as Wf_online


class OfflineDecreasing(Offline):
        '''An offline version of the AnyFit algorithms, ordering the weight stream 
        and delegating to the associated online version (avoiding code duplication)'''

        def _process(self, capacity: int, weights: WeightSet) -> Solution:
            weights = sorted(weights, reverse=True)
            return self.__delegation((capacity, weights))


class NextFit(OfflineDecreasing):

    _OfflineDecreasing__delegation = Nf_online()


class FirstFit(OfflineDecreasing):

    _OfflineDecreasing__delegation = Ff_online()


class BestFit(OfflineDecreasing):

    _OfflineDecreasing__delegation = Bf_online()


class WorstFit(OfflineDecreasing):

    _OfflineDecreasing__delegation = Wf_online()
