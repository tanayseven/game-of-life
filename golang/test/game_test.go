package test

import (
	"github.com/stretchr/testify/assert"
	"simple-game/game_of_life"
	"testing"
)

func TestThatASingleCellShouldDieInTheNextGeneration(t *testing.T) {
	universe := game_of_life.NewUniverse()
	universe.AddCell(0, 0)
	universe.IncrementGeneration()
	assert.Equal(t, 0, universe.TotalCells())
}

func TestThatTwoNeighbourCellsShouldDieInTheNextGeneration(t *testing.T) {
	universe := game_of_life.NewUniverse()
	universe.AddCell(0, 0)
	universe.AddCell(0, 1)
	universe.IncrementGeneration()
	assert.Equal(t, 0, universe.TotalCells())
}

func TestThatSingleCellSurvivesIfPreviousGenerationHasThreeDiagonalCells(t *testing.T) {
	universe := game_of_life.NewUniverse()
	universe.AddCell(0, 0)
	universe.AddCell(1, 1)
	universe.AddCell(2, 2)
	universe.IncrementGeneration()
	assert.Equal(t, 1, universe.TotalCells())
}

func TestThatABlockStaysInTheNextGeneration(t *testing.T)  {
	universe := game_of_life.NewUniverse()
	universe.AddCell(0, 0)
	universe.AddCell(1, 0)
	universe.AddCell(0, 1)
	universe.AddCell(1, 1)
	universe.IncrementGeneration()
	assert.Equal(t, 4, universe.TotalCells())
}

func TestThatThereShouldBeASingleCellAsSurvivorIfThereAreThreeCellsReproducingIt(t *testing.T) {
	universe := game_of_life.NewUniverse()
	universe.AddCell(0, 2)
	universe.AddCell(1, 0)
	universe.AddCell(2, 1)
	universe.IncrementGeneration()
	assert.Equal(t, 1, universe.TotalCells())
}

func TestThatHorizontalRowOfBlinkShouldBecomeVertical(t *testing.T) {
	universe := game_of_life.NewUniverse()
	universe.AddCell(0, 1)
	universe.AddCell(1, 1)
	universe.AddCell(2, 1)
	universe.IncrementGeneration()
	assert.Equal(t, 3, universe.TotalCells())
}
