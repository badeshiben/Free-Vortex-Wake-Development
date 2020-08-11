import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fastlib
from create_studies import study1, study2, study3, study4, study5, study6
import math
import weio

""" PLOTTING MEAN QUANTITIES """
####################################################################################################################

""" RAW DATA """
def resolution_raw(paramfull, WS, plot):
    """
    Parameters
    ----------
    paramfull:    parameter varied in study
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
        df = pd.read_csv('./PostPro/' + paramfull +'/Results_ws{:.0f}_'.format(ws) + paramfull + '.csv', sep='\t')
        oo = df[['OoPDefl1_[m]', 'IPDefl1_[m]']]
        """ Deflections"""
        ax[0, 0].set_ylabel('Deflection [m]')
        ax[0, 0].plot(df[paramfull], df['OoPDefl1_[m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[0, 0].text(.5, .5, 'OoPDefl1', transform=ax[0, 0].transAxes)
        ax[0, 1].plot(df[paramfull], df['IPDefl1_[m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[0, 1].text(.5, .5, 'IPDefl1', transform=ax[0, 1].transAxes)
        ax[0, 2].plot(df[paramfull], df['TTDspFA_[m]'], 'o-', label='WS = {:}'.format(ws))
        ax[0, 2].text(.5, .5, 'TTDspFA', transform=ax[0, 2].transAxes)
        """Blade root moments"""
        ax[1, 0].set_ylabel('Moment [kN-m]')
        ax[1, 0].plot(df[paramfull], df['RootMIP1_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[1, 0].text(.5, .5, 'RootMxb1', transform=ax[1, 0].transAxes)
        ax[1, 1].plot(df[paramfull], df['RootMOoP1_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[1, 1].text(.5, .5, 'RootMyb1', transform=ax[1, 1].transAxes)
        ax[1, 2].plot(df[paramfull], df['RootMzb1_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[1, 2].text(.5, .5, 'RootMzb1', transform=ax[1, 2].transAxes)
        """LSS moments"""
        ax[2, 0].set_ylabel('Moment [kN-m]')
        ax[2, 0].plot(df[paramfull], df['RotTorq_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[2, 0].text(.5, .5, 'RotTorq', transform=ax[2, 0].transAxes)
        ax[2, 1].plot(df[paramfull], df['LSSGagMya_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[2, 1].text(.5, .5, 'LSSGagMya', transform=ax[2, 1].transAxes)
        ax[2, 2].plot(df[paramfull], df['LSSGagMza_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[2, 2].text(.5, .5, 'LSSGagMza', transform=ax[2, 2].transAxes)
        """Tower top moments"""
        ax[3, 0].set_ylabel('Moment [kN-m]')
        ax[3, 0].plot(df[paramfull], df['YawBrMxp_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[3, 0].text(.5, .5, 'YawBrMxp', transform=ax[3, 0].transAxes)
        ax[3, 1].plot(df[paramfull], df['YawBrMyp_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[3, 1].text(.5, .5, 'YawBrMyp', transform=ax[3, 1].transAxes)
        ax[3, 2].plot(df[paramfull], df['YawBrMzp_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[3, 2].text(.5, .5, 'YawBrMzp', transform=ax[3, 2].transAxes)
        """Tower base moments"""
        ax[4, 0].set_ylabel('Moment [kN-m]')
        ax[4, 0].plot(df[paramfull], df['TwrBsMxt_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[4, 0].text(.5, .5, 'TwrBsMxt', transform=ax[4, 0].transAxes)
        ax[4, 1].plot(df[paramfull], df['TwrBsMyt_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[4, 1].text(.5, .5, 'TwrBsMyt', transform=ax[4, 1].transAxes)
        ax[4, 2].plot(df[paramfull], df['TwrBsMzt_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[4, 2].text(.5, .5, 'TwrBsMzt', transform=ax[4, 2].transAxes)
        ax[4, 2].set_xlabel(paramfull)
        """Generator power"""
        ax[5, 0].set_ylabel('Power [kW]')
        ax[5, 0].plot(df[paramfull], df['GenPwr_[kW]'], 'o-',  label='WS = {:}'.format(ws))
        ax[5, 0].text(.5, .5, 'GenPwr', transform=ax[5, 0].transAxes)
        ax[5, 0].set_xlabel(paramfull)
        """Generator torque"""
        ax[5, 1].set_ylabel('Torque [kN-m]')
        ax[5, 1].plot(df[paramfull], df['GenTq_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[5, 1].text(.5, .5, 'GenTq', transform=ax[5, 1].transAxes)
        ax[5, 1].set_xlabel(paramfull)
    plt.delaxes()
    ax[5, 1].legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tick_params(direction='in')
    if plot == 1:
        plt.show()
        plt.close()
    elif plot == 2:
        plot_name = "PostPro/" + paramfull + "_raw" + ".pdf"
        plt.savefig(plot_name, bbox_inches='tight')

""" DIFF VS FINEST RESOLUTION non aero quantities """
def resolution_pDiff(paramfull, WS, plot):
    """
    Parameters
    ----------
    paramfull:    parameter varied in study
    WS:         list of wind speeds [m/s]
    plot:       plot options. [0, 1, 2] - [no plot, show plot, save plot]

    Returns
    -------
    plots of % diff between results at current and finest resolution

    """
    fig, ax = plt.subplots(6, 3, sharey=False, sharex=True, figsize=(15, 20))  # (6.4,4.8)
    for ws in WS:
        df = pd.read_csv('./PostPro/' + paramfull +'/Results_ws{:.0f}_'.format(ws) + paramfull + '.csv', sep='\t')
        n = len(df[paramfull])
        df_fine = df.loc[n-1]
        dfpdiff = (df - df_fine) / df_fine * 100
        dfpdiff = dfpdiff.fillna(0)
        """ Deflections"""
        ax[0, 0].set_ylabel('% Difference')
        ax[0, 0].plot(df[paramfull], dfpdiff['OoPDefl1_[m]'], 'o-', label='WS = {:}'.format(ws))
        ax[0, 0].text(.5, .5, 'OoPDefl1', transform=ax[0, 0].transAxes)
        ax[0, 1].plot(df[paramfull], dfpdiff['IPDefl1_[m]'], 'o-', label='WS = {:}'.format(ws))
        ax[0, 1].text(.5, .5, 'IPDefl1', transform=ax[0, 1].transAxes)
        ax[0, 2].plot(df[paramfull], dfpdiff['TTDspFA_[m]'], 'o-', label='WS = {:}'.format(ws))
        ax[0, 2].text(.5, .5, 'TTDspFA', transform=ax[0, 2].transAxes)
        """Blade root moments"""
        ax[1, 0].set_ylabel('% Difference')
        ax[1, 0].plot(df[paramfull], dfpdiff['RootMIP1_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[1, 0].text(.5, .5, 'RootMxb1', transform=ax[1, 0].transAxes)
        ax[1, 1].plot(df[paramfull], dfpdiff['RootMOoP1_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[1, 1].text(.5, .5, 'RootMyb1', transform=ax[1, 1].transAxes)
        ax[1, 2].plot(df[paramfull], dfpdiff['RootMzb1_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[1, 2].text(.5, .5, 'RootMzb1', transform=ax[1, 2].transAxes)
        """LSS moments"""
        ax[2, 0].set_ylabel('% Difference')
        ax[2, 0].plot(df[paramfull], dfpdiff['RotTorq_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[2, 0].text(.5, .5, 'RotTorq', transform=ax[2, 0].transAxes)
        ax[2, 1].plot(df[paramfull], dfpdiff['LSSGagMya_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[2, 1].text(.5, .5, 'LSSGagMya', transform=ax[2, 1].transAxes)
        ax[2, 2].plot(df[paramfull], dfpdiff['LSSGagMza_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[2, 2].text(.5, .5, 'LSSGagMza', transform=ax[2, 2].transAxes)
        """Tower top moments"""
        ax[3, 0].set_ylabel('% Difference')
        ax[3, 0].plot(df[paramfull], dfpdiff['YawBrMxp_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[3, 0].text(.5, .5, 'YawBrMxp', transform=ax[3, 0].transAxes)
        ax[3, 1].plot(df[paramfull], dfpdiff['YawBrMyp_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[3, 1].text(.5, .5, 'YawBrMyp', transform=ax[3, 1].transAxes)
        ax[3, 2].plot(df[paramfull], dfpdiff['YawBrMzp_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[3, 2].text(.5, .5, 'YawBrMzp', transform=ax[3, 2].transAxes)
        """Tower base moments"""
        ax[4, 0].set_ylabel('% Difference')
        ax[4, 0].plot(df[paramfull], dfpdiff['TwrBsMxt_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[4, 0].text(.5, .5, 'TwrBsMxt', transform=ax[4, 0].transAxes)
        ax[4, 1].plot(df[paramfull], dfpdiff['TwrBsMyt_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[4, 1].text(.5, .5, 'TwrBsMyt', transform=ax[4, 1].transAxes)
        ax[4, 2].plot(df[paramfull], dfpdiff['TwrBsMzt_[kN-m]'], 'o-', label='WS = {:}'.format(ws))
        ax[4, 2].text(.5, .5, 'TwrBsMzt', transform=ax[4, 2].transAxes)
        ax[4, 2].set_xlabel(paramfull)
        """HSS power"""
        ax[5, 0].set_ylabel('% Difference')
        ax[5, 0].plot(df[paramfull], dfpdiff['HSShftPwr_[kW]'], 'o-', label='WS = {:}'.format(ws))
        ax[5, 0].text(.5, .5, 'GenPwr', transform=ax[5, 0].transAxes)
        ax[5, 0].set_xlabel(paramfull)
        """HSS torque"""
        ax[5, 1].set_ylabel('Torque [kN-m]')
        ax[5, 1].plot(df[paramfull], df['HSShftTq_[kN-m]'], 'o-',  label='WS = {:}'.format(ws))
        ax[5, 1].text(.5, .5, 'GenTq', transform=ax[5, 1].transAxes)
        ax[5, 1].set_xlabel(paramfull)
    plt.delaxes()
    ax[5, 1].legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tick_params(direction='in')
    if plot == 1:
        plt.show()
        plt.close()
    elif plot == 2:
        plot_name = "PostPro/" + paramfull + '/' + paramfull + "_%diff" + ".pdf"
        plt.savefig(plot_name, bbox_inches='tight')

def resolution_pDiff_aero(paramfull, WS, plot):
    """
    Parameters
    ----------
    paramfull:    parameter varied in study
    WS:         list of wind speeds [m/s]
    plot:       plot options. [0, 1, 2] - [no plot, show plot, save plot]

    Returns
    -------
    plots of % diff between results at current and finest resolution

    """
    #  use nodes 8, 23 @ 25%, 75%
    outlist = ['HSShftPwr_[kW]', 'RootMIP1_[kN-m]', 'RootMOoP1_[kN-m]', 'RootMzb1_[kN-m]', 'TwrBsMxt_[kN-m]',
               'TwrBsMyt_[kN-m]', 'TwrBsMzt_[kN-m]', 'AB1N008AxInd_[-]', 'AB1N023AxInd_[-]', 'AB1N008TnInd_[-]',
               'AB1N023TnInd_[-]', 'AB1N008Gam_[m^2/s]', 'AB1N023Gam_[m^2/s]']
    n_plot = len(outlist)
    n_col = 3
    n_row = int(np.ceil(n_plot/n_col))
    fig, ax = plt.subplots(n_row, n_col, sharey=False, sharex=True, figsize=(8.5, 11))  # (6.4,4.8)

    for ws in WS:
        df = pd.read_csv('./PostPro/' + paramfull +'/Results_ws{:.0f}_'.format(ws) + paramfull + '.csv', sep='\t')
        n = len(df[paramfull])
        df_fine = df.loc[n - 1]
        dfpdiff = (df - df_fine) / df_fine * 100
        dfpdiff = dfpdiff.fillna(0)
        for i in range(0, n_row):
            for j in range(0, n_col):
                idx = i*n_col + j
                if idx < n_plot:
                    ax[i, j].plot(df[paramfull], dfpdiff[outlist[idx]], '-', label='WS = {:}'.format(ws))
                    ax[i, j].set_title(outlist[idx], fontsize=10)
                        # text(.5, .5, outlist[idx], transform=ax[i, j].transAxes)
                    if j==0:
                        ax[i, j].set_ylabel('% Difference')
                    if i==n_row-1:
                        ax[i, j].set_xlabel(paramfull)
                    if idx==(n_plot-1):
                        ax[i, j].legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.tick_params(direction='in')
    plt.delaxes()
    if plot == 1:
        plt.show()
        plt.close()
    elif plot == 2:
        plot_name = "PostPro/" + paramfull + '/' + paramfull + "_%diff" + ".pdf"
        plt.savefig(plot_name, bbox_inches='tight')

""" PLOT OUTPUTS ALONG BLADE SPAN, VARYING WS and param """
def spanwise_vary_both(paramfull, values, WS, plot):
    """
    Parameters
    ----------
    paramfull:      param to use
    values:      list of param values
    WS:         list of wind speeds [m/s]
    plot:       plot options. [0, 1, 2] - [no plot, show plot, save plot]

    Returns
    -------
    plots outputs along blade span
    """
    fig, ax = plt.subplots(3, 2, sharey=False, sharex=False, figsize=(15, 20))
    norm_node_r = np.array([0.000000000000000e+00, 3.448147165807185e+00, 6.896294331614371e+00, 1.034444149742155e+01, 1.379258866322874e+01,
                            1.724073582903592e+01, 2.068888299484311e+01, 2.413703016065029e+01, 2.758517732645748e+01, 3.103332449226467e+01,
                            3.448147165807185e+01, 3.792961882387903e+01, 4.137776598968622e+01, 4.482591315549340e+01, 4.827406032130058e+01,
                            5.172220748710778e+01, 5.517035465291496e+01, 5.861850181872214e+01, 6.206664898452934e+01, 6.551479615033651e+01,
                            6.896294331614371e+01, 7.241109048195088e+01, 7.585923764775806e+01, 7.930738481356525e+01, 8.275553197937244e+01,
                            8.620367914517962e+01, 8.965182631098681e+01, 9.309997347679399e+01, 9.654812064260116e+01, 9.999626780840836e+01]) / 103
    legend_labels = []
    legend_handles = []
    for ws in WS:
        i = WS.index(ws)
        a = 0
        for value in values[i, :]:
            # pull out spanwise values
            df = pd.read_csv('./PostPro/' + paramfull +'/Results_ws{:.0f}_'.format(ws) + paramfull + '.csv', sep='\t')
            cols = df.columns.tolist()
            axind_cols = [j for j in cols if 'AxInd' in j]
            AxInd = df[axind_cols]
            tanind_cols = [j for j in cols if 'TnInd' in j]
            TnInd = df[tanind_cols]
            fn_cols = [j for j in cols if 'Fn' in j]
            Fn = df[fn_cols]
            ft_cols = [j for j in cols if 'Ft' in j]
            Ft = df[ft_cols]
            fl_cols = [j for j in cols if 'Fl' in j]
            Fl = df[fl_cols]
            fd_cols = [j for j in cols if 'Fd' in j]
            Fd = df[fd_cols]
            gam_cols = [j for j in cols if 'Gam' in j]
            Circ = df[gam_cols]

            # compute spanwise stats, append to df, and write back to csv
            AxIndMean = AxInd.mean(axis=1); AxIndMean = AxIndMean.rename('AxIndMean')
            AxIndMax  = AxInd.max(axis=1);   AxIndMax = AxIndMax.rename('AxIndMax')
            CircMean  = Circ.mean(axis=1);   CircMean = CircMean.rename('CircMean')
            CircMax   = Circ.max(axis=1);    CircMax  = CircMax.rename('CircMax')
            df = pd.concat([df, AxIndMean, AxIndMax, CircMean, CircMax], axis=1)
            df.to_csv('Results_ws{:04.1f}'.format(ws) + '_' + paramfull + '.csv', sep='\t', index=False)
            # AxInd = pd.concat([AxInd, mean, max], axis=1)
            #plot everything
            k = df.index[abs(df[paramfull]-value)<1e-5][0]  # assert almost equal
            linestyle = [':', '-.', '--', '-', ':']
            linewidth = [1, 1, 1, 1, 2]
            colors = ['xkcd:blue', 'xkcd:green', 'xkcd:red', 'xkcd:orange', 'xkcd:cyan', 'xkcd:magenta']
            #(0, (3, 5, 1, 5, 1, 5))
            ax[0, 0].set_ylabel('Axial Induction')
            ax[0, 0].plot(norm_node_r, AxInd.iloc[k], linestyle=linestyle[i], linewidth=linewidth[i], color=colors[a])
            ax[0, 1].set_ylabel('Tangential Induction')
            ax[0, 1].plot(norm_node_r, TnInd.iloc[k], linestyle=linestyle[i], linewidth=linewidth[i], color=colors[a])
            ax[1, 0].set_ylabel('Normal Force [N]')
            ax[1, 0].plot(norm_node_r, Fn.iloc[k], linestyle=linestyle[i], linewidth=linewidth[i], color=colors[a])
            ax[1, 1].set_ylabel('Tangential Force [N]')
            ax[1, 1].plot(norm_node_r, Ft.iloc[k], linestyle=linestyle[i], linewidth=linewidth[i], color=colors[a])
            # ax[2, 0].set_ylabel('Lift Force [N]')
            # ax[2, 0].plot(norm_node_r, Fl.iloc[k], linestyle=linestyle[i], linewidth=linewidth[i], color=colors[a])
            # ax[2, 1].set_ylabel('Drag Force [N]')
            # ax[2, 1].plot(norm_node_r, Fd.iloc[k], linestyle=linestyle[i], linewidth=linewidth[i], color=colors[a])
            ax[2, 0].set_ylabel('Circulation')
            ax[2, 0].plot(norm_node_r, Circ.iloc[k], linestyle=linestyle[i], linewidth=linewidth[i], color=colors[a], label='ws = {:}'.format(ws))
            legend_labels = legend_labels + [paramfull + " = {:04.3f}".format(value) + '; ws_[m/s] = {:}'.format(ws)]
            a+=1
    ax[2, 0].legend(legend_labels, loc='upper left', bbox_to_anchor=(1, 1))
    ax[0, 0].grid(); ax[0, 1].grid(); ax[1, 0].grid(); ax[1, 1].grid(); ax[2, 0].grid();
    plt.tick_params(direction='in')
    plt.delaxes()
    plt.grid(True)
    if plot == 1:
        plt.show()
        plt.close()
    elif plot == 2:
        plot_name = "PostPro/" + paramfull + '/SPANWISE_' + paramfull + ".pdf"
        plt.savefig(plot_name, bbox_inches='tight')

""" RUN RESOLUTION STUDY """
def run_study(WS, paramfull, values):
    """ run a resolution study
    Parameters
    ----------
    WS:                 list of wind speeds [m/s]
    paramfull:          parameter name to vary + _[units]
    parameter values:   list of parameter values

    Returns
    -------
    plots of % diff between results at current and finest resolution
    """
    param = paramfull.split('_', 1)[0]  # param name w/o units
    cwd = os.getcwd()
    work_dir = 'BAR_02_discretization_inputs/' + param + '/'
    postpro_dir = './PostPro/' + paramfull + '/'
    if not os.path.isdir(cwd + postpro_dir[1:]):
        os.mkdir(cwd + postpro_dir[1:])
    for wsp in WS:
        i = WS.index(wsp)
        outFiles=[]
        for val in values[i,:]:
            case     ='ws{:.0f}'.format(wsp)+'_'+param+'{:.3f}'.format(val)
            filename = os.path.join(work_dir, case + '.outb')
            outFiles.append(filename)
        # print(outFiles)
        dfAvg = fastlib.averagePostPro(outFiles,avgMethod='periods',avgParam=1,ColMap={'WS_[m/s]':'Wind1VelX_[m/s]'})
        dfAvg.insert(0,paramfull, values[i, :])
        # --- Save to csv since step above can be expensive
        csvname = 'Results_ws{:.0f}_'.format(wsp) + paramfull + '.csv'
        csvpath = os.path.join(postpro_dir, csvname)
        dfAvg.to_csv(csvpath, sep='\t', index=False)
        #print(dfAvg)
    # resolution_raw(paramfull, WS, 2)
    print('created all csvs ')
    # resolution_pDiff(paramfull, WS, 2)
    resolution_pDiff_aero(paramfull, WS, 1)
    # spanwise_vary_both(paramfull, values, WS, 2)
    print('Ran ' + paramfull + ' post processing')

if __name__ == "__main__":
    study = study1
    run_study(WS=study['WS'], paramfull=study['paramfull'], values=study[study['param']])





