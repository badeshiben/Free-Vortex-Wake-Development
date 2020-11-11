import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fastlib
from create_studies import study1, study2, study3, study4, study5, study6
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
    outputs:    list of fastlib df output names [str]

    Returns
    -------
    plots results vs resolution

    """
    # outputs = ['OoPDefl1_[m]', 'IPDefl1_[m]', 'TTDspFA_[m]', 'RootMxb1_[kN-m]', 'RootMyb1_[kN-m]', 'RootMzb1_[kN-m]',\
    #            'RotTorq_[kN-m]', 'LSSGagMya_[kN-m]', 'LSSGagMza_[kN-m]', 'YawBrMxp_[kN-m]', 'YawBrMyp_[kN-m]',\
    #            'YawBrMzp_[kN-m]', 'TwrBsMxt_[kN-m]', 'TwrBsMyt_[kN-m]', 'TwrBsMzt_[kN-m]', 'GenPwr_[kW]', 'RotTorq_[kN-m]']
    # nplots = len(outputs)
    fig, ax = plt.subplots(6, 3, sharey=False, sharex = True, figsize=(15, 20))  # (6.4,4.8)
    for ws in WS:
        df = pd.read_csv('Results_ws{:04.1f}.csv'.format(ws),sep='\t')
        oo = df[['OoPDefl1_[m]', 'IPDefl1_[m]']]
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
        ax[4, 2].plot(df[varying], df['TwrBsMzt_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[4, 2].text(.5, .5, 'TwrBsMzt', transform=ax[4, 2].transAxes)
        ax[4, 2].set_xlabel(varying)
        """Generator power"""
        ax[5, 0].set_ylabel('Power [kW]')
        ax[5, 0].plot(df[varying], df['GenPwr_[kW]'], 'o-',  label='WS = {:}'.format(ws))
        ax[5, 0].text(.5, .5, 'GenPwr', transform=ax[5, 0].transAxes)
        ax[5, 0].set_xlabel(varying)
        """Generator torque"""
        ax[5, 1].set_ylabel('Torque [kN-m]')
        ax[5, 1].plot(df[varying], df['GenTq_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[5, 1].text(.5, .5, 'GenTq', transform=ax[5, 1].transAxes)
        ax[5, 1].set_xlabel(varying)
    plt.delaxes()
    ax[5, 1].legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tick_params(direction='in')
    if plot == 1:
        plt.show()
        plt.close()
    elif plot == 2:
        plot_name = "Figures/" + varying + "_raw" + ".pdf"
        plt.savefig(plot_name, bbox_inches='tight')

""" DIFF VS FINEST RESOLUTION """
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
    fig, ax = plt.subplots(6, 3, sharey=False, sharex=True, figsize=(15, 20))  # (6.4,4.8)
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
        ax[4, 2].plot(df[varying], dfpdiff['TwrBsMzt_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[4, 2].text(.5, .5, 'TwrBsMzt', transform=ax[4, 2].transAxes)
        ax[4, 2].set_xlabel(varying)
        """Generator power"""
        ax[5, 0].set_ylabel('% Difference')
        ax[5, 0].plot(df[varying], dfpdiff['GenPwr_[kW]'], 'o-', label='WS = {:}'.format(ws))
        ax[5, 0].text(.5, .5, 'GenPwr', transform=ax[5, 0].transAxes)
        ax[5, 0].set_xlabel(varying)
        """Generator torque"""
        ax[5, 1].set_ylabel('Torque [kN-m]')
        ax[5, 1].plot(df[varying], df['GenTq_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[5, 1].text(.5, .5, 'GenTq', transform=ax[5, 1].transAxes)
        ax[5, 1].set_xlabel(varying)
    plt.delaxes()
    ax[5, 1].legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tick_params(direction='in')
    if plot == 1:
        plt.show()
        plt.close()
    elif plot == 2:
        plot_name = "Figures/" + varying + "_%diff" + ".pdf"
        plt.savefig(plot_name, bbox_inches='tight')

""" PLOT OUTPUTS ALONG BLADE SPAN, VARYING PARAMS """
def spanwise_vary_param(varying, WS, plot):
    """
    Parameters
    ----------
    varying:    parameter varied in study
    WS:         single chosen wind speeds [m/s]
    plot:       plot options. [0, 1, 2] - [no plot, show plot, save plot]

    Returns
    -------
    plots outputs along blade span
    """

    fig, ax = plt.subplots(4, 2, sharey=False, sharex=True, figsize=(15, 20))
    norm_node_r = np.linspace(0, 1, 9)
    df = pd.read_csv('Results_ws{:04.1f}'.format(WS) + '_' + varying + '.csv', sep='\t')
    AxInd = df[['B1N1AxInd', 'B1N2AxInd', 'B1N3AxInd', 'B1N4AxInd', 'B1N5AxInd', 'B1N6AxInd', 'B1N7AxInd', 'B1N8AxInd', 'B1N9AxInd']]
    TnInd = df[['B1N1TnInd', 'B1N2TnInd', 'B1N3TnInd', 'B1N4TnInd', 'B1N5TnInd', 'B1N6TnInd', 'B1N7TnInd', 'B1N8TnInd', 'B1N9TnInd']]
    Fn = df[['B1N1Fn', 'B1N2Fn', 'B1N3Fn', 'B1N4Fn', 'B1N5Fn', 'B1N6Fn', 'B1N7Fn', 'B1N8Fn', 'B1N9Fn']]
    Ft = df[['B1N1Ft', 'B1N2Ft', 'B1N3Ft', 'B1N4Ft', 'B1N5Ft', 'B1N6Ft', 'B1N7Ft', 'B1N8Ft', 'B1N9Ft']]
    Fl = df[['B1N1Fl', 'B1N2Fl', 'B1N3Fl', 'B1N4Fl', 'B1N5Fl', 'B1N6Fl', 'B1N7Fl', 'B1N8Fl', 'B1N9Fl']]
    Fd = df[['B1N1Fd', 'B1N2Fd', 'B1N3Fd', 'B1N4Fd', 'B1N5Fd', 'B1N6Fd', 'B1N7Fd', 'B1N8Fd', 'B1N9Fd']]
    Circ = df[['Gam1B1', 'Gam2B1', 'Gam3B1', 'Gam4B1', 'Gam5B1', 'Gam6B1', 'Gam7B1', 'Gam8B1', 'Gam9B1']]

    for i in range(0, len(df['B1N1Fn'])):
        ax[0, 0].set_ylabel('Axial Induction')
        ax[0, 0].plot(norm_node_r, AxInd[i, :], 'o-', label='WS = {:}'.format(WS))
        ax[0, 1].set_ylabel('Tangential Induction')
        ax[0, 1].plot(norm_node_r, TnInd[i, :], 'o-', label='WS = {:}'.format(WS))
        ax[1, 0].set_ylabel('Normal Force [N]')
        ax[1, 0].plot(norm_node_r, Fn[i, :], 'o-', label='WS = {:}'.format(WS))
        ax[1, 1].set_ylabel('Tangential Force [N]')
        ax[1, 1].plot(norm_node_r, Ft[i, :], 'o-', label='WS = {:}'.format(WS))
        ax[2, 0].set_ylabel('Lift Force [N]')
        ax[2, 0].plot(norm_node_r, Fl[i, :], 'o-', label='WS = {:}'.format(WS))
        ax[2, 1].set_ylabel('Drag Force [N]')
        ax[2, 1].plot(norm_node_r, Fd[i, :], 'o-', label='WS = {:}'.format(WS))
        ax[3, 0].set_ylabel('Circulation')
        ax[3, 0].plot(norm_node_r, Fl[i, :], 'o-', label='WS = {:}'.format(WS))

        ax[3, 0].legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.tick_params(direction='in')

    if plot == 1:
        plt.show()
        plt.close()
    elif plot == 2:
        plot_name = "Figures/" + 'SPANWISE_' + varying + "_ws{:04.1f}".format(WS) + ".pdf"
        plt.savefig(plot_name, bbox_inches='tight')

""" PLOT OUTPUTS ALONG BLADE SPAN, VARYING WS """
def spanwise_vary_WS(param, value, WS, plot):
    """
    Parameters
    ----------
    param:      param to use
    value:      single param value
    WS:         list of wind speeds [m/s]
    plot:       plot options. [0, 1, 2] - [no plot, show plot, save plot]

    Returns
    -------
    plots outputs along blade span
    """

    fig, ax = plt.subplots(4, 2, sharey=False, sharex=True, figsize=(15, 20))
    norm_node_r = np.linspace(0, 1, 9)
    for ws in WS:
        df = pd.read_csv('Results_ws{:04.1f}'.format(ws) + '_' + param + '.csv', sep='\t')
        AxInd = df[['B1N1AxInd', 'B1N2AxInd', 'B1N3AxInd', 'B1N4AxInd', 'B1N5AxInd', 'B1N6AxInd', 'B1N7AxInd', 'B1N8AxInd', 'B1N9AxInd']]
        TnInd = df[['B1N1TnInd', 'B1N2TnInd', 'B1N3TnInd', 'B1N4TnInd', 'B1N5TnInd', 'B1N6TnInd', 'B1N7TnInd', 'B1N8TnInd', 'B1N9TnInd']]
        Fn = df[['B1N1Fn', 'B1N2Fn', 'B1N3Fn', 'B1N4Fn', 'B1N5Fn', 'B1N6Fn', 'B1N7Fn', 'B1N8Fn', 'B1N9Fn']]
        Ft = df[['B1N1Ft', 'B1N2Ft', 'B1N3Ft', 'B1N4Ft', 'B1N5Ft', 'B1N6Ft', 'B1N7Ft', 'B1N8Ft', 'B1N9Ft']]
        Fl = df[['B1N1Fl', 'B1N2Fl', 'B1N3Fl', 'B1N4Fl', 'B1N5Fl', 'B1N6Fl', 'B1N7Fl', 'B1N8Fl', 'B1N9Fl']]
        Fd = df[['B1N1Fd', 'B1N2Fd', 'B1N3Fd', 'B1N4Fd', 'B1N5Fd', 'B1N6Fd', 'B1N7Fd', 'B1N8Fd', 'B1N9Fd']]
        Circ = df[['Gam1B1', 'Gam2B1', 'Gam3B1', 'Gam4B1', 'Gam5B1', 'Gam6B1', 'Gam7B1', 'Gam8B1', 'Gam9B1']]

        i = df.index[df[[param] == value]]
        ax[0, 0].set_ylabel('Axial Induction')
        ax[0, 0].plot(norm_node_r, AxInd[i, :], 'o-', label='ws = {:}'.format(ws))
        ax[0, 1].set_ylabel('Tangential Induction')
        ax[0, 1].plot(norm_node_r, TnInd[i, :], 'o-', label='ws = {:}'.format(ws))
        ax[1, 0].set_ylabel('Normal Force [N]')
        ax[1, 0].plot(norm_node_r, Fn[i, :], 'o-', label='ws = {:}'.format(ws))
        ax[1, 1].set_ylabel('Tangential Force [N]')
        ax[1, 1].plot(norm_node_r, Ft[i, :], 'o-', label='ws = {:}'.format(ws))
        ax[2, 0].set_ylabel('Lift Force [N]')
        ax[2, 0].plot(norm_node_r, Fl[i, :], 'o-', label='ws = {:}'.format(ws))
        ax[2, 1].set_ylabel('Drag Force [N]')
        ax[2, 1].plot(norm_node_r, Fd[i, :], 'o-', label='ws = {:}'.format(ws))
        ax[3, 0].set_ylabel('Circulation')
        ax[3, 0].plot(norm_node_r, Fl[i, :], 'o-', label='ws = {:}'.format(ws))

    ax[3, 0].legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tick_params(direction='in')

    if plot == 1:
        plt.show()
        plt.close()
    elif plot == 2:
        plot_name = "Figures/" + 'SPANWISE_' + param + "{:04.1f}".format(value) + ".pdf"
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
    work_dir = '../SampleOutputs'
    for wsp in WS:
        i = WS.index(wsp)
        outFiles=[]
        for val in values:
            case     ='ws{:04.1f}_reg{:.4f}'.format(wsp, val)
            filename = os.path.join(work_dir, case + '.outb')
            outFiles.append(filename)
        dfAvg = fastlib.averagePostPro(outFiles,avgMethod='periods',avgParam=1,ColMap={'WS_[m/s]':'Wind1VelX_[m/s]'})
        dfAvg.insert(0,name, values)
        # --- Save to csv since step above can be expensive
        dfAvg.to_csv('Results_ws{:04.1f}_'.format(wsp) + name + '.csv', sep='\t', index=False)
        #print(dfAvg)
    resolution_raw(name, WS, 2)
    resolution_pDiff(name, WS, 2)
    spanwise_vary_param(name, WS, 2)
    print('Ran ' + name + ' post processing')


if __name__ == "__main__":
    run_study(WS=[5, 10], name='Reg_[m]', values=[.5, 2.75, 5])






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