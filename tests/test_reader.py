from macpacking.reader import DatasetReader, JburkardtReader, SolutionReader
from sample_bench import list_case_files

def test_JburkardtReader():
    #testing p01
    capacity_file = '_datasets/jburkardt/p01_c.txt'
    weights_file = '_datasets/jburkardt/p01_w.txt'
    capacity = 100
    oracle = [70, 60, 50, 33, 33, 33, 11, 7, 3]
    reader: DatasetReader = JburkardtReader(capacity_file, weights_file)
    assert capacity == reader.offline()[0]
    assert oracle == sorted(reader.offline()[1], reverse=True)

    #testing p02
    capacity_file = '_datasets/jburkardt/p02_c.txt'
    weights_file = '_datasets/jburkardt/p02_w.txt'
    capacity = 100
    oracle = [99, 94, 79, 64, 50, 46, 43, 37, 32, 19, 18, 7, 6, 3]
    reader: DatasetReader = JburkardtReader(capacity_file, weights_file)
    assert capacity == reader.offline()[0]
    assert oracle == sorted(reader.offline()[1], reverse=True)

    #testing p03
    capacity_file = '_datasets/jburkardt/p03_c.txt'
    weights_file = '_datasets/jburkardt/p03_w.txt'
    capacity = 100
    oracle = [49, 41, 34, 33, 29, 26, 26, 22, 20, 19]
    reader: DatasetReader = JburkardtReader(capacity_file, weights_file)
    assert capacity == reader.offline()[0]
    assert oracle == sorted(reader.offline()[1], reverse=True)

    #testing p04
    capacity_file = '_datasets/jburkardt/p04_c.txt'
    weights_file = '_datasets/jburkardt/p04_w.txt'
    capacity = 524
    oracle = [442, 252, 252, 252, 252, 252, 252, 252, 127, 127, 127, 127, 127, 106, 106, 106, 106, 85, 84, 46, 37, 37, 12, 12, 12, 10, 10, 10, 10, 10, 10, 9, 9]
    reader: DatasetReader = JburkardtReader(capacity_file, weights_file)
    assert capacity == reader.offline()[0]
    assert oracle == sorted(reader.offline()[1], reverse=True)


def test_SolutionReader():
    #testing binpp-hard
    solution_file = '_datasets/solutions/binpp-hard.csv'
    CASES = '_datasets/binpp-hard'
    cases = list_case_files(CASES)
    oracle = [56, 57, 56, 55, 57, 56, 57, 55, 57, 56]
    reader: SolutionReader = SolutionReader(cases, solution_file)
    assert oracle == reader.readSolutions()    
