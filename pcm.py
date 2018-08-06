
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

class pcm(DRAMCtrl):
    # size of device in bytes
    write_buffer_size = 32

    device_size = '512MB'
    
    channels = 4

    # 8x8 configuration, 8 devices each with an 8-bit interface
    device_bus_width = 8

    # DDR3 is a BL8 device
    burst_length = 8

    # Each device has a page (row buffer) size of 1 Kbyte (1K columns x8)
    device_rowbuffer_size = '1kB'

    # 8x8 configuration, so 8 devices
    devices_per_rank = 8

    # Use one rank
    ranks_per_channel = 1

    # DDR3 has 8 banks in all configurations
    banks_per_rank = 8

    # 400 MHz
    tCK = '2.5ns'

    # 8 beats across an x64 interface translates to 4 clocks @ 800 MHz
    tBURST = '10ns'

    # DDR3-1600 11-11-11
    tRCD = '120ns'
    tCCD_L = '10ns'
    tCCD_L_WR = '10ns'
    tCL = '12.5ns'
    tRP = '150ns'
    tRAS = '42.5ns'
    tRRD = '6ns'
    tXAW = '30ns'
    activation_limit = 4
    tRFC = '260ns'

    tWR = '15ns'

    # Greater of 4 CK or 7.5 ns
    tWTR = '7.5ns'

    # Greater of 4 CK or 7.5 ns
    tRTP = '7.5ns'

    # Default same rank rd-to-wr bus turnaround to 2 CK, @800 MHz = 2.5 ns
    tRTW = '2.5ns'

    # Default different rank bus delay to 2 CK, @800 MHz = 2.5 ns
    tCS = '2.5ns'

    # <=85C, half for >85C
    tREFI = '7.8us'

    # active powerdown and precharge powerdown exit time
    tXP = '6ns'

    # self refresh exit time
    tXS = '270ns'

    # Current values from datasheet Die Rev E,J
    IDD0 = '55mA'
    IDD2N = '32mA'
    IDD3N = '38mA'
    IDD4W = '125mA'
    IDD4R = '157mA'
    IDD5 = '235mA'
    IDD3P1 = '38mA'
    IDD2P1 = '32mA'
    IDD6 = '20mA'
    VDD = '1.5V'
