#!/usr/bin/env python
import numpy as np
import os

if __name__ == "__main__":

    jsonDir = '/Users/yuntse/data/coherent/preLArTPC/marley/2024/json'
    outDir = '/Users/yuntse/data/coherent/preLArTPC/marley/2024'
    nFiles = 10
    nEvtsPerFile = 10000

    for iFile in range( nFiles ):

        seed = np.random.randint(0, 2**32, dtype = np.uint32)
        jsonF = f'{jsonDir}/nueArCC_sns_yDir_{iFile:02d}.js'
        with open( jsonF, 'w') as f:
            f.write(
f'''
{{
  seed: {seed},
  direction: {{ x: 0.0, y: 1.0, z: 0.0 }},
  target: {{
    nuclides: [ 1000180400 ],
    atom_fractions: [ 1.0 ],
  }},
  reactions: [ "ve40ArCC_Bhattacharya2009.react" ],
  source: {{
    type: "dar",
    neutrino: "ve",
  }},
  executable_settings: {{
    events: {nEvtsPerFile}, 
    output: [ {{ file: "{outDir}/nueArCC_sns_yDir_{iFile:02d}.ascii", format: "ascii", mode: "overwrite" }} ],
  }},
}}
'''
)

        cmd = f'marley {jsonF}'
        os.system( cmd )