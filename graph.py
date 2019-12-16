#!/usr/bin/env python
# coding: utf-8

# In[209]:


from collections import defaultdict 
   
#This class represents a directed graph using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    # A function used by DFS 
    def DFSUtil(self,v,visited): 
        # Mark the current node as visited and print it 
        visited[v]= True
        print(v)
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.DFSUtil(i,visited) 
  
  
    def fillOrder(self,v,visited, stack): 
        # Mark the current node as visited  
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
        stack = stack.append(v) 
      
  
    # Function that returns reverse (or transpose) of this graph 
    def getTranspose(self): 
        g = Graph(self.V) 
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph: 
            for j in self.graph[i]: 
                g.addEdge(j,i) 
        return g 
  
    def isSC(self): 
  
        # Step 1: Mark all the vertices as not visited (For first DFS) 
        visited =[False]*(self.V) 
          
        # Step 2: Do DFS traversal starting from first vertex. 
        self.DFSUtil(0,visited) 
  
        # If DFS traversal doesnt visit all vertices, then return false 
        if any(i == False for i in visited): 
            return False
  
        # Step 3: Create a reversed graph 
        gr = self.getTranspose() 
          
        # Step 4: Mark all the vertices as not visited (For second DFS) 
        visited =[False]*(self.V) 
  
        # Step 5: Do DFS for reversed graph starting from first vertex. 
        # Staring Vertex must be same starting point of first DFS 
        gr.DFSUtil(0,visited) 
  
        # If all vertices are not visited in second DFS, then 
        # return false 
        if any(i == False for i in visited): 
            return False
  
        return True
   
    # The main function that finds and prints all strongly 
    # connected components 
    def printSCCs(self): 
          
        stack = [] 
        # Mark all the vertices as not visited (For first DFS) 
        visited =[False]*(self.V) 
        # Fill vertices in stack according to their finishing 
        # times 
        for i in range(self.V): 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
  
        # Create a reversed graph 
        gr = self.getTranspose() 
           
         # Mark all the vertices as not visited (For second DFS) 
        visited =[False]*(self.V) 
  
         # Now process all vertices in order defined by Stack 
        while stack: 
            i = stack.pop() 
            if visited[i]==False: 
                print(gr.DFSUtil(i, visited))
                
   


# In[196]:





# In[124]:


import pandas as pd


# In[141]:


j= pd.read_csv('xyz.csv', header= None, sep= '/s')


# In[145]:


j[1]= j[0].str.split()


# In[ ]:


gg.stack().apply(pd.Series).stack().unstack(1)


# In[155]:


ip= j[[1]].stack().apply(pd.Series)


# In[157]:


ip= ip.applymap(lambda x: int(x))


# In[191]:


np= [(ip.iloc[i, 0], ip.iloc[i, 1]) for i in range(len(ip))]


# In[210]:


g= Graph(30)


# In[211]:


for i in np:
    g.addEdge(i[0], i[1])


# # Create a graph given in the above diagram 
# g = Graph(5) 
# g.addEdge(1, 0) 
# g.addEdge(0, 2) 
# g.addEdge(2, 1) 
# g.addEdge(0, 3) 
# g.addEdge(3, 4) 
#   
#    
# print ("Following are strongly connected components " +
#                            "in given graph") 
# g.printSCCs() 
# #This code is contributed by Neelam Yadav 

# In[212]:


print("Yes") if g.isSC() else "No"


# In[215]:


g.printSCCs()


# In[218]:


from collections import defaultdict 
   
#This class represents an directed graph  
# using adjacency list representation 
class Graph1: 
   
    def __init__(self,vertices): 
        #No. of vertices 
        self.V= vertices  
          
        # default dictionary to store graph 
        self.graph = defaultdict(list)  
          
        self.Time = 0
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
          
   
    '''A recursive function that find finds and prints strongly connected 
    components using DFS traversal 
    u --> The vertex to be visited next 
    disc[] --> Stores discovery times of visited vertices 
    low[] -- >> earliest visited vertex (the vertex with minimum 
                discovery time) that can be reached from subtree 
                rooted with current vertex 
     st -- >> To store all the connected ancestors (could be part 
           of SCC) 
     stackMember[] --> bit/index array for faster check whether 
                  a node is in stack 
    '''
    def SCCUtil(self,u, low, disc, stackMember, st): 
  
        # Initialize discovery time and low value 
        disc[u] = self.Time 
        low[u] = self.Time 
        self.Time += 1
        stackMember[u] = True
        st.append(u) 
  
        # Go through all vertices adjacent to this 
        for v in self.graph[u]: 
              
            # If v is not visited yet, then recur for it 
            if disc[v] == -1 : 
              
                self.SCCUtil(v, low, disc, stackMember, st) 
  
                # Check if the subtree rooted with v has a connection to 
                # one of the ancestors of u 
                # Case 1 (per above discussion on Disc and Low value) 
                low[u] = min(low[u], low[v]) 
                          
            elif stackMember[v] == True:  
  
                '''Update low value of 'u' only if 'v' is still in stack 
                (i.e. it's a back edge, not cross edge). 
                Case 2 (per above discussion on Disc and Low value) '''
                low[u] = min(low[u], disc[v]) 
  
        # head node found, pop the stack and print an SCC 
        w = -1 #To store stack extracted vertices 
        if low[u] == disc[u]: 
            while w != u: 
                w = st.pop() 
                print(w)
                stackMember[w] = False
                  
            
              
      
  
    #The function to do DFS traversal.  
    # It uses recursive SCCUtil() 
    def SCC(self): 
   
        # Mark all the vertices as not visited  
        # and Initialize parent and visited,  
        # and ap(articulation point) arrays 
        disc = [-1] * (self.V) 
        low = [-1] * (self.V) 
        stackMember = [False] * (self.V) 
        st =[] 
          
  
        # Call the recursive helper function  
        # to find articulation points 
        # in DFS tree rooted with vertex 'i' 
        for i in range(self.V): 
            if disc[i] == -1: 
                self.SCCUtil(i, low, disc, stackMember, st) 
  
  
   
   
   


# In[219]:


g1= Graph1(30)


# In[220]:


for i in np:
    g1.addEdge(i[0], i[1])


# In[221]:


g1.SCC()


# In[228]:


class Graph3: 
      
    # init function to declare class variables 
    def __init__(self,V): 
        self.V = V 
        self.adj = [[] for i in range(V)] 
  
    def DFSUtil(self, temp, v, visited): 
  
        # Mark the current vertex as visited 
        visited[v] = True
  
        # Store the vertex to list 
        temp.append(v) 
  
        # Repeat for all vertices adjacent 
        # to this vertex v 
        for i in self.adj[v]: 
            if visited[i] == False: 
                  
                # Update the list 
                temp = self.DFSUtil(temp, i, visited) 
        return temp 
  
    # method to add an undirected edge 
    def addEdge(self, v, w): 
        self.adj[v].append(w) 
        self.adj[w].append(v) 
  
    # Method to retrieve connected components 
    # in an undirected graph 
    def connectedComponents(self): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc 
  


# In[253]:


g9= Graph3(32)


# In[254]:


np


# In[255]:


for i in np:
    g9.addEdge(i[0], i[1])


# In[256]:


cc = g9.connectedComponents() 


# In[257]:


print(cc) 


# In[ ]:




