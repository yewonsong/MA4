#!/usr/bin/env python3
from time import perf_counter as pc
from numba import njit

from matplotlib import pyplot as plt


def fib_py(n):
    if n<= 1:
        return n
    else:
        return(fib_py(n-1)+fib_py(n-2))
    
@njit
def fib_numba(n):
    if n<= 1:
        return n
    else:
        return(fib_numba(n-1)+fib_numba(n-2))
    
from person import Person


def main():
     
    
	time_c = []
    
	time_py = []
    
	time_numba = []
    
	for i in range(30,46):
        
		start = pc()
		f = Person(i)
		f.fib()
		end = pc()         
		time_c.append(end - start)
          
		start = pc()
		fib_py(i)
		end = pc()
		time_py.append(end - start)
          
		start = pc()
		fib_numba(i)
		end = pc()
		time_numba.append(end-start)
	
	x_coor = [ i for i in range(30,46)]
	plt.plot(x_coor, time_c, 'r', x_coor, time_py, 'g', x_coor, time_numba, 'b') 
	plt.title("red: C++, green: python, blue: numba")
	plt.savefig('fib comparision graph')
     
	start = pc()
	f = Person(47)
	f.fib()
	end = pc()
	print(f"Fibonacci number for n=47, c++ {end-start}")
     
	start = pc()
	fib_numba(47)
	end = pc()
	print(f"Fibonacci number for n=47, numba {end-start}")
    #  print(f.get())
    #  f.set(7)
    #  print(f.fib())
    #  print(fib_py(10))
    #  print(fib_numba(10))     
	#n = 10
    #start = pc()
	#f = Person(n)
    #f.fib()
	#end = pc()
	#print(f"Process took {round(end-start)} seconds")

	#f.fib(10)
      


if __name__ == '__main__':
	main()
