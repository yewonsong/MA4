from time import perf_counter as pc
import concurrent.futures as future

import random

def get_volume(lst):
    n = lst[0]
    d = lst[1]
    n_c = 0
    for _ in range(n):
        if sum([random.uniform(-1,1)**2 for _ in range(d)]) <= 1:
            n_c+=1
    return (d**2)*n_c/n

if __name__ == '__main__':
    n = 10000000
    d = 11
    process_num = 10
    start = pc()

    get_volume([n, d])

    end = pc()

    print(f"Process took {round(end-start)} seconds")

    start = pc()

    with future.ProcessPoolExecutor() as ex:
        p = [ [n//process_num,d] for i in range(process_num) ]

        results = ex.map(get_volume, p)

    end = pc()
    
    print(f"Process took {round(end-start)} seconds")
    