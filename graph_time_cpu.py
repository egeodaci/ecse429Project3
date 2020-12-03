import psutil
import time
import matplotlib.pyplot as plt




result=[]
result2=[]
t_end = time.time() + 20
currentTime=time.time()
while time.time() < t_end:
    result.append([psutil.cpu_percent(interval=1)])
    result2.append([round(time.time()-currentTime)])
plt.scatter(result2, result)
plt.plot(result2,result)
plt.ylim(0,100)
plt.xticks(result2)
plt.xlabel('Time(seconds)')
plt.ylabel('Cpu use (%)')
plt.title('System is idle doing no requests')
plt.savefig('System is idle.png')
plt.show()