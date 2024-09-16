import datetime
import time

# Get and print current date and time in mm/dd/YY H:M:S format
now = datetime.datetime.now()
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

while True:
    # Update 'now' inside the loop to get current time each iteration
    now = datetime.datetime.now()
    # Print the current time
    print(now)
    
    # (Raspi create code optional)
    #timenow = time.localtime()
    #print(timenow)
    #print(timenow.tm_hour)
    #print(timenow.tm_min)
    #t = now.strftime("%H%M%S")
    #print("time:", t)
    #if (t >= '130700'):
        #print("lets go")

    # Optional: You can print the current hour and minute like this (Noted) - (Optional)
    # print("Current hour:", now.hour)
    # print("Current minute:", now.minute)
    
    # Example to demonstrate a condition based on time (Noted) - (Optional)
    # t = now.strftime("%H%M%S")  # Get the current time in HH:MM:SS format
    # print("Formatted time:", t)
    
    # Check for a specific time (e.g., 13:07:00) (Noted) - (Optional)
    # if t >= '130700':
    #     print("Let's go!")
    #     break  # Optionally exit the loop if the condition is met

    # Sleep for 2 seconds before the next iteration
    time.sleep(2.0)
