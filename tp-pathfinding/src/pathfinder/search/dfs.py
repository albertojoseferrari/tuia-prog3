from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search
        Args:
            grid (Grid): Grid of points
        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        # Initialize expanded with the empty dictionary
        expanded = dict()
        # Initialize frontier with the root node
        frontier = StackFrontier()
        frontier.add(root)
        if grid.objective_test(root.state):
            return Solution(root, expanded)
        
        while True:
            if frontier.is_empty():
                return NoSolution(expanded)
            n = frontier.remove()
            if n.state in expanded:
                continue

            expanded[n.state] = True
            for a in grid.actions(n.state):
                ss = grid.result(n.state,a)
                if ss not in expanded:
                    nn = Node("",ss,n.cost+grid.individual_cost(n.state,a),n,a)
                    if grid.objective_test(ss):
                        return Solution(nn, expanded)
                    frontier.add(nn)
                    #expanded[ss] = True   # ← AGREGÁ ESTA LÍNEA

        #return NoSolution(expanded)
