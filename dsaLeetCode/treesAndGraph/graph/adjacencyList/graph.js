
// vertice
class GraphNode {
  neighbors = [];

  constructor(name, index) {
    this.name = name;
    this.index = index;
  };
}


class Graph {
  constructor(nodeList = []) {
    this.nodeList = nodeList;
  }

  addUndirectedEdge(i, j) {
    const first = nodeList[i];
    const second = nodeList[j];

    if(!first.neighbors.includes(second)) {
      first.neighbors.push(second);
    };

    if(!second.neighbors.includes(first)) {
      second.neighbors.push(first);
    };
  }

  toString() {
    let string = '';

    for(let i = 0; i < nodeList.length; i++) {
      const node = nodeList[i];

      string += `${node.name}: `;

      const neighbors = node.neighbors;

      for(let j = 0; j < neighbors.length; j++) {
        string += ` ${neighbors[j].name}`;

        if(j + 1 !== neighbors.length) {
          string += ' ->'

        }
      }

      string += '\n';
    }

    return string;

  }

};


const node1 = new GraphNode('A', 0);
const node2 = new GraphNode('B', 1);
const node3 = new GraphNode('C', 2);
const node4 = new GraphNode('D', 3);
const node5 = new GraphNode('E', 4);

const nodeList = [node1, node2, node3, node4, node5];

const graph = new Graph(nodeList);

graph.addUndirectedEdge(0,1);
graph.addUndirectedEdge(0,2);
graph.addUndirectedEdge(0,3);

graph.addUndirectedEdge(1,0);
graph.addUndirectedEdge(1,4);


graph.addUndirectedEdge(2,0);
graph.addUndirectedEdge(2,3);

graph.addUndirectedEdge(3,2);
graph.addUndirectedEdge(3,0);
graph.addUndirectedEdge(3,4);


graph.addUndirectedEdge(4,1);
graph.addUndirectedEdge(4,3);

console.log(graph.toString())
