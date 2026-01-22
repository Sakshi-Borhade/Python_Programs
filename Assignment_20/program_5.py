import threading

def DisplayNum():

    print("Inside EvenNum : ",threading.get_ident())

    for i in range(1,51):

        print(i)

def Display():

    print("Inside OddNum : ",threading.get_ident())

    for i in range(50,0,-1):

        print(i)

def main():

    t1 = threading.Thread(target = DisplayNum)
    t1.start()
    t1.join()

    t2 = threading.Thread(target = Display)
    t2.start()
    t2.join()


if __name__ == "__main__":
    main()