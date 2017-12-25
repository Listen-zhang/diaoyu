import timeit
import time


def a():
  x = 1
  while x<10:
    print(x)
    time.sleep(1)
    x=x+1;
ti = timeit.Timer(stmt=a)
print(ti.timeit(1))
