def tax (income, rate):
    tax = (rate/100)*income
    return tax


def PIT (income):
    total_tax = 0
    if income < 800000:
        return 0 
    
    if income > 800000:
        rem_income = income - 800000
        if income > 3000000:
            tax_ = tax(2200000,15)
            diff_income = income - 3000000
        else:
            tax_ = tax(rem_income, 15)
        total_tax += tax_    

    if income > 3000000:
        if income > 12000000:
            tax_ = tax(9000000,18)
            diff_income = income - 12000000
        else:
            tax_ = tax(diff_income, 18)
        total_tax += tax_
        
    if income > 12000000:
        if income > 25000000:
            tax_ = tax(13000000,21)
            diff_income = income - 25000000
        else:
            tax_ = tax(diff_income, 21)
        total_tax += tax_
        
    if income > 25000000:
        if income > 50000000:
            tax_ = tax(25000000,23)
            diff_income -= 50000000
        else:
            tax_ = tax(diff_income, 23)  
        total_tax += tax_
        
    if income > 50000000:
        diff_income = income - 50000000
        tax_ = tax(diff_income, 25)
        total_tax += tax_
    
    return total_tax