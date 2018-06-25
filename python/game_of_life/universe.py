from functools import reduce
from typing import Set, Tuple


def get_all_possible_neighbours_for(cell):
    x, y = cell
    return {(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y),                 (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
            }


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
        def survival_condition(cell_count: int) -> bool:
            return 2 <= cell_count <= 3

        def reproduction_condition(cell_count: int) -> bool:
            return cell_count == 3

        new_universe_dead_or_alive = self._tick_for_alive_neighbours(survival_condition)
        new_universe_reproduced = self._tick_for_reproduction(reproduction_condition)
        return Universe(new_universe_dead_or_alive._cells.union(new_universe_reproduced._cells))

    def _compute_alive_neighbours(self, cell: tuple) -> int:
        return len(get_all_possible_neighbours_for(cell).intersection(self._cells))

    def _tick_for_alive_neighbours(self, condition):
        return Universe([cell for cell in self._cells if condition(self._compute_alive_neighbours(cell))])

    def _tick_for_reproduction(self, condition):
        potential_neighbours_of_alive_cells = reduce(
            lambda x, y: x.union(y),
            [get_all_possible_neighbours_for(cell) for cell in self._cells]
        )
        return Universe(
            [cell for cell in potential_neighbours_of_alive_cells if condition(self._compute_alive_neighbours(cell))]
        )
