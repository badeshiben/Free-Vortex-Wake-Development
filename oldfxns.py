########################################################################################################################
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

########################################################################################################################
'''GENERATING INPUTS'''
#################################################################################################################
    #IF multiple file per submit script
    # for chunk in chunks:
    #     f = open(work_dir + "Submit_" + str(chunks.index(chunk)) + ".txt", "w")
    #     f.write('#! /bin/bash\n')
    #     f.write('#SBATCH --job-name=FVWcheck                     # Job name\n')
    #     f.write('#SBATCH --time 48:00:00\n')
    #     f.write('#SBATCH -A bar\n')
    #     f.write('#SBATCH --nodes=1                               # Number of nodes\n')
    #     f.write('#SBATCH --ntasks-per-node=36                    # Number of processors per node\n')
    #     f.write('#SBATCH --mail-user benjamin.anderson@nrel.gov\n')
    #     f.write('#SBATCH --mail-type BEGIN,END,FAIL\n')
    #     f.write('#SBATCH -o slurm-%x-%j.log                      # Output\n')
    #     f.write('\n')
    #     f.write('module purge\n')
    #     f.write('ml comp-intel mkl\n')
    #     f.write('\n')
    #     for file in chunk:
    #         fname = file.replace(work_dir, '')
    #         f.write(FAST_EXE + ' ' + fname + ' &\n')
    #     f.write('wait')
    #     f.close()


    def old_functions():
        def generic_study_params_for_one_sim():
            x=0
            # p = BaseDict.copy()  # Important, create a copy for each simulation
            # # Parameters for one simulation
            # p['EDFile|RotSpeed'] = study['RPM']
            # p['EDFile|BlPitch(1)'] = study['pitch']
            # p['EDFile|BlPitch(2)'] = study['pitch']
            # p['EDFile|BlPitch(3)'] = study['pitch']
            # p['InflowFile|HWindSpeed'] = study['WS']
            # p['AeroFile|FVWFile|DTfvw'] = study['DTfvw']
            # p['AeroFile|FVWFile|nNWPanel'] = study['nNWPanel']
            # p['AeroFile|FVWFile|WakeLength'] = study['WakeLength']
            # p['AeroFile|FVWFile|WakeRegFactor'] = study['WakeRegFactor']
            # p['AeroFile|FVWFile|WingRegFactor'] = study['WingRegFactor']
            # p['AeroFile|FVWFile|CoreSpreadEddyVisc'] = study['CoreSpreadEddyVisc']
            #
            #
            #
            #
            # # Name used for inputs files
            # p['__name__'] = 'ws4_nNWPanel' + str(study['nNWPanel']) + '_test'
            #
            # PARAMS.append(p)
            #
            # # Add this simulation to the list of simulations
            # fastfiles = fastlib.templateReplace(PARAMS, ref_dir, workdir=work_dir, RemoveRefSubFiles=True, main_file=main_file,
            #                                     oneSimPerDir=False)
        def WakeDiscretizationStudy(ref_dir, work_dir, main_file):
            """ Generate OpenFAST inputs for wake discretization study

            INPUTS:
               - ref_dir  : Folder where the fast input files are located (will be copied)
               - main_file: Main file in ref_dir, used as a template
               - work_dir : Output folder (will be created)


            This script uses a reference directory (`ref_dir`) which contains a reference input file (.fst)
            1) The reference directory is copied to a working directory (`work_dir`).
            2) All the fast input files are generated in this directory based on a list of dictionaries (`PARAMS`).
            For each dictionary in this list:
               - The keys are "path" to a input parameter, e.g. `EDFile|RotSpeed`  or `FAST|TMax`.
                 These should correspond to the variables used in the FAST inputs files.
               - The values are the values corresponding to this parameter
            For instance:
                 PARAMS[0]['EDFile|RotSpeed']       = 5
                 PARAMS[0]['InflowFile|HWindSpeed'] = 10

            Optional:
                3) The simulations are run, successively distributed on `nCores` CPUs.
                4) The output files are read, and averaged based on a method (e.g. average over a set of periods,
                    see averagePostPro in fastlib for the different averaging methods).
                   A pandas DataFrame is returned
            """
            # --- The parameters we will change
            # WS RPM and Pitch are combined parameters defining operating conditions (hence, same length)
            WS = [4, 6, 8, 10, 12]
            RPM = np.array([3.894, 5.846, 7.771, 7.881, 7.881])
            rotSpd = RPM * 0.104719755  # rad/s
            dpsi = np.array([2.5, 5, 7.5, 10, 12.5, 15]) * np.pi / 180  # rad
            Pitch = [0, 0, 0, 6.585, 10.161]  # deg
            # This is the parameter we change in that case
            DTfvw = np.outer(dpsi, rotSpd)
            print(DTfvw)

            # --- Defining a "basic dictionary", all simulations will have these parameters
            BaseDict = {'TMax': 10, 'DT': 0.01,
                        'DT_Out': 0.1}  # NOTE: for other parametric studies these could be parameters
            BaseDict['AeroFile|WakeMod'] = 3
            BaseDict['AeroFile|FVWFile|RegFunction'] = 3  # Vatistas
            BaseDict['AeroFile|FVWFile|RegDeterMethod'] = 0  # manual(0), not auto(1), we vary the RegParam
            BaseDict = fastlib.paramsNoController(BaseDict)  # Remove the controller
            # BaseDict = fastlib.paramsControllerDLL(BaseDict) # Activate the controller
            # BaseDict = fastlib.paramsStiff(BaseDict)         # Make the turbine stiff (except generator)
            # BaseDict = fastlib.paramsNoGen(BaseDict)         # Remove the Generator DOF

            # --- Defining the parametric study, parameters that changes (list of dictionnaries with keys as FAST parameters)
            PARAMS = []
            j = 0
            for wsp, rpm, pitch in zip(WS, RPM, Pitch):  # here we zip since these are combined parameters
                for dt in DTfvw[:, j]:
                    p = BaseDict.copy()  # Important, create a copy for each simulation
                    # Parameters for one simulation
                    p['EDFile|RotSpeed'] = rpm
                    p['EDFile|BlPitch(1)'] = pitch
                    p['EDFile|BlPitch(2)'] = pitch
                    p['EDFile|BlPitch(3)'] = pitch
                    p['EDFile|NacYaw'] = 0  # NacYaw or PropagationDir, if Servo, also YawNeut!
                    p['InflowFile|HWindSpeed'] = wsp
                    p['InflowFile|WindType'] = 1
                    p['AeroFile|FVWFile|DTfvw'] = dt
                    p['AeroFile|FVWFile|WakeRegFactor'] = 3
                    p['AeroFile|FVWFile|WingRegFactor'] = 3
                    # p['AeroFile|FVWFile|DTfvw']           = 0.1
                    # p['AeroFile|FVWFile|nNWPanel']        = 100
                    # p['AeroFile|FVWFile|nFWPanel']        = 200
                    # p['AeroFile|FVWFile|nFWPanelFree']    = 200

                    # Name used for inputs files
                    p['__name__'] = 'ws{:04.1f}_DTfvw{:06.3f}'.format(wsp, dt)

                    # Add this simulation to the list of simulations
                    PARAMS.append(p)
                j += 1
            # --- Generating all files in a workdir
            fastfiles = fastlib.templateReplace(PARAMS, ref_dir, workdir=work_dir, RemoveRefSubFiles=True,
                                                main_file=main_file, oneSimPerDir=False)
            return fastfiles

        def NearWakeExtentStudy(ref_dir, work_dir, main_file):
            """ Generate OpenFAST inputs for near wake extent study

            INPUTS:
               - ref_dir  : Folder where the fast input files are located (will be copied)
               - main_file: Main file in ref_dir, used as a template
               - work_dir : Output folder (will be created)


            This script uses a reference directory (`ref_dir`) which contains a reference input file (.fst)
            1) The reference directory is copied to a working directory (`work_dir`).
            2) All the fast input files are generated in this directory based on a list of dictionaries (`PARAMS`).
            For each dictionary in this list:
               - The keys are "path" to a input parameter, e.g. `EDFile|RotSpeed`  or `FAST|TMax`.
                 These should correspond to the variables used in the FAST inputs files.
               - The values are the values corresponding to this parameter
            For instance:
                 PARAMS[0]['EDFile|RotSpeed']       = 5
                 PARAMS[0]['InflowFile|HWindSpeed'] = 10

            Optional:
                3) The simulations are run, successively distributed on `nCores` CPUs.
                4) The output files are read, and averaged based on a method (e.g. average over a set of periods,
                    see averagePostPro in fastlib for the different averaging methods).
                   A pandas DataFrame is returned
            """
            # --- The parameters we will change
            # WS RPM and Pitch are combined parameters defining operating conditions (hence, same length)
            WS = [4, 6, 8, 10, 12]
            RPM = np.array([3.894, 5.846, 7.771, 7.881, 7.881])
            Pitch = [0, 0, 0, 6.585, 10.161]  # deg
            rotSpd = RPM * 0.104719755  # rad/s
            NWE = np.array([30, 60, 120, 180, 240, 300, 360, 540, 720, 1080, 1440, 1800, 2160, 2520]) * np.pi / 180
            DTfvw = np.array([1, 1, 1, 1, 2])  # TODO from previous study
            prod = DTfvw * rotSpd

            # This is the parameter we change in that case
            nNWPanel = np.outer(NWE, 1 / prod)

            print(nNWPanel)

            # --- Defining a "basic dictionary", all simulations will have these parameters
            BaseDict = {'TMax': 10, 'DT': 0.01,
                        'DT_Out': 0.1}  # NOTE: for other parametric studies these could be parameters
            BaseDict['AeroFile|WakeMod'] = 3
            BaseDict['AeroFile|FVWFile|RegFunction'] = 3  # Vatistas
            BaseDict['AeroFile|FVWFile|RegDeterMethod'] = 0  # manual(0), not auto(1), we vary the RegParam
            BaseDict = fastlib.paramsNoController(BaseDict)  # Remove the controller
            # BaseDict = fastlib.paramsControllerDLL(BaseDict) # Activate the controller
            # BaseDict = fastlib.paramsStiff(BaseDict)         # Make the turbine stiff (except generator)
            # BaseDict = fastlib.paramsNoGen(BaseDict)         # Remove the Generator DOF

            # --- Defining the parametric study, parameters that changes (list of dictionnaries with keys as FAST parameters)
            PARAMS = []
            j = 0
            for wsp, rpm, pitch in zip(WS, RPM, Pitch):  # here we zip since these are combined parameters
                for nnwp in nNWPanel[:, j]:
                    p = BaseDict.copy()  # Important, create a copy for each simulation
                    # Parameters for one simulation
                    p['EDFile|RotSpeed'] = rpm
                    p['EDFile|BlPitch(1)'] = pitch
                    p['EDFile|BlPitch(2)'] = pitch
                    p['EDFile|BlPitch(3)'] = pitch
                    p['EDFile|NacYaw'] = 0  # NacYaw or PropagationDir, if Servo, also YawNeut!
                    p['InflowFile|HWindSpeed'] = wsp
                    p['InflowFile|WindType'] = 1
                    p['AeroFile|FVWFile|DTfvw'] = 0.2165
                    p['AeroFile|FVWFile|nNWPanel'] = nnwp
                    p['AeroFile|FVWFile|WakeRegFactor'] = 2
                    p['AeroFile|FVWFile|WingRegFactor'] = 2

                    # Name used for inputs files
                    p['__name__'] = 'ws{:04.1f}_nNWPanel{:06.3f}'.format(wsp, nnwp)

                    # Add this simulation to the list of simulations
                    PARAMS.append(p)
                j += 1
            # --- Generating all files in a workdir
            fastfiles = fastlib.templateReplace(PARAMS, ref_dir, workdir=work_dir, RemoveRefSubFiles=True,
                                                main_file=main_file, oneSimPerDir=False)
            return fastfiles

        def FarWakeExtentStudy(ref_dir, work_dir, main_file):
            """ Generate OpenFAST inputs for far wake extent study

            INPUTS:
               - ref_dir  : Folder where the fast input files are located (will be copied)
               - main_file: Main file in ref_dir, used as a template
               - work_dir : Output folder (will be created)


            This script uses a reference directory (`ref_dir`) which contains a reference input file (.fst)
            1) The reference directory is copied to a working directory (`work_dir`).
            2) All the fast input files are generated in this directory based on a list of dictionaries (`PARAMS`).
            For each dictionary in this list:
               - The keys are "path" to a input parameter, e.g. `EDFile|RotSpeed`  or `FAST|TMax`.
                 These should correspond to the variables used in the FAST inputs files.
               - The values are the values corresponding to this parameter
            For instance:
                 PARAMS[0]['EDFile|RotSpeed']       = 5
                 PARAMS[0]['InflowFile|HWindSpeed'] = 10

            Optional:
                3) The simulations are run, successively distributed on `nCores` CPUs.
                4) The output files are read, and averaged based on a method (e.g. average over a set of periods,
                    see averagePostPro in fastlib for the different averaging methods).
                   A pandas DataFrame is returned
            """
            # --- The parameters we will change
            # WS RPM and Pitch are combined parameters defining operating conditions (hence, same length)
            WS = [4, 6, 8, 10, 12]
            RPM = np.array([3.894, 5.846, 7.771, 7.881, 7.881])
            Pitch = [0, 0, 0, 6.585, 10.161]
            rotSpd = RPM * 0.104719755  # rad/s
            FWE = np.array([231, 308, 385, 462, 539, 616, 693, 770, 847, 924])  # m
            dpsi = np.array([1, 1, 1, 1, 2])  # TODO from previous study
            part = rotSpd / WS / dpsi
            WakeLength = np.outer(FWE, part)
            print(WakeLength)

            # --- Defining a "basic dictionary", all simulations will have these parameters
            BaseDict = {'TMax': 10, 'DT': 0.01,
                        'DT_Out': 0.1}  # NOTE: for other parametric studies these could be parameters
            BaseDict['AeroFile|WakeMod'] = 3
            BaseDict['AeroFile|FVWFile|RegFunction'] = 3  # Vatistas
            BaseDict['AeroFile|FVWFile|RegDeterMethod'] = 0  # manual(0), not auto(1), we vary the RegParam
            BaseDict = fastlib.paramsNoController(BaseDict)  # Remove the controller
            # BaseDict = fastlib.paramsControllerDLL(BaseDict) # Activate the controller
            # BaseDict = fastlib.paramsStiff(BaseDict)         # Make the turbine stiff (except generator)
            # BaseDict = fastlib.paramsNoGen(BaseDict)         # Remove the Generator DOF

            # --- Defining the parametric study, parameters that changes (list of dictionnaries with keys as FAST parameters)
            PARAMS = []
            j = 0
            for wsp, rpm, pitch in zip(WS, RPM, Pitch):  # here we zip since these are combined parameters
                for wl in WakeLength[:, j]:
                    p = BaseDict.copy()  # Important, create a copy for each simulation
                    # Parameters for one simulation
                    p['EDFile|RotSpeed'] = rpm
                    p['EDFile|BlPitch(1)'] = pitch
                    p['EDFile|BlPitch(2)'] = pitch
                    p['EDFile|BlPitch(3)'] = pitch
                    p['EDFile|NacYaw'] = 0  # NacYaw or PropagationDir, if Servo, also YawNeut!
                    p['InflowFile|HWindSpeed'] = wsp
                    p['InflowFile|WindType'] = 1
                    p['AeroFile|FVWFile|WakeLength'] = wl
                    p['AeroFile|FVWFile|WakeRegFactor'] = 2
                    p['AeroFile|FVWFile|WingRegFactor'] = 2

                    # Name used for inputs files
                    p['__name__'] = 'ws{:04.1f}_WakeLength{:06.3f}'.format(wsp, wl)

                    # Add this simulation to the list of simulations
                    PARAMS.append(p)
                j += 1

            # --- Generating all files in a workdir
            fastfiles = fastlib.templateReplace(PARAMS, ref_dir, workdir=work_dir, RemoveRefSubFiles=True,
                                                main_file=main_file, oneSimPerDir=False)
            return fastfiles

        def ParametericStudyRegularization(ref_dir, work_dir, main_file):
            """ Example to run a set of OpenFAST simulations (parametric study)

            INPUTS:
               - ref_dir  : Folder where the fast input files are located (will be copied)
               - main_file: Main file in ref_dir, used as a template
               - work_dir : Output folder (will be created)


            This script uses a reference directory (`ref_dir`) which contains a reference input file (.fst)
            1) The reference directory is copied to a working directory (`work_dir`).
            2) All the fast input files are generated in this directory based on a list of dictionaries (`PARAMS`).
            For each dictionary in this list:
               - The keys are "path" to a input parameter, e.g. `EDFile|RotSpeed`  or `FAST|TMax`.
                 These should correspond to the variables used in the FAST inputs files.
               - The values are the values corresponding to this parameter
            For instance:
                 PARAMS[0]['EDFile|RotSpeed']       = 5
                 PARAMS[0]['InflowFile|HWindSpeed'] = 10

            Optional:
                3) The simulations are run, successively distributed on `nCores` CPUs.
                4) The output files are read, and averaged based on a method (e.g. average over a set of periods,
                    see averagePostPro in fastlib for the different averaging methods).
                   A pandas DataFrame is returned
            """
            # --- The parameters we will change
            # WS RPM and Pitch are combined parameters defining operating conditions (hence, same length)
            WS = [5, 10]
            RPM = [6, 8]
            Pitch = [0, 5]
            # This is the parameter we change in that case
            regFactor = np.linspace(0.5, 5, 3)
            print(regFactor)

            # --- Defining a "basic dictionary", all simulations will have these parameters
            BaseDict = {'TMax': 10, 'DT': 0.01,
                        'DT_Out': 0.1}  # NOTE: for other parametric studies these could be parameters
            BaseDict['AeroFile|WakeMod'] = 3
            BaseDict['AeroFile|FVWFile|RegFunction'] = 3  # Vatistas
            BaseDict['AeroFile|FVWFile|RegDeterMethod'] = 0  # manual(0), not auto(1), we vary the RegParam
            BaseDict = fastlib.paramsNoController(BaseDict)  # Remove the controller
            # BaseDict = fastlib.paramsControllerDLL(BaseDict) # Activate the controller
            # BaseDict = fastlib.paramsStiff(BaseDict)         # Make the turbine stiff (except generator)
            # BaseDict = fastlib.paramsNoGen(BaseDict)         # Remove the Generator DOF

            # --- Defining the parametric study, parameters that changes (list of dictionnaries with keys as FAST parameters)
            PARAMS = []
            for wsp, rpm, pitch in zip(WS, RPM, Pitch):  # here we zip since these are combined parameters
                for reg in regFactor:
                    p = BaseDict.copy()  # Important, create a copy for each simulation
                    # Parameters for one simulation
                    p['EDFile|RotSpeed'] = rpm
                    p['EDFile|BlPitch(1)'] = pitch
                    p['EDFile|BlPitch(2)'] = pitch
                    p['EDFile|BlPitch(3)'] = pitch
                    p['EDFile|NacYaw'] = 0  # NacYaw or PropagationDir, if Servo, also YawNeut!
                    p['InflowFile|HWindSpeed'] = wsp
                    p['InflowFile|WindType'] = 1
                    p['AeroFile|FVWFile|WakeRegFactor'] = reg
                    p['AeroFile|FVWFile|WingRegFactor'] = reg
                    # p['AeroFile|FVWFile|DTfvw']           = 0.1
                    # p['AeroFile|FVWFile|nNWPanel']        = 100
                    # p['AeroFile|FVWFile|nFWPanel']        = 200
                    # p['AeroFile|FVWFile|nFWPanelFree']    = 200

                    # Name used for inputs files
                    p['__name__'] = 'ws{:04.1f}_UHHHHHH{:06.4f}'.format(wsp, reg)

                    # Add this simulation to the list of simulations
                    PARAMS.append(p)

            # --- Generating all files in a workdir
            fastfiles = fastlib.templateReplace(PARAMS, ref_dir, workdir=work_dir, RemoveRefSubFiles=True,
                                                main_file=main_file, oneSimPerDir=False)
            return fastfiles

        def RegularizationStudy1(ref_dir, work_dir, main_file):
            """ Generate OpenFAST inputs for regularization study 1

            INPUTS:
               - ref_dir  : Folder where the fast input files are located (will be copied)
               - main_file: Main file in ref_dir, used as a template
               - work_dir : Output folder (will be created)


            This script uses a reference directory (`ref_dir`) which contains a reference input file (.fst)
            1) The reference directory is copied to a working directory (`work_dir`).
            2) All the fast input files are generated in this directory based on a list of dictionaries (`PARAMS`).
            For each dictionary in this list:
               - The keys are "path" to a input parameter, e.g. `EDFile|RotSpeed`  or `FAST|TMax`.
                 These should correspond to the variables used in the FAST inputs files.
               - The values are the values corresponding to this parameter
            For instance:
                 PARAMS[0]['EDFile|RotSpeed']       = 5
                 PARAMS[0]['InflowFile|HWindSpeed'] = 10

            Optional:
                3) The simulations are run, successively distributed on `nCores` CPUs.
                4) The output files are read, and averaged based on a method (e.g. average over a set of periods,
                    see averagePostPro in fastlib for the different averaging methods).
                   A pandas DataFrame is returned
            """
            # --- The parameters we will change
            # WS RPM and Pitch are combined parameters defining operating conditions (hence, same length)
            WS = [4, 6, 8, 10, 12]
            RPM = np.array([3.894, 5.846, 7.771, 7.881, 7.881])
            rotSpd = RPM * 0.104719755  # rad/s
            Pitch = [0, 0, 0, 6.585, 10.161]  # deg
            WakeRegFactor = np.array([0, 1, 0.5, 1, 1.5, 2, 2.5, 3, 5])

            # --- Defining a "basic dictionary", all simulations will have these parameters
            BaseDict = {'TMax': 10, 'DT': 0.01,
                        'DT_Out': 0.1}  # NOTE: for other parametric studies these could be parameters
            BaseDict['AeroFile|WakeMod'] = 3
            BaseDict['AeroFile|FVWFile|RegFunction'] = 3  # Vatistas
            BaseDict['AeroFile|FVWFile|RegDeterMethod'] = 0  # manual(0), not auto(1), we vary the RegParam
            BaseDict = fastlib.paramsNoController(BaseDict)  # Remove the controller
            # BaseDict = fastlib.paramsControllerDLL(BaseDict) # Activate the controller
            # BaseDict = fastlib.paramsStiff(BaseDict)         # Make the turbine stiff (except generator)
            # BaseDict = fastlib.paramsNoGen(BaseDict)         # Remove the Generator DOF

            # --- Defining the parametric study, parameters that changes (list of dictionnaries with keys as FAST parameters)
            PARAMS = []
            for wsp, rpm, pitch in zip(WS, RPM, Pitch):  # here we zip since these are combined parameters
                for reg in WakeRegFactor:
                    p = BaseDict.copy()  # Important, create a copy for each simulation
                    # Parameters for one simulation
                    p['EDFile|RotSpeed'] = rpm
                    p['EDFile|BlPitch(1)'] = pitch
                    p['EDFile|BlPitch(2)'] = pitch
                    p['EDFile|BlPitch(3)'] = pitch
                    p['EDFile|NacYaw'] = 0  # NacYaw or PropagationDir, if Servo, also YawNeut!
                    p['InflowFile|HWindSpeed'] = wsp
                    p['InflowFile|WindType'] = 1
                    p['AeroFile|FVWFile|WakeRegFactor'] = reg
                    p['AeroFile|FVWFile|WingRegFactor'] = reg
                    p['AeroFile|FVWFile|CoreSpreadEddyVisc'] = 1000

                    # Name used for inputs files
                    p['__name__'] = 'ws{:04.1f}_WakeRegFactor{:06.4f}'.format(wsp, reg)

                    # Add this simulation to the list of simulations
                    PARAMS.append(p)

            # --- Generating all files in a workdir
            fastfiles = fastlib.templateReplace(PARAMS, ref_dir, workdir=work_dir, RemoveRefSubFiles=True,
                                                main_file=main_file, oneSimPerDir=False)
            return fastfiles

        def RegularizationStudy2(ref_dir, work_dir, main_file):
            """ Example to run a set of OpenFAST simulations (parametric study)

            INPUTS:
               - ref_dir  : Folder where the fast input files are located (will be copied)
               - main_file: Main file in ref_dir, used as a template
               - work_dir : Output folder (will be created)


            This script uses a reference directory (`ref_dir`) which contains a reference input file (.fst)
            1) The reference directory is copied to a working directory (`work_dir`).
            2) All the fast input files are generated in this directory based on a list of dictionaries (`PARAMS`).
            For each dictionary in this list:
               - The keys are "path" to a input parameter, e.g. `EDFile|RotSpeed`  or `FAST|TMax`.
                 These should correspond to the variables used in the FAST inputs files.
               - The values are the values corresponding to this parameter
            For instance:
                 PARAMS[0]['EDFile|RotSpeed']       = 5
                 PARAMS[0]['InflowFile|HWindSpeed'] = 10

            Optional:
                3) The simulations are run, successively distributed on `nCores` CPUs.
                4) The output files are read, and averaged based on a method (e.g. average over a set of periods,
                    see averagePostPro in fastlib for the different averaging methods).
                   A pandas DataFrame is returned
            """
            # --- The parameters we will change
            # WS RPM and Pitch are combined parameters defining operating conditions (hence, same length)
            WS = [4, 6, 8, 10, 12]
            RPM = np.array([3.894, 5.846, 7.771, 7.881, 7.881])
            rotSpd = RPM * 0.104719755  # rad/s
            Pitch = [0, 0, 0, 6.585, 10.161]  # deg
            WingRegFactor = np.array([0, 1, 0.5, 1, 1.5, 2, 2.5, 3, 5])
            WakeRegFactor = 2  # TODO from previous study

            # --- Defining a "basic dictionary", all simulations will have these parameters
            BaseDict = {'TMax': 10, 'DT': 0.01,
                        'DT_Out': 0.1}  # NOTE: for other parametric studies these could be parameters
            BaseDict['AeroFile|WakeMod'] = 3
            BaseDict['AeroFile|FVWFile|RegFunction'] = 3  # Vatistas
            BaseDict['AeroFile|FVWFile|RegDeterMethod'] = 0  # manual(0), not auto(1), we vary the RegParam
            BaseDict = fastlib.paramsNoController(BaseDict)  # Remove the controller
            # BaseDict = fastlib.paramsControllerDLL(BaseDict) # Activate the controller
            # BaseDict = fastlib.paramsStiff(BaseDict)         # Make the turbine stiff (except generator)
            # BaseDict = fastlib.paramsNoGen(BaseDict)         # Remove the Generator DOF

            # --- Defining the parametric study, parameters that changes (list of dictionnaries with keys as FAST parameters)
            PARAMS = []
            for wsp, rpm, pitch in zip(WS, RPM, Pitch):  # here we zip since these are combined parameters
                for reg in WingRegFactor:
                    p = BaseDict.copy()  # Important, create a copy for each simulation
                    # Parameters for one simulation
                    p['EDFile|RotSpeed'] = rpm
                    p['EDFile|BlPitch(1)'] = pitch
                    p['EDFile|BlPitch(2)'] = pitch
                    p['EDFile|BlPitch(3)'] = pitch
                    p['EDFile|NacYaw'] = 0  # NacYaw or PropagationDir, if Servo, also YawNeut!
                    p['InflowFile|HWindSpeed'] = wsp
                    p['InflowFile|WindType'] = 1
                    p['AeroFile|FVWFile|WakeRegFactor'] = WakeRegFactor
                    p['AeroFile|FVWFile|WingRegFactor'] = WingRegFactor
                    p['AeroFile|FVWFile|CoreSpreadEddyVisc'] = 1000

                    # Name used for inputs files
                    p['__name__'] = 'ws{:04.1f}_WingRegFactor{:06.4f}'.format(wsp, reg)

                    # Add this simulation to the list of simulations
                    PARAMS.append(p)

            # --- Generating all files in a workdir
            fastfiles = fastlib.templateReplace(PARAMS, ref_dir, workdir=work_dir, RemoveRefSubFiles=True,
                                                main_file=main_file, oneSimPerDir=False)
            return fastfiles

        def RegularizationStudy3(ref_dir, work_dir, main_file):
            """ Generate OpenFAST inputs for regularization study 3

            INPUTS:
               - ref_dir  : Folder where the fast input files are located (will be copied)
               - main_file: Main file in ref_dir, used as a template
               - work_dir : Output folder (will be created)


            This script uses a reference directory (`ref_dir`) which contains a reference input file (.fst)
            1) The reference directory is copied to a working directory (`work_dir`).
            2) All the fast input files are generated in this directory based on a list of dictionaries (`PARAMS`).
            For each dictionary in this list:
               - The keys are "path" to a input parameter, e.g. `EDFile|RotSpeed`  or `FAST|TMax`.
                 These should correspond to the variables used in the FAST inputs files.
               - The values are the values corresponding to this parameter
            For instance:
                 PARAMS[0]['EDFile|RotSpeed']       = 5
                 PARAMS[0]['InflowFile|HWindSpeed'] = 10

            Optional:
                3) The simulations are run, successively distributed on `nCores` CPUs.
                4) The output files are read, and averaged based on a method (e.g. average over a set of periods,
                    see averagePostPro in fastlib for the different averaging methods).
                   A pandas DataFrame is returned
            """
            # --- The parameters we will change
            # WS RPM and Pitch are combined parameters defining operating conditions (hence, same length)
            WS = [4, 12]
            RPM = np.array([3.894, 7.881])
            rotSpd = RPM * 0.104719755  # rad/s
            Pitch = [0, 0.161]  # deg
            CoreSpreadEddyVisc = np.array([100, 500, 1000, 5000])
            WingRegFactor = 2  # TODO from previous study
            WakeRegFactor = 2  # TODO from previous study

            # --- Defining a "basic dictionary", all simulations will have these parameters
            BaseDict = {'TMax': 10, 'DT': 0.01,
                        'DT_Out': 0.1}  # NOTE: for other parametric studies these could be parameters
            BaseDict['AeroFile|WakeMod'] = 3
            BaseDict['AeroFile|FVWFile|RegFunction'] = 3  # Vatistas
            BaseDict['AeroFile|FVWFile|RegDeterMethod'] = 0  # manual(0), not auto(1), we vary the RegParam
            BaseDict = fastlib.paramsNoController(BaseDict)  # Remove the controller
            # BaseDict = fastlib.paramsControllerDLL(BaseDict) # Activate the controller
            # BaseDict = fastlib.paramsStiff(BaseDict)         # Make the turbine stiff (except generator)
            # BaseDict = fastlib.paramsNoGen(BaseDict)         # Remove the Generator DOF

            # --- Defining the parametric study, parameters that changes (list of dictionnaries with keys as FAST parameters)
            PARAMS = []
            for wsp, rpm, pitch in zip(WS, RPM, Pitch):  # here we zip since these are combined parameters
                for visc in CoreSpreadEddyVisc:
                    p = BaseDict.copy()  # Important, create a copy for each simulation
                    # Parameters for one simulation
                    p['EDFile|RotSpeed'] = rpm
                    p['EDFile|BlPitch(1)'] = pitch
                    p['EDFile|BlPitch(2)'] = pitch
                    p['EDFile|BlPitch(3)'] = pitch
                    p['EDFile|NacYaw'] = 0  # NacYaw or PropagationDir, if Servo, also YawNeut!
                    p['InflowFile|HWindSpeed'] = wsp
                    p['InflowFile|WindType'] = 1
                    p['AeroFile|FVWFile|WakeRegFactor'] = WakeRegFactor
                    p['AeroFile|FVWFile|WingRegFactor'] = WingRegFactor
                    p['AeroFile|FVWFile|CoreSpreadEddyVisc'] = visc

                    # Name used for inputs files
                    p['__name__'] = 'ws{:04.1f}_CoreSpreadEddyVisc{:06.4f}'.format(wsp, visc)

                    # Add this simulation to the list of simulations
                    PARAMS.append(p)

            # --- Generating all files in a workdir
            fastfiles = fastlib.templateReplace(PARAMS, ref_dir, workdir=work_dir, RemoveRefSubFiles=True,
                                                main_file=main_file, oneSimPerDir=False)
            return fastfiles