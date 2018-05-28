# Programmer: Edgard Luigi Sanchez
# program: SOYD (Sum of the years digit) depreciation method
#           for Engineering economics


import sys
B_str = sys.argv[1]
SV_str= sys.argv[2]
N_str = sys.argv[3]


B = float(B_str)
SV = float(SV_str)
N = int(N_str)


# find SOYD
SOYD = N*(N + 1)/2

sum_d_t = 0
BV_t = 0
for t in range(1, N+1):
    d_t = round((float((N - t + 1))/(SOYD))*(B - SV))
    sum_d_t += d_t
    BV_t = (B - sum_d_t)

    print("time: {} \t dt: {} \t SUM-dt: {} \t BV: {}".format(t, d_t, sum_d_t, BV_t))
