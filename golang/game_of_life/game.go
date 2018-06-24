package game_of_life

type Cell struct {
	X int
	Y int
}
type Universe struct {
	Cells map[Cell]bool
}

func NewUniverse() Universe {
	return Universe{Cells: map[Cell]bool{}}
}

func (u *Universe) AddCell(x, y int) {
	u.Cells[Cell{X: x, Y: y}] = true
}

func (u *Universe) TotalCells() int {
	return len(u.Cells)
}

func (u *Universe) IncrementGeneration() {
	newCells := map[Cell]bool{}
	for cell := range u.Cells {
		if len(u.getNeighbours(cell)) >= 2 {
			newCells[cell] = true
		}
		computeSurroundingReproductions(cell, u, newCells)
	}
	u.Cells = newCells
}

func computeSurroundingReproductions(cell Cell, u *Universe, newCells map[Cell]bool) {
	for _, possibleReproduction := range getAllPossibleNeighbours(cell) {
		if len(u.getNeighbours(possibleReproduction)) == 3 {
			newCells[possibleReproduction] = true
		}
	}
}

func (u *Universe) getNeighbours(cell Cell) map[Cell]bool {
	possibleNeighbours := getAllPossibleNeighbours(cell)
	actualNeighbours := map[Cell]bool{}
	for _, possibleNeighbour := range possibleNeighbours {
		if _, ok := u.Cells[possibleNeighbour]; ok {
			actualNeighbours[possibleNeighbour] = true
		}
	}
	return actualNeighbours
}

func getAllPossibleNeighbours(cell Cell) []Cell {
	possibleNeighbours := []Cell{
		{X: cell.X - 1, Y: cell.Y - 1}, {X: cell.X + 0, Y: cell.Y - 1}, {X: cell.X + 1, Y: cell.Y - 1},
		{X: cell.X - 1, Y: cell.Y + 0}, {X: cell.X + 1, Y: cell.Y + 0},
		{X: cell.X - 1, Y: cell.Y + 1}, {X: cell.X + 0, Y: cell.Y + 1}, {X: cell.X + 1, Y: cell.Y + 1},
	}
	return possibleNeighbours
}
