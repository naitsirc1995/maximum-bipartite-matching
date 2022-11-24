# Maximum-bipartite-matching

### The problem. 

Given a bipartite graph  G = (V,E) , we want to find a set of edges in such a way that no two edges share an endpoint. Here is an illustration of what we would have to do. 


This is an example of a random bipartite graph.

![Alt text](resources/img1.png)


For the given bipartite , the following edges do not share an endpoint. 

![Alt text](resources/img2.png)


Looking for edges with the property just described is trivial, but looking 
for the **MAXIMUM** number of edges with such property is not trivial. 


### How to solve the problem ?

The approach to solve this problem will be the Ford Fulkerson algorithm.
The very first step will be to the source and sink nodes as ilustrated
in the following picture.

![Alt text](resources/img3.png)


The very first question that we have to ask, now that we have a source, 
a sink and the rest of the edges, how are we going to get assign the 
capacities. 


Initially, we will set the capacities for the edges that we want to 
maximize as 1. Which would look as follows. 

![Alt text](resources/img4.png)



<img src="https://latex.codecogs.com/gif.latex?\int_{a}^{b}"/>