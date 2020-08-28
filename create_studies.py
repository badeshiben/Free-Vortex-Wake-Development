import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

""" DEFAULTS """
dpsi1 = np.array([2.5, 3.75, 5, 7.5, 10, 12.5]) * np.pi / 180  # rad
dpsi = np.array([2.5, 5, 7.5, 10, 12.5, 15]) * np.pi / 180  # rad
wakeLengthD = 6
rot_D = 102.996267808408*2 # m
nearWakeExtent = 540*np.pi/180  # rad
WS = [4, 6, 8, 10, 12]
RPM = np.array([4, 5.5, 7.5, 7.84, 7.85])
rotSpd = RPM * 0.104719755  # rad/s
Pitch = [0, 0, 0, 6, 10]  # deg
# DTfvw_default = np.round(dpsi_default/rotSpd, decimals=3) # sec
FWE = wakeLengthD * rot_D # m
WakeRegFactor_default = 3
WingRegFactor_default = 3
CoreSpreadEddyVisc_default = 100
rotSpdM = np.outer(rotSpd, np.ones(len(dpsi)))
WSM = np.outer(WS, np.ones(len(dpsi)))
dpsiM1 = np.outer(np.ones(len(WS)), dpsi1)

""" FILL THESE IN BASED ON DISCRETIZATION STUDY RESULTS """
dpsi_cvg = 5*np.pi/180*np.ones(5)
DTfvw_cvg = np.round(np.multiply(1/rotSpd, dpsi_cvg), decimals=3)
nNWPanel_cvg = np.ones(5)  # TODO
nearWakeExtent_cvg = 720*np.pi/180  # rad
nNWPanel_cvg = np.round(nearWakeExtent_cvg/(np.multiply(rotSpd, DTfvw_cvg)), decimals=0)
FWE_cvg = 6 * rot_D
WakeLength_cvg = np.round(FWE_cvg * rotSpd/WS/dpsi_cvg)  # TODO
WakeRegFactor_cvg = np.ones(5)  # TODO
WingRegFactor_cvg = np.ones(5)  # TODO

dpsi_cvgM = np.outer(np.ones(len(WS)), dpsi_cvg)
WakeLength1 = np.round(FWE * rotSpdM/WSM/dpsiM1, decimals=0)  # Npanels
WakeLength2 = np.round(FWE * rotSpd/WS/dpsi_cvg, decimals=0)  # Npanels

""" study 1: DTfvw """
DTfvw = np.round(np.outer(1/rotSpd, dpsi1), decimals=3)
nNWPanel1 = np.round(nearWakeExtent/(np.multiply(rotSpdM, DTfvw)), decimals=0)
study1 = {
        'param'                         : 'DTfvw',
        'paramfull'                     : 'DTfvw_[s]',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : DTfvw,
        'nNWPanel'                      : nNWPanel1,
        'WakeLength'                    : WakeLength1,
        'WakeRegFactor'                 : WakeRegFactor_default * np.ones([len(WS), len(dpsi)]),
        'WingRegFactor'                 : WingRegFactor_default * np.ones([len(WS), len(dpsi)]),
        'CoreSpreadEddyVisc'            : CoreSpreadEddyVisc_default * np.ones([len(WS), len(dpsi)]),
        'TMax'                          : 900
}
study1Maxtime = 2 * wakeLengthD*rot_D/np.min(WS)+200
# rounding up study 1 max time to 400s

"""study 2: nNWpanel """
NWE = np.array([30, 60, 120, 180, 240, 300, 360, 540, 720, 1080, 1440, 1800, 2160, 2520]) * np.pi / 180
prod = DTfvw_cvg * rotSpd
nNWPanel = np.round(np.outer(1/prod, NWE), decimals=0)
study2 = {
        'param'                         : 'nNWPanel',
        'paramfull'                     : 'nNWPanel_[-]',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : np.outer(DTfvw_cvg, np.ones(len(NWE))),
        'nNWPanel'                      : nNWPanel,
        'WakeLength'                    : np.outer(WakeLength2, np.ones(len(NWE))),
        'WakeRegFactor'                 : WakeRegFactor_default * np.ones([len(WS), len(NWE)]),
        'WingRegFactor'                 : WingRegFactor_default * np.ones([len(WS), len(NWE)]),
        'CoreSpreadEddyVisc'            : CoreSpreadEddyVisc_default * np.ones([len(WS), len(NWE)]),
        'TMax'                          : 900
}

"""study 3: WakeLength"""
FWE = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) * rot_D  # m
part = rotSpd / WS / dpsi_cvg
WakeLength = np.round(np.outer(part, FWE), decimals=0)
wlt = FWE[-1]*rotSpd[0]/WS[0]/dpsi_cvg[0]
study3 = {
        'param'                         : 'WakeLength',
        'paramfull'                     : 'WakeLength_[-]',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : np.outer(DTfvw_cvg, np.ones(len(FWE))),
        'nNWPanel'                      : np.outer(nNWPanel_cvg, np.ones(len(FWE))),
        'WakeLength'                    : WakeLength,
        'WakeRegFactor'                 : WakeRegFactor_default * np.ones([len(WS), len(FWE)]),
        'WingRegFactor'                 : WingRegFactor_default * np.ones([len(WS), len(FWE)]),
        'CoreSpreadEddyVisc'            : CoreSpreadEddyVisc_default * np.ones([len(WS), len(FWE)]),
        'TMax'                          : 1450
}
study3Maxtime = 2*max(FWE)/np.min(WS)+200

"""study 4: WakeRegFactor"""
WaRF = np.array([0.1, 0.5, 1, 1.5, 2, 2.5, 3, 5])
WakeRegFactor = np.outer(np.ones(len(WS)), WaRF)
study4 = {
        'param'                         : 'WakeRegFactor',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : np.outer(DTfvw_cvg, np.ones(len(WaRF))),
        'nNWPanel'                      : np.outer(nNWPanel_cvg, np.ones(len(WaRF))),
        'WakeLength'                    : np.outer(WakeLength_cvg, np.ones(len(WaRF))),
        'WakeRegFactor'                 : WakeRegFactor,
        'WingRegFactor'                 : WingRegFactor_default * np.ones([len(WS), len(WaRF)]),
        'CoreSpreadEddyVisc'            : CoreSpreadEddyVisc_default * np.ones([len(WS), len(WaRF)]),
        'TMax': 950
}
study4Maxtime = 2*7*rot_D/np.min(WS)+200


"""study 5: WingRegFactor"""
WiRF = np.array([0, 0.1, 0.5, 1, 1.5, 2, 2.5, 3, 5])
WingRegFactor = np.outer(np.ones(len(WS)), WiRF)
study5 = {
        'param'                         : 'WingRegFactor',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : np.outer(DTfvw_cvg, np.ones(len(WiRF))),
        'nNWPanel'                      : np.outer(nNWPanel_cvg, np.ones(len(WiRF))),
        'WakeLength'                    : np.outer(WakeLength_cvg, np.ones(len(WiRF))),
        'WakeRegFactor'                 : np.outer(WakeRegFactor_cvg, np.ones(len(WiRF))),
        'WingRegFactor'                 : WingRegFactor,
        'CoreSpreadEddyVisc'            : CoreSpreadEddyVisc_default * np.ones([len(WS), len(WiRF)])
}
"""study 6: """
WS = [4, 12]
RPM = np.array([4, 7.85])
rotSpd = RPM * 0.104719755  # rad/s
Pitch = [0, 10]  # deg
CSEV = np.array([100, 500, 1000, 5000])
CoreSpreadEddyVisc = np.outer(np.ones(len(WS)), np.array([100, 500, 1000, 5000]))
study6 = {
        'param'                         : 'CoreSpreadEddyVisc',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : np.outer(DTfvw_cvg[[1, -1]], np.ones(len(CSEV))),
        'nNWPanel'                      : np.outer(nNWPanel_cvg[[1, -1]], np.ones(len(CSEV))),
        'WakeLength'                    : WakeLength,
        'WakeRegFactor'                 : np.outer(WakeRegFactor_cvg[[1, -1]], np.ones(len(CSEV))),
        'WingRegFactor'                 : np.outer(WingRegFactor_cvg[[1, -1]], np.ones(len(CSEV))),
        'CoreSpreadEddyVisc'            : CoreSpreadEddyVisc
}

"""test study: WakeLength """
WakeLength = np.round(FWE[-4:]*rotSpd[0]/WS[0]/dpsi[0], decimals=0)
test_study = {
        'param'                         : 'TEST',
        'WS'                            : WS[0] * np.ones(len(WakeLength)),
        'RPM'                           : RPM[0] * np.ones(len(WakeLength)),
        'pitch'                         : Pitch[0] * np.ones(len(WakeLength)),
        'DTfvw'                         : DTfvw[0, 0] * np.ones(len(WakeLength)),
        'nNWPanel'                      : np.round(NWE[-1]/DTfvw[0, 0]/rotSpd[0], decimals=0) * np.ones(len(WakeLength)),
        'WakeLength'                    : np.round(WakeLength, decimals=0),
        'WakeRegFactor'                 : WakeRegFactor_default * np.ones(len(WakeLength)),
        'WingRegFactor'                 : WingRegFactor_default * np.ones(len(WakeLength)),
        'CoreSpreadEddyVisc'            : CoreSpreadEddyVisc_default * np.ones(len(WakeLength))
}

def calc_sim_times(paramfull, plot):
    """calculate and plot simulation times for each run"""
    param = paramfull.split('_', 1)[0]
    timefile = './BAR_02_discretization_inputs/'+param+'/times.txt'
    runsfile = './BAR_02_discretization_inputs/'+param+'/runs.txt'
    CPU_hrs = []
    ws = []
    val = []
    """extract values to plot"""
    data = pd.read_csv(timefile, delimiter=r"\s+", header=None)
    data.columns = ['fname','-','-','-','time','unit']
    for row in data.iterrows():
            if row[1]['unit'] == 'minutes':
                    CPU_hrs = CPU_hrs + [row[1]['time']/60]
            elif row[1]['unit'] == 'hours':
                    CPU_hrs = CPU_hrs + [row[1]['time']]
            elif row[1]['unit'] == 'days':
                    CPU_hrs = CPU_hrs + [row[1]['time']*24]
    runs = pd.read_csv(runsfile, delimiter=r"\s+", header=None)
    runs = runs.iloc[:, -1]
    for run in runs:
            numbers = re.findall(r'\d+(?:\.\d+)?', run)
            ws += [int(numbers[0])]
            val += [float(numbers[1])]
    ws = np.array(ws)
    wsuq = np.unique(ws)

    """plot stuff"""
    fig, ax = plt.subplots(1, figsize=(8.5, 11))
    for w in wsuq:
            idxs = np.where(ws==w)[0]
            idxs = idxs.tolist()
            CPU_hrs_i = [CPU_hrs[i] for i in idxs]
            val_i = [val[i] for i in idxs]
            ax.scatter(val_i, CPU_hrs_i, marker='o', label='WS = {:}'.format(w))
    ax.set_title('Simulation Time', fontsize=10)
    ax.grid()
    ax.legend(loc='best')
    ax.set_ylabel('CPU hours')
    ax.set_xlabel(paramfull)
    if plot == 1:
        plt.show()
        plt.close()
    elif plot == 2:
        plot_name = "PostPro/" + paramfull + '/' + param + "_simtime" + ".pdf"
        plt.savefig(plot_name, bbox_inches='tight')

calc_sim_times('DTfvw_[s]', 2)
