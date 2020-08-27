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

    k = 0
    for wsp, rpm ,pitch in zip(study['WS'], study['RPM'], study['pitch']):
        j = 0
        for DTfvw, nNWP, WL, WaRF, WiRF, CSEV in zip(study['DTfvw'][k, :], study['nNWPanel'][k, :], study['WakeLength'][k, :],\
                                                 study['WakeRegFactor'][k, :], study['WingRegFactor'][k, :], study['CoreSpreadEddyVisc'][k, :]):

            p=BaseDict.copy() # Important, create a copy for each simulation
            # Parameters for one simulation
            p['TMax']                   = study['TMax']
            p['TStart']                 = study['TMax'] - 200
            p['DT']                     = DTfvw
            p['DT_Out']                 = DTfvw
            p['EDFile|RotSpeed']        = rpm
            p['EDFile|BlPitch(1)']      = pitch
            p['EDFile|BlPitch(2)']      = pitch
            p['EDFile|BlPitch(3)']      = pitch
            if study['param'] == 'DTfvw':
                p['EDFile|ShftTilt'] = 0
            if nNWP < 30:
                p['AeroFile|FVWFile|FWShedVorticity'] = True
            p['InflowFile|HWindSpeed']  = wsp
            p['AeroFile|FVWFile|DTfvw'] = DTfvw
            p['AeroFile|FVWFile|nNWPanel'] = int(nNWP)
            p['AeroFile|FVWFile|WakeLength'] = int(WL)
            p['AeroFile|FVWFile|WakeRegFactor'] = WaRF
            p['AeroFile|FVWFile|WingRegFactor'] = WiRF
            p['AeroFile|FVWFile|CoreSpreadEddyVisc'] = CSEV
            # Name used for inputs filesx =
            x = study[study['param']][k]
            p['__name__']='ws{:.0f}_'.format(wsp)+study['param']+'{:.3f}'.format(study[study['param']][k, j])
            PARAMS.append(p)
            j += 1
        k += 1
    # Add this simulation to the list of simulations
    fastfiles=fastlib.templateReplace(PARAMS,ref_dir,workdir=work_dir,RemoveRefSubFiles=True,main_file=main_file, oneSimPerDir=False)

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
    #one file per submit script
    for chunk in chunks:
        fname = chunk[0].replace(work_dir, '')
        name = fname[:-4]
        f = open(work_dir + "Submit_" + name + ".sh", "w")
        f.write('#! /bin/bash\n')
        f.write('#SBATCH --job-name=FVWcheck                     # Job name\n')
        f.write('#SBATCH --time 8:00:00\n')
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
        f.write(FAST_EXE + ' ' + fname + '\n')


        f.write('wait')
        f.close()


if __name__=='__main__':
    # --- "Global" Parameters for this script
    study = study3
    ref_dir          = './BAR_02_template/'   # Folder where the fast input files are located (will be copied)
    main_file        = 'OpenFAST_BAR_02.fst'    # Main file in ref_dir, used as a template
    work_dir         = 'BAR_02_discretization_inputs/'+study['param']+'/'          # Output folder (will be created)
    FAST_EXE = '/home/banderso2/openfast/build/glue-codes/openfast/openfast'
    npf = 1  # number of FAST runs per submission script
    # --- Generate inputs files
    fastfiles = genericStudy(study, ref_dir, work_dir, main_file)
    createSubmit(fastfiles, FAST_EXE, npf)




