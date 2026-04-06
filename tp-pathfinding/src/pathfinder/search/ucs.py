from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root, root.cost)

        while True:
            if frontier.is_empty():
                return NoSolution(reached)
            n = frontier.pop()
            if grid.objective_test(n.state):
                return Solution(n, reached)
            for a in grid.actions(n.state):
                ss = grid.result(n.state, a)
                cc = n.cost + grid.individual_cost(n.state, a)
                if ss not in reached or cc < reached[ss]:
                    nn = Node("", ss, cc, n, a)
                    reached[ss] = cc
                    frontier.add(nn, cc)