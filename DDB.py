# Programmer: Edgard Luigi Sanchez
# program: This program will use the Double-declining method
#           to calculate the yearly depreciation

import sys

# B_str = raw_input("Cost Basis: ")
# SV_str= raw_input("Salvage value: ")
# N_str = raw_input("Depreciable life: ")

B_str = sys.argv[1]
SV_str= sys.argv[2]
N_str = sys.argv[3]

B = float(B_str)
SV = float(SV_str)
N = int(N_str)

# DDB variables
d_t = 0
sum_d_t = 0
BV_t = 0

# SL variables
sl_BV_t = 0
sl_d_t = 0
sl_sum_dt = 0

for t in range(1, N+1):
    BV_t =  B - sum_d_t
    d_t = (2.0/float(N))*(BV_t)
    d_t = round(d_t)

    # SL
    sl_sum_dt = sum_d_t
    # BV_t of SL is from previous BV w/o depreciation
    sl_BV_t = BV_t

    # DDB
    sum_d_t += d_t
    BV_t = B - sum_d_t
    hasPrinted = False

    if (SV <= BV_t):
        sl_d_t = (B - sl_sum_dt - SV) / (N - t + 1)
        sl_d_t = round(sl_d_t)

        if(d_t < sl_d_t):

            newSum = sum_d_t + (sl_d_t - d_t)
            newBV = BV_t - (sl_d_t - d_t)
            new_dt  = sl_d_t
            print("===================DDB_dt < SL_dt====================")
            # print("time: {}\t     new dt:{} \t new SUM-dt: {} \t new BV: {}".format(t,d_t, sum_d_t, BV_t))
            print("time: {}\t      dt: {} --> {} \t SUM-dt: {} --> {} \t  BV: {} --> {}".format(t,d_t, new_dt, sum_d_t, newSum, BV_t, newBV))
            sum_d_t += sl_d_t - d_t
            BV_t -= sl_d_t - d_t
            d_t = sl_d_t
            hasPrinted = True

    else:
        SV_diff = SV - BV_t
        print("======@@ SV: {} \t BV: {} \t --> GIVE BACK: {}  From old dt: {} --> {}  @@=====".format(SV, BV_t, SV_diff, d_t, (d_t - SV_diff)))
        d_t -= SV_diff
        sum_d_t -= SV_diff
        BV_t += SV_diff

    if(not hasPrinted):
        print("time: {}\t     dt:{} \t    SUM-dt: {} \t  BV: {}".format(t,d_t, sum_d_t, BV_t))
        hasPrinted = False
