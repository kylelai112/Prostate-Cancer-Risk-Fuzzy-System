import numpy as np
from matplotlib import pyplot as plt


def gaussian(x, mu, sigma):
    r = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
    return r

def sigmoid(x,a,b):
    r=1/(1+np.exp(-a*(x-b)))
    return r

def inc(x,a,b):
    if (x<=a):
        return 0
    elif (x>=b):
        return 1
    else:
        return ((x-a)/(b-a))

def dec(x,a,b):
    return(1-inc(x,a,b))

def valuevalidate1(ques):
    while True:
        try:
            num1 = int(input(ques))
        except ValueError:
            print("Invalid input. Please enter a integer number.\n")
            continue
        if num1 < 0 or num1 >5:
            print("Invalid input.Please enter a number range from 0-5.\n")
            continue
        else:
            break
    return num1

def valuevalidate2(ques):
    while True:
        try:
            num1 = float(input(ques))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue
        if num1 < 15 or num1 >100:
            print("Invalid input.Please enter a number range from 15-100.\n")
            continue
        else:
            break
    return num1

def valuevalidate3(ques):
    while True:
        try:
            num1 = float(input(ques))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue
        if num1 < 0 or num1 >10:
            print("Invalid input.Please enter a number range from 0-10.\n")
            continue
        else:
            break
    return num1

def valuevalidate4(ques):
    while True:
        try:
            num1 = float(input(ques))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue
        if num1 < 15 or num1 >80:
            print("Invalid input.Please enter a number range from 15-80.\n")
            continue
        else:
            break
    return num1


def valuevalidate5(ques):
    while True:
        try:
            num1 = int(input(ques))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue
        if num1 < 0 or num1 >5:
            print("Invalid input.You can only select an integer from 0 to 5.\n")
            continue
        else:
            break
    return num1

def RuleEvaluate(ip1, ip2, ip3, ip4, op):
    ipR = np.fmin(np.fmin(np.fmin(ip1, ip2), ip3 ), ip4)
    opR = np.fmin(ipR, op)

    return opR

def RuleAggregate(R1, R2, R3, R4, R5):
    RA = np.fmax(np.fmax(np.fmax(R1, R2), R3 ), R4)
    TRA = np.fmax(R5, RA)

    return TRA




# display = np.linspace(0, 1000, 10000)
# # g = gaussian(display, 500, 60)
# # s = sigmoid(display, 0.02, 500)
# incNum = np.zeros_like(display)
# decNum = np.zeros_like(display)
# for i in range(0,len(display)):
#     incNum[i] = inc(display[i], 300, 600)
#     decNum[i] = dec(display[i], 300, 600)
#
# # print(g[2500])
#
# plt.figure(0)
# plt.plot(display, incNum, label="Very Cold")
# plt.plot(display, decNum, label="Very Cold")
# plt.legend()
# plt.show()
