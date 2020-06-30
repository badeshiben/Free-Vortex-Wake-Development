import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fastlib
import weio




# # --- Plotting mean quantities
# def plotme(study, WS, output, df):
#     """plot discretization study results
#     Input wind speed range, study, output to plot, and df to use"""
""" PLOTTING MEAN QUANTITIES """

####################################################################################################################

""" RAW DATA """
def resolution_raw(varying, WS, plot):
    """
    Parameters
    ----------
    varying:    parameter varied in study
    WS:         list of wind speeds [m/s]
    plot:       plot options. [0, 1, 2] - [no plot, show plot, save plot]

    Returns
    -------
    plots results vs resolution

    """
    fig, ax = plt.subplots(6, 3, sharey=False, sharex = True, figsize=(10, 10))  # (6.4,4.8)
    for ws in WS:
        df = pd.read_csv('Results_ws{:04.1f}.csv'.format(ws),sep='\t')
        """ Deflections"""
        ax[0, 0].set_ylabel('Deflection [m]')
        ax[0, 0].plot(df[varying], df['OoPDefl1_[m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[0, 0].text(.5, .5, 'OoPDefl1', transform=ax[0, 0].transAxes)
        ax[0, 1].plot(df[varying], df['IPDefl1_[m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[0, 1].text(.5, .5, 'IPDefl1', transform=ax[0, 1].transAxes)
        ax[0, 2].plot(df[varying], df['TTDspFA_[m]'], 'o-', label='WS = {:}'.format(ws))
        ax[0, 2].text(.5, .5, 'TTDspFA', transform=ax[0, 2].transAxes)
        """Blade root moments"""
        ax[1, 0].set_ylabel('Moment [kN-m]')
        ax[1, 0].plot(df[varying], df['RootMxb1_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[1, 0].text(.5, .5, 'RootMxb1', transform=ax[1, 0].transAxes)
        ax[1, 1].plot(df[varying], df['RootMyb1_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[1, 1].text(.5, .5, 'RootMyb1', transform=ax[1, 1].transAxes)
        ax[1, 2].plot(df[varying], df['RootMzb1_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[1, 2].text(.5, .5, 'RootMzb1', transform=ax[1, 2].transAxes)
        """LSS moments"""
        ax[2, 0].set_ylabel('Moment [kN-m]')
        ax[2, 0].plot(df[varying], df['RotTorq_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[2, 0].text(.5, .5, 'RotTorq', transform=ax[2, 0].transAxes)
        ax[2, 1].plot(df[varying], df['LSSGagMya_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[2, 1].text(.5, .5, 'LSSGagMya', transform=ax[2, 1].transAxes)
        ax[2, 2].plot(df[varying], df['LSSGagMza_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[2, 2].text(.5, .5, 'LSSGagMza', transform=ax[2, 2].transAxes)
        """Tower top moments"""
        ax[3, 0].set_ylabel('Moment [kN-m]')
        ax[3, 0].plot(df[varying], df['YawBrMxp_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[3, 0].text(.5, .5, 'YawBrMxp', transform=ax[3, 0].transAxes)
        ax[3, 1].plot(df[varying], df['YawBrMyp_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[3, 1].text(.5, .5, 'YawBrMyp', transform=ax[3, 1].transAxes)
        ax[3, 2].plot(df[varying], df['YawBrMzp_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[3, 2].text(.5, .5, 'YawBrMzp', transform=ax[3, 2].transAxes)
        """Tower base moments"""
        ax[4, 0].set_ylabel('Moment [kN-m]')
        ax[4, 0].plot(df[varying], df['TwrBsMxt_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[4, 0].text(.5, .5, 'TwrBsMxt', transform=ax[4, 0].transAxes)
        ax[4, 1].plot(df[varying], df['TwrBsMyt_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[4, 1].text(.5, .5, 'TwrBsMyt', transform=ax[4, 1].transAxes)
        ax[4, 1].set_xlabel(varying)
        ax[4, 2].plot(df[varying], df['TwrBsMzt_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[4, 2].text(.5, .5, 'TwrBsMzt', transform=ax[4, 2].transAxes)
        ax[4, 2].set_xlabel(varying)
        """Generator power"""
        ax[5, 0].set_ylabel('Power [kW]')
        ax[5, 0].plot(df[varying], df['GenPwr_[kW]'], 'o-',  label='WS = {:}'.format(ws))
        ax[5, 0].text(.5, .5, 'GenPwr', transform=ax[5, 0].transAxes)
        ax[5, 0].set_xlabel(varying)
    plt.delaxes()
    plt.delaxes()
    ax[5, 0].legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tick_params(direction='in')
    if plot == 1:
        plt.show()
        plt.close()
    elif plot == 2:
        plot_name = "Figures/" + varying + "_raw" + ".pdf"
        plt.savefig(plot_name, bbox_inches='tight')


""" % DIFF VS FINEST RESOLUTION """
def resolution_pDiff(varying, WS, plot):
    """
    Parameters
    ----------
    varying:    parameter varied in study
    WS:         list of wind speeds [m/s]
    plot:       plot options. [0, 1, 2] - [no plot, show plot, save plot]

    Returns
    -------
    plots of % diff between results at current and finest resolution

    """
    fig, ax = plt.subplots(6, 3, sharey=False, sharex=True, figsize=(10, 10))  # (6.4,4.8)
    for ws in WS:
        df = pd.read_csv('Results_ws{:04.1f}.csv'.format(ws), sep='\t')
        n = len(df[varying])
        a = df[varying]
        b = df[varying][n-1]
        df_fine = df.loc[n-1]
        dfpdiff = (df - df_fine) / df_fine * 100
        dfpdiff = dfpdiff.fillna(0)
        """ Deflections"""
        ax[0, 0].set_ylabel('% Difference')
        ax[0, 0].plot(df[varying], dfpdiff['OoPDefl1_[m]'], 'o-', label='WS = {:}'.format(ws))
        ax[0, 0].text(.5, .5, 'OoPDefl1', transform=ax[0, 0].transAxes)
        ax[0, 1].plot(df[varying], dfpdiff['IPDefl1_[m]'], 'o-', label='WS = {:}'.format(ws))
        ax[0, 1].text(.5, .5, 'IPDefl1', transform=ax[0, 1].transAxes)
        ax[0, 2].plot(df[varying], dfpdiff['TTDspFA_[m]'], 'o-', label='WS = {:}'.format(ws))
        ax[0, 2].text(.5, .5, 'TTDspFA', transform=ax[0, 2].transAxes)
        """Blade root moments"""
        ax[1, 0].set_ylabel('% Difference')
        ax[1, 0].plot(df[varying], dfpdiff['RootMxb1_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[1, 0].text(.5, .5, 'RootMxb1', transform=ax[1, 0].transAxes)
        ax[1, 1].plot(df[varying], dfpdiff['RootMyb1_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[1, 1].text(.5, .5, 'RootMyb1', transform=ax[1, 1].transAxes)
        ax[1, 2].plot(df[varying], dfpdiff['RootMzb1_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[1, 2].text(.5, .5, 'RootMzb1', transform=ax[1, 2].transAxes)
        """LSS moments"""
        ax[2, 0].set_ylabel('% Difference')
        ax[2, 0].plot(df[varying], dfpdiff['RotTorq_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[2, 0].text(.5, .5, 'RotTorq', transform=ax[2, 0].transAxes)
        ax[2, 1].plot(df[varying], dfpdiff['LSSGagMya_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[2, 1].text(.5, .5, 'LSSGagMya', transform=ax[2, 1].transAxes)
        ax[2, 2].plot(df[varying], dfpdiff['LSSGagMza_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[2, 2].text(.5, .5, 'LSSGagMza', transform=ax[2, 2].transAxes)
        """Tower top moments"""
        ax[3, 0].set_ylabel('% Difference')
        ax[3, 0].plot(df[varying], dfpdiff['YawBrMxp_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[3, 0].text(.5, .5, 'YawBrMxp', transform=ax[3, 0].transAxes)
        ax[3, 1].plot(df[varying], dfpdiff['YawBrMyp_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[3, 1].text(.5, .5, 'YawBrMyp', transform=ax[3, 1].transAxes)
        ax[3, 2].plot(df[varying], dfpdiff['YawBrMzp_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[3, 2].text(.5, .5, 'YawBrMzp', transform=ax[3, 2].transAxes)
        """Tower base moments"""
        ax[4, 0].set_ylabel('% Difference')
        ax[4, 0].plot(df[varying], dfpdiff['TwrBsMxt_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[4, 0].text(.5, .5, 'TwrBsMxt', transform=ax[4, 0].transAxes)
        ax[4, 1].plot(df[varying], dfpdiff['TwrBsMyt_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[4, 1].text(.5, .5, 'TwrBsMyt', transform=ax[4, 1].transAxes)
        ax[4, 1].set_xlabel(varying)
        ax[4, 2].plot(df[varying], dfpdiff['TwrBsMzt_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[4, 2].text(.5, .5, 'TwrBsMzt', transform=ax[4, 2].transAxes)
        ax[4, 2].set_xlabel(varying)
        """Generator power"""
        ax[5, 0].set_ylabel('% Difference')
        ax[5, 0].plot(df[varying], dfpdiff['GenPwr_[kW]'], 'o-', label='WS = {:}'.format(ws))
        ax[5, 0].text(.5, .5, 'GenPwr', transform=ax[5, 0].transAxes)
        ax[5, 0].set_xlabel(varying)
    plt.delaxes()
    plt.delaxes()
    ax[5, 0].legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tick_params(direction='in')
    if plot == 1:
        plt.show()
        plt.close()
    elif plot == 2:
        plot_name = "Figures/" + varying + "_%diff" + ".pdf"
        plt.savefig(plot_name, bbox_inches='tight')


""" RUN RESOLUTION STUDY """
def run_study(WS, name, values):
    """ run a resolution study
    Parameters
    ----------
    WS:                 list of wind speeds [m/s]
    name:               parameter name to vary
    parameter values:   list of parameter values

    Returns
    -------
    plots of % diff between results at current and finest resolution
    """
    work_dir = 'BAR_02_discretization_inputs/'  # Output folder
    for ws in WS:
        outFiles=[]
        for i, value in enumerate(values):
            case     ='ws{:.0f}_'.format(ws) + name + '{:.3f}'.format(value)
            filename = os.path.join(work_dir, case + '.out')
            outFiles.append(filename)
        dfAvg = fastlib.averagePostPro(outFiles,avgMethod='periods',avgParam=1,ColMap={'WS_[m/s]':'Wind1VelX_[m/s]'})
        dfAvg.insert(0,'Reg_[m]', values)
        # --- Save to csv since step above can be expensive
        dfAvg.to_csv('Results_ws{:04.1f}_'.format(ws) + name + '.csv', sep='\t', index=False)
        #print(dfAvg)
    resolution_raw('Reg_[m]', WS, 2)
    resolution_pDiff('Reg_[m]', WS, 2)
    print('Ran ' + name + ' post processing')


if __name__ == "__main__":
    studies = {
        'DTfvw': {
            'WS': [4, 6, 8, 10, 12],
            'param': 'DTfvw',
            'values': np.linspace(0.5, 5, 3)
        }
    }

    for study in studies:
        run_study(studies[study]['WS'], studies[study]['param'], studies[study]['values'])






    #--- Simple Postprocessing
    # - Open all the output files,
    # - Average the quantities over the last revolution
    # - Return a dataframe, sorted by Wind Speed
    # dfs=[] # results per wind speed
    # Postprocessing files, wind speed per wind speed
































# fig,ax = plt.subplots(1, 1, sharey=False, figsize=(6.4,4.8)) # (6.4,4.8)
# fig.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.11, hspace=0.20, wspace=0.20)
# for ws in WS:
#     df = pd.read_csv('Results_ws{:04.1f}.csv'.format(ws),sep='\t')
#     num_plots = 7
#     tags = 420 + np.linspace(1,7,7)
#     ax.plot(df['Reg_[m]'], df['OoPDefl1_[m]'], 'o-',  label='WS = {:}'.format(ws))
#     ax.plot(df['Reg_[m]'], df['IPDefl1_[m]'], 'o-', label='WS = {:}'.format(ws))
#     ax.plot(df['Reg_[m]'], df['TTDspFA_[m]'], 'o-',  label='WS = {:}'.format(ws))
#     ax.plot(df['Reg_[m]'], df['RootMyb1_[kN-m]'], 'o-', label='WS = {:}'.format(ws))  # in plane
#     ax.plot(df['Reg_[m]'], df['RootMyb1_[kN-m]'], 'o-', label='WS = {:}'.format(ws))  # out of plane
#     ax.plot(df['Reg_[m]'], df['RootMzb1_[kN-m]'], 'o-', label='WS = {:}'.format(ws))  # pitching
#     ax.plot(df['Reg_[m]'], df['RotTorq_[kN-m]'], 'o-', label='WS = {:}'.format(ws))  # LSS torque @ main bearing
#     ax.plot(df['Reg_[m]'], df['LSSGagMya_[kN-m]'], 'o-', label='WS = {:}'.format(ws))  # LSS bending y @ main bearing
#     ax.plot(df['Reg_[m]'], df['LSSGagMza_[kN-m]'], 'o-', label='WS = {:}'.format(ws))  # LSS bending z @ main bearing
#     ax.plot(df['Reg_[m]'], df['YawBrMxp_[kN-m]'], 'o-', label='WS = {:}'.format(ws))  # TT SS moment
#     ax.plot(df['Reg_[m]'], df['YawBrMyp_[kN-m]'], 'o-', label='WS = {:}'.format(ws))  # TT FA moment
#     ax.plot(df['Reg_[m]'], df['YawBrMzp_[kN-m]'], 'o-', label='WS = {:}'.format(ws))  # TT yaw moment
#     ax.plot(df['Reg_[m]'], df['TwrBsMxt_[kN-m]'], 'o-', label='WS = {:}'.format(ws))  # TB SS moment
#     ax.plot(df['Reg_[m]'], df['TwrBsMyt_[kN-m]'], 'o-', label='WS = {:}'.format(ws))  # TB FA moment
#     ax.plot(df['Reg_[m]'], df['TwrBsMzt_[kN-m]'], 'o-', label='WS = {:}'.format(ws))  # TB yaw moment
#     ax.plot(df['Reg_[m]'], df['GenPwr_[kW]'], 'o-', label='WS = {:}'.format(ws))  # Electrical Generator Power
# ax.set_xlabel('Reg. param [m]')
# ax.set_ylabel('Thrust [kN]')
# ax.legend()
# ax.tick_params(direction='in')
# plt.show()