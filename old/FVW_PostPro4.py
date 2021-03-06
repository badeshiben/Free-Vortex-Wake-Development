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

""" DIFF VS FINEST RESOLUTION non aero quantities """
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

def resolution_pDiff_aero(varying, WS, plot):
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

    outlist = ['B1N001AIn_[-]', 'B1N002AIn_[-]', 'B1N003AIn_[-]', 'B1N004AIn_[-]', 'B1N005AIn_[-]',
               'B1N006AIn_[-]', 'B1N007AIn_[-]', 'B1N008AIn_[-]', 'B1N009AIn_[-]',
               # 'B1N001TnInd', 'B1N002TnInd', 'B1N003TnInd', 'B1N004TnInd', 'B1N005TnInd', 'B1N006TnInd', 'B1N007TnInd', 'B1N008TnInd', 'B1N009TnInd',
               'B1N001Fn_[N/m]', 'B1N002Fn_[N/m]', 'B1N003Fn_[N/m]', 'B1N004Fn_[N/m]', 'B1N005Fn_[N/m]',
               'B1N006Fn_[N/m]', 'B1N007Fn_[N/m]', 'B1N008Fn_[N/m]', 'B1N009Fn_[N/m]',
               'B1N002Ft_[N/m]', 'B1N003Ft_[N/m]', 'B1N004Ft_[N/m]', 'B1N005Ft_[N/m]',
               'B1N001Ft_[N/m]', 'B1N006Ft_[N/m]', 'B1N007Ft_[N/m]', 'B1N008Ft_[N/m]', 'B1N009Ft_[N/m]',
               'B1N001Fl_[N/m]', 'B1N002Fl_[N/m]', 'B1N003Fl_[N/m]', 'B1N004Fl_[N/m]', 'B1N005Fl_[N/m]',
               'B1N006Fl_[N/m]', 'B1N007Fl_[N/m]', 'B1N008Fl_[N/m]', 'B1N009Fl_[N/m]',
               'B1N001Fd_[N/m]', 'B1N002Fd_[N/m]', 'B1N003Fd_[N/m]', 'B1N004Fd_[N/m]', 'B1N005Fd_[N/m]',
               'B1N006Fd_[N/m]', 'B1N007Fd_[N/m]', 'B1N008Fd_[N/m]', 'B1N009Fd_[N/m]',
               'B1N001Gam_[m^2/s]', 'B1N002Gam_[m^2/s]', 'B1N003Gam_[m^2/s]', 'B1N004Gam_[m^2/s]', 'B1N005Gam_[m^2/s]',
               'B1N006Gam_[m^2/s]', 'B1N007Gam_[m^2/s]', 'B1N008Gam_[m^2/s]', 'B1N009Gam_[m^2/s]']
    n_plot = len(outlist)
    n_col = 3
    n_row = int(np.ceil(n_plot/n_col))
    fig, ax = plt.subplots(n_row, n_col, sharey=False, sharex=True, figsize=(8.5, 11))  # (6.4,4.8)

    for ws in WS:
        df = pd.read_csv('Results_ws{:04.1f}.csv'.format(ws), sep='\t')
        n = len(df[varying])
        a = df[varying]
        b = df[varying][n - 1]
        df_fine = df.loc[n - 1]
        dfpdiff = (df - df_fine) / df_fine * 100
        dfpdiff = dfpdiff.fillna(0)
        for i in range(0, n_row):
            for j in range(0, n_col):
                idx = i*n_col + j
                ax[i, j].plot(df[varying], dfpdiff[outlist[idx]], 'o-', label='WS = {:}'.format(ws))
                ax[i, j].text(.5, .5, outlist[idx], transform=ax[i, j].transAxes)
                if j==0:
                    ax[i, j].set_ylabel('% Difference')
                if i==n_row-1:
                    ax[i, j].set_xlabel(varying)
                if (i+1)*(j+1)==len(outlist):
                    ax[i, j].legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.tick_params(direction='in')
    if plot == 1:
        plt.show()
        plt.close()
    elif plot == 2:
        plot_name = "Figures/" + varying + "_%diff_AERO" + ".pdf"
        plt.savefig(plot_name, bbox_inches='tight')

""" PLOT OUTPUTS ALONG BLADE SPAN, VARYING WS and param """
def spanwise_vary_both(param, values, WS, plot):
    """
    Parameters
    ----------
    param:      param to use
    values:      list of param values
    WS:         list of wind speeds [m/s]
    plot:       plot options. [0, 1, 2] - [no plot, show plot, save plot]

    Returns
    -------
    plots outputs along blade span
    """

    fig, ax = plt.subplots(4, 2, sharey=False, sharex=False, figsize=(15, 20))
    norm_node_r = np.linspace(0, 1, 9)
    legend_labels = []
    for ws in WS:
        for value in values:
            df = pd.read_csv('Results_ws{:04.1f}'.format(ws) + '_' + param + '.csv', sep='\t')
            AxInd = df[['B1N001AIn_[-]', 'B1N002AIn_[-]', 'B1N003AIn_[-]', 'B1N004AIn_[-]', 'B1N005AIn_[-]',
                        'B1N006AIn_[-]', 'B1N007AIn_[-]', 'B1N008AIn_[-]', 'B1N009AIn_[-]', ]]
            TnInd = df[['B1N001ApI_[-]', 'B1N002ApI_[-]', 'B1N003ApI_[-]', 'B1N004ApI_[-]', 'B1N005ApI_[-]',
                        'B1N006ApI_[-]', 'B1N007ApI_[-]', 'B1N008ApI_[-]', 'B1N009ApI_[-]', ]]
            Fn = df[['B1N001Fn_[N/m]', 'B1N002Fn_[N/m]', 'B1N003Fn_[N/m]', 'B1N004Fn_[N/m]', 'B1N005Fn_[N/m]',
                     'B1N006Fn_[N/m]', 'B1N007Fn_[N/m]', 'B1N008Fn_[N/m]', 'B1N009Fn_[N/m]']]
            Ft = df[['B1N001Ft_[N/m]', 'B1N002Ft_[N/m]', 'B1N003Ft_[N/m]', 'B1N004Ft_[N/m]', 'B1N005Ft_[N/m]',
                     'B1N006Ft_[N/m]', 'B1N007Ft_[N/m]', 'B1N008Ft_[N/m]', 'B1N009Ft_[N/m]']]
            Fl = df[['B1N001Fl_[N/m]', 'B1N002Fl_[N/m]', 'B1N003Fl_[N/m]', 'B1N004Fl_[N/m]', 'B1N005Fl_[N/m]',
                     'B1N006Fl_[N/m]', 'B1N007Fl_[N/m]', 'B1N008Fl_[N/m]', 'B1N009Fl_[N/m]']]
            Fd = df[['B1N001Fd_[N/m]', 'B1N002Fd_[N/m]', 'B1N003Fd_[N/m]', 'B1N004Fd_[N/m]', 'B1N005Fd_[N/m]',
                     'B1N006Fd_[N/m]', 'B1N007Fd_[N/m]', 'B1N008Fd_[N/m]', 'B1N009Fd_[N/m]']]
            Circ = df[['B1N001Gam_[m^2/s]', 'B1N002Gam_[m^2/s]', 'B1N003Gam_[m^2/s]', 'B1N004Gam_[m^2/s]', 'B1N005Gam_[m^2/s]',
                       'B1N006Gam_[m^2/s]', 'B1N007Gam_[m^2/s]', 'B1N008Gam_[m^2/s]', 'B1N009Gam_[m^2/s]']]

            x = df[param] == value
            i = df.index[df[param] == value][0]
            data = AxInd.iloc[i, :]
            data2 = AxInd.iloc[i]
            ax[0, 0].set_ylabel('Axial Induction')
            ax[0, 0].plot(norm_node_r, AxInd.iloc[i], 'o-', label='ws = {:}'.format(ws))
            ax[0, 1].set_ylabel('Tangential Induction')
            ax[0, 1].plot(norm_node_r, TnInd.iloc[i], 'o-', label='ws = {:}'.format(ws))
            ax[1, 0].set_ylabel('Normal Force [N]')
            ax[1, 0].plot(norm_node_r, Fn.iloc[i], 'o-', label='ws = {:}'.format(ws))
            ax[1, 1].set_ylabel('Tangential Force [N]')
            ax[1, 1].plot(norm_node_r, Ft.iloc[i], 'o-', label='ws = {:}'.format(ws))
            ax[2, 0].set_ylabel('Lift Force [N]')
            ax[2, 0].plot(norm_node_r, Fl.iloc[i], 'o-', label='ws = {:}'.format(ws))
            ax[2, 1].set_ylabel('Drag Force [N]')
            ax[2, 1].plot(norm_node_r, Fd.iloc[i], 'o-', label='ws = {:}'.format(ws))
            ax[3, 0].set_ylabel('Circulation')
            ax[3, 0].plot(norm_node_r, Circ.iloc[i], 'o-', label='ws = {:}'.format(ws))
            legend_labels = legend_labels + [param + " = {:04.3f}".format(value) + '; ws_[m/s] = {:}'.format(ws)]

    ax[3, 0].legend(legend_labels, loc='upper left', bbox_to_anchor=(1, 1))
    ax[0, 0].grid(); ax[0, 1].grid(); ax[1, 0].grid(); ax[1, 1].grid(); ax[2, 0].grid(); ax[2, 1].grid(); ax[3, 0].grid();
    plt.tick_params(direction='in')
    plt.delaxes()
    plt.grid(True)
    if plot == 1:
        plt.show()
        plt.close()
    elif plot == 2:
        plot_name = "Figures/" + 'SPANWISE_' + param + ".pdf"
        # plot_name = "Figures/" + 'SPANWISE_' + param + "{:04.1f}".format(value)  + '_ws{:}'.format(ws) + ".pdf"
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
            case     ='ws{:04.1f}'.format(wsp)+'_'+name+'{:.4f}'.format(val)
            filename = os.path.join(work_dir, case + '.outb')
            outFiles.append(filename)
        dfAvg = fastlib.averagePostPro(outFiles,avgMethod='periods',avgParam=1,ColMap={'WS_[m/s]':'Wind1VelX_[m/s]'})
        dfAvg.insert(0,name, values)
        # --- Save to csv since step above can be expensive
        dfAvg.to_csv('Results_ws{:04.1f}_'.format(wsp) + name + '.csv', sep='\t', index=False)
        #print(dfAvg)
    # resolution_raw(name, WS, 2)
    resolution_pDiff_aero(name, WS, 1)
    # spanwise_vary_both(name, values, WS, 1)
    print('Ran ' + name + ' post processing')


if __name__ == "__main__":
    run_study(WS=[5, 10], name='Reg_[m]', values=[.5, 2.75, 5])

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
        AxInd = df[
            ['B1N001AxInd', 'B1N002AxInd', 'B1N003AxInd', 'B1N004AxInd', 'B1N005AxInd', 'B1N006AxInd', 'B1N007AxInd',
             'B1N008AxInd', 'B1N009AxInd']]
        TnInd = df[
            ['B1N001TnInd', 'B1N002TnInd', 'B1N003TnInd', 'B1N004TnInd', 'B1N005TnInd', 'B1N006TnInd', 'B1N007TnInd',
             'B1N008TnInd', 'B1N009TnInd']]
        Fn = df[['B1N001Fn', 'B1N002Fn', 'B1N003Fn', 'B1N004Fn', 'B1N005Fn', 'B1N006Fn', 'B1N007Fn', 'B1N008Fn',
                 'B1N009Fn']]
        Ft = df[['B1N001Ft', 'B1N002Ft', 'B1N003Ft', 'B1N004Ft', 'B1N005Ft', 'B1N006Ft', 'B1N007Ft', 'B1N008Ft',
                 'B1N009Ft']]
        Fl = df[['B1N001Fl', 'B1N002Fl', 'B1N003Fl', 'B1N004Fl', 'B1N005Fl', 'B1N006Fl', 'B1N007Fl', 'B1N008Fl',
                 'B1N009Fl']]
        Fd = df[['B1N001Fd', 'B1N002Fd', 'B1N003Fd', 'B1N004Fd', 'B1N005Fd', 'B1N006Fd', 'B1N007Fd', 'B1N008Fd',
                 'B1N009Fd']]
        Circ = df[['Gam001B1', 'Gam002B1', 'Gam003B1', 'Gam004B1', 'Gam005B1', 'Gam006B1', 'Gam007B1', 'Gam008B1',
                   'Gam009B1']]

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
            AxInd = df[['B1N001AxInd', 'B1N002AxInd', 'B1N003AxInd', 'B1N004AxInd', 'B1N005AxInd', 'B1N006AxInd',
                        'B1N007AxInd', 'B1N008AxInd', 'B1N009AxInd']]
            TnInd = df[['B1N001TnInd', 'B1N002TnInd', 'B1N003TnInd', 'B1N004TnInd', 'B1N005TnInd', 'B1N006TnInd',
                        'B1N007TnInd', 'B1N008TnInd', 'B1N009TnInd']]
            Fn = df[['B1N001Fn', 'B1N002Fn', 'B1N003Fn', 'B1N004Fn', 'B1N005Fn', 'B1N006Fn', 'B1N007Fn', 'B1N008Fn',
                     'B1N009Fn']]
            Ft = df[['B1N001Ft', 'B1N002Ft', 'B1N003Ft', 'B1N004Ft', 'B1N005Ft', 'B1N006Ft', 'B1N007Ft', 'B1N008Ft',
                     'B1N009Ft']]
            Fl = df[['B1N001Fl', 'B1N002Fl', 'B1N003Fl', 'B1N004Fl', 'B1N005Fl', 'B1N006Fl', 'B1N007Fl', 'B1N008Fl',
                     'B1N009Fl']]
            Fd = df[['B1N001Fd', 'B1N002Fd', 'B1N003Fd', 'B1N004Fd', 'B1N005Fd', 'B1N006Fd', 'B1N007Fd', 'B1N008Fd',
                     'B1N009Fd']]
            Circ = df[['Gam001B1', 'Gam002B1', 'Gam003B1', 'Gam004B1', 'Gam005B1', 'Gam006B1', 'Gam007B1', 'Gam008B1',
                       'Gam009B1']]

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

