import threading
import random
import time


class Philosopher(threading.Thread):

    running = True

    def __init__(self, name, fork_left, fork_right):
        threading.Thread.__init__(self)
        self.name = name
        self.fork_left = fork_left
        self.fork_right = fork_right

    def run(self):
        while(self.running):
            time.sleep(random.uniform(1, 10))
            print(self.name + ": hungry ")
            self.dine()

    def dine(self):
        fork1, fork2 = self.fork_left, self.fork_right

        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print(self.name + ": forks switch ")
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print(self.name + ": eat start ")
        time.sleep(random.uniform(1, 10))
        print(self.name + ": eat done - leaving dinner ")


if __name__ == '__main__':
    forks = [threading.Lock() for n in range(5)]
    philosopherNames = ('Philosopher1', 'Philosopher2',
                        'Philosopher3', 'Philosopher4', 'Philosopher5')

    philosophers = [Philosopher(philosopherNames[i], forks[i % 5], forks[(i+1) % 5])
                    for i in range(5)]

    random.seed()
    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(100)
    Philosopher.running = False
    print("Program done.")
