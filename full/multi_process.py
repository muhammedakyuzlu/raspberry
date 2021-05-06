import multiprocessing,time
import sys

def process_one():
   while True:
      p3 = multiprocessing.Process(target = process_three,daemon=True)
      p3.start()
      print('process one started')
      time.sleep(1)
      print('process one finished')
      p3.join()

def process_two(q):
   print('process two started')
   time.sleep(1)
   print('process two finished')
   q.put(1)


def process_three():
      print('process three started')
      time.sleep(2)
      print('process three finished')


if __name__ == '__main__':   
      q = multiprocessing.Queue()
      p1 = multiprocessing.Process(target = process_one)
      p1.start()
      while True:
         p2 = multiprocessing.Process(target = process_two,args=[q])
         p2.start()
         p2.join()
         if q.get()  == 1 :
            p1.terminate()
            print('p1 is terminated')
            break
      print('exit')
      sys.exit()
      # killing the parents does not kill the child until all methods are executed