from os import listdir
from os.path import isfile, join
from macpacking.algorithms.offline import NextFitOff as NFOff, WorstFitOff as WFOff, BestFitOff as BFOff, FirstFitOff as FFOff
from macpacking.algorithms.online import NextFitOn as NFOn, WorstSolution as WS, WorstFitOn as WFOn, BestFitOn as BFOn, FirstFitOn as FFOn, RefinedFirstFitOn as RffOn
from macpacking.reader import BinppReader
from macpacking.reader import SolutionReader

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
    solution_reader = SolutionReader(cases, "./_datasets/solutions/binpp.csv")
    optimal_solutions = solution_reader.readSolutions()
    for func in functions:
        num_of_excess_bins = 0
        percent_excess = 0
        num_of_correct_solutions = 0
        for i in range(len(cases)):
            strategy = func()
            if func in OFFLINE_STRATEGIES:
                data = BinppReader(cases[i]).offline()
            else:
                data = BinppReader(cases[i]).online()

            num_of_bins = len(strategy(data))
            optimal_solution = optimal_solutions[i]

            num_of_correct_solutions += num_of_bins == optimal_solution
            num_of_excess_bins += num_of_bins - optimal_solutions[i]
            percent_excess += num_of_bins/optimal_solution

        print(f'{func.__name__} mean excess {num_of_excess_bins/len(cases)}')
        print(f'{func.__name__} % excess {round(100*percent_excess/len(cases),2)}')
        print(f'{func.__name__} Correct % = {100*num_of_correct_solutions/len(cases)}')
        print()

if __name__ == "__main__":
    main()