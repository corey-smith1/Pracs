"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("enter sales: $"))

if sales >= 1000:
    bonus = sales*0.15
    print (bonus)
elif  0 < sales < 1000:
    bonus = sales*0.10
    print (bonus)
else :
    print ("You are being reported to the police for stealing company money")
