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

    elif value > self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      
      else:
        self.right.insert(value)


  def contains(self, target):
    if target == self.value:
      return True
    
    if target < self.value:
      if not self.left:
        return False

      else:
        if target == self.left:
          print('in true area for left')
          return True
        else:
          return self.left.contains(target)
          # garbage code ;p

    else: 
      if not self.right:
        return False

      else:
        if target == self.right:
          print('in true area for right')
          return True
        else:
          return self.right.contains(target) 

    



  def get_max(self):
    maxy = self.value

    while self.right is not None:

      # if maxy < self.value:
      #   maxy = self.value
      # maxy = self.value

      self = self.right
      print(self.value)
      maxy = self.value

    return maxy



  def for_each(self, cb):
    # stuff = []
    cb(self.value)

    if self.left is not None:
      # cb(self.left.value)
      self.left.for_each(cb)


    if self.right is not None:
      # cb(self.right.value)
      self.right.for_each(cb)

    

    


# ================================

# troll = BinarySearchTree(14)

# troll.insert(15)
# troll.insert(10)
# troll.insert(21)
# troll.insert(5)
# troll.insert(16)
# troll.insert(8)

# troll.contains(5)
# troll.contains(456)

# print(troll.get_max())