import time

# Get the current time
current_time = time.strftime('%H:%M:%S')
print(current_time)

# Get the current hour
current_hour = int(time.strftime('%H'))
print(current_hour)

# Print greeting based on the hour
if current_hour < 12:
    print("Good Morning")
elif 12 <= current_hour < 18:
    print("Good Afternoon")
else:
    print("Good Evening")

