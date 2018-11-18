from functools import reduce
from typing import Set, Tuple


def get_all_possible_neighbours_for(cell):
    x, y = cell
    return {(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y),                 (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
            }


def survival_rule(neighbour_count: int) -> bool:
    return 2 <= neighbour_count <= 3


def reproduction_rule(neighbour_count: int) -> bool:
    return neighbour_count == 3


class Universe:
    def __init__(self, cells=None):
        self._cells: Set[Tuple[int, int]] = set(cells or [])

    def __len__(self):
        return len(self._cells)

    def __add__(self, cell: set) -> 'Universe':
        new_universe = Universe(self._cells)
        new_universe._cells.add(cell)
        return new_universe

    def __str__(self):
        return str(self._cells)

    def __eq__(self, other: 'Universe'):
        return self._cells == other._cells if type(other) == Universe else self._cells == other

    def tick_generation(self) -> 'Universe':
        new_universe_dead_or_alive = self._activate_cells(survival_rule, self._cells)
        potential_neighbours_of_alive_cells = reduce(
            lambda x, y: x.union(y),
            [get_all_possible_neighbours_for(cell) for cell in self._cells]
        )
        new_universe_reproduced = self._activate_cells(reproduction_rule, potential_neighbours_of_alive_cells)
        return Universe(new_universe_dead_or_alive._cells.union(new_universe_reproduced._cells))

    def _compute_alive_neighbours(self, cell: tuple) -> int:
        return len(get_all_possible_neighbours_for(cell).intersection(self._cells))

    def _activate_cells(self, rule, cells):
        return Universe([cell for cell in cells if rule(self._compute_alive_neighbours(cell))])
