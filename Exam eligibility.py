total_days = int(input("Total working days: "))
absent_days = int(input("Days absent: "))

attended_days = total_days - absent_days
percentage = (attended_days / total_days) * 100

print("Attendance: ", round(percentage, 2), "%")

if percentage >= 75:
    print("You can sit for the exam :) . ")
else:
    print("You cannot sit for the exam :( . ")