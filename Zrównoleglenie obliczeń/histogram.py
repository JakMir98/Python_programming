import threading
import random
import time


class MyThread(threading.Thread):
    def __init__(self, name, data):
        threading.Thread.__init__(self)
        self.name = name
        self.data = data
        self.histogram = [0, 0, 0, 0, 0]

    def run(self):
        print("Starting " + self.name)
        console_print(self.name, self.data, 0.1)
        print("Exiting " + self.name)


histogram = [0, 0, 0, 0, 0]
flag = 0
random.seed()
data = []


def console_print(name, data, delay):
    for i in range(0, len(data)):
        if flag:
            name.exit()
        time.sleep(delay)

        if data[i] < 20:
            histogram[0] += 1
            print(name, "1")
        elif data[i] < 40:
            histogram[1] += 1
            print(name, "2")
        elif data[i] < 60:
            histogram[2] += 1
            print(name, "3")
        elif data[i] < 80:
            histogram[3] += 1
            print(name, "4")
        else:
            histogram[4] += 1
            print(name, "5")


for i in range(0, 100):
    data.append(int(random.random() * 100))

t1 = MyThread("Thread 1", data[:50])
t2 = MyThread("Thread 2", data[50:])

t1.start()
t2.start()

while True:
    if sum(histogram) == 100:
        time.sleep(1)
        print("HISTOGRAM")
        print("( 1, 20 ) : ", histogram[0] * "o")
        print("(21, 40 ) : ", histogram[1] * "o")
        print("(41, 60 ) : ", histogram[2] * "o")
        print("(61, 80 ) : ", histogram[3] * "o")
        print("(81, 100) : ", histogram[4] * "o")
        break
