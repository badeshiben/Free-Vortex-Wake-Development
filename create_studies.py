import numpy as np

""" DEFAULTS """
dpsi_default = 10*np.pi/180  # rad
wakeLengthD = 6
rot_D = 102.996267808408*2 # m
nearWakeExtent = 540*np.pi/180  # rad
WS = [4, 6, 8, 10, 12]
RPM = np.array([4, 5.5, 7.5, 7.84, 7.85])
rotSpd = RPM * 0.104719755  # rad/s
Pitch = [0, 0, 0, 6, 10]  # deg
DTfvw_default = np.round(dpsi_default/rotSpd, decimals=3) # sec
nNWPanel_default = np.round(nearWakeExtent/(DTfvw_default * rotSpd), decimals=0)
FWE = wakeLengthD * rot_D # m
WakeLength_default = np.round(FWE * rotSpd/WS/dpsi_default, decimals=0)  # Npanels
WakeRegFactor_default = 3
WingRegFactor_default = 3
CoreSpreadEddyVisc_default = 100

DTfvw_cvg = np.ones(5)  # TODO
dpsi_cvg = np.ones(5)  # TODO
nNWPanel_cvg = np.ones(5)  # TODO
nNWPanel_cvg = np.ones(5)  # TODO
nNWPanel_cvg = np.ones(5)  # TODO
WakeLength_cvg = np.ones(5)  # TODO
WakeRegFactor_cvg = np.ones(5)  # TODO
WingRegFactor_cvg = np.ones(5)  # TODO


""" study 1: DTfvw """
dpsi = np.array([2.5, 5, 7.5, 10, 12.5, 15]) * np.pi / 180  # rad

DTfvw = np.round(np.outer(1/rotSpd, dpsi), decimals=3)
study1 = {
        'param'                         : 'DTfvw',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : DTfvw,
        'nNWPanel'                      : nNWPanel_default,
        'WakeLength'                    : WakeLength_default,
        'WakeRegFactor_default'         : WakeRegFactor_default * np.ones(len(WS)),
        'WingRegFactor_default'         : WingRegFactor_default * np.ones(len(WS)),
        'CoreSpreadEddyVisc_default'    : CoreSpreadEddyVisc_default * np.ones(len(WS))
    }

"""study 2: nNWpanel """
NWE = np.array([30, 60, 120, 180, 240, 300, 360, 540, 720, 1080, 1440, 1800, 2160, 2520]) * np.pi / 180
prod = DTfvw_cvg * rotSpd
nNWPanel = np.round(np.outer(1/prod, NWE), decimals=0)
study2 = {
        'param'                         : 'nNWPanel',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : DTfvw_cvg,
        'nNWPanel'                      : nNWPanel,
        'WakeLength'                    : WakeLength_default,
        'WakeRegFactor_default'         : WakeRegFactor_default * np.ones(len(WS)),
        'WingRegFactor_default'         : WingRegFactor_default * np.ones(len(WS)),
        'CoreSpreadEddyVisc_default'    : CoreSpreadEddyVisc_default * np.ones(len(WS))
}

"""study 3: WakeLength"""
FWE = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) * rot_D  # m
part = rotSpd / WS / dpsi_cvg
WakeLength = np.round(np.outer(part, FWE), decimals=0)
study3 = {
        'param'                         : 'WakeLength',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : DTfvw_cvg,
        'nNWPanel'                      : nNWPanel_cvg,
        'WakeLength'                    : WakeLength,
        'WakeRegFactor_default'         : WakeRegFactor_default * np.ones(len(WS)),
        'WingRegFactor_default'         : WingRegFactor_default * np.ones(len(WS)),
        'CoreSpreadEddyVisc_default'    : CoreSpreadEddyVisc_default * np.ones(len(WS))
}

"""study 4: WakeRegFactor"""
WakeRegFactor = np.outer(np.ones(len(WS)), np.array([0, 0.1, 0.5, 1, 1.5, 2, 2.5, 3, 5]))
study4 = {
        'param'                         : 'WakeRegFactor',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : DTfvw_cvg,
        'nNWPanel'                      : nNWPanel_cvg,
        'WakeLength'                    : WakeLength_cvg,
        'WakeRegFactor_default'         : WakeRegFactor,
        'WingRegFactor_default'         : WingRegFactor_default * np.ones(len(WS)),
        'CoreSpreadEddyVisc_default'    : CoreSpreadEddyVisc_default * np.ones(len(WS))
}


"""study 5: WingRegFactor"""
WingRegFactor = np.outer(np.ones(len(WS)), np.array([0, 0.1, 0.5, 1, 1.5, 2, 2.5, 3, 5]))
study5 = {
        'param'                         : 'WingRegFactor',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : DTfvw_cvg,
        'nNWPanel'                      : nNWPanel_cvg,
        'WakeLength'                    : WakeLength_cvg,
        'WakeRegFactor_default'         : WakeRegFactor_cvg,
        'WingRegFactor_default'         : WingRegFactor,
        'CoreSpreadEddyVisc_default'    : CoreSpreadEddyVisc_default * np.ones(len(WS))
}
"""study 6: """
WS = [4, 12]
RPM = np.array([4, 7.85])
rotSpd = RPM * 0.104719755  # rad/s
Pitch = [0, 10]  # deg
CoreSpreadEddyVisc = np.outer(np.ones(len(WS)), np.array([100, 500, 1000, 5000]))
study6 = {
        'param'                         : 'CoreSpreadEddyVisc',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : DTfvw_cvg[[1, -1]],
        'nNWPanel'                      : nNWPanel_cvg[[1, -1]],
        'WakeLength'                    : WakeLength_cvg[[1, -1]],
        'WakeRegFactor_default'         : WakeRegFactor_cvg[[1, -1]],
        'WingRegFactor_default'         : WingRegFactor_cvg[[1, -1]],
        'CoreSpreadEddyVisc_default'    : CoreSpreadEddyVisc
}
m=0
n = m+1