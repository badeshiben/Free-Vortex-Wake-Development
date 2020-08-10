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

# TODO make arrays of vectors.....
""" study 1: DTfvw """
dpsi = np.array([2.5, 5, 7.5, 10, 12.5, 15]) * np.pi / 180  # rad

DTfvw = np.round(np.outer(1/rotSpd, dpsi), decimals=3)
study1 = {
        'param'                         : 'DTfvw',
        'paramfull'                     : 'DTfvw_[s]',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : DTfvw,
        'nNWPanel'                      : np.outer(nNWPanel_default, np.ones(len(dpsi))),
        'WakeLength'                    : np.outer(WakeLength_default, np.ones(len(dpsi))),
        'WakeRegFactor'                 : WakeRegFactor_default * np.ones([len(WS), len(dpsi)]),
        'WingRegFactor'                 : WingRegFactor_default * np.ones([len(WS), len(dpsi)]),
        'CoreSpreadEddyVisc'            : CoreSpreadEddyVisc_default * np.ones([len(WS), len(dpsi)]),
        'TMax'                          : 400
}
study1Maxtime = np.max(WakeLength_default)/np.min(WS)+200
# rounding up study 1 max time to 400s

"""study 2: nNWpanel """
NWE = np.array([30, 60, 120, 180, 240, 300, 360, 540, 720, 1080, 1440, 1800, 2160, 2520]) * np.pi / 180
prod = DTfvw_cvg * rotSpd
nNWPanel = np.round(np.outer(1/prod, NWE), decimals=0)
WakeLength_rev = np.round(FWE*rotSpd/WS/dpsi_cvg, decimals=0)  # Npanels# revised wakelength based on dpsi_cvg
study2 = {
        'param'                         : 'nNWPanel',
        'WS'                            : WS,
        'RPM'                           : RPM,
        'pitch'                         : Pitch,
        'DTfvw'                         : np.outer(DTfvw_cvg, np.ones(len(NWE))),
        'nNWPanel'                      : nNWPanel,
        'WakeLength'                    : np.outer(WakeLength_rev, np.ones(len(NWE))),
        'WakeRegFactor'                 : WakeRegFactor_default * np.ones([len(WS), len(NWE)]),
        'WingRegFactor'                 : WingRegFactor_default * np.ones([len(WS), len(NWE)]),
        'CoreSpreadEddyVisc'            : CoreSpreadEddyVisc_default * np.ones([len(WS), len(NWE)])
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
        'DTfvw'                         : np.outer(DTfvw_cvg, np.ones(len(FWE))),
        'nNWPanel'                      : np.outer(nNWPanel_cvg, np.ones(len(FWE))),
        'WakeLength'                    : WakeLength,
        'WakeRegFactor'                 : WakeRegFactor_default * np.ones([len(WS), len(FWE)]),
        'WingRegFactor'                 : WingRegFactor_default * np.ones([len(WS), len(FWE)]),
        'CoreSpreadEddyVisc'            : CoreSpreadEddyVisc_default * np.ones([len(WS), len(FWE)])
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
"""study 4: WakeRegFactor"""
WaRF = np.array([0, 0.1, 0.5, 1, 1.5, 2, 2.5, 3, 5])
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
        'CoreSpreadEddyVisc'            : CoreSpreadEddyVisc_default * np.ones([len(WS), len(WaRF)])
}


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


m=0
n = m+1