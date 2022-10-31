import matplotlib.pyplot as plt
# micro seconds
NFOff_dur = [4.27,4.39,4.46,4.34,4.39,4.36,4.33,4.51,4.30,4.41,4.35,4.32,4.40,4.38,4.38,4.41,4.36,4.38,4.40,4.45]
BFOff_dur = [57.7,65.2,73.5,61.2,63.2,62.5,68.5,64.3,53.5,65.9,61.5,59.2,64.1,64.7,58.7,56.4,56.1,55.4,67.4,67.4]
WFOff_dur = [58.8,69.1,79,63.4,62.1,62.4,71,64.5,53.8,68.4,63.5,59.6,67.6,66.4,57.7,56,56.2,56.2,70.8,69.4]
FFOff_dur = [38,37.2,37.9,38.8,40.6,39.9,37.3,40,37.9,39.5,40.3,39.1,38.7,37.6,39.3,38.3,38.2,38.3,39.2,40.1]

# nano seconds
NFOn_dur = [158,159,160,151,159,160,162,163,160,162,161,159,160,161,160,162,160,159,161,160]
WS_dur = [137,134,134,133,132,132,135,133,131,131,132,134,134,132,133,135,132,133,135,134]
BFOn_dur = [154,157,157,159,155,155,155,157,154,157,155,156,156,158,156,157,156,156,154,160]
WFOn_dur = [154,154,157,152,159,155,154,155,158,156,156,155,154,155,154,154,155,154,156,155]
FFOn_dur = [154,155,154,155,154,156,157,154,156,152,156,155,154,154,152,156,154,159,154,155]

# micro seconds
NFOff_error = [0.13,0.10,0.15,0.11,0.19,0.14,0.13,0.19,0.15,0.15,0.11,0.13,0.12,0.16,0.15,0.25,0.17,0.13,0.15,0.15]
BFOff_error = [2.1,2.4,1.5,1.7,1.4,1.2,2.3,1.7,1.4,1.1,1.5,1.4,1.6,1.0,1.6,1.5,1.9,1.7,1.6,2.3]
WFOff_error = [2,2.1,2.1,2.3,1.3,1.9,4.9,2.2,1.8,1.9,2.5,2.0,6.3,2.7,1.6,1.6,1.9,3.5,1.7,1.7]
FFOff_error = [1.3,1.3,1.4,1.5,3.9,1.1,1.4,1.7,1.4,1.8,1.8,1.2,1.8,1.0,1.7,1.3,1.6,1.6,2.1,1.2]

# nano seconds
BFOn_error = [8,9,7,7,6,6,7,10,6,7,6,5,6,11,7,7,7,6,7,16]
WFOn_error = [7,7,5,5,6,7,5,6,6,5,6,6,6,7,10,6,8,6,5,8]
FFOn_error = [4,8,8,8,7,7,9,8,7,7,8,6,6,6,5,6,7,7,6,6]
WS_error = [10,5,6,6,7,5,8,4,6,5,6,7,4,8,5,8,5,4,6,6]
NFOn_error = [4,7,7,8,6,7,6,7,6,9,7,7,6,7,7,6,7,6,7,6]

# file_libary= "N1C3W2"
file_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

def pltOffline():
     plt.clf() 
     # Plot the points above point graph 
     plt.plot(file_names, NFOff_dur, label = "NextFit Offline")
     plt.plot(file_names, BFOff_dur, label = "BestFit Offline")
     plt.plot(file_names, WFOff_dur, label = "WorstFit Offline")
     plt.plot(file_names, FFOff_dur, label = "FirstFit Offline")

     plt.errorbar(file_names, NFOff_dur, yerr=NFOff_error, fmt='o', label = "NextFit Offline")
     plt.errorbar(file_names, BFOff_dur, yerr=BFOff_error, fmt='o', label = "BestFit Offline")
     plt.errorbar(file_names, WFOff_dur, yerr=WFOff_error, fmt='o', label = "WorstFit Offline")
     plt.errorbar(file_names, FFOff_dur, yerr=FFOff_error, fmt='o', label = "FirstFit Offline")


     plt.xlabel('Case')
     plt.ylabel('Duration in Micro Seconds')
     plt.title('Duration of Offline Algorithms')
     plt.legend()
     plt.show()
     #plt.savefig("./analysis_tools/outputs/offline.png")

def pltOnline():
     plt.clf()
     # Plot the points above point graph 
     plt.plot(file_names, NFOn_dur, label = "NextFit Online")
     plt.plot(file_names, WS_dur, label = "Worst Solution")
     plt.plot(file_names, BFOn_dur, label = "BestFit Online")
     plt.plot(file_names, WFOn_dur, label = "WorstFit Online")
     plt.plot(file_names, FFOn_dur, label = "FirstFit Online")

     plt.errorbar(file_names, NFOn_dur, yerr=NFOn_error, fmt='o', label = "NextFit Online")
     plt.errorbar(file_names, BFOn_dur, yerr=BFOn_error, fmt='o', label = "BestFit Online")
     plt.errorbar(file_names, WFOn_dur, yerr=WFOn_error, fmt='o', label = "WorstFit Online")
     plt.errorbar(file_names, FFOn_dur, yerr=FFOn_error, fmt='o', label = "FirstFit Online")
     plt.errorbar(file_names, WS_dur, yerr=WS_error, fmt='o', label = "FirstFit Online")


     plt.xlabel('Case')
     plt.ylabel('Duration in Nano Seconds')
     plt.title('Duration of Online Algorithms')
     plt.legend()
     plt.show()
     #plt.savefig("./analysis_tools/outputs/online.png")

def main():
     #pltOffline()
     pltOnline()

if __name__ == "__main__":
    main()
