# Programmer: Edgard Luigi Sanchez
# program: calculate depreciation per year using Straight-Line method

# B = float(raw_input("Cost Basis: "))
# SV= float(raw_input("Salvage value: "))
# N = int(raw_input("Depreciable life: "))
import sys

B_str = sys.argv[1]
SV_str= sys.argv[2]
N_str = sys.argv[3]

B = float(B_str)
SV = float(SV_str)
N = int(N_str)


# print("\nB: " + str(B) + " SV: "+ str(SV) + " N: "+ str(N))
sum_d_t = 0
BV_t = B
d_t = (B - SV)/N

print("dt = $" + str(d_t))
for t in range(1,N+1):
    sum_d_t += d_t
    BV_t = B - sum_d_t
    print("time: {} \t dt: {} \t SUM-dt: {} \t BV: {}".format(t, d_t, sum_d_t, BV_t))

