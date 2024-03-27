#!/usr/bin/env python

import os

if __name__ == "__main__":

    indir  = '/Users/yuntse/data/coherent/preLArTPC/marley/outFiducial'
    outdir = '/Users/yuntse/data/coherent/preLArTPC/geant4/nueArCCoutFiducial'
    nEventPerFile = 10000
    nFiles = 40

    for iFile in range(nFiles):

        script = f'{outdir}/mac/run_nueArCC{iFile:02d}.mac'
        infile = f'{indir}/nueArCC_sns_yDir_{iFile:02d}.root'
        outfile = f'{outdir}/nueArCC_sns_yDir_g4_{iFile:02d}.root'

        with open( script, 'w') as f:
            f.write(f"""
/LArG4/generator/infile {infile}
/LArG4/output/outfile {outfile}
/run/beamOn {nEventPerFile}
""")
            
        cmd = f'./SimpleLArG4 {script}'
        os.system( cmd )
