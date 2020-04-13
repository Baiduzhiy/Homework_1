from sys import argv

script_name, first_param, second_param, third_param = argv

a = int(first_param)
b = int(second_param)
d = int(third_param)

c = (a * b) + d
c = str(c)

print("Script name: ", script_name)
print("Enter the number of hours worked: ", first_param)
print("Enter the employee rate per hour: ", second_param)
print("Enter the award amount: ", third_param)
print("The employee's salary was: " + c)