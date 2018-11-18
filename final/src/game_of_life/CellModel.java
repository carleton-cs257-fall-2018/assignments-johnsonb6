package game_of_life;

/*
Created by Brennan Johnson and Silas Monahan, 2018
part of MVC. CellModel is manipulated by Controller, and relays manipulations to CellView.
 */


public class CellModel {
    public enum CellValue {
        DEAD, ALIVE
    }

    public CellValue[][] cells;



    public CellModel(int rowCount, int columnCount) {
        assert rowCount > 0 && columnCount > 0;
        this.cells = new CellValue[rowCount][columnCount];
        this.startSimulation();
    }

    public void startSimulation() {
        this.initializeSimulation();
    }

    private void initializeSimulation() {
        int rowCount = this.cells.length;
        int columnCount = this.cells[0].length;

        // all cells dead
        for (int row = 0; row < rowCount; row++) {
            for (int column = 0; column < columnCount; column++) {
                this.cells[row][column] = CellValue.DEAD;
            }
        }

    }

    public CellValue getCellValue(int row, int column, CellValue[][] list) {
        assert row >= 0 && row < list.length && column >= 0 && column < list[0].length;
        return list[row][column];
    }


    public int getRowCount() {
        return this.cells.length;
    }

    public int getColumnCount() {
        assert this.cells.length > 0;
        return this.cells[0].length;
    }


    public void setCellDead(int row, int column, CellValue[][] list) {
        list[row][column] = CellValue.DEAD;
    }

    public void setCellAlive(int row, int column, CellValue[][] list) {
        list[row][column] = CellValue.ALIVE;
    }

    public int checkAdjacent(int row, int column, CellValue[][] list) {
        // checks the status of the adjacent cells
        int rowCount = list.length;
        int columnCount = list[0].length;

        int adjacentCount = 0;
        //up left
        if (row > 0 && column > 0 && list[row - 1][column - 1] == CellValue.ALIVE) {
            adjacentCount++;
        }
        //up
        if (row > 0 && list[row - 1][column] == CellValue.ALIVE) {
            adjacentCount++;
        }
        //up right
        if (column < columnCount - 1 && row > 0 && list[row - 1][column + 1] == CellValue.ALIVE) {
            adjacentCount++;
        }
        if (column < (columnCount - 1)) { //right
            if (list[row][column + 1] == CellValue.ALIVE) {
                adjacentCount++;
            }
        }
        if (column < columnCount - 1 && row < rowCount - 1) { //down right
            if (list[row + 1][column + 1] == CellValue.ALIVE) {
                adjacentCount++;
            }
        }
        if (row < rowCount - 1) { //down
            if (list[row + 1][column] == CellValue.ALIVE) {
                adjacentCount++;
            }
        }
        //down left
        if (row < rowCount - 1 && column > 0 && cells[row + 1][column - 1] == CellValue.ALIVE) {
            adjacentCount++;
        }
        //left
        if (column > 0 && cells[row][column - 1] == CellValue.ALIVE) {
            adjacentCount++;
        }
        return adjacentCount;
    }
}
