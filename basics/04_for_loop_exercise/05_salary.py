tabs_opened = int(input())
salary = float(input())

for index in range(tabs_opened):
    site_name = input()
    if site_name == "Facebook":
        salary -= 150
    elif site_name == "Instagram":
        salary -= 100
    elif site_name == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if (salary > 0):
    print(f"{int(salary)}")
