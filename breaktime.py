import time
import webbrowser

print('Time to take a break')

total_breaks = 3
wait = 0
print("This program started on " + time.ctime())
while wait <= total_breaks:
    time.sleep(10)
    wait = wait + 1
    webbrowser.open("https://www.youtube.com/watch?v=1SJ7RZFvEhA")
