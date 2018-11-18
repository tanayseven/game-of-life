from game_of_life.universe import Universe


def test_single_cell_should_die_in_the_next_generation():
    universe = Universe(cells=[(0, 0)])
    new_universe = universe.tick_generation()
    assert len(new_universe) == 0


def test_two_neighbouring_cells_should_die_in_the_next_generation():
    universe = Universe(cells=[(0, 0), (0, 1)])
    new_universe = universe.tick_generation()
    assert len(new_universe) == 0


def test_single_cell_survives_if_previous_generation_has_three_diagonal_cells():
    universe = Universe(cells=[(0, 0), (1, 1), (2, 2)])
    new_universe = universe.tick_generation()
    assert len(new_universe) == 1


def test_a_block_stays_in_the_next_generation():
    universe = Universe(cells=[(0, 0), (0, 1), (1, 0), (1, 1)])
    new_universe = universe.tick_generation()
    assert len(new_universe) == 4
    assert new_universe == Universe({(0, 0), (0, 1), (1, 0), (1, 1)})


def test_there_should_be_a_single_cell_as_survivor_if_there_are_three_cells_that_reproduce_it():
    universe = Universe(cells=[(0, 2), (1, 0), (2, 1)])
    new_universe = universe.tick_generation()
    assert len(new_universe) == 1
    assert new_universe == {(1, 1)}


def test_a_horizontal_blinker_should_be_vertical_in_next_generation():
    universe = Universe(cells=[(0, 0), (1, 0), (2, 0)])
    new_universe = universe.tick_generation()
    assert len(new_universe) == 3
    assert new_universe == {(1, 0), (1, -1), (1, 1)}
