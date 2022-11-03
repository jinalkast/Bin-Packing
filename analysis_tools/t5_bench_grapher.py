import matplotlib.pyplot as plt
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

Multifit_dur = [
    37.4,
    37.6,
    37.9,
    38.1,
    37.4,
    36.7,
    37.0,
    35.8,
    37.2,
    39.4,
    44.9,
    42.8,
    45.6,
    43.8,
    44.6,
    42.5,
    44.2,
    44.1,
    43.9,
    45.6]

# micro seconds
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

Multifit_error = [
    2.0,
    1.0,
    1.5,
    1.5,
    1.7,
    1.6,
    2.2,
    1.4,
    1.5,
    3.2,
    1.9,
    2.5,
    3.5,
    1.7,
    1.9,
    3.0,
    1.5,
    2.3,
    0.8,
    1.9]

# file_libary= "N1C3W2"
file_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
              'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']


def plot():
    plt.clf()
    # Plot the points above point graph
    plt.plot(file_names, Baseline_dur, label = "Baseline")
    plt.plot(file_names, Multifit_dur, label = "MultiFit")

    plt.errorbar(file_names, Baseline_dur, yerr=Baseline_error, fmt='o', label = "Baseline")
    plt.errorbar(file_names, Multifit_dur, yerr=Multifit_error, fmt='o', label = "Multifit")

    plt.xlabel('Case')
    plt.ylabel('Duration in Micro Seconds')
    plt.title('Duration of Multiway Number Partitioning Algorithms (n = 5)')
    plt.legend()
    # plt.show()
    plt.savefig("./analysis_tools/outputs/t5.png")


def main():
    plot()


if __name__ == "__main__":
    main()
