from models.bipartite_graph import BipartiteGraph


def main():
    
    bpGraph =[
        [1,0,0],
        [0,1,0],
        [0,0,1]
          ]

    trivialCase = BipartiteGraph(bpGraph)

    print(f"At the trivial case there should be a maximum of 3 matchings which is {trivialCase.getMaximumNumberOfMatches()==3}")


    bpGraph =[
        [1,0,0],
        [1,0,0],
        [1,0,0]
          ]

    trivialCase = BipartiteGraph(bpGraph)

    print(f"Now every vertex from the source is connected to a single vertex therefore there should only 1 matching which is {trivialCase.getMaximumNumberOfMatches()==1}")



    bpGraph =[
        [0,1,0],
        [1,0,0],
        [1,0,0]
          ]

    trivialCase = BipartiteGraph(bpGraph)

    print(f"For this last case by looking at the given matrix we should have 2 matches, which is {trivialCase.getMaximumNumberOfMatches()==2}")



if __name__ == '__main__':
    main()