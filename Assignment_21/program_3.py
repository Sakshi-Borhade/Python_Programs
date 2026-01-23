import threading

counter = 0
lock = threading.Lock()

def IncrementCounter():
    
    global counter

    print("Thread started:", threading.current_thread().name,"ID:", threading.get_ident())

    for i in range(100000):
        
        lock.acquire()
        counter += 1
        lock.release()

def main():

    threads = []

    
    for i in range(5):

        t = threading.Thread(target = IncrementCounter, name = f"Thread-{i+1}")
        threads.append(t)
        t.start()

    
    for t in threads:

        t.join()

    print("Final value of counter:", counter)

if __name__ == "__main__":
    main()
