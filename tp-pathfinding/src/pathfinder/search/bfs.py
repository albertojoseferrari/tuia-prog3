from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Apply objective test
        if (grid.objective_test(root.state)):
            return Solution(root, reached)

        # Initialize frontier with the root node
        frontier = QueueFrontier()
        frontier.add(root)

        while True:
            if frontier.is_empty():
                return NoSolution(reached)
            n = frontier.remove()
            for a in grid.actions(n.state):
                ss = grid.result(n.state, a)
                if ss not in reached:
                    nn = Node("", ss, n.cost + grid.individual_cost(n.state, a), n, a)
                    if grid.objective_test(ss):
                        return Solution(nn, reached)
                    reached[ss] = True
                    frontier.add(nn)