monthlyIncome = 2500
totalExpenses = 0

rent = float(input("Enter your rent for the month: $"))
groceries = float(input("Enter your groceries cost for the month: $"))
utilities = float(input("Enter your utilities cost for the month: $"))
entertainment = float(input("Enter your entertainment cost for the month: $"))

totalExpenses = rent + groceries + utilities + entertainment

if monthlyIncome == totalExpenses:
    print("\nYou're perfectly on button!")
elif monthlyIncome > totalExpenses:
    print("\nGreat! You're under budget by: $", monthlyIncome - totalExpenses)
else:
    print("\nYou're over budget by: $", totalExpenses - monthlyIncome)

essentialExpenses = rent + utilities + groceries
savingsRate = ((monthlyIncome - essentialExpenses) / monthlyIncome) * 100
print("\nYour savings rate, after essential expenese, is: {:.2f} percent".format(savingsRate))

savingsGoal = 10000
monthsToSave = savingsGoal // (monthlyIncome - essentialExpenses)
print("It will take approximately", monthsToSave, "months to save $10,000 with your current spending")

if savingsGoal % (monthlyIncome - essentialExpenses) == 0:
    print("You will reach exactly $10,000 after", monthsToSave, "months.")
else: 
    print("You will have a little extra savings after", monthsToSave, "months.")

print("\nFinal Summary:")
print("1. Your total monthly essential expenses are: $", essentialExpenses)
print("2. You're saving {:.2f} percent of your income after essential expenses.".format(savingsRate))
print("2. You can reach your $10,000 savings goal in about", monthsToSave, "months.\n")