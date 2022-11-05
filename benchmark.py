import pyperf
from os import listdir
from os.path import isfile, join, basename
from macpacking.algorithms.baseline import MultiwayNumberPartitioning as base
from macpacking.algorithms.offline import (
    NextFitOff as NFOff,
    WorstFitOff as WFOff,
    BestFitOff as BFOff,
    FirstFitOff as FFOff,
    RefinedFirstFitOff as RffOff,
    MultifitOff as MfOff
)

from macpacking.algorithms.online import (
    NextFitOn as NFOn,
    WorstSolution as WS,
    WorstFitOn as WFOn,
    BestFitOn as BFOn,
    FirstFitOn as FFOn,
    RefinedFirstFitOn as RffOn,
    MultifitOn as MfOn
)

from macpacking.reader import BinppReader
from macpacking.multiway_adapter import MultiwayAdapter

# We consider:
#   - 50 objects (N1)
#   - bin capacity of 150 (C3)
#   - and weight in the [20,100] interval (W2)
CASES = './_datasets/binpp/N1C3W2'

OFFLINE_STRATEGIES = [
    NFOff, WFOff, BFOff, FFOff, RffOff, base
]

ONLINE_STRATEGIES = [
    NFOn, WS, WFOn, BFOn, FFOn, RffOn
]


def main():
    '''Example of benchmark code'''
    cases = list_case_files(CASES)
    run_bench_TFive(cases, [base, MfOn, MfOff])


def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])


def run_bench_binpacking(cases: list[str], functions: list):
    runner = pyperf.Runner()
    for func in functions:
        for case in cases:
            name = f'{func.__name__}-{basename(case)}'
            if func in OFFLINE_STRATEGIES:
                data = BinppReader(case).offline()
            else:
                data = BinppReader(case).online()

            binpacker = func()
            runner.bench_func(name, binpacker, data)


def run_bench_TFive(cases: list[str], functions: list):
    runner = pyperf.Runner()
    for func in functions:
        for case in cases:
            if func in OFFLINE_STRATEGIES:
                data = MultiwayAdapter.to_multiway(BinppReader(case).offline(),20)
            else:
                data = MultiwayAdapter.to_multiway(BinppReader(case).online(),20)
                
            name = f'{func.__name__}-{basename(case)}'
            binpacker = func()
            # print(data)
            # print(name)
            # print(binpacker)
            runner.bench_func(name, binpacker, data)


if __name__ == "__main__":
    main()
