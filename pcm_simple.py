
from __future__ import print_function

# import the m5 (gem5) library created when gem5 is built
import m5
# import all of the SimObjects
from m5.objects import *

# Add the common scripts to our path
m5.util.addToPath('../../')

# import the caches which we made
from caches import *

# import the SimpleOpts module
from common import SimpleOpts

class pcm_simple(DDR3_1600_8x8):
    # DDR3-1600 11-11-11
    tRCD = '120ns'
    tWR = '7.5ns'
