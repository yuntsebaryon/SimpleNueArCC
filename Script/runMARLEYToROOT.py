#!/usr/bin/env python

import os

if __name__ == "__main__":

    dir = '/Users/yuntse/data/coherent/preLArTPC/marley/outFiducial'
    nFiles = 40

    for iFile in range( nFiles ):
        infile = f'{dir}/nueArCC_sns_yDir_{iFile:02d}.ascii'
        outfile = f'{dir}/nueArCC_sns_yDir_{iFile:02d}.root'

        cmd = f'root -q -b \'MARLEYToROOT.C("{infile}", "{outfile}")\''
        print( cmd )
        os.system( cmd )