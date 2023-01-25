import sys


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

# AVL tree class which supports the
# Insert operation


class AVL_Tree(object):

    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, key):

        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key[1] < root.val[1]:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key[1] < root.left.val[1]:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and key[1] > root.right.val[1]:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and key[1] > root.left.val[1]:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and key[1] < root.right.val[1]:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # Recursive function to delete a node with
    # given key from subtree with given root.
    # It returns root of the modified subtree.
    def delete(self, root, key):

        # Step 1 - Perform standard BST delete
        if not root:
            return root

        elif key[1] < root.val[1]:
            root.left = self.delete(root.left, key)

        elif key[1] > root.val[1]:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        # If the tree has only one node,
        # simply return it
        if root is None:
            return root

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    def tree_range(self, root, k1, k2):
        global yrange
        # Base Case
        if root is None:
            return

        # Since the desired o/p is sorted, recurse for left
        # subtree first. If root.data is greater than k1, then
        # only we can get o/p keys in left subtree
        if k1 < root.val[1]:
            self.tree_range(root.left, k1, k2)

        # If root's data lies in range, then prints root's data
        if k1 <= root.val[1] and k2 >= root.val[1]:
            yrange.append(root.val)

        # recursively call the right subtree
        self.tree_range(root.right, k1, k2)


data = sys.stdin.read().split('\n')



line = 0
while True:
    if len(data) - 2 < line:
        break
    nr_points = int(data[line])
    if nr_points == 0:
        break
    line += 1
    if nr_points == 1:
        print('INFINITY')
        line += 1
        continue
    temp = []
    j = 0
    while j < nr_points:
        temp.append(tuple(map(float, data[line].split())))
        j += 1
        line += 1

    points = tuple(sorted(temp, key=lambda x: x[0]))
    p = points[0]
    q = points[1]
    xqueue = [p, q]
    tree = AVL_Tree()
    root = tree.insert(None, p)
    root = tree.insert(root, q)

    distance = ((p[0] - q[0])**2 +
                (p[1] - q[1])**2)**0.5
    for i in range(2, len(points)):
        if distance == 0:
            break
        s = points[i]
        xqueue.append(s)
        u = xqueue[0]
        while u[0] <= s[0] - distance:
            root = tree.delete(root, u)
            xqueue.pop(0)
            u = xqueue[0]
        yrange = []
        tree.tree_range(root, s[1] - distance, s[1] + distance)
        for t in yrange:
            if distance > ((s[0] - t[0])**2 + (s[1] - t[1])**2)**0.5:
                distance = ((s[0] - t[0])**2 + (s[1] - t[1])**2)**0.5
        root = tree.insert(root, s)
    if distance < 10000:
        print(format(distance, '.4f'))
    else:
        print('INFINITY')
