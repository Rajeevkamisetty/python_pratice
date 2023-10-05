accountnumber = int(input("enter account number:"))
pin = int(input("enter pin number:"))
if accountnumber == 123456789 and pin == 1234:
    print("select 1 to with draw ,2 to balance enquiry")
    select = int(input("select 1 or 2 :"))
    if select == 1:
        print("you have selected to withdraw")
        totalamount = 150000
        withdrawamount = int(input("enter how much value to enter:"))
        balance = totalamount - withdrawamount
        if withdrawamount <= 150000:
            print("transasition is sucess")
            print(balance)
        else:
            print("insufcent fund")
    elif select == 2:
        print("you have selected for balance enquiry")
        totalamount = 150000
        print(totalamount)
    else:
        print("given data is invalid please select 1 or 2")
else:
    print("enter valid account number or pin ")
