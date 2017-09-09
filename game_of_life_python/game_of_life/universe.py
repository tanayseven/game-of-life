def get_all_possible_neighbours_for(cell):
    x, y = cell
    return {(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y),                 (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
            }


class Universe:
    def __init__(self, cells=None):
        if cells is None:
            cells = set()
        self._cells = set(cells)

    def __len__(self):
        return len(self._cells)

    def _actual_neighbours_for(self, cell) -> set:
        return self._cells.intersection(get_all_possible_neighbours_for(cell))

    def _potential_reproducible_neighbours(self) -> set:
        all_possible_neighbouring_cells = set()
        [all_possible_neighbouring_cells.update(set(get_all_possible_neighbours_for(cell))) for cell in self._cells]
        return all_possible_neighbouring_cells

    def _compute_survivors(self):
        return (cell for cell in self._cells if
                len(self._actual_neighbours_for(cell)) == 2 or len(self._actual_neighbours_for(cell)) == 3)

    def _compute_reproductions(self, potential_reproducible_neighbours):
        return (cell
                for cell in potential_reproducible_neighbours if len(self._actual_neighbours_for(cell)) == 3)

    def increment_generation(self):
        potential_reproducible_neighbours = self._potential_reproducible_neighbours()
        reproduced_cells = set(
            self._compute_reproductions(potential_reproducible_neighbours)
        )
        self._cells = set(
            self._compute_survivors()
        ).union(reproduced_cells)

    def has_cells(self, cells=None) -> bool:
        if cells is None:
            cells = set()
        cells = set(cells)
        return len(cells) == len(cells.intersection(self._cells))
