import matplotlib.pyplot as plt
import random as rm
import statistics as st

x = []
y = []
for i in range(100):
    a = rm.randint(-10000, 10000)
    x.append(i)
    y.append(a)



# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
min = min(y)
max = max(y)

mean = st.mean(y)
def meann(list):
    summ = 0
    for i in range(len(list)):
        summ = summ + list[i]
    return summ/len(list)

def mediann(list):
    temp = list
    temp.sort()
    leng = int(len(temp))
    len2 = int(leng/2)
    if leng%2==0:
        return(temp[len2]+temp[len2-1])/2
    return temp(len2)
def devst(list):
    summ = 0
    mean = meann(list)
    for i in range(0,len(list)):
        xi = (list[i] - mean) ** 2
        summ += xi
    return (summ/(len(list)-1))**(1/2)

dev2 = devst(y)
mediann = mediann(y)
meann = meann(y)
median = st.median(y)
dev = st.stdev(y)

# giving a title to my graph
plt.title('Min='+str(min)+' : ('+str(y.index(min))+':'+str(min)+')'
          +', '+ 'Max='+str(max)+' : ('+str(y.index(max))+':'+str(max)+')'
          +'\n'+'Mean='+str(mean)+' '+str(meann)
          +', '+'Median='+str(median)+' '+str(mediann)
          +'\n'+'Standard deviate='+ str(dev) +' '+str(dev2))

# function to show the plot
plt.show()