import matplotlib.pyplot as plt
def nanoToMicro(n):
    return n/1000

# micro seconds
Baseline_dur = [
    49.5,
    47.3,
    47.9,
    47.7,
    47.1,
    49.2,
    54.9,
    54.4,
    52.5,
    54.1,
    53.6,
    51.9,
    53.5,
    52.6,
    52.7,
    53.3,
    53.5,
    53.9,
    51.7,
    51.0]
Baseline_error = [
    4.6,
    1.2,
    1.9,
    1.5,
    1.3,
    3.2,
    4.7,
    4.5,
    2.5,
    3.0,
    2.9,
    3.0,
    2.1,
    2.0,
    2.6,
    3.3,
    2.7,
    4.8,
    1.6,
    1.3]

# Nano Secs
EmptiestBinOn_dur = [
    614,
    611,
    616,
    618,
    619,
    622,
    618,
    620,
    619,
    621,
    622,
    612,
    619,
    620,
    615,
    628,
    621,
    626,
    620,
    611
    ]
EmptiestBinOn_error = [
    16,
    12,
    15,
    16,
    16,
    25,
    18,
    15,
    19,
    43,
    18,
    27,
    8,
    13,
    23,
    13,
    34,
    12,
    35,
    25,
    ]

#Micro Seconds
EmptiestBinOn_dur = list(map(nanoToMicro, EmptiestBinOn_dur))
EmptiestBinOn_error = list(map(nanoToMicro, EmptiestBinOn_error))

# Micro Seconds
EmptiestBinOff_dur = [
    1.01,
    1.01,
    1.02,
    1.02,
    1.02,
    1.02,
    1.02,
    1.02,
    1.05,
    1.02,
    1.02,
    1.03,
    1.03,
    1.04,
    1.07,
    1.06,
    1.04,
    1.05,
    1.03,
    1.04
]
EmptiestBinOff_error = [
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.03,
    0.02,
    0.03,
    0.11,
    0.03,
    0.02,
    0.03,
    0.03,
    0.06,
    0.05,
    0.04,
    0.04,
    0.03,
    0.04,
    0.02
]

# file_libary= "N1C3W2"
file_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
              'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']


def plot():
    plt.clf()
    # Plot the points above point graph
    plt.plot(file_names, EmptiestBinOff_dur, label="EmptiestBinOff")
    plt.plot(file_names, EmptiestBinOn_dur, label="EmptiestBinOn")

    # Uncomment to see base function in graphs
    # plt.plot(file_names, Baseline_dur, label="Baseline")
    # plt.errorbar(
    #     file_names,
    #     Baseline_dur,
    #     yerr=Baseline_error,
    #     fmt='o',
    #     label="Baseline")
    plt.errorbar(
        file_names,
        EmptiestBinOff_dur,
        yerr=EmptiestBinOff_error,
        fmt='o',
        label="EmptiestBinOff")
    plt.errorbar(
        file_names,
        EmptiestBinOn_dur,
        yerr=EmptiestBinOn_error,
        fmt='o',
        label="EmptiestBinOn")

    plt.xlabel('Case')
    plt.ylabel('Duration in Micro Seconds')
    plt.title('Duration of Multiway Number Partitioning Algorithms - N1C3W2 - k = 5')
    plt.legend()
    # plt.show()
    plt.savefig("./analysis_tools/outputs/t5_no_bench.png")
    # plt.savefig("./analysis_tools/outputs/t5.png")


def main():
    plot()


if __name__ == "__main__":
    main()
