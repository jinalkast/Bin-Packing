import pyperf
from os import listdir
from os.path import isfile, join, basename
from macpacking.algorithms.baseline import BenMaier as bp_base, MultiwayNumberPartitioning as multiway_base
from macpacking.algorithms.offline import (
    NextFitOff as NFOff,
    WorstFitOff as WFOff,
    BestFitOff as BFOff,
    FirstFitOff as FFOff,
    RefinedFirstFitOff as RffOff,
    EmptiestBinOff as EbOff
)

from macpacking.algorithms.online import (
    NextFitOn as NFOn,
    WorstSolution as WS,
    WorstFitOn as WFOn,
    BestFitOn as BFOn,
    FirstFitOn as FFOn,
    RefinedFirstFitOn as RffOn,
    EmptiestBinOn as EbOn
)

from macpacking.reader import BinppReader
from macpacking.multiway_adapter import MultiwayAdapter

# We consider:
#   - 50 objects (N1)
#   - bin capacity of 150 (C3)
#   - and weight in the [20,100] interval (W2)
CASES = './_datasets/binpp/N1C3W2'

OFFLINE_STRATEGIES = [
    NFOff, WFOff, BFOff, FFOff, RffOff, EbOff, bp_base, multiway_base
]

ONLINE_STRATEGIES = [
    NFOn, WS, WFOn, BFOn, FFOn, RffOn, EbOn
]


def main():
    '''Example of benchmark code'''
    cases = list_case_files(CASES)
    run_bench_binpacking(cases, [NFOff, WFOff, BFOff, FFOff, RffOff, bp_base, NFOn, WS, WFOn, BFOn, FFOn, RffOn])
    run_bench_TFive(cases, [multiway_base, EbOn, EbOff])


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
            runner.bench_func(name, binpacker, data)


if __name__ == "__main__":
    main()
