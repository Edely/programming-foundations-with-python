import time
import webbrowser

vez = 0
print("Times program started on "+ time.ctime())
while (vez < 3):
	time.sleep(10)
	webbrowser.open('https://www.youtube.com/watch?v=6c-RbGZBnBI ')
	vez = vez + 1