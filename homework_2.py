time_user = int(input("Please enter the time in seconds: "))

hours = time_user // 3600
minutes = (time_user - (hours * 3600)) // 60
seconds = time_user - (hours * 3600) - (minutes * 60)
if hours < 10:
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)


print(f"{hours}:{minutes}:{seconds}")