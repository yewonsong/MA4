#!/usr/bin/env python3
from time import perf_counter as pc



def fib_py(n):
    if n<= 1:
        return n
    else:
        return(fib_py(n-1)+fib_py(n-2))

from person import Person

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())

	print(fib_py(10))
      
	#n = 10
    #start = pc()
	#f = Person(n)
    #f.fib()
	#end = pc()
	#print(f"Process took {round(end-start)} seconds")

	#f.fib(10)
      


if __name__ == '__main__':
	main()
