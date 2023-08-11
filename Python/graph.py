class Graph:
    
    def __init__(self,directs):
        self.__matrix=[];
        self.__directs=directs;
    
    def addvertex(self):
        self.__matrix.append([0 for i in range(len(self.__matrix)+1)]);
        for i in range(len(self.__matrix)-1):
            self.__matrix[i].append(0);            
    
    def addEdge(self,start,end):
        self.__matrix[start][end]=1;
        if not self.__directs:
            self.__matrix[end][start]=1;
            
    def __str__(self):
        return str(self.__matrix);
            
if __name__=='__main__':
    graph=Graph(False);
    
    graph.addvertex();
    graph.addvertex();
    graph.addvertex();
    
    graph.addEdge(0,1);
    graph.addEdge(1,2);
    graph.addEdge(2,0);
    
    print(graph);