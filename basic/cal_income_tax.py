'''
Calculate income tax for the given income by adhering to the below rules
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20

For example, suppose the taxable income is 45000 the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000
'''
print("Income Tax calculation..")
sal = int(input("Enter Salary: "))
tax_payable = 0
def Tax_calculation(sal):
    if sal <= 10000:
        tax_payable = 0
    elif sal > 10000 and sal <= 20000:
        tax_payable = (sal - 10000) * 10/100
    else:
        tax_payable = 0
        tax_payable = (sal - 10000) * 10 / 100
        tax_payable += (sal - 20000) * 20 / 100
    print("Tax Payable: ", tax_payable)

Tax_calculation(sal)