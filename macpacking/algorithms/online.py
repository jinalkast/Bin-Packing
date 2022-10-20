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

class WorstSolution(Online):
    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        solution = []
        for w in stream:
            solution.append([w])
        return solution

class FirstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        solution = [[]]
        for w in stream:
            added = False
            for bin in solution:
                if sum(bin) + w <= capacity:
                    bin.append(w)
                    added = True
                    break
            if not added:
                solution.append([w])
        return solution

class BestFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        solution = [[]]
        for w in stream:
            bin_index = -1
            max_load = 0
            for i in range(len(solution)):
                if sum(solution[i]) + w <= capacity:
                    if sum(solution[i]) >= max_load:
                        bin_index = i
                        max_load = sum(solution[i])
            if bin_index >= 0:
                solution[bin_index].append(w)    
            else:
                solution.append([w])
        return solution

class WorstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        solution = [[]]
        for w in stream:
            bin_index = -1
            min_load = capacity
            for i in range(len(solution)):
                if sum(solution[i]) + w <= capacity:
                    if sum(solution[i]) <= min_load:
                        bin_index = i
                        min_load = sum(solution[i])
            if bin_index >= 0:
                solution[bin_index].append(w)    
            else:
                solution.append([w])
        return solution
