def bonAppetit(bill, k, b):
    value=bill[k]
    bill.remove(value)
    totbill=sum(bill)
    actual=totbill//2
    if(actual==b):
        print("Bon Appetit")
    else:
        print(b-actual)
https://www.hackerrank.com/contests/devops3yr/challenges/bon-appetit/submissions/code/1317809966
