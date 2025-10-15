#assignment dyslexia occurs when the variable and value are written in reverse order, like 1500 = totalCalorie

dailyCalories = 2500
totalCalories = 0


breakfast = float(input("Enter your breakfast calories: "))
lunch = float(input("Enter your lunch calories: "))
dinner = float(input("Enter your dinner calories: "))
snacks = float(input("Enter your snack calories: "))

totalCalories = breakfast + lunch + dinner + snacks

calorieDeficit = dailyCalories - totalCalories

if calorieDeficit > 0:
    print("\nYou're in a calorie deficit! Deficit:", calorieDeficit, "calories.")
elif calorieDeficit == 0:
    print("\nYou're maintaining your weight.")
else:
    print("\nYou're in a calorie surplus! Surplus:", abs(calorieDeficit), "calories.")

weightLossGoal = 5
caloriesToLose1Pound = 3500
totalCaloriesToLose = weightLossGoal * caloriesToLose1Pound

daysToLoseWeight = totalCaloriesToLose // calorieDeficit

if totalCaloriesToLose % calorieDeficit == 0:
    print("It will take exactly", daysToLoseWeight, "days to lose", weightLossGoal, "pounds.")
else:
    print("It will take approximately", daysToLoseWeight, "days to lose", weightLossGoal, "pounds, with some extra defecit left.")

print("\nFinal Summary:")
print("1. Your total daily calorie intake is: ", totalCalories)
print("2. You're in a deficit of ", calorieDeficit, " calories per day.")
print("3. It will take you around", daysToLoseWeight, "days to lose", weightLossGoal, "pounds.\n")


