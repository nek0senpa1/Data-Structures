class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def __str__(self):
    s = ""
    if self.size == 0:
      return "List is empty"

    for i in range(0,self.size):
      s += self.storage[0]
      s += " "
      
    return s

  def enqueue(self, item):
    self.size = self.size +1

    self.storage.append(item)

  def dequeue(self):

    if self.size < 1:
      print('there is no queue...')
      return None

    else:
      front = self.storage[0]

      del self.storage[0]

      self.size = self.size -1

      return front

  def len(self):
    return self.size


bob = Queue()

bob.enqueue('Patty')
bob.enqueue('Selma')
bob.enqueue('Lenny')
bob.enqueue('Carl')

print(bob)

print(bob.len)
