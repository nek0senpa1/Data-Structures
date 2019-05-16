class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def __int__(self):
    s = None
    if self.value == None:
      return "BST is empty"

    else:
      s = self.value
      return s

  def insert(self, value):
    if value == None:
      return None
    
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      
      else:
        self.left.insert(value)

    elif value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      
      else:
        self.right.insert(value)


  def contains(self, target):
    if target == self.value:
      return True
    
    elif target < self.value:
      if not self.left:
        return False

      else:
        if target == self.left:
          return True
        else:
          self.left.contains(target)

    else: 
      if not self.right:
        return False

      else:
        if target == self.right:
          return True
        else:
          self.right.contains(target) 



  def get_max(self):
    maxy = 0

    while self.right is not None:

      if maxy < self.value:
        maxy = self.value

        self = self.right

    return maxy



  def for_each(self, cb):
    stuff = []

    


# ================================

# troll = BinarySearchTree(14)

# troll.insert(15)
# troll.insert(10)
# troll.insert(21)
# troll.insert(5)
# troll.insert(16)
# troll.insert(8)

# print(troll)