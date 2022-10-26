from .. import Solution, WeightSet
from ..model import Offline
from .online import NextFitOn as Nf_online, FirstFitOn as Ff_online, BestFitOn as Bf_online, WorstFitOn as Wf_online


class OfflineDecreasing(Offline):
        '''An offline version of the AnyFit algorithms, ordering the weight stream 
        and delegating to the associated online version (avoiding code duplication)'''

        def _process(self, capacity: int, weights: WeightSet) -> Solution:
            weights = sorted(weights, reverse=True)
            return self.__delegation((capacity, weights))


class NextFitOff(OfflineDecreasing):

    _OfflineDecreasing__delegation = Nf_online()


# T2 Algorithms -------------------

class FirstFitOff(OfflineDecreasing):

    _OfflineDecreasing__delegation = Ff_online()


class BestFitOff(OfflineDecreasing):

    _OfflineDecreasing__delegation = Bf_online()


class WorstFitOff(OfflineDecreasing):

    _OfflineDecreasing__delegation = Wf_online()

# End of T2 Offline Algorithms -----