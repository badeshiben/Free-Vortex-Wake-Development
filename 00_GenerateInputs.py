import numpy as np
import os
import pandas as pd
import fastlib
import weio
from create_studies import study1, study2, study3, study4, study5, study6, test_study


def genericStudy(study, ref_dir, work_dir, main_file):
    """ Generate OpenFAST inputs for wake discretization study

    INPUTS:
       - study                            : dictionary containing:
            Param                         : Varied parameter name [str]
            WS                            : lists of wind speeds [m/s]
            RPM                           : list of RPMs
            pitch                         : list of pitches [deg]
            DTfvw                         : array of DTfvw
            nNWPanel                      : array of nNWPanel
            WakeLength                    : array of WakeLength
            WakeRegFactor                 : array of WakeRegFactor
            WingRegFactor                 : array of WingRegFactor
            CoreSpreadEddyVisc            : array of CoreSpreadEddyVisc
       - ref_dir                          : Folder where the fast input files are located (will be copied)
       - main_file                        : Main file in ref_dir, used as a template
       - work_dir                         : Output folder (will be created)


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

    # --- Defining a "basic dictionary", all simulations will have these parameters
    # BaseDict = {'TMax': 10, 'DT': 0.01, 'DT_Out': 0.1} # NOTE: for other parametric studies these could be parameters
    BaseDict = {}
    BaseDict['AeroFile|WakeMod']=3
    BaseDict['AeroFile|FVWFile|RegFunction'] = 3   # Vatistas
    BaseDict['AeroFile|FVWFile|RegDeterMethod'] = 0  # manual(0), not auto(1), we vary the RegParam
    # --- Defining the parametric study, parameters that changes (list of dictionnaries with keys as FAST parameters)
    PARAMS=[]





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


    k = 0
    for wsp, rpm ,pitch, DTfvw, nNWP, WL, WaRF, WiRF, CSEV in zip(study['WS'], study['RPM'], study['pitch'], study['DTfvw'], study['nNWPanel'], study['WakeLength'],\
                                                 study['WakeRegFactor'], study['WingRegFactor'], study['CoreSpreadEddyVisc']):
        p=BaseDict.copy() # Important, create a copy for each simulation
        # Parameters for one simulation
        p['DT']                     = DTfvw
        p['DT_Out']                 = DTfvw
        p['EDFile|RotSpeed']        = rpm
        p['EDFile|BlPitch(1)']      = pitch
        p['EDFile|BlPitch(2)']      = pitch
        p['EDFile|BlPitch(3)']      = pitch
        p['InflowFile|HWindSpeed']  = wsp
        p['AeroFile|FVWFile|DTfvw'] = DTfvw
        p['AeroFile|FVWFile|nNWPanel'] = nNWP
        p['AeroFile|FVWFile|WakeLength'] = WL
        p['AeroFile|FVWFile|WakeRegFactor'] = WaRF
        p['AeroFile|FVWFile|WingRegFactor'] = WiRF
        p['AeroFile|FVWFile|CoreSpreadEddyVisc'] = CSEV

        # Name used for inputs files
        p['__name__']='ws{:.0f}_'.format(wsp)+'WakeLength'+'{:.3f}'.format(study['WakeLength'][k])

        PARAMS.append(p)

        # Add this simulation to the list of simulations
        fastfiles=fastlib.templateReplace(PARAMS,ref_dir,workdir=work_dir,RemoveRefSubFiles=True,main_file=main_file, oneSimPerDir=False)
        k += 1
    # j = 0
    # for wsp,rpm,pitch in zip(study['WS'], study['RPM'], study['pitch']): # here we zip since these are combined parameters
    #     k = 0
    #     for DTfvw, nNWP, WL, WaRF, WiRF, CSEV in zip(study['DTfvw'][j], study['nNWPanel'][j], study['WakeLength'][j],\
    #                                                  study['WakeRegFactor'][j], study['WingRegFactor'][j], study['CoreSpreadEddyVisc'][j]):
    #         p=BaseDict.copy() # Important, create a copy for each simulation
    #         # Parameters for one simulation
    #         p['EDFile|RotSpeed']        = rpm
    #         p['EDFile|BlPitch(1)']      = pitch
    #         p['EDFile|BlPitch(2)']      = pitch
    #         p['EDFile|BlPitch(3)']      = pitch
    #         p['InflowFile|HWindSpeed']  = wsp
    #         p['AeroFile|FVWFile|DTfvw'] = DTfvw
    #         p['AeroFile|FVWFile|nNWPanel'] = nNWP
    #         p['AeroFile|FVWFile|WakeLength'] = WL
    #         p['AeroFile|FVWFile|WakeRegFactor'] = WaRF
    #         p['AeroFile|FVWFile|WingRegFactor'] = WiRF
    #         p['AeroFile|FVWFile|CoreSpreadEddyVisc'] = CSEV
    #
    #         # Name used for inputs files
    #         p['__name__']='ws{:.0f}_'.format(wsp)+study['param']+'{:.3f}'.format(study[study['param']][j, k])
    #
    #         PARAMS.append(p)
    #
    #         # Add this simulation to the list of simulations
    #         fastfiles=fastlib.templateReplace(PARAMS,ref_dir,workdir=work_dir,RemoveRefSubFiles=True,main_file=main_file, oneSimPerDir=False)
    #         k += 1
    #     j += 1
    # --- Generating all files in a workdir

    return fastfiles

def divide_chunks(l, n):
    """divides list l into chunks of length n"""
    for i in range(0, len(l), n):
        yield fastfiles[i:i + n]

def createSubmit(fastfiles, FAST_EXE, npf):
    """creates submission scripts from fast filenames and FAST_EXE path. Up to n files per script
    FAST_EXE: absolute path to FAST executable [str]
    fastfiles: list of FAST file names [str]
    npf: number of runs per submit script
    """
    nfiles = len(fastfiles)

    chunks = list(divide_chunks(fastfiles, npf))

    for chunk in chunks:
        f = open(work_dir + "Submit_" + str(chunks.index(chunk)) + ".txt", "w")
        f.write('#! /bin/bash\n')
        f.write('#SBATCH --job-name=FVWcheck                     # Job name\n')
        f.write('#SBATCH --time 24:00:00\n')
        f.write('#SBATCH -A bar\n')
        f.write('#SBATCH --nodes=1                               # Number of nodes\n')
        f.write('#SBATCH --ntasks-per-node=36                    # Number of processors per node\n')
        f.write('#SBATCH --mail-user benjamin.anderson@nrel.gov\n')
        f.write('#SBATCH --mail-type BEGIN,END,FAIL\n')
        f.write('#SBATCH -o slurm-%x-%j.log                      # Output\n')
        f.write('\n')
        f.write('module purge\n')
        f.write('ml comp-intel mkl\n')
        f.write('\n')
        for file in chunk:
            fname = file.replace(work_dir,'')
            f.write(FAST_EXE + ' ' + fname + '\n')
            f.write('&\n')
        f.write('wait')
        f.close()


if __name__=='__main__':
    # --- "Global" Parameters for this script
    study = test_study
    ref_dir          = './BAR_02_template/'   # Folder where the fast input files are located (will be copied)
    main_file        = 'OpenFAST_BAR_02.fst'    # Main file in ref_dir, used as a template
    work_dir         = 'BAR_02_discretization_inputs/'+study['param']+'/'          # Output folder (will be created)
    FAST_EXE = '/home/banderso2/OLAF/build/glue-codes/openfast/openfast'
    npf = 4  # number of FAST runs per submission script
    # --- Generate inputs files
    fastfiles = genericStudy(study, ref_dir, work_dir, main_file)
    createSubmit(fastfiles, FAST_EXE, npf)

    # --- Creating a batch script
    # fastlib.writeBatch(os.path.join(work_dir,'_RUN_ALL.bat'),fastfiles,fastExe=FAST_EXE)
    # TODO potentially replace by a batch script to submit on eagle..

    # --- Running the simulations locally
    #fastlib.run_fastfiles(fastfiles, fastExe=FAST_EXE, parallel=True, ShowOutputs=True, nCores=4)

    # --- Simple Postprocessing
    # - Open all the output files,
    # - Average the quantities over the last revolution
    # - Return a dataframe, sorted by Wind Speed
    #outFiles    = [os.path.splitext(f)[0]+'.outb' for f in fastfiles]
    #avg_results = fastlib.averagePostPro(outFiles,avgMethod='periods',avgParam=1, ColMap = {'WS_[m/s]':'Wind1VelX_[m/s]'},ColSort='WS_[m/s]')
    #print(avg_results)

    # nNWPanel = np.array([3, 6, 12, 18, 24, 30, 36, 54, 72, 108, 144, 180, 216, 252])
    # WakeLength = np.array([107, 142, 178, 213, 249, 285, 320, 356, 391, 427])

    def old_functions():
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