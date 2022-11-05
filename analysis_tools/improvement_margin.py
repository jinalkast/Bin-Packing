from os import listdir
from collections import defaultdict
from os.path import isfile, join, basename
from macpacking.reader import BinppReader
from macpacking.reader import SolutionReader
from macpacking.algorithms.offline import (
    NextFitOff as NFOff,
    WorstFitOff as WFOff,
    BestFitOff as BFOff,
    FirstFitOff as FFOff,
    EmptiestBinOff as EBOff,
    Multifit as Mf,
    )
from macpacking.algorithms.online import (
    NextFitOn as NFOn,
    WorstSolution as WS,
    WorstFitOn as WFOn,
    BestFitOn as BFOn,
    FirstFitOn as FFOn,
    RefinedFirstFitOn as RffOn,
    EmptiestBinOn as EBOn
    )
from macpacking.algorithms.baseline import MultiwayNumberPartitioning as MNP, BenMaier
from macpacking.multiway_adapter import MultiwayAdapter

OFFLINE_STRATEGIES = [
    NFOff, WFOff, BFOff, FFOff, MNP, BenMaier
]

ONLINE_STRATEGIES = [
    NFOn, WS, WFOn, BFOn, FFOn, RffOn
]

CASES = './_datasets/binpp/N1C3W2'


def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])


def main():
    '''Example of benchmark code'''
    cases = list_case_files(CASES)
    run_analyze_correctness(cases, OFFLINE_STRATEGIES + ONLINE_STRATEGIES)


def run_analyze_correctness(cases: list[str], functions: list):
    # Get optimal bin nums for all problems in cases
    solution_reader = SolutionReader(cases, "./_datasets/solutions/binpp.csv")
    optimal_solutions = solution_reader.readSolutions()

    avg_excess = {}
    correct_percentage = {}

    # For each function, find the avg num of excess bins it uses as well as
    # the num of correct solutions it found
    for func in functions:
        num_of_excess_bins = 0
        num_of_correct_solutions = 0

        # For each case, compare the answer with the correct answer
        for i in range(len(cases)):
            strategy = func()
            if func in OFFLINE_STRATEGIES:
                data = BinppReader(cases[i]).offline()
            else:
                data = BinppReader(cases[i]).online()

            num_of_bins = len(strategy(data))
            optimal_solution = optimal_solutions[i]

            # Increase count of correct solution and excess bin count
            num_of_correct_solutions += num_of_bins == optimal_solution
            num_of_excess_bins += num_of_bins - optimal_solutions[i]

        # Calculate average excess and percentage correct after running all
        # cases
        avg_excess[func.__name__] = num_of_excess_bins / len(cases)
        correct_percentage[func.__name__] = 100 * \
            num_of_correct_solutions / len(cases)

    return [avg_excess, correct_percentage]

def find_max_bin_size_fixed_k(cases: list[str], functions: list, k: int):
    max_sizes = defaultdict(dict)
    for func in functions:
        for case in cases:
            if func in OFFLINE_STRATEGIES:
                data = MultiwayAdapter.to_multiway(BinppReader(case).offline(), k)
            else:
                data = MultiwayAdapter.to_multiway(BinppReader(case).online(), k)
            strategy = func()
            result = strategy(data)
            max_bin_size = max([sum(bin) for bin in result])
            max_sizes[func.__name__][basename(case)] = max_bin_size

    return max_sizes

def find_min_bin_size_fixed_k(cases: list[str], functions: list, k: int):
    min_sizes = defaultdict(dict)
    for func in functions:
        for case in cases:
            if func in OFFLINE_STRATEGIES:
                data = MultiwayAdapter.to_multiway(BinppReader(case).offline(), k)
            else:
                data = MultiwayAdapter.to_multiway(BinppReader(case).online(), k)
            strategy = func()
            result = strategy(data)
            min_bin_size = min([sum(bin) for bin in result])
            min_sizes[func.__name__][basename(case)] = min_bin_size

    return min_sizes

def find_max_bin_size_var_k(testcase: str, functions: list, lower: int, upper: int):
    max_sizes = defaultdict(dict)
    for func in functions:
        for k in range(lower,upper):
            if func in OFFLINE_STRATEGIES:
                data = MultiwayAdapter.to_multiway(BinppReader(testcase).offline(), k)
            else:
                data = MultiwayAdapter.to_multiway(BinppReader(testcase).online(), k)
            strategy = func()
            result = strategy(data)
            max_bin_size = max([sum(bin) for bin in result])
            max_sizes[func.__name__][k] = max_bin_size

    return max_sizes

def find_min_bin_size_var_k(testcase: str, functions: list, lower: int, upper: int):
    min_sizes = defaultdict(dict)
    for func in functions:
        for k in range(lower,upper):
            if func in OFFLINE_STRATEGIES:
                data = MultiwayAdapter.to_multiway(BinppReader(testcase).offline(), k)
            else:
                data = MultiwayAdapter.to_multiway(BinppReader(testcase).online(), k)
            strategy = func()
            result = strategy(data)
            min_bin_size = min([sum(bin) for bin in result])
            min_sizes[func.__name__][k] = min_bin_size

    return min_sizes
    
if __name__ == "__main__":
    main()
