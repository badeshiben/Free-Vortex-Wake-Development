import numpy as np

""" study 1: DTfvw """
WS = [4, 6, 8, 10, 12]
RPM = np.array([4, 5.5, 7.5, 7.84, 7.85])
rotSpd = RPM * 0.104719755  # rad/s
dpsi = np.array([2.5, 5, 7.5, 10, 12.5, 15]) * np.pi / 180  # rad
Pitch = [0, 0, 0, 6, 10]  # deg
DTfvw = np.round(np.outer(1/rotSpd, dpsi), decimals=3)
study1 = {
        'param' : 'DTfvw',
        'WS'    : WS,
        'RPM'   : RPM,
        'pitch' : Pitch,
        'values': DTfvw
    }

"""study 2: nNWpanel """
NWE = np.array([30, 60, 120, 180, 240, 300, 360, 540, 720, 1080, 1440, 1800, 2160, 2520]) * np.pi / 180
DTfvw = 0.2165*np.ones(5)  # TODO from previous study
prod = DTfvw * rotSpd
nNWPanel = np.round(np.outer(1/prod, NWE), decimals=3)
study2 = {
        'param' : 'nNWPanel',
        'WS'    : WS,
        'RPM'   : RPM,
        'pitch' : Pitch,
        'values': nNWPanel
    }

"""study 3: WakeLength"""
FWE = np.array([231, 308, 385, 462, 539, 616, 693, 770, 847, 924])  # m
dpsi = .1745*np.ones(5)  # TODO from previous study
part = rotSpd / WS / dpsi
WakeLength = np.round(np.outer(part, FWE), decimals=3)
study3 = {
        'param' : 'WakeLength',
        'WS'    : WS,
        'RPM'   : RPM,
        'pitch' : Pitch,
        'values': WakeLength
    }

"""study 4: WakeRegFactor"""
WakeRegFactor = np.outer(np.ones(len(WS)), np.array([0, 0.1, 0.5, 1, 1.5, 2, 2.5, 3, 5]))
study4 = {
        'param' : 'WakeRegFactor',
        'WS'    : WS,
        'RPM'   : RPM,
        'pitch' : Pitch,
        'values': WakeRegFactor
    }

"""study 5: WingRegFactor"""
WingRegFactor = np.outer(np.ones(len(WS)), np.array([0, 0.1, 0.5, 1, 1.5, 2, 2.5, 3, 5]))
study5 = {
        'param' : 'WingRegFactor',
        'WS'    : WS,
        'RPM'   : RPM,
        'pitch' : Pitch,
        'values': WingRegFactor
    }
"""study 6: """
WS = [4, 12]
RPM = np.array([4, 7.85])
rotSpd = RPM * 0.104719755  # rad/s
Pitch = [0, 10]  # deg
CoreSpreadEddyVisc = np.outer(np.ones(len(WS)), np.array([100, 500, 1000, 5000]))
study6 = {
        'param' : 'CoreSpreadEddyVisc',
        'WS'    : WS,
        'RPM'   : RPM,
        'pitch' : Pitch,
        'values': CoreSpreadEddyVisc
    }