import math

loanData = {
    "amount": [45000, 93000, 43000, 10000, 12000],
    "interestRate": (1000, 2000, 900, 100, 300),
    "paybackTime": {1, 2, 3, 4, 5}
}

compoundings = 4
regularpayment = 1000
numberofpayment = 6
alreadymadepayment = 2


def calcSimpleInterest(principal, interest, time):
    return principal * interest * time


def calcCoumpoundInterest(principal, interest, time, compoundings):
    return principal * math.pow((1 + (interest / compoundings)), compoundings * time)


def calcEffectiveRate(interest, compoundings):
    return (math.pow(1 + (interest / compoundings), compoundings)) - 1


def calcAmortizedLoanPayment(pricipal, interest, compoundings):
    return (pricipal * interest) / (1 - math.pow((1 + interest), compoundings))


def calcRemainingBalancs(regularpayment, interest, numberofpayment, alreadymadepayment):
    return regularpayment * ((1 - math.pow((1 + interest), -(numberofpayment - alreadymadepayment))) / interest)


def getInput():
    return (loanData["amount"], loanData["interestRate"], loanData["paybackTime"])

def compute(amount,interest,paybackTime):
    SI=list()
    CI=list()
    ER=list()
    ALP=list()
    RB=list()
    for x in range(len(amount)):
        SI.append(calcSimpleInterest(amount[x],interest[x],4))
        CI.append(calcCoumpoundInterest(amount[x],interest[x],3,compoundings))
        ER.append(calcEffectiveRate(interest[x],compoundings))
        ALP.append(calcAmortizedLoanPayment(amount[x],interest[x],compoundings))
        RB.append(calcRemainingBalancs(regularpayment,interest[x],numberofpayment,alreadymadepayment))

    return (SI,CI,ER,ALP,RB)
def outputValue(simpleintetest,compoundinterest,effeciverate,amortizeloanpayment,remainingbalance,Loaddata):
    loanData["simpleinterst"]=simpleintetest
    loanData["compoundinterest"]=compoundinterest
    loanData["effectiverate"]=effeciverate
    loanData["amortizeloanpayment"]=amortizeloanpayment
    loanData["remainingbalance"]=remainingbalance

    print(loanData)

A,IR,PT=getInput()
SI,CI,ER,ALP,RB=compute(A,IR,PT)
outputValue(SI,CI,ER,ALP,RB,loanData)