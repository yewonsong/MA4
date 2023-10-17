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
	plt.title("Red: C++, Green: python, Blue: numba")
	plt.savefig('fib comparision from 30 to 47')
     

	time2_c = []
	time2_numba = []
	for i in range(20,31):
		start = pc()
		f = Person(i)
		f.fib()
		end = pc()
		time2_c.append(end-start)
          
		start = pc()
		fib_numba(i)
		end = pc()
		time2_numba.append(end-start)
	x_coor2 = [i for i in range(20,31)]
	plt.plot(x_coor2, time2_c, 'r', x_coor2, time2_numba, 'g')
	plt.title("Red: C++, Green: numba")
	plt.savefig('C++ and numba comparision')
     
	
	f = Person(47)	
	print(f"Fibonacci number for n=47, c++ {f.fib()}")

	print(f"Fibonacci number for n=47, numba {fib_numba(47)}")
    
if __name__ == '__main__':
	main()
