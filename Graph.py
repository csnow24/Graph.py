from typing import Any

class Graph:
    def __init__(self, is_directed=False, num_verticies=4):
        """Initialize graph with specified number of vertices (default: 4).""" 

        self.num_verticies = num_verticies

        # The 'Brain' of the graph: Dictionary
        self.adj_list: dict[Any, list[tuple[Any, int]]] = {}

        # Keys: Node IDs, Values: List of (neighbor, weight) tuples
        self.is_directed = is_directed 

        

    def __str__(self) -> str:
        """ Verbal explanation of the graph"""

        return (
        f"There are a total of {self.num_edges()} edges, {self.num_vertices()} vertices,\n"
        f"and the largest connection is {self.longest_edge()}.\n"
        f"The shortest connection is {self.shortest_edge()}.\n"
        )
                    
        
    def describe(self) -> str | int:
        """ Returns a direct description of the graph. """
        print(self.adj_list)
        print(self.num_vertices())
        print(self.num_edges())
        print(self.shortest_edge())
        print(self.longest_edge())
        
    def num_vertices(self) -> int:
        """ Returns the total amount of nodes. """
        counter = 0 
        # Iterate throught the outer list to count inner list
        for node in self.adj_list:
            counter += 1
        return counter

    def num_edges(self) -> int:
        """ Returns the total amount of edges. """
        counter = 0 
        # Iterate throught the outer list
        for node in self.adj_list:
            # For each element in inner list, add to counter
            neighbors = len(self.adj_list[node])
            counter += neighbors
        return counter

    def shortest_edge(self) -> str:
        """ Returns the index of the vertex with the least neighbors."""
        # Will hold the current amount of neighbors for node to compare with
        # - updated neighbor 
        current_lowest = "" 
        for node in self.adj_list:

            # Edge case b/c 0 will likely be the smallest value(loop pointless)
            current_biggest = len(self.adj_list[node])
            neighbors = len(self.adj_list[node])
            if neighbors < current_biggest:
                current_biggest = node
                current_lowest += node
        return node

    def longest_edge(self) -> str:
        """ Returns the index of the vertex with the most neighbors."""
        # Will hold the current amount of neighbors for node to compare with
        # - new neighbor 
        current_biggest = 0 
        for node in self.adj_list:

            neighbors = len(self.adj_list[node])
            current_lowest = 0
            
            if neighbors > current_lowest:
                current_biggest = node

            return node

    
    def add_edge(self, from_node: Any, to_node: Any, weight=1) -> None:
        """ Adds an edge between vertices from_node and to_node with
            the specified non-negative weight """
        
        # 1. Ensure both nodes exist in out dictionary
        # (If the don't, we create them on the fly!)
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        # 2. Add the connection (from_node to to_node)
        self.adj_list[from_node].append((to_node, weight))

        # 3. If NOT directed, the connection goes both ways
        if not self.is_directed:
            self.adj_list[to_node].append(from_node, weight)

    def adjust_edge(self, from_node, to_node, weight) -> None:
        """ Change the weight of an edge between vertices
            from_node and to_node to the specified non-negative weight """
        # Checks for edge
        exists = self.exists_edge(from_node, to_node)

        if exists is True:
            for e in enumerate(self.adj_list[from_node]):
                index = e[0]
                edge_tuple = e[1]
                if edge_tuple[0] == to_node:
                    self.remove_edge(from_node, to_node)
                    self.add_edge(from_node, to_node, weight)
                    return

    def remove_edge(self, from_node, to_node) -> None:
        """ Removes edge between vertices from_node and to_node. """

        # Checks for edge
        exists = self.exists_edge(from_node, to_node)
        
        if exists is True:
            # Find the index of the to_node
            
            for e in enumerate(self.adj_list[from_node]):
                index = e[0]
                
                edge_tuple = e[1]
                
                if edge_tuple[0] == to_node:
                    del self.adj_list[from_node][index]
                    return
        
            

    def exists_edge(self, from_node, to_node) -> bool | ValueError:
        """ Tells if an edge between vertices from_node and to_node exists or not"""

        # Check if the from node exist in the list
        if from_node not in self.adj_list:
            raise ValueError("Node doesn't exist!")

        # Checks the from nodes connections; if destination node exist
        for e in self.adj_list[from_node]:
            if e[0] == to_node:
                return True

        # Edge case for the edge not existing 
        ValueError("Edge does not exist!")
        

    def add_node(self,node: Any) -> None:
        """Adds a node to the graph if it does not exist. """
        # Only add if it doesn't exist yet 
        if node not in self.adj_list:
            self.adj_list[node] = []
            return True
        return False 

    def display(self) -> int:
        """Prints the Adjacency List representation of the graph."""
        for node in self.adj_list:
            # Get the list of neighbors
            neighbors = self.adj_list[node]
            print(f"{node} -> {neighbors}")

# --------------------- TESTER FUNCTION --------------------        
if __name__ == "__main__":
    g = Graph(True)
    g.add_node('Alice')
    g.add_edge('Alice', 'Bob')
    g.add_edge('Alice', 'Chris')

    g.display()

    print()

    g.remove_edge('Alice', 'Bob')
    g.adjust_edge('Alice', 'Chris', 5)

    print()

    print(g)
   
    
    
