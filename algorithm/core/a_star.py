"""
A draft version, not workable yet.
"""


class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def pop_next(open_list):
    """
    TODO: Should be optimized by priority queue
    """
    min_node = None
    for (position, node) in open_list.items():
        if not min_node or min_node.f < node.f:
            min_node = node
    open_list.pop(min_node.position)
    return min_node


def distance(src, dst):
    return abs(dst[0] - src[0]) ** 2 + abs(dst[1] - src[1]) ** 2


def a_star(maze, start, end):
    """
    Returns a list of tuples as a path from the given start to the given end in the given maze
    """

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_dict = dict()
    closed_set = set()

    # Add the start node
    open_dict[start] = start_node

    # Loop until you find the end
    while open_dict:

        # Get the current node
        current_node = pop_next(open_dict)

        # Add to closed list
        closed_set.add(current_node.position)

        # Found the goal
        if current_node == end_node:
            path = []
            node = current_node
            while node:
                path.append(node.position)
                node = node.parent
            return path[::-1]  # Return reversed path

        def adjacent(position):
            i, j = position[0], position[1]
            m, n = len(maze), len(maze[0])
            for (x, y) in (
                    (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j),
                    (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1),):
                if 0 <= x < m and 0 <= y < n:
                    yield (x, y)

        # Generate children
        for (x, y) in adjacent(current_node.position):
            if maze[x][y] == 1:
                continue

            if (x, y) in closed_set:
                continue

            new_node = Node(current_node, (x, y))
            new_node.g = current_node.g + 1
            new_node.h = distance(new_node.position, end_node.position)
            new_node.f = new_node.g + new_node.h

            if (x, y) in open_dict and open_dict[(x, y)].g < new_node.g:
                continue

            open_dict[(x, y)] = new_node


def main():
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (0, 6)

    path = a_star(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()
