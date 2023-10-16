#import math
import random
import matplotlib.pyplot as plt



n_list = [1000, 10000, 100000]
n_c=0

result = {}

i = 1

for n in n_list:
    x_in = []
    x_out = []
    y_in = []
    y_out = []

    for _ in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        #plt.plot(x,y)

        if (x**2+y**2)<=1:
            n_c += 1
            x_in.append(x)
            y_in.append(y)
        else:
            x_out.append(x)
            y_out.append(y)
    plt.subplot(1,3,i)
    plt.title(f'n = {n}')
    plt.scatter(x_in,y_in,s=1,c='#0000cd')
    plt.scatter(x_out,y_out,s=1,c='#FF69B4')
    
    result[n] = 4*n_c/n
    n_c = 0
    i+=1

plt.show()
print(result)