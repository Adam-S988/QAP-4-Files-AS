def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr


def FirstMonthDate(Date):
    import datetime
    TODAY = datetime.date.today()
#Determine the payment date as the fist date of the next month
    
    Year = TODAY.year
    Month = TODAY.month
    Day = TODAY.day

    NewYear = Year
    NewMonth = Month + 1

    #If the month exceeds 12, set it back to January, and add 1 to the year
    if NewMonth > 12:
        NewMonth -= 12
        NewYear += 1

    NewDay = 1

    if Day >= 25:
        NewMonth += 1
        if NewMonth > 12:
            NewMonth -= 12
            NewYear += 1

    PayDate = datetime.datetime(NewYear, NewMonth, NewDay)
    return PayDate

def PostalCode(Prompt):
    # Function will validate and format a Postal Code to X#X #X#.
    while True:
        PostalCode = input(Prompt).upper()
        if PostalCode == "":
            print()
            print("Data entry error - postal code must be valid format (X#X#X#)")
            print()
        elif len(PostalCode) != 6:
            print()
            print("Data entry error - postal code must be 6 characters.")
            print()
        elif PostalCode[0].isalpha() == False or PostalCode[2].isalpha() == False or PostalCode[4].isalpha() == False or PostalCode[1].isdigit() == False or PostalCode[3].isdigit() == False or PostalCode[5].isdigit() == False:
            print()
            print("Data entry error - Postal code must be in the correct format.")
            print()
        else:
            PostalCodeFull = PostalCode[0:3] + " " + PostalCode[3:]
            return PostalCodeFull

def YesOrNo(Prompt):
    # Function will validate for a Yes/No input prompt.

    while True:
        UserInput = input(Prompt).upper()
        if UserInput == "":
            print()
            print("Data entry error - must be a 'Y' or a 'N'.")
            print()
        elif UserInput != "Y" and UserInput != "N":
            print()
            print("Data entry error - must be a 'Y' or a 'N'.")
            print()
        else:
            return UserInput
        
def YesOrNoFull(Prompt):
    # Function will change the 'Y' and 'N' to 'Yes' and 'No' respectively.

    if Prompt == 'Y':
        Output = "Yes"
        return Output
    elif Prompt == 'N':
        Output = "No"
        return Output