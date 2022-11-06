from macpacking.reader import BinppReader
import macpacking.algorithms.offline as offline
import macpacking.algorithms.online as online
from analysis_tools.improvement_margin import list_case_files
from macpacking.multiway_adapter import MultiwayAdapter


def test_NFOff():
    answers = [30, 35, 26, 32, 31, 32, 30, 35, 31,
               32, 31, 38, 34, 30, 37, 32, 35, 31, 33, 34]
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = offline.NextFitOff()
    for i in range(len(cases)):
        data = BinppReader(cases[i]).offline()
        result = strategy(data)
        assert len(result) == answers[i]


def test_FFOff():
    answers = [25, 31, 21, 28, 26, 27, 25, 31, 25,
               26, 26, 33, 30, 26, 32, 26, 28, 25, 28, 28]
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = offline.FirstFitOff()
    for i in range(len(cases)):
        data = BinppReader(cases[i]).offline()
        result = strategy(data)
        assert len(result) == answers[i]


def test_BFOff():
    answers = [25, 31, 21, 28, 26, 27, 25, 31, 25,
               26, 26, 33, 30, 26, 32, 26, 28, 25, 28, 28]
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = offline.BestFitOff()
    for i in range(len(cases)):
        data = BinppReader(cases[i]).offline()
        result = strategy(data)
        assert len(result) == answers[i]


def test_WFOff():
    answers = [25, 31, 21, 28, 26, 27, 26, 31, 25,
               26, 26, 33, 30, 26, 32, 26, 28, 25, 28, 28]
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = offline.WorstFitOff()
    for i in range(len(cases)):
        data = BinppReader(cases[i]).offline()
        result = strategy(data)
        assert len(result) == answers[i]


def test_RFFOff():
    answers = [30, 36, 27, 33, 31, 33, 31, 36, 31,
               30, 32, 38, 34, 30, 38, 33, 35, 32, 34, 35]
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = offline.RefinedFirstFitOff()
    for i in range(len(cases)):
        data = BinppReader(cases[i]).offline()
        result = strategy(data)
        assert len(result) == answers[i]


def test_NFOn():
    answers = [32, 36, 28, 35, 33, 35, 33, 37, 32,
               33, 32, 39, 36, 32, 39, 32, 35, 31, 36, 36]
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = online.NextFitOn()
    for i in range(len(cases)):
        data = BinppReader(cases[i]).online()
        result = strategy(data)
        assert len(result) == answers[i]


def test_WS():
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = online.WorstSolution()
    for i in range(len(cases)):
        data = BinppReader(cases[i]).online()
        result = strategy(data)
        assert len(result) == 50


def test_FFOn():
    answers = [26, 31, 23, 28, 28, 29, 26, 31, 26,
               27, 27, 33, 30, 27, 33, 27, 29, 26, 29, 29]
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = online.FirstFitOn()
    for i in range(len(cases)):
        data = BinppReader(cases[i]).online()
        result = strategy(data)
        assert len(result) == answers[i]


def test_BFOn():
    answers = [26, 31, 22, 28, 27, 28, 26, 31, 26,
               27, 26, 33, 30, 26, 32, 27, 28, 26, 29, 29]
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = online.BestFitOn()
    for i in range(len(cases)):
        data = BinppReader(cases[i]).online()
        result = strategy(data)
        assert len(result) == answers[i]


def test_WFOn():
    answers = [28, 33, 25, 29, 28, 30, 28, 33, 28,
               28, 28, 36, 32, 28, 35, 29, 31, 28, 31, 32]
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = online.WorstFitOn()
    for i in range(len(cases)):
        data = BinppReader(cases[i]).online()
        result = strategy(data)
        assert len(result) == answers[i]


def test_RFFOn():
    answers = [30, 36, 27, 33, 31, 33, 31, 36, 31,
               30, 32, 38, 34, 30, 38, 33, 35, 32, 34, 35]
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = online.RefinedFirstFitOn()
    for i in range(len(cases)):
        data = BinppReader(cases[i]).online()
        result = strategy(data)
        assert len(result) == answers[i]


def test_EBOn():
    answers = [
        175,
        189,
        149,
        177,
        170,
        178,
        177,
        185,
        167,
        179,
        168,
        195,
        188,
        174,
        196,
        169,
        175,
        169,
        185,
        184]
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = online.EmptiestBinOn()
    for i in range(len(cases)):
        data = MultiwayAdapter.to_multiway(BinppReader(cases[i]).online(), 20)
        result = strategy(data)
        assert max([sum(res) for res in result]) == answers[i]


def test_EBOff():
    answers = [
        129,
        145,
        101,
        136,
        128,
        134,
        129,
        145,
        125,
        128,
        127,
        155,
        145,
        126,
        160,
        126,
        141,
        130,
        141,
        140]
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = offline.EmptiestBinOff()
    for i in range(len(cases)):
        data = MultiwayAdapter.to_multiway(BinppReader(cases[i]).offline(), 20)
        result = strategy(data)
        assert max([sum(res) for res in result]) == answers[i]


def test_MF():
    answers = [
        129,
        145,
        101,
        136,
        128,
        134,
        129,
        145,
        125,
        128,
        127,
        155,
        145,
        126,
        160,
        126,
        141,
        130,
        141,
        140]
    dataset = "./_datasets/binpp/N1C1W1/"
    cases = list_case_files(dataset)
    strategy = offline.EmptiestBinOff()
    for i in range(len(cases)):
        data = MultiwayAdapter.to_multiway(BinppReader(cases[i]).offline(), 20)
        result = strategy(data)
        assert max([sum(res) for res in result]) == answers[i]
