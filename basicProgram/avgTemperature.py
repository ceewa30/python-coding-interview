# Calculate Average Temperature

numofdays = int(input("How many days temperature :"))
total = 0
dayslist = []
for i in range(numofdays):
    daystemp = int(input(f"Days {i + 1}'s high temperature: "))
    dayslist.append(daystemp)
    total += daystemp

avg = round(total/numofdays, 2)
count = 0
print("\nAverage = " + str(avg))
for days in dayslist:
    if days > avg:
        count += 1
print(f"{count} days is above the Average temperature")
