from .. import Solution, WeightIterator
from ..model import Online


class NextFitOn(Online):

    def _process(self, capacity: int, stream: WeightIterator) -> Solution:
        bin_index = 0
        solution = [[]]
        remaining = capacity
        for w in stream:
            if remaining >= w:
                solution[bin_index].append(w)
                remaining = remaining - w
            else:
                bin_index += 1
                solution.append([w])
                remaining = capacity - w
        return solution

# T1 - Worst Possible Algorithm ----


class WorstSolution(Online):

    def _process(self, capacity: int, stream: WeightIterator) -> Solution:
        solution = []
        # For each item, create its own bin and append it to the
        # solution list
        for w in stream:
            solution.append([w])
        return solution

# T2 - Online Algorithms ------------


class FirstFitOn(Online):

    def _process(self, capacity: int, stream: WeightIterator) -> Solution:
        solution = [[]]
        # For each item, find the first bin with enough capacity to hold it
        # If no such bin exists, create a new bin containing it
        for w in stream:
            added = False
            # Search for bin with enough space
            for bin in solution:
                if sum(bin) + w <= capacity:
                    bin.append(w)
                    added = True
                    break

            # No new bin found
            if not added:
                solution.append([w])

        return solution


class BestFitOn(Online):

    def _process(self, capacity: int, stream: WeightIterator) -> Solution:
        solution = [[]]
        # For each item, find the most full bin with enough capacity to hold it
        # If no such bin exists, create a new bin containing it
        for w in stream:
            bin_index = -1
            max_load = 0
            for i in range(len(solution)):
                # Bin found
                if sum(solution[i]) + w <= capacity:
                    # Compare to max bin
                    if sum(solution[i]) >= max_load:
                        bin_index = i
                        max_load = sum(solution[i])
            if bin_index >= 0:
                solution[bin_index].append(w)
            # No bin found with enough space, creating new bin
            else:
                solution.append([w])
        return solution


class WorstFitOn(Online):

    def _process(self, capacity: int, stream: WeightIterator) -> Solution:
        solution = [[]]
        # For each item, find the emptiest bin with enough capacity to hold it
        # If no such bin exists, create a new bin containing it
        for w in stream:
            bin_index = -1
            min_load = capacity
            for i in range(len(solution)):
                # Bin found
                if sum(solution[i]) + w <= capacity:
                    # Compare to min bin
                    if sum(solution[i]) <= min_load:
                        bin_index = i
                        min_load = sum(solution[i])
            if bin_index >= 0:
                solution[bin_index].append(w)
            # No bin found with enough space, creating new bin
            else:
                solution.append([w])
        return solution

# End of T2 Online Algorithms -----

# T4 - Online Algorithms ---


class RefinedFirstFitOn(Online):

    def classifyItem(self, weight: int) -> int:
        ratio = weight/self.capacity
        # A-Piece
        if 1/2 < ratio <= 1:
            return 1

        # B1-Piece
        elif 2/5 < ratio <= 1/2:
            return 2

        # B2-Piece
        elif 1/3 < ratio <= 2/5:
            self.num_of_BTwos += 1
            for i in (6, 7, 8, 9):
                # Is (mk)th b2 piece we've seen
                if self.num_of_BTwos % i == 0:
                    return 1

            # Not (mk)th b2 piece
            return 3

        # X-Piece
        elif 0 < ratio <= 1/3:
            return 4

    def _process(self, capacity: int, stream: WeightIterator) -> Solution:
        self.capacity = capacity
        self.num_of_BTwos = 0
        solution = []
        classes_of_bins = []
        # For each item, find the first bin of the same class with enough
        # capacity to hold it. If no such bin exists, create a new bin
        # and classify it with the same designation of the item
        for w in stream:
            found = False
            item_class = self.classifyItem(w)
            for i in range(len(solution)):
                # If bin is proper class and has room
                if (classes_of_bins[i] == item_class
                   and (sum(solution[i]) + w < capacity)):
                    solution[i].append(w)
                    found = True
                    break

            # No bin found, creating new bin
            if not (found):
                solution.append([w])
                classes_of_bins.append(item_class)

        return solution

# End of T4 Online Algorithms ----

# T5 Algorithm ----

class EmptiestBinOn(Online):
    def _process(self, bins: int, stream: WeightIterator) -> Solution:
        # Make all bins
        solution = [[] for i in range(bins)]
        # For each item in the stream, find the least full bin it can
        # fit into
        for w in stream:
            smallest_index = 0
            # Initial smallest weight is inf
            smallest_weight = float('inf')
            for i in range(bins):
                # check if bin weight < smallest seen weight
                if sum(solution[i]) < smallest_weight:
                    # Record new record weight and corresponding index
                    smallest_weight = sum(solution[i])
                    smallest_index = i
            # After checking all bins, append item to smallest bin 
            # discovered
            solution[smallest_index].append(w)

        return solution
