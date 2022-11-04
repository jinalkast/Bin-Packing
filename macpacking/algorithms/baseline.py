from .. import Solution, WeightList
from ..model import Offline
import binpacking as bp


class BenMaier(Offline):

    def _process(self, capacity: int, weights: WeightList) -> Solution:
        return bp.to_constant_volume(weights, capacity)


class MultiwayNumberPartitioning(Offline):

    def _process(self, num_bins: int, weights: WeightList) -> Solution:
        return bp.to_constant_bin_number(weights, num_bins)
