import time

my_time = int(input("Enter the time in seconds : "))

for _ in range(my_time,0,-1):
    seconds = _%60
    minutes = int(_/60)%60 
    hours= int(int(_/60)/60)%60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP !")