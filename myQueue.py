import random
import json

class Queue:
    def __init__ (self):
        self.queue = []

    def enqueue(self, value):
        try:
            self.queue.append(value)
        except Exception as e:
            print(e)

    def dequeue(self):
        if self.isEmpty() == False:
            self.queue.pop(-1)
        else:
            raise MyException("Queue empty; no value to dequeue.")

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
        
    def displayQueue(self, n):
        if n == 0:
            return self.queue
        else:
            n= n if self.size() > n else self.size()
        return self.queue[0:n]
    
    def get(self, n):
        return self.queue[n]
    
    def remove(self, x):
        for i in self.queue:
            if i["title"] == x:
                self.queue.remove(i)

    def shuffle(self):
        random.shuffle(self.queue)

    def load_json(self):
        try:
            with open("data.json") as f:
                self.queue = json.load(f)
            return "data loaded!"
        except Exception as e:
            return "no data loaded!"

    def save_json(self):
        with open("data.json", "w") as f:
            json.dump(self.queue, f)
    
class MyException(Exception):
    pass