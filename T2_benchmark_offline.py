import pyperf
from os import listdir
from os.path import isfile, join, basename
from macpacking.algorithms.offline import NextFit as NFOff, WorstFit as WFOff, BestFit as BFOff, FirstFit as FFOff 
from macpacking.reader import BinppReader

# We consider:
#   - 50 objects (N1)
#   - bin capacity of 150 (C3)
#   - and weight in the [20,100] interval (W2)
CASES = './_datasets/binpp/N1C3W2'

OFFLINE_STRATEGIES = [
    NFOff, WFOff, BFOff, FFOff,
]

def main():
    '''Example of benchmark code'''
    cases = list_case_files(CASES)
    #run_bench_offline_runningTime([cases[0]],OFFLINE_STRATEGIES)
    run_analyze_correctness(cases, OFFLINE_STRATEGIES)

def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])

def run_bench_offline_runningTime(cases: list[str], functions: list):
    runner = pyperf.Runner()
    for func in functions:
     for case in cases:
          name = f'{func.__name__}-{"Offline"}-{case[-6:]}'
          data = BinppReader(case).offline()
          binpacker = func()
          runner.bench_func(name, binpacker, data)

def run_analyze_correctness(cases: list[str], functions:list):
    # optimal_solutions = get_solution_set(cases)
    for func in functions:
        # num_of_excess_bins = 0
        # percent_excess
        for case in cases:
            strategy = func()
            data = BinppReader(case).offline()
            num_of_bins = len(strategy(data))
            # optimal_solution = solution[case]
            # num_of_excess_bins += num_of_bins - optimal_solutions[case]
            # percent_excess += num_of_bins/optimal_solution
            print(f'{func.__name__}-{basename(case)}-{num_of_bins}')
        # print(f'{func.__name__} mean excess {num_of_excess_bins/len(cases))
        # print(f'{func.__name__} % excess {percent_excess/len(cases))

if __name__ == "__main__":
    main()
