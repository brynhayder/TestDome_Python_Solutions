def get_neighbour_idx(x, y, map_matrix):
  candidates = [
    (x-1, y),
    (x, y-1),
    (x, y+1),
    (x+1, y),
  ]
  map_ydim = len(map_matrix[0])
  map_xdim = len(map_matrix)
  return [(xp, yp) for xp, yp in candidates if 0<=xp<map_xdim and
          0<=yp<map_ydim]
    
def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    dest = to_row, to_column
    current = from_row, from_column
    if current == dest:
        return True
    if not map_matrix[from_row][from_column]:
        return False

    def options_not_visited(current, map_matrix, visited):
        return [
            (x, y) for x, y in get_neighbour_idx(*current, map_matrix)
            if map_matrix[x][y] and
            (x, y) not in visited
            ]

    visited = set([current])
    stored_options = list()
    while True:
        current_options = options_not_visited(
                current, map_matrix, visited)
        if dest in current_options:
            return True

        if not current_options:
            if not stored_options:
                return False
            else:
                next_node = stored_options.pop()
        else:
            next_node = current_options.pop()
            stored_options.extend(current_options)

        current = next_node
        visited.add(current)

if __name__ == '__main__':
    # print(get_neighbour_idx(1, 1, map_matrix))
    # print(get_neighbour_idx(0, 0, map_matrix))
    # print(get_neighbour_idx(2, 0, map_matrix))

    map_matrix0 = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ]

    map_matrix1 = [
        [True, False, False],
        [True, False, False],
        [False, True, True]
    ]

    map_matrix2 = [
        [True, True, False],
        [True, True, True],
        [False, False, True]
    ]

    map_matrix3 = [
        [True, True, False],
        [True, True, True],
        [False, False, True],
        [True, True, True],
    ]
    matrices_and_answers = [
     ( map_matrix0, True),
     ( map_matrix1, False),
     ( map_matrix2, True),
     ( map_matrix3, True),
     ]

    for map_mat, ans in matrices_and_answers:
        # for row in map_mat:
            # print(row)
        print(route_exists(0, 0, 2, 2, map_mat), ans)
