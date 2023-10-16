from time import perf_counter as pc
from time import sleep as pause
# import multiprocessing as mp

def runner(n):
    print("performing a costly function")
    pause(n)
    print(f"function {n} complete")


# # if __name__ == "__main__":
# #     start = pc()
# #     runner()
# #     end = pc()
# #     print(f"Process took {round(end-start)} seconds")


# if __name__ == "__main__":
#     start = pc()

#     p1 = mp.Process(target = runner)
#     p2 = mp.Process(target = runner)
#     p1.start()
#     p2.start()

#     end = pc()
#     print(f"Process took {round(end-start, 2)} seconds")


import concurrent.futures as future

# futures - with랑 사용
# submit( ) 사용할 것임.
# result( ) 사용할 것임.

# if __name__ == "__main__":

#     start = pc()

#     with future.ProcessPoolExecutor() as ex:
#         p1 = ex.submit(runner)
#         p2 = ex.submit(runner)

#         r1 = p1.result()
#         r2 = p2.result()

#     end = pc()
#     print(f"all done {end-start }")


# if __name__ == "__main__":

#     start = pc()
#     for i in [5, 4, 3, 2, 1]:
#         runner(i)
#     end = pc()

#     print(f"it took {round(end-start)}")



if __name__ == "__main__":
    start = pc()

    with future.ThreadPoolExecutor() as ex:
        p = [5,4,3,2,1]
        results = ex.map(runner, p)

        # for r in results:
        #     print(r)

    end = pc()

    print(f"Process took {round(end-start,2)}")

