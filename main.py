from models.bipartite_graph import BipartiteGraph


def main():

    #This is a graph where all vertices on one side are connected to a single vertex on the other. 
    #Therefore the maximum should be 1
    
    bpGraph =[[1,0,0],
          [1, 0, 0],
          [1, 0, 0]]

    g = BipartiteGraph(bpGraph)

    print(f"Maximum number of bipartite matchings would be {g.maximumBipartiteMatching()}")



if __name__ == '__main__':
    main()