import matplotlib.pyplot as plt

file_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

def plt_correct_percent(correct_percentage: dict):
     # Plot the points above point graph     
     plt.figure(figsize=(10,3))
     plt.scatter([i for i in correct_percentage], correct_percentage.values())
     plt.xlabel('Algorithm')
     plt.ylabel('% Correct')
     plt.title('Correct % per algorithm')
     plt.show()
     # plt.savefig("./analysis_tools/outputs/offline.png")

def plt_correct_percent(avg_excess: dict):
     # Plot the points above point graph     
     plt.figure(figsize=(10,3))
     plt.scatter([i for i in avg_excess], avg_excess.values())
     plt.xlabel('Algorithm')
     plt.ylabel('avg excess')
     plt.title('avg excess per algorithm')
     plt.show()
     # plt.savefig("./analysis_tools/outputs/offline.png")