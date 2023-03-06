day1 = float(input("Укажите расход за сегодня 1:"))
day2 = float(input("Укажите расход за сегодня 2:"))
day3 = float(input("Укажите расход за сегодня 3:"))
day4 = float(input("Укажите расход за сегодня 4:"))
day5 = float(input("Укажите расход за сегодня 5:"))
day6 = float(input("Укажите расход за сегодня 6:"))
day7 = float(input("Укажите расход за сегодня 7:"))
sum_day = day1 + day2 + day3 + day4 + day5 + day6 + day7
print("Сумма расходов :", round(sum_day, 2))
day_amount = 7
a = sum_day / day_amount
print ("Cредний расход за день:", round(a, 1))

