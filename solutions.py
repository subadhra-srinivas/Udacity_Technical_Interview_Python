######### Question 1 ##################################


# Finding the substring of the given string.
# Substring is done like a window. i.e. for
# a given i = 7 for a 8 letter word. there are two 7
# letter substring. One includes the 0th character up to
# 6th character and other substring 1st to 7th character
# This is done for length of t

def subString(str1,i):
    word = []
    word.append(str1[:i])
    for j in range(1,len(str1)-i+1):
        word.append(str1[j:i+1])
        i=i+1
    return word

# Function to check the anagram of word
def anagram(word,t):
    t=list(t)
    t.sort()
    word = list(word)
    word.sort()

    return t==word

def question1(s, t):

    # make sure s is a string
    if type(s) != str:
        return "Error: s not string!"

    # make sure t is a string
    if type(t) != str:
        return "Error: t not string!"


    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()

    if len(s) == 0 or len(t) > len(s):
        print "It is not substring of s. t is greater than s"
        return False

    if len(t) == 0:
        return True

    # Find the substring
    words = subString(s,len(t))
    #print words
    for word in words:
        #print word
        # Check whether anagram for each substring
        if anagram(word,t):
            return True

    return False

#print question1("subadhrasrinivasan","an")



def test1():
    print "Testing 1"
    print "Example test case (udacity, ad):", "PASS" if True == question1("udacity", "ad") else "FAIL"
    print "Edge case (not string):", "PASS" if "Error: s not string!" == question1(456, 4.56) else "FAIL"
    print "Edge case (t longer than s):", "PASS" if False == question1("su", "subadhra") else "FAIL"
    print "Case (s equal to t):", "PASS" if True == question1("edfg", "edfg") else "FAIL"
    print "Case (very long string):", "PASS" if True == question1("yumoklp.iytewsaqdgjklgfsdgfatdfsadsvgvdvdadvdiowuweueuewhieewgcvGvsvsvsbsbbvsvabvabASMvbsamsabsamvhsavhsa","it.ye") else "FAIL"


######### Question 2 ##################################

# function to check string is
# palindrome or not

def isPalindrome(str1):
    # Run loop from 0 to len/2
    for i in range(0, len(str1)//2):
        if str1[i] != str1[len(str1)-i-1]:
            return False
    return True

# Finding the substring of the given string.
# Substring is done like a window. i.e. for
# a given i = 7 for a 8 letter word. there are two 7
# letter substring. One includes the 0th character upto
# 6th character and other substring 1st to 7th character
# This is done for each value of i till i is 1
def subString(str1,i):
    word = []
    word.append(str1[:i])
    for j in range(1,len(str1)-i+1):
        word.append(str1[j:i+1])
        i=i+1
    return word

# For each i value substring is calculated and
# stored in list words. Then for word i.e. substring
# we are checking palindrome or not.
def question2(str1):

    # make sure a is a string
    if type(str1) != str:
        return "Error: a not string!"

    # make sure a has at least 2 characters
    if len(str1) < 2:
        return str1

    str1 = str1.replace(" ", "").lower()
    for i in range(len(str1),1,-1):
        words = subString(str1,i)
        #print words
        for word in words:
            if isPalindrome(word):
                #print("palindrome")
                return word
            else:
                continue

    return "Not a palindrome"

#str2="A Santa dog lived as a devil God at NASA."
#print question2(str2)


def test2():
    print "\nTesting 2"
    print "Edge case (not string):", "Pass" if "Error: a not string!" == question2(456) else "Fail"
    print "Edge case (empty string):", "Pass" if "" == question2("") else "Fail"
    print "Case (1 = \"xyzyx\"):", "Pass" if "xyzyx" == question2("bcxyzyxb") else "Fail"
    print "Case (2 = \"Not a palindrome\"):", "Pass" if "Not a palindrome" == question2("abcdefghijkl") else "Fail"
    print "Case (3 = \"\bab\"):", "Pass" if "bab" == question2("BBABCBCAB") else "Fail"
    print "Case (4 = \"aba\"):", "Pass" if "asantadoglivedasadevilgodatnasa" == question2("A Santa dog lived as a devil God at NASA.") else "Fail"
    print "Case (5 = \"geeksskeeg\"):", "Pass" if "geeksskeeg" == question2("forgeeksskeegfor") else "Fail"
    print "Case (6 = \"radar\"):", "Pass" if "radar" == question2("radar") else "Fail"

######### Question 3 ##################################

# Creating class Edge to store v1, v2 and cost
class Edge:
    def __init__(self,v1,v2,cost):
        self.v1 = v1
        self.v2 = v2
        self.cost = cost

    # Function for printing
    def __repr__(self):
        return "[%s%s%d]" % (self.v1, self.v2, self.cost)

    # Function to get value of v1
    def get_vertex_v1(self):
        return self.v1

    # Function to get value of v2
    def get_vertex_v2(self):
        return self.v2

    # Function to get value of cost
    def get_cost(self):
        return self.cost

def question3(G):
    # Check whether G is a dictionary
    if type(G) != dict:
        return "Error: G is not dictionary"

    # Make sure G have more than one node
    if len(G) < 2:
        return "Error: G has not enough vertices to form edges!"

    # Get a set of vertices
    vertices = G.keys()

    # Assigning the vertices in list of sets
    vertices = [set(i) for i in vertices]

    # Assigning the edges list
    edges = []

    # Iterating for each key and value in a dictionary
    for key,value in G.items():
        # Iterating for each item in value
        for i in value:
            v2, val = i
            #print "v2 is %s, val is %s"% (v2,val)
            # Creating new_edge objects of type Edge
            new_edge = Edge(key, v2, val)
            #print "new_edge is ",new_edge
            # Appending the edge objects to edges list
            edges.append(new_edge)

    #print edges
    # Sorting the edges according to value
    edges.sort(key = lambda x: x.cost)
    #print edges
    #print vertices
    # Assigning output_edges list
    output_edges = []
    # Iterating for each edge object in edges list
    for edge in edges:
        # Iterating for each of vertices in vertices list
        for j in range(len(vertices)):
            #print j
            # Getting the value of vertex 1 from Edge class
            v1 = edge.get_vertex_v1()
            #print v1
            # Getting the value of vertex 2 from Edge class
            v2 = edge.get_vertex_v2()
            #print v2
            # Getting the value of cost from Edge class
            cost = edge.get_cost()
            # Getting the index of v1
            if v1 in vertices[j]:
                i1 = j
                #print "i1"+str(i1)

            # Getting the index of v2
            if v2 in vertices[j]:
                i2 = j
                #print "i2" + str(i2)

        # Checking if the indices are not equal
        if i1 != i2:
            # Assigning the union of vertices v1 and v2 to v1
            vertices[i1] = set.union(vertices[i1],vertices[i2])
            #print "vertices"+str(vertices[i1])
            # Removing the vertices of v2
            vertices.pop(i2)
            # Decrementing the loop
            j=j-1
            # Appending v1,v2 and cost to output_edges
            output_edges.append(v1+v2+str(cost))
        else:
            # Continue to the for loop
            continue

        # Terminate early when all vertices are in one graph
        if len(vertices) == 1:
            break

    #print output_edges

    # Convert output edges to a dictionary of graph
    output_graph = dict()
    for i in output_edges:
        v1,v2,val = i
        #print "v1 is %s,v2 is %s, val is %s"% (v1,v2,val)
        #print i[0] +i[1] +i[2]
        if i[0] in output_graph:
            output_graph[i[0]].append((i[1],int(i[2])))
        else:
            output_graph[i[0]] = [(i[1],int(i[2]))]

        if i[1] in output_graph:
            output_graph[i[1]].append((i[0],int(i[2])))
        else:
            output_graph[i[1]] = [(i[0],int(i[2]))]

    #print output_graph
    return output_graph


#print(question3(G1))

def test3():
    G = {'A': [('B', 2)],
	          'B': [('A', 2), ('C', 5)],
	          'C': [('B', 5)]}
    print "\nTesting 3"
    print "Edge case (not dictionary):", "PASS" if "Error: G is not dictionary" == question3(456) else "FAIL"
    print "Edge case (empty dictionary):", "PASS" if "Error: G has not enough vertices to form edges!" == question3({}) else "FAIL"
    H = question3(G)

    for k,v in G.items():
        if H[k] == v:
            result = "PASS"
        else:
            result = "FAIL"
    print "Case (example case): %s" %result


    R  = {'S':[('A',7),('C',8)],
	            'A':[('B',6),('C',3),('S',7)],
	            'B':[('A',6),('C',4),('D',2),('T',5)],
	            'C':[('A',3),('B',4),('D',3),('S',8)],
	            'D':[('C',3),('B',2),('T',2)],
	            'T':[('B',5),('D',2)]}
    I = {'A': [('C', 3), ('S', 7)],
	          'B': [('D', 2)],
	          'C': [('A', 3), ('D', 3)],
	          'D': [('B', 2), ('T', 2), ('C', 3)],
	          'S': [('A', 7)],
	          'T': [('D', 2)]}

    J = question3(R)

    for k,v in I.items():
        if J[k] == v:
            result = "PASS"
        else:
            result = "FAIL"

    print "Case (example case): %s" %result

######### Question 4 ##################################
from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # Function to insert data into a Tree
    def insert(self,data):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = TreeNode(data)
            else:
                self.leftChild.insert(data)
        else:
            if not self.rightChild:
                self.rightChild = TreeNode(data)
            else:
                self.rightChild.insert(data)

    # A utility function to search a given key in BST
    def search(self,root,key):

        # Base Cases: root is null or key is present at root
        if root is None or root.data ==key:
            return root.data

        # Key is greater than root's key
        if root.data < key:
            return self.search(root.rightChild,key)

        # Key is smaller than root's key
        return self.search(root.leftChild,key)


    # Function to traverse the tree InOrder traversal
    def traverseInOrder(self):
        if self.leftChild:
            self.leftChild.traverseInOrder()

        print self.data

        if self.rightChild:
            self.rightChild.traverseInOrder()

    # Function to find least common ancestor
    def lca(self,root, n1, n2):

        # Base case
        if root is None:
            return None

        # If both n1 and n2 are smaller than root,
        # then LCA lies on left
        if(root.data > n1 and root.data > n2):
            return self.lca(root.leftChild, n1, n2)

        # if both n1 and n2 are greater than root,
        # then LCA lies on right
        if(root.data < n1 and root.data < n2):
            return self.lca(root.rightChild, n1, n2)

        return root.data

def question4(T,r,n1,n2):

    # make sure r, n1 and n2 are integers
    if type(r) != int:
        return "Error: r not integer!"
    if type(n1) != int:
        return "Error: n1 not integer!"
    if type(n2) != int:
        return "Error: n2 not integer!"

    # Convert r to type Node i.e. tree
    root = TreeNode(r)
    root.leftChild = None
    root.rightChild = None

    # Store the r in a queue
    queue1 = deque([r])

    # Iterate until the queue is not None
    while queue1:
        #print queue1
        # Pop the data
        data = queue1.popleft()
        # Iterate j till length of matrix
        for j in range(len(T)):
            # If the position of matrix is 1
            if T[data][j] == 1:
                #print "j" + str(j)
                # Add the data of j to the queue
                queue1.append(j)
        # If data is not the root node
        if data != r:
            # Insert the data to he tree
            root.insert(data)

    # make sure n1 and n2 in the tree
    n1_data = root.search(root, n1)
    #print n1_data
    if n1_data != n1:
        return "Error: n1 not in the tree!"

    n2_data = root.search(root, n2)
    #print n2_data
    if n2_data != n2:
        return "Error: n2 not in the tree!"

    # Traverse the tree
    root.traverseInOrder()

    # Return the lca of n1 and n2
    return root.lca(root, n1, n2)


#print(question4(A,3,1,4))
#print(question4(T,5,4,6))



def test4():
    print "\nTesting 4"
    A = [[0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0]]
    print "Edge case (r not integer):", "PASS" if "Error: r not integer!" == question4(A,"g",-1,4) else "FAIL"
    print "Edge case (n1 not integer):", "PASS" if "Error: n1 not integer!" == question4(A,3,"i",4) else "FAIL"
    print "Case (n1 = 1 and n2 = 4):", "PASS" if 3 == question4(A,3,1,4) else "FAIL"
    T = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,1,0,1,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,1,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,1,0,1],
         [0,0,0,0,0,0,0,0,0]]
    print "Case (n1 = 4 and n2 = 6):", "PASS" if 5 == question4(T,5,4,6) else "FAIL"

######### Question 5 ##################################

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def insertNode(self,node):
        if self.head is None:
            self.head = node
            #print "Node inserted"
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = node

    def printNode(self):
        current = self.head
        while current is not None:
            print current.data
            current = current.next


def question5(ll, m):

    # make sure m is an integer
    if type(m) != int:
        return "Error: m not an integer!"


    left_pointer  = ll
    right_pointer = ll

    # Set right pointer at m nodes away from head
    for i in xrange(m-1):

        # Check for edge case of not having enough nodes!
        if not right_pointer.next:
            return 'Error: m is larger than the linked list.'

        # Otherwise, we can set the block
        right_pointer = right_pointer.next

    # Move the block down the linked list
    while right_pointer.next != None:
        left_pointer  = left_pointer.next
        right_pointer = right_pointer.next

        # Now return left pointer, its at the mth to last element!
    return left_pointer.data


def test5():

    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)

    l1 = LinkedList()
    l1.insertNode(n1)
    l1.insertNode(n2)
    l1.insertNode(n3)
    l1.insertNode(n4)
    l1.insertNode(n5)
    #l1.printNode()

    print "\nTesting 5"
    print "Edge case (m is larger than the linked list):", "PASS" if "Error: m is larger than the linked list." == question5(n1, 9) else "FAIL"
    print "Edge case (m not an integer):", "PASS" if "Error: m not an integer!" == question5(n1, 'a') else "FAIL"
    print "Case (ll = n1 and m = 3):", "PASS" if 30 == question5(n1, 3) else "FAIL"
    print "Case (ll = n1 and m = 4):", "PASS" if 20 == question5(n1, 4) else "FAIL"


test1()
test2()
test3()
test4()
test5()
