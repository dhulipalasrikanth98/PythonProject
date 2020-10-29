import time
from functools import lru_cache
@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)
    return n


if __name__ =='__main__':
    print("srikanth")
    some_work(1)
    print("method called")
    some_work(4)
    some_work(2)
  
    print("method called")
    some_work(5)
    print("after 5 seconds")
