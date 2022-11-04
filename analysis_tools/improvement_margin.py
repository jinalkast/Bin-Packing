from os import listdir
from os.path import isfile, join
from macpacking.reader import BinppReader
from macpacking.reader import SolutionReader
from macpacking.algorithms.offline import (
    NextFitOff as NFOff,
    WorstFitOff as WFOff,
    BestFitOff as BFOff,
    FirstFitOff as FFOff)
from macpacking.algorithms.online import (
    NextFitOn as NFOn,
    WorstSolution as WS,
    WorstFitOn as WFOn,
    BestFitOn as BFOn,
    FirstFitOn as FFOn,
    RefinedFirstFitOn as RffOn)

OFFLINE_STRATEGIES = [
    NFOff, WFOff, BFOff, FFOff,
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


if __name__ == "__main__":
    main()
