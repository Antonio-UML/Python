class Node:
    """A node class for A* Pathfinding"""

    # Constructor
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    # Metodo para comparar si un nodo con otro nodo tiene la misma posicion
    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Crear Nodo Inicio y Nodo Fin
    start_node = Node(None, start)
    end_node = Node(None, end)

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [
            (0, -1),  # ↓
            (0, 1),  # ↑
            (-1, 0),  # ←
            (1, 0),  # →
            (-1, -1),  # ↙
            (-1, 1),  # ↖
            (1, -1),  # ↗
            (1, 1),  # ↘
        ]:  # Adjacent squares
            # Get node position
            node_position = (
                current_node.position[0] + new_position[0],
                current_node.position[1] + new_position[1],
            )

            # Make sure within range
            if (
                node_position[0] > (len(maze) - 1)
                or node_position[0] < 0
                or node_position[1] > (len(maze[len(maze) - 1]) - 1)
                or node_position[1] < 0
            ):
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                (child.position[1] - end_node.position[1]) ** 2
            )
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main(start, end):
    maze = [
        # 10 x 10
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    path = astar(maze, start, end)

    for row in maze:
        for cell in row:
            print(
                cell, end=" "
            )  # Imprimir el elemento de la celda seguido de un espacio
        print()

    print("---------------------------------")

    # Guardar coordenadas a reemplazar
    coordinates_to_replace = path

    # Reemplazar por puntos las coordenadas
    for coord in coordinates_to_replace:
        row, col = coord
        maze[row][col] = "."  # Reemplazar el valor en la posición con un punto

    # Imprimir la matriz con los nuevos puntos
    for row in maze:
        for cell in row:
            print(
                cell, end=" "
            )  # Imprimir el elemento de la celda seguido de un espacio
        print()  # Salto de línea después de imprimir la fila

    # Imprimir las coordenadas que cambiaron por puntos
    print(path)


if __name__ == "__main__":
    main((0, 0), (3, 8))
