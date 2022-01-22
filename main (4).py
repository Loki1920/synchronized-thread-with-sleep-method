import threading
import time

n = int(input("enter number :"))
lock = threading.Lock()
def print_1_n(n):  
  for i in range(1,n+1):
    lock.acquire()
    print(threading.current_thread().getName() +" "+ str(i))
    lock.release()
    time.sleep(1)

  

th1 = threading.Thread(target= print_1_n,args=(n,))

th2 = threading.Thread(target=print_1_n,args=(n,))

th1.start()
th2.start()
th1.join()
th2.join()