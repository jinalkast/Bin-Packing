from .. import Solution, WeightStream
from ..model import Online


class NextFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
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

# T1 - Worst Possible algorithm ----

class WorstSolution(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        solution = []
        # For each item, create its own bin and append it to the
        # solution list
        for w in stream:
            solution.append([w])
        return solution

# T2 - Online algorithms ------------

class FirstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
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


class BestFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
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


class WorstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
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