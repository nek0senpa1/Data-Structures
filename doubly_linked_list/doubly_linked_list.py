"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev






"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def __str__(self):
    s = ""
    if self.length == 0:
      return "List is empty"

    current = self.head
    while current:
      s += current.value
      s += " "
      current = current.next
    return s


  def add_to_head(self, value):
    new_node = ListNode(value)
    self.length = self.length +1
    
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node

    else: 
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  
  def remove_from_head(self):
    
    if not self.head and not self.tail:
      return None
    
    self.length = self.length -1

    if self.head == self.tail:
      old = self.head
      self.head = None
      self.tail = None

      return old

    old_head = self.head
    self.head = self.head.next
    self.head.prev = None
    
    return old_head


  def add_to_tail(self, value):
    new_tail = ListNode(value)
    self.length = self.length +1

    if not self.head and not self.tail:
      self.head = new_tail
      self.tail = new_tail

    else:
      new_tail.prev = self.tail
      self.tail.next = new_tail
      self.tail = new_tail

  def remove_from_tail(self):
    
    if not self.head and not self.tail:
      return None

    if self.tail == self.head:
      old_tail = self.tail
      self.head = None
      self.tail = None

      return old_tail

    old_tail = self.tail
    self.tail = self.tail.prev
    self.tail.next = None

  def move_to_front(self, node):
    

    #how do I reference the node I want... like, what is the syntax... ???


    # if node == self.tail:
    #   self.tail = node.prev

    # node.delete

    # holder1 = node.prev
    # holder2 = node.next

    # node.prev =self.head.prev
    # node.next =self.head
    
    # self.head.prev = node
    
    # holder1.next = holder2
    # holder2.prev = holder1
        
    # self.head = node

    # chaChaRealSmooth = None

    # if self.value == node:
    #   chaChaRealSmooth = self
    #   print(chaChaRealSmooth)

    if self.head == self.tail:
      pass

    node.delete()

    self.head.prev = node

    node.next = self.head
    node.prev = None
    
    self.head = node





  def move_to_end(self, node):

    if self.head == self.tail:
      pass

    node.delete()

    self.tail.next = node
    
    node.next = None
    node.prev = self.tail
    
    self.tail = node



  def delete(self, node):
    
    node.delete()
    


  def get_max(self):
    pass
    # get max WHAT ??? what am i getting a max of, or the max in ?






# ----------------------------------
# stuff = DoublyLinkedList()

# stuff.add_to_head('bob')
# stuff.add_to_head('susan')
# stuff.add_to_head('tom')

# print(stuff)

# stuff.remove_from_head()

# print(stuff)

# stuff.add_to_tail('cheryl')
# stuff.add_to_tail('roger')
# stuff.add_to_tail('is dead')

# print(stuff)

# stuff.remove_from_tail()

# print(stuff)

# stuff.move_to_front(1)