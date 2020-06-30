import numpy as np

""" study 1: DTfvw """
WS = [4, 6, 8, 10, 12]
RPM = np.array([3.894, 5.846, 7.771, 7.881, 7.881])
rotSpd = RPM * 0.104719755  # rad/s
dpsi = np.array([2.5, 5, 7.5, 10, 12.5, 15]) * np.pi / 180  # rad
Pitch = [0, 0, 0, 6.585, 10.161]  # deg
DTfvw = np.outer(dpsi, rotSpd).tolist()
study1 = {
        'param' : 'DTfvw',
        'WS'    : WS,
        'RPM'   : RPM,
        'pitch' : Pitch,
        'values': DTfvw
    }

"""study 2: nNWpanel """
NWE = np.array([30, 60, 120, 180, 240, 300, 360, 540, 720, 1080, 1440, 1800, 2160, 2520]) * np.pi / 180
DTfvw = np.array([1, 1, 1, 1, 2])  # TODO from previous study
prod = DTfvw * rotSpd
nNWPanel = np.outer(NWE, 1 / prod).tolist()
study2 = {
        'param' : 'nNWPanel',
        'WS'    : WS,
        'RPM'   : RPM,
        'pitch' : Pitch,
        'values': DTfvw
    }

"""study 3: WakeLength"""
FWE = np.array([231, 308, 385, 462, 539, 616, 693, 770, 847, 924])  # m
dpsi = np.array([1, 1, 1, 1, 2])  # TODO from previous study
nNWPanel = [1, 1, 1, 1, 1]  # todo from previous study
part = rotSpd / WS / dpsi
WakeLength = np.outer(FWE, part).tolist()
study3 = {
        'param' : 'WakeLength',
        'WS'    : WS,
        'RPM'   : RPM,
        'pitch' : Pitch,
        'values': DTfvw
    }

"""study 4: WakeRegFactor"""
WakeRegFactor = [0, 0.1, 0.5, 1, 1.5, 2, 2.5, 3, 5]
study4 = {
        'param' : 'WakeRegFactor',
        'WS'    : WS,
        'RPM'   : RPM,
        'pitch' : Pitch,
        'values': DTfvw
    }

"""study 5: WingRegFactor"""
WingRegFactor = [0, 0.1, 0.5, 1, 1.5, 2, 2.5, 3, 5]
WakeRegFactor = 2 #todo from previous study
study5 = {
        'param' : 'WingRegFactor',
        'WS'    : WS,
        'RPM'   : RPM,
        'pitch' : Pitch,
        'values': DTfvw
    }
"""study 6: """
WS = [4, 12]
RPM = np.array([3.894, 7.881])
rotSpd = RPM * 0.104719755  # rad/s
Pitch = [0, 0.161]  # deg
CoreSpreadEddyVisc = [100, 500, 1000, 5000]
study6 = {
        'param' : 'CoreSpreadEddyVisc',
        'WS'    : WS,
        'RPM'   : RPM,
        'pitch' : Pitch,
        'values': DTfvw
    }