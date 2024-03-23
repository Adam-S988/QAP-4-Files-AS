# Description: A program designed to help One Stop Insurance Company enter/calculate insurance policy information for the customers
# Author: Adam Stevenson
# Date(s): March 14-22, 2024


# Define required libraries.
import Functions
import datetime

# Define program constants.
CLAIM_NUMBER = 1944
CLAIM_NUMBER = int(CLAIM_NUMBER)
FIRST_AUTO = 869.00
XTRA_AUTO_RATE = 0.25
XTRA_LIABILITY = 130.00
GLASS_COVER = 86.00
LOAN_CAR = 58.00
HST_RATE = 0.15
MONTHLY_PAY = 8
PROCESS_FEE = 39.99
TODAY = datetime.date.today()


# Define program functions.
# All functions used are located in the Functions Library

CustCtr = 1943
# Main program starts here.
while True:
    PayDate = Functions.FirstMonthDate("Date")

    # #Initialize counters and accumulators.

    # Gather user inputs.
    CustCtr += 1
    while True:
        FirstName = "Sally" #input("Enter the customer's first name: ").title()
        if FirstName == "":
            print()
            print("Data entry error - must fill out the customer's first name.")
            print()
        elif FirstName.upper() == "END":
            break
        else:
            FirstName = FirstName.title()
            break

    while True:
        LastName = "Sparrow" #input("Enter the customer's last name: ").title()
        if LastName == "":
            print()
            print("Data entry error - must fill out the customer's last name.")
            print()
        else:
            LastName = LastName.title()
            break

    while True:
        StAdd = "123 Funny Lane" #input("Enter the customer's street address: ")
        if StAdd == "":
            print()
            print("Data entry error - must fill out the customer's street address.")
            print()
        else:
            break

    while True:
        City = "Funnyville" #input("Enter the customer's city: ").title()
        if City == "":
            print()
            print("Data entry error - must fill out the customer's city.")
            print()
        else:
            break

    ProvLst = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "SK", "AB", "BC", "NT", "YT", "NV"]
    while True:
        Prov = "NL" #input("Enter the cusomer's province (XX): ").upper()
        if Prov == "":
            print()
            print("Data entry error - province cannot be blank")
            print()
        elif len(Prov) != 2:
            print()
            print("Data entry error - must be 2 characters")
            print()
        elif Prov not in ProvLst:
            print()
            print("Data entry error - invalid Province")
            print()
        else:
            break
        
    PostalCode = "s2s2s2" #Functions.PostalCode("Enter the customer's postal code: ")

    while True:
        PhNum = "7091234567" #input("Enter the customer's phone number (##########): ")
        if PhNum.isdigit() == False:
            print()
            print("Data entry error - phone number must be digits.")
            print()
        elif len(PhNum) != 10:
            print()
            print("Data entry error - phone number must be 10 digits.")
            print()
        else:
            break
    
    while True:
        try:
            CarsInsured = 1 #input("Enter the number of cars to be insured: ")
            CarsInsured = int(CarsInsured)
        except:
            print()
            print("Data entry error - must enter a valid integer.")
            print()
        else:
            if CarsInsured < 1:
                print()
                print("Data entry error - must insure at least 1 vehicle.")
                print()
            else:
                break


    XtraLiability = "Y" #Functions.YesOrNo("Does the customer desire extra liability up to $1,000,000 (Y/N): ")
    GlassCover = "N" #Functions.YesOrNo("Does the customer desire glass coverage (Y/N): ")
    LoanCar = "N" #Functions.YesOrNo("Does the customer require a loaner car (Y/N): ")
    
    PayMethodLst = ["Full", "Monthly"]
    while True:
        PayMethod = input("What is the payment method the customer is going to pay with (Full/Monthly): ").title()
        if PayMethod == "":
            print()
            print("Data entry error - payment method cannot be blank")
            print()
        elif PayMethod not in PayMethodLst:
            print()
            print("Data entry error - invalid payment method")
            print()
        else:
            break

    while True:
        if PayMethod == "Monthly":
            DoDownPay = Functions.YesOrNo("Would the customer like to put a down payment on the insurance (Y/N): ")
            if DoDownPay == "Y":
                try:
                    DownPay = input("Enter the amount of the down payment: ")
                    DownPay = float(DownPay)
                except:
                    print()
                    print("Data entry error - must enter a valid integer.")
                    print()
                else:
                    if DownPay <= 0:
                        print()
                        print("Data entry error - must put down money for a down payment.")
                        print()
                    else:
                        break
            else:
                DownPay = 0
                break
        else:
            DownPay = 0
            break

    ClaimNumLst = []
    ClaimDateLst = []
    ClaimAmtLst = []
    while True:
        while True:
            print()
            try:
                OldClaimNum = (input("Enter customer's previous claim number ('0' to end): "))
                OldClaimNum = int(OldClaimNum)
            except:
                print()
                print("Data entry error - must enter a valid claim number. ")
                print()
                continue
            if OldClaimNum == "":
                print()
                print("Data entry error - old claim number or a '0' must be input.")
                print()
            elif OldClaimNum == 0:
                break
            else:
                if OldClaimNum >= CLAIM_NUMBER:
                    print()
                    print("Data entry error - old claim number must be less than the current claim number.")
                    print()
                else:
                    ClaimNumLst.append(OldClaimNum)
                    break 
        if OldClaimNum == 0:
            break

        while True:
            try:
                OldClaimDate = input("Enter customer's previous claim date (YYYY-MM-DD): ")
                OldClaimDate = datetime.datetime.strptime(OldClaimDate, "%Y-%m-%d")
            except:
                print()
                print("Data Entry Error - claim date is not in a valid format.")
                print()
            else:
                ClaimDateLst.append(OldClaimDate)
                break

        while True:
            try:
                OldClaimAmt = input("Enter customer's previous claim amount: ")
                OldClaimAmt = float(OldClaimAmt)
            except:
                print()
                print("Data entry error - must enter a valid claim amount.")
                print()
            else:
                ClaimAmtLst.append(OldClaimAmt)
                break

    # Perform required calculations.
    if XtraLiability == 'N':
        XTRA_LIABILITY = 0
    else:
        XTRA_LIABILITY *= CarsInsured
    if GlassCover == 'N':
        GLASS_COVER = 0
    else:
        GLASS_COVER *= CarsInsured
    if LoanCar == 'N':
        LOAN_CAR = 0
    else:
        LOAN_CAR *= CarsInsured
    
    TotalExtraCost = XTRA_LIABILITY + GLASS_COVER + LOAN_CAR
    InsPremium = FIRST_AUTO + (FIRST_AUTO * XTRA_AUTO_RATE * (CarsInsured - 1))
    TotalInsPremium = InsPremium + TotalExtraCost
    HST = TotalInsPremium * HST_RATE
    TotalCost = TotalInsPremium + HST
    TotalCostDP = TotalCost - DownPay
    if PayMethod == "Full":
        MonthlyPayment = 0
    else:
        MonthlyPayment = (TotalCostDP + PROCESS_FEE) / MONTHLY_PAY

    # Display results
    print()
    print("================================================================") 
    print()
    print("                       One Stop Insurance")
    print()
    print("----------------------------------------------------------------")
    print()
    print("                      Customer Information")
    print()
    print(f" Claim Number: {CustCtr:<5d}")
    LastName += ", "
    LastName += FirstName
    print(f" {LastName:<30s} Number of cars insured: {CarsInsured}")
    print(f" {PhNum:<10s}                     Extra Liability:        {Functions.YesOrNoFull(XtraLiability):<3s}")
    print(f" {StAdd:<15s}                Glass Coverage:         {Functions.YesOrNoFull(GlassCover):<3s}")
    City += ", "
    City += Prov
    print(f" {City:<15s}                Loaner Car:             {Functions.YesOrNoFull(LoanCar):<3s}")
    print(f" {PostalCode:<7s}                        Payment Method:         {PayMethod}")
    print("----------------------------------------------------------------")
    print()
    print("                      Payment Information")
    print()
    print(f"                  Down Payment:       {Functions.FDollar2(DownPay):>8s}")
    print(f"                  Insurance Premium: {Functions.FDollar2(InsPremium):>9s}")
    print(f"                  Total Extra Cost:    {Functions.FDollar2(TotalExtraCost):>7s}")
    print(f"                  HST:                 {Functions.FDollar2(HST):>5s}")
    print(f"                  Total Cost:        {Functions.FDollar2(TotalCost):>8s}")
    print()
    print(f"                  Monthly Payment:     {Functions.FDollar2(MonthlyPayment):>7s}")
    print("----------------------------------------------------------------")
    print()
    print("                         Payment Dates")
    print()
    print(f" Invoice Date: {Functions.FDateM(TODAY):<9s}          First Payment Date: {Functions.FDateM(PayDate):<9s}")
    print("----------------------------------------------------------------")
    print()
    print("                         Previous Claims")
    print()
    print("               Claim #  Claim Date        Amount")
    print("               ---------------------------------")        
    for i in range(len(ClaimNumLst)):
        print(f"               {ClaimNumLst[i]:<5d}    {Functions.FDateS(ClaimDateLst[i]):<10s}    {Functions.FDollar2(ClaimAmtLst[i]):>10s}")
    print("================================================================") 


# Any housekeeping duties at the end of the program
    print()
    AnotherCustomer = Functions.YesOrNo("Do you want to enter in information about another customer (Y/N): ").upper()
    print()
    if AnotherCustomer == "N":
        break
print()
print("You have ended the program")
print()