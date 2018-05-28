#Programmer Edgard Luigi Sanchez
# Program calculate the MACRS
import sys
#array defined by MARCRS
THREE_YEAR = [0.3333, 0.4445, 0.1481, 0.0741]
FIVE_YEAR = [0.2, 0.32, 0.1920, 0.1152, 0.1152, 0.0576]
SEVEN_YEAR = [0.1429,0.2449, 0.1749, 0.1249, 0.0893, 0.0892, 0.0893, 0.0446]
TEN_YEAR = [0.1, 0.18, 0.144, 0.1152, 0.0922, 0.0737, 0.0655, 0.0655, 0.0656, 0.0655, 0.0328]
FIFTHEEN_YEAR = [0.05, 0.095, 0.0855, 0.077, 0.0693, 0.0623, 0.059, 0.059, 0.0591, 0.059, 0.0591, 0.059, 0.0591, 0.059, 0.0591, 0.0295]
TWENTY_YEAR = [0.0375, 0.07219, 0.06677, 0.06177, 0.05713, 0.05285, 0.04888, 0.04522, 0.04462, 0.04461, 0.04462, 0.04461, 0.04462, 0.04461, 0.04462, 0.04461, 0.04462, 0.04461, 0.04462, 0.04461, 0.02231]
dt = 0
sum_dt = 0
B = float(sys.argv[1])
choice = int(sys.argv[2])
model = []

if(choice == 3):
    model = THREE_YEAR
elif (choice == 5):
    model = FIVE_YEAR
elif (choice == 7):
    model = SEVEN_YEAR
elif choice == 10:
    model = TEN_YEAR
elif choice == 15:
    model = FIFTHEEN_YEAR
elif choice == 20:
    model = TWENTY_YEAR


for t in range(0, choice+1):
    dt = (model[t] * B)
    sum_dt += dt
    print("time : {} \tCost: {} \tdt: {}\t SUM_dt: {}\tBV: {}".format(t+1,B, dt, sum_dt, (B - sum_dt)))



