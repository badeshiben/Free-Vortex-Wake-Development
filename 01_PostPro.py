import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fastlib
import weio


WS        = [5 ,10]
regFactor = np.linspace(0.5, 5, 3)
work_dir    = 'SampleOutputs/'          # Output folder 
ExampleFst  = 'BAR/Main_OpenFAST_BAR_00.fst' # Some kind of fst file to get radial data

#--- Simple Postprocessing
# - Open all the output files,
# - Average the quantities over the last revolution
# - Return a dataframe, sorted by Wind Speed
dfs=[] # results per wind speed
# Postprocessing files, wind speed per wind speed
for ws in WS: 
    outFiles=[]
    for i,reg in enumerate(regFactor): 
        case     ='ws{:04.1f}_reg{:06.4f}'.format(ws, reg)
        filename = os.path.join(work_dir, case + '.outb' )
        outFiles.append(filename)
    dfAvg = fastlib.averagePostPro(outFiles,avgMethod='periods',avgParam=1,ColMap={'WS_[m/s]':'Wind1VelX_[m/s]'})
    dfAvg.insert(0,'Reg_[m]', regFactor)
    # --- Save to csv since step above can be expensive 
    dfAvg.to_csv('Results_ws{:04.1f}.csv'.format(ws),sep='\t',index=False)
    #print(dfAvg)


# --- Plotting mean quantities
fig,ax = plt.subplots(1, 1, sharey=False, figsize=(6.4,4.8)) # (6.4,4.8)
fig.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.11, hspace=0.20, wspace=0.20)
for ws in WS: 
    df = pd.read_csv('Results_ws{:04.1f}.csv'.format(ws),sep='\t')
    ax.plot(df['Reg_[m]'], df['RotThrust_[kN]'], 'o-',  label='WS = {:}'.format(ws))
ax.set_xlabel('Reg. param [m]')
ax.set_ylabel('Thrust [kN]')
ax.legend()
ax.tick_params(direction='in')
# 
# --- Plotting radial data quantities
fig,ax = plt.subplots(1, 1, sharey=False, figsize=(6.4,4.8)) # (6.4,4.8)
fig.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.11, hspace=0.20, wspace=0.20)
for ws in WS: 
    # Extract radial 
    df = pd.read_csv('Results_ws{:04.1f}.csv'.format(ws),sep='\t')
    M_AD, Col_AD, _, _, _, _=fastlib.spanwisePostProRows(df, FST_In=ExampleFst)
    for i,reg in enumerate(regFactor): 
        dfRad=pd.DataFrame(data=M_AD[i,:,:], columns=Col_AD)
        ax.plot(dfRad['r/R_[-]'], dfRad['B1AxInd_[-]'], label='WS = {:}, reg={:}'.format(ws,reg))
ax.set_xlabel('r [m]')
ax.set_ylabel('axial induction [-]')
ax.legend()
ax.tick_params(direction='in')

plt.show()
