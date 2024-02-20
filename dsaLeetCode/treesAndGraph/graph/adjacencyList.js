class GraphNode {
  constructor(name, index) {
    this.name = name;
    this.index = index;
    this.neighbors = [];
    this.isVisited = false;
  };
};


class Graph {
  constructor(nodeList) {
    this.nodeList = nodeList;
  };

  addUndirectedEdge(i, j) {
    const first = this.nodeList[i]; 
    const second = this.nodeList[j]; 

    first.neighbors.push(second);
    second.neighbors.push(first);
  };

  toString() {
    let string = "";

    for(const { name, neighbors} of nodeList) {
      string += `${name}: `;

      for(let i = 0; i < neighbors.length; i++) {
        string += `${neighbors[i].name}`;

        if(i !== neighbors.length - 1) {
          string += " -> ";
        }
      };

      string += '\n';

    };

    return string;

  };

  bfsHelper(vertice) {
    const queue = [vertice];

    while(queue.length) {
      const curr = queue.shift();
      curr.isVisited = true;
      const neighbors = curr.neighbors;

      console.log(curr.name, '==========');

      for(const neighbor of neighbors) {
        if(!neighbor.isVisited) {
          queue.push(neighbor);
          neighbor.isVisited = true;
        };
      };
    };
  };

  // TC: O(V) + O(E) ===> O(E) = O(V) + O(adj)
  bfs() {
    for(const vertice of this.nodeList) {
      // O(E) ===> O(E) = O(V) + O(adj)
      if(!vertice.isVisited) {
        this.bfsHelper(vertice);
      }
    };

  };
  
};

const A = new GraphNode("A", 0);
const B = new GraphNode("B", 1);
const C = new GraphNode("C", 2);
const D = new GraphNode("D", 3);
const E = new GraphNode("E", 4);

const nodeList = [A, B, C, D, E];

const graph = new Graph(nodeList);

graph.addUndirectedEdge(0, 1);
graph.addUndirectedEdge(0, 2);
graph.addUndirectedEdge(0, 3);

graph.addUndirectedEdge(1, 4);

graph.addUndirectedEdge(2, 3);

graph.addUndirectedEdge(3, 4);


console.log(graph.toString())
graph.bfs()

/*

 A: -> B -> C
 B: -> A -> E
 C: -> A -> D
 D: -> A -> C -> E
 E: -> B -> D
 */
