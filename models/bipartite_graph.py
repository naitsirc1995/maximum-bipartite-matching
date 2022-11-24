from typing import List

class BipartiteGraph:

    numberOfSourceVertices:int = 0
    numberOfTargetVertices:int = 0
    matches:List[int] = None

    def __init__(self,graph:List[List]):
        self.graph = graph
        if len(graph) > 0:
            self.numberOfSourceVertices = len(graph)
            self.numberOfTargetVertices = len(graph[0])
            self.matches = [-1 for _ in range(self.numberOfTargetVertices)] #This vector represents the matched correspondances. 
        else:
            raise ValueError("The matrix should have at least one element")
    





    def traversePossibleMatches(self,sourceVertex:int,visited:List[bool])->bool:
        for targetVertice in range(self.numberOfTargetVertices):
            if self.graph[sourceVertex][targetVertice] == 1 and visited[targetVertice]==False:
                visited[targetVertice] = True

                if self.matches[targetVertice] == -1 or self.traversePossibleMatches(self.matches[targetVertice],visited):
                    self.matches[targetVertice] = sourceVertex
                    return True
        return False

    def getMaximumNumberOfMatches(self):
        
        maxNumberMatches:int = 0
        for i in range(self.numberOfSourceVertices):
            visited:List[bool] = [False for _ in range(self.numberOfTargetVertices)]
            if self.traversePossibleMatches(sourceVertex=i,visited=visited):
                maxNumberMatches+=1
        
        return maxNumberMatches