class BipartiteGraph:
    def __init__(self,graph):
         
        
        self.graph = graph
        self.numberOfSourceVertices = len(graph)
        self.numberOfTargetVertices = len(graph[0])
 
    
    def matchVertex(self, u, matchedVerticesTarget, seen):
 
        
        for v in range(self.numberOfTargetVertices):
 
            
            
            if self.graph[u][v]==1 and seen[v] == False:
                 
                
                seen[v] = True
 
                
                if matchedVerticesTarget[v] == -1 or self.matchVertex(matchedVerticesTarget[v],matchedVerticesTarget, seen):
                    matchedVerticesTarget[v] = u
                    return True
        return False
 
    
    def maximumBipartiteMatching(self):
        
        matchedVerticesTarget = [-1  for i in  range(self.numberOfTargetVertices)]
         
        
        finalResult = 0
        for i in range(self.numberOfSourceVertices):
     
            
            seen = [False for i in range(self.numberOfTargetVertices)]
            if self.matchVertex(i, matchedVerticesTarget, seen):
                finalResult += 1
        return finalResult