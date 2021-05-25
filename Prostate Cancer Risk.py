import Function as fc
import numpy as np
from matplotlib import pyplot as plt

## Define Membership for input and output

# Input1 Heredity Mship
heredity = np.linspace(0, 5, 500)

def Normal(x):
    r = fc.sigmoid(x, -5, 1.5)
    return r

def High(x):
    r = fc.sigmoid(x, 5, 2)
    return r

GraphNormal = Normal(heredity)
GraphHigh = High(heredity)


# Input2 Age Mship
age = np.linspace(15, 100, 500)

def Young(x):
    r = fc.sigmoid(x, -0.4, 45)
    return r

def Old(x):
    r = fc.sigmoid(x, 0.3, 50)
    return r

GraphYoung = Young(age)
GraphOld = Old(age)


# Input3 PSA lvl Mship
PSA = np.linspace(0, 10, 500)

def LowLvl(x):
    r = fc.sigmoid(x, -5, 1.5)
    return r

def MiddleLvl(x):
    r = fc.gaussian(x, 3, 0.7)
    return r

def HighLvl(x):
    r = fc.sigmoid(x, 3, 3.5)
    return r

GraphLowLvl = LowLvl(PSA)
GraphMiddleLvl = MiddleLvl(PSA)
GraphHighLvl = HighLvl(PSA)


# Input4 PV Mship
PV = np.linspace(15, 80, 500)

def SmallSize(x):
    r = fc.sigmoid(x, -0.5, 35)
    return r

def MediumSize(x):
    r = fc.gaussian(x, 50, 7.5)
    return r

def LargeSize(x):
    r = fc.sigmoid(x, 0.5, 65)
    return r

GraphSmallSize = SmallSize(PV)
GraphMediumSize = MediumSize(PV)
GraphLargeSize = LargeSize(PV)


# Output PCR Mship
PCR = np.linspace(0, 100, 500)

def LowRisk(x):
    r = fc.sigmoid(x, -0.2, 30)
    return r

def IntermediateRisk(x):
    r = fc.gaussian(x, 50, 12)
    return r

def HighRisk(x):
    r = fc.sigmoid(x, 0.4, 75)
    return r

GraphLowRisk = LowRisk(PCR)
GraphIntermediateRisk = IntermediateRisk(PCR)
GraphHighRisk = HighRisk(PCR)


## Loop for keep asking until user request to stop
cont = 5
while(cont != 0):
    # Getting all inputs
    Hmsg = "\nPlease enter the Heredity info \n" \
           "(0- No history, 1- Not Sure, 2- Maybe 1," \
           "\n3- 1 family member," \
           "\n4- maybe 2 or more, 5- 2 or more)\t\t\t: "
    if cont==1:
        InHeredity = fc.valuevalidate1(Hmsg)
    elif cont==2:
        InAge = fc.valuevalidate2("Please enter the age (15-100)\t\t\t\t: ")
    elif cont==3:
        InPSA = fc.valuevalidate3("Please enter the PSA Level (0-10)ng/mL\t\t: ")
    elif cont == 4:
        InPV = fc.valuevalidate4("Please enter the Prostate Volume (15-80)cc\t: ")
    else:
        InHeredity = fc.valuevalidate1(Hmsg)
        InAge = fc.valuevalidate2("Please enter the age (15-100)\t\t\t\t: ")
        InPSA = fc.valuevalidate3("Please enter the PSA Level (0-10)ng/mL\t\t: ")
        InPV = fc.valuevalidate4("Please enter the Prostate Volume (15-80)cc\t: ")


    # Mship of each inputs.
    MemNormal = Normal(InHeredity)
    MemHigh = High(InHeredity)
    print("\nThe Membership of Normal Heredity is\t", "%.4f" % MemNormal)
    print("The Membership of High Heredity is\t\t", "%.4f" % MemHigh)

    MemYoung = Young(InAge)
    MemOld = Old(InAge)
    print("The Membership of Young Age is\t\t\t", "%.4f" % MemYoung)
    print("The Membership of Old Age is\t\t\t", "%.4f" % MemOld)

    MemLowLvl = LowLvl(InPSA)
    MemMiddleLvl = MiddleLvl(InPSA)
    MemHighLvl = HighLvl(InPSA)
    print("The Membership of Low Level PSA is\t\t", "%.4f" % MemLowLvl)
    print("The Membership of Middle Level PSA is\t", "%.4f" % MemMiddleLvl)
    print("The Membership of High Level PSA is\t\t", "%.4f" % MemHighLvl)

    MemSmallSize = SmallSize(InPV)
    MemMediumSize = MediumSize(InPV)
    MemLargeSize = LargeSize(InPV)
    print("The Membership of Small Size PV is\t\t", "%.4f" % MemSmallSize)
    print("The Membership of Medium Size PV is\t\t", "%.4f" % MemMediumSize)
    print("The Membership of Large Size PV is\t\t", "%.4f" % MemLargeSize)


    ## Rules Evaluation
    # R1: (Normal Heredity) and (Young Age) and (Low Level PSA) and (Small Size PV) have (Low Risk PCR)
    R1 = fc.RuleEvaluate(MemNormal, MemYoung, MemLowLvl, MemSmallSize, GraphLowRisk)

    # R2: (Normal Heredity) and (Young Age) and (Low Level PSA) and (Medium Size PV) have (Low Risk PCR)
    R2 = fc.RuleEvaluate(MemNormal, MemYoung, MemLowLvl, MemMediumSize, GraphLowRisk)

    # R3: (Normal Heredity) and (Young Age) and (Low Level PSA) and (Large Size PV) have (Low Risk PCR)
    R3 = fc.RuleEvaluate(MemNormal, MemYoung, MemLowLvl, MemLargeSize, GraphLowRisk)

    # R4: (Normal Heredity) and (Young Age) and  (Middle Level PSA) and (Small Size PV) have (Intermediate Risk PCR)
    R4 = fc.RuleEvaluate(MemNormal, MemYoung, MemMiddleLvl, MemSmallSize, GraphIntermediateRisk)

    # R5: (Normal Heredity) and (Young Age) and (Middle Level PSA) and (Medium Size PV) have (Low Risk PCR)
    R5 = fc.RuleEvaluate(MemNormal, MemYoung, MemMiddleLvl, MemMediumSize, GraphLowRisk)

    # R6: (Normal Heredity) and (Young Age) and (Middle Level PSA) and (Large Size PV) have (Low Risk PCR)
    R6 = fc.RuleEvaluate(MemNormal, MemYoung, MemMiddleLvl, MemLargeSize, GraphLowRisk)

    # R7: (Normal Heredity) and (Young Age) and  (High Level PSA) and (Small Size PV) have (Intermediate Risk PCR)
    R7 = fc.RuleEvaluate(MemNormal, MemYoung, MemHighLvl, MemSmallSize, GraphIntermediateRisk)

    # R8: (Normal Heredity) and (Young Age) and (High Level PSA) and (Medium Size PV) have (Intermediate Risk PCR).
    R8 = fc.RuleEvaluate(MemNormal, MemYoung, MemHighLvl, MemMediumSize, GraphIntermediateRisk)

    # R9: (Normal Heredity) and (Young Age) and (High Level PSA) and (Large Size PV) have (Low Risk PCR)
    R9 = fc.RuleEvaluate(MemNormal, MemYoung, MemHighLvl, MemLargeSize, GraphLowRisk)

    # R10: (Normal Heredity) and (Old Age)  and (Low Level PSA) and (Small Size PV) have (Low Risk PCR)
    R10 = fc.RuleEvaluate(MemNormal, MemOld, MemLowLvl, MemSmallSize, GraphLowRisk)

    # R11: (Normal Heredity) and (Old Age)  and (Low Level PSA) and (Medium Size PV) have (Low Risk PCR)
    R11 = fc.RuleEvaluate(MemNormal, MemOld, MemLowLvl, MemMediumSize, GraphLowRisk)

    # R12: (Normal Heredity) and (Old Age)  and (Low Level PSA) and (Large Size PV) have (Low Risk PCR)
    R12 = fc.RuleEvaluate(MemNormal, MemOld, MemLowLvl, MemLargeSize, GraphLowRisk)

    # R13: (Normal Heredity) and (Old Age)  and  (Middle Level PSA) and (Small Size PV) have (Intermediate Risk PCR)
    R13 = fc.RuleEvaluate(MemNormal, MemOld, MemMiddleLvl, MemSmallSize, GraphIntermediateRisk)

    # R14: (Normal Heredity) and (Old Age)  and (Middle Level PSA) and (Medium Size PV) have (Low Risk PCR)
    R14 = fc.RuleEvaluate(MemNormal, MemOld, MemMiddleLvl, MemMediumSize, GraphLowRisk)

    # R15: (Normal Heredity) and (Old Age)  and (Middle Level PSA) and (Large Size PV) have (Low Risk PCR)
    R15 = fc.RuleEvaluate(MemNormal, MemOld, MemMiddleLvl, MemLargeSize, GraphLowRisk)

    # R16: (Normal Heredity) and (Old Age)  and  (High Level PSA) and (Small Size PV) have (High Risk PCR)
    R16 = fc.RuleEvaluate(MemNormal, MemOld, MemHighLvl, MemSmallSize, GraphHighRisk)

    # R17: (Normal Heredity) and (Old Age)  and (High Level PSA) and (Medium Size PV) have (Intermediate Risk PCR).
    R17 = fc.RuleEvaluate(MemNormal, MemOld, MemHighLvl, MemMediumSize, GraphIntermediateRisk)

    # R18: (Normal Heredity) and (Old Age)  and (High Level PSA) and (Large Size PV) have (Intermediate Risk PCR)
    R18 = fc.RuleEvaluate(MemNormal, MemOld, MemHighLvl, MemLargeSize, GraphIntermediateRisk)

    # R19: (High  Heredity) and (Young Age) and (Low Level PSA) and (Small Size PV) have (Low Risk PCR)
    R19 = fc.RuleEvaluate(MemHigh, MemYoung, MemLowLvl, MemSmallSize, GraphLowRisk)

    # R20: (High  Heredity) and (Young Age) and (Low Level PSA) and (Medium Size PV) have (Low Risk PCR)
    R20 = fc.RuleEvaluate(MemHigh, MemYoung, MemLowLvl, MemMediumSize, GraphLowRisk)

    # R21: (High  Heredity) and (Young Age) and (Low Level PSA) and (Large Size PV) have (Low Risk PCR)
    R21 = fc.RuleEvaluate(MemHigh, MemYoung, MemLowLvl, MemLargeSize, GraphLowRisk)

    # R22: (High  Heredity) and (Young Age) and  (Middle Level PSA) and (Small Size PV) have (Intermediate Risk PCR)
    R22 = fc.RuleEvaluate(MemHigh, MemYoung, MemMiddleLvl, MemSmallSize, GraphIntermediateRisk)

    # R23: (High  Heredity) and (Young Age) and (Middle Level PSA) and (Medium Size PV) have (Intermediate Risk PCR)
    R23 = fc.RuleEvaluate(MemHigh, MemYoung, MemMiddleLvl, MemMediumSize, GraphIntermediateRisk)

    # R24: (High  Heredity) and (Young Age) and (Middle Level PSA) and (Large Size PV) have (Low Risk PCR)
    R24 = fc.RuleEvaluate(MemHigh, MemYoung, MemMiddleLvl, MemLargeSize, GraphLowRisk)

    # R25: (High  Heredity) and (Young Age) and  (High Level PSA) and (Small Size PV) have (High Risk PCR)
    R25 = fc.RuleEvaluate(MemHigh, MemYoung, MemHighLvl, MemSmallSize, GraphHighRisk)

    # R26: (High  Heredity) and (Young Age) and (High Level PSA) and (Medium Size PV) have (Intermediate Risk PCR).
    R26 = fc.RuleEvaluate(MemHigh, MemYoung, MemHighLvl, MemMediumSize, GraphIntermediateRisk)

    # R27: (High  Heredity) and (Young Age) and (High Level PSA) and (Large Size PV) have (Intermediate Risk PCR)
    R27 = fc.RuleEvaluate(MemHigh, MemYoung, MemHighLvl, MemLargeSize, GraphIntermediateRisk)

    # R28: (High  Heredity) and (Old Age)  and (Low Level PSA) and (Small Size PV) have (Intermediate Risk PCR)
    R28 = fc.RuleEvaluate(MemHigh, MemOld, MemLowLvl, MemSmallSize, GraphIntermediateRisk)

    # R29: (High  Heredity) and (Old Age)  and (Low Level PSA) and (Medium Size PV) have (Intermediate Risk PCR)
    R29 = fc.RuleEvaluate(MemHigh, MemOld, MemLowLvl, MemMediumSize, GraphIntermediateRisk)

    # R30: (High  Heredity) and (Old Age)  and (Low Level PSA) and (Large Size PV) have (Low Risk PCR)
    R30 = fc.RuleEvaluate(MemHigh, MemOld, MemLowLvl, MemLargeSize, GraphLowRisk)

    # R31: (High  Heredity) and (Old Age)  and  (Middle Level PSA) and (Small Size PV) have (High Risk PCR)
    R31 = fc.RuleEvaluate(MemHigh, MemOld, MemMiddleLvl, MemSmallSize, GraphHighRisk)

    # R32: (High  Heredity) and (Old Age)  and (Middle Level PSA) and (Medium Size PV) have (Intermediate Risk PCR)
    R32 = fc.RuleEvaluate(MemHigh, MemOld, MemMiddleLvl, MemMediumSize, GraphIntermediateRisk)

    # R33: (High  Heredity) and (Old Age)  and (Middle Level PSA) and (Large Size PV) have (Intermediate Risk PCR)
    R33 = fc.RuleEvaluate(MemHigh, MemOld, MemMiddleLvl, MemLargeSize, GraphIntermediateRisk)

    # R34: (High  Heredity) and (Old Age)  and  (High Level PSA) and (Small Size PV) have (High Risk PCR)
    R34 = fc.RuleEvaluate(MemHigh, MemOld, MemHighLvl, MemSmallSize, GraphHighRisk)

    # R35: (High  Heredity) and (Old Age)  and (High Level PSA) and (Medium Size PV) have (High Risk PCR).
    R35 = fc.RuleEvaluate(MemHigh, MemOld, MemHighLvl, MemMediumSize, GraphHighRisk)

    # R36: (High  Heredity) and (Old Age)  and (High Level PSA) and (Large Size PV) have (High Risk PCR)
    R36 = fc.RuleEvaluate(MemHigh, MemOld, MemHighLvl, MemLargeSize, GraphHighRisk)



    ## Rules Aggregation
    RA1 = fc.RuleAggregate(R1, R2, R3, R4, R5)
    RA2 = fc.RuleAggregate(R6, R7, R8, R9, R10)
    RA3 = fc.RuleAggregate(R11, R12, R13, R14, R15)
    RA4 = fc.RuleAggregate(R16, R17, R18, R19, R20)
    RA5 = fc.RuleAggregate(R21, R22, R23, R24, R25)
    RA6 = fc.RuleAggregate(R26, R27, R28, R29, R30)
    RA7 = fc.RuleAggregate(R31, R32, R33, R34, R35)

    TRA = fc.RuleAggregate(RA1, RA2, RA3, RA4, RA5)
    R = np.fmax(np.fmax(np.fmax(RA6, RA7), TRA), R36)


    ## Average PCR by Centroid method defuzzification
    PCRisk = np.trapz(R*PCR, PCR)/np.trapz(R, PCR)
    print("\nThe risk of developing prostate cancer is ", "%.4f" % PCRisk, "%")
    print("\n\nPlease close the 2 graph figures to continue.")

    ## Plot Mship graph
    plt.figure(0)
    plt.subplot(2, 2, 1)
    plt.title(label="Heredity Membership")
    plt.plot(heredity, GraphNormal, label="Normal")
    plt.plot(heredity, GraphHigh, label="High")
    plt.scatter([InHeredity, InHeredity], [MemNormal, MemHigh], marker='s')
    plt.xlabel("Heredity Input")
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.title(label="Age Membership")
    plt.plot(age, GraphYoung, label="Young")
    plt.plot(age, GraphOld, label="Old")
    plt.scatter([InAge, InAge], [MemYoung, MemOld], marker='s')
    plt.xlabel("Age Input")
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.title(label="PSA Membership")
    plt.plot(PSA, GraphLowLvl, label="Low Level")
    plt.plot(PSA, GraphMiddleLvl, label="Middle Level")
    plt.plot(PSA, GraphHighLvl, label="High Level")
    plt.scatter([InPSA, InPSA, InPSA], [MemLowLvl, MemMiddleLvl, MemHighLvl], marker='s')
    plt.xlabel("PSA Level Input (ng/mL)")
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.title(label="Prostate Volume Membership")
    plt.plot(PV, GraphSmallSize, label="Small Size")
    plt.plot(PV, GraphMediumSize, label="Medium Size")
    plt.plot(PV, GraphLargeSize, label="Large size")
    plt.scatter([InPV, InPV, InPV], [MemSmallSize, MemMediumSize, MemLargeSize], marker='s')
    plt.xlabel("PV Input (cc)")
    plt.legend()

    plt.figure(1)
    plt.title(label="Prostate Cancer Risk Membership")
    plt.plot(PCR, GraphLowRisk, label="Low Risk")
    plt.plot(PCR, GraphIntermediateRisk, label="Intermediate Risk")
    plt.plot(PCR, GraphHighRisk, label="High Risk")
    plt.fill_between(PCR, R, color=(1, 0, 0))
    plt.scatter([PCRisk], [0], marker='s')
    plt.xlabel("Risk (%)")
    plt.legend()
    plt.show()


    ## Ask for cont
    cmsg ="\nPlease choose your option:" \
          "\n 0 - Exit the System " \
          "\n 1 - Only edit the Heredity input" \
          "\n 2 - Only edit the Age input" \
          "\n 3 - Only edit the PSA input" \
          "\n 4 - Only edit the Prostate Volume input" \
          "\n 5 - Continue by re-enter all input values" \
          "\n Enter here: "
    cont = fc.valuevalidate5(cmsg)


print("\n\nThank you for using this system")

