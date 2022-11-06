from .. import Solution, WeightList
from ..model import Offline
from .online import (
    NextFitOn as Nf_online,
    FirstFitOn as Ff_online,
    BestFitOn as Bf_online,
    WorstFitOn as Wf_online,
    RefinedFirstFitOn as Rff_online,
    EmptiestBinOn as EB_online
)


class OfflineDecreasing(Offline):
    '''An offline version of the AnyFit algorithms, ordering the weight
    stream and delegating to the associated online version
    (avoiding code duplication)'''

    def _process(self, capacity: int, weights: WeightList) -> Solution:
        weights = sorted(weights, reverse=True)
        return self.__delegation((capacity, weights))


class NextFitOff(OfflineDecreasing):

    _OfflineDecreasing__delegation = Nf_online()


# T2 - Offline Algorithms -------------------

class FirstFitOff(OfflineDecreasing):

    _OfflineDecreasing__delegation = Ff_online()


class BestFitOff(OfflineDecreasing):

    _OfflineDecreasing__delegation = Bf_online()


class WorstFitOff(OfflineDecreasing):

    _OfflineDecreasing__delegation = Wf_online()

# End of T2 Offline Algorithms -----


# T4 - Offline Algorithms ----

class RefinedFirstFitOff(OfflineDecreasing):

    _OfflineDecreasing__delegation = Rff_online()

# End of T4 Offline Algorithms ----

# T5 Algorithms ----


class Multifit(Offline):
    def _process(self, n: int, weights: WeightList) -> Solution:
        weights = sorted(weights, reverse=True)
        lower = max(sum(weights) / n, max(weights))
        upper = max(2 * sum(weights) / n, max(weights))
        strategy: Offline = FirstFitOff()
        for i in range(1000):
            c = (lower + upper) / 2
            num_bins = len(strategy([c, weights]))
            if num_bins <= n:
                upper = c
            else:
                lower = c
        return strategy([upper, weights])


class EmptiestBinOff(OfflineDecreasing):

    _OfflineDecreasing__delegation = EB_online()

# End of T5 Algorithms ----
