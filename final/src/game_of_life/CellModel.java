package game_of_life;

/*
Created by Brennan Johnson and Silas Monahan, 2018
part of MVC. CellModel is manipulated by Controller, and relays manipulations to CellView.
 */


public class CellModel {
    /*
    @author Brennan Johnson & Silas Monahan
     */
    public enum CellValue {
        DEAD, ALIVE
    }

    public CellValue[][] cells;



    public CellModel(int rowCount, int columnCount) {
        /*
        @param int num rows, int num columns
        @return none
         */
        assert rowCount > 0 && columnCount > 0;
        this.cells = new CellValue[rowCount][columnCount];
        this.startSimulation();
    }

    public void startSimulation() {
        /*
        @param none
        @return none
         */
        this.initializeSimulation();
    }

    private void initializeSimulation() {
        /*
        @param none
        @return none
         */
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
        /*
        @param int row, int column, CellValue[][] list of cells to be searched through
        @return CellValue value of cell at row, column that was passed in through params
         */
        assert row >= 0 && row < list.length && column >= 0 && column < list[0].length;
        return list[row][column];
    }


    public int getRowCount() {
        /*
        @param none
        @return int number of rows in grid
         */
        return this.cells.length;
    }

    public int getColumnCount() {
        /*
        @param none
        @return int number of columns in grid
         */
        assert this.cells.length > 0;
        return this.cells[0].length;
    }


    public void setCellDead(int row, int column, CellValue[][] list) {
        /*
        @param int row, int column, CellValue[][] list
        @return none
         */
        list[row][column] = CellValue.DEAD;
    }

    public void setCellAlive(int row, int column, CellValue[][] list) {
        /*
        @param int row, int column, CellValue[][] list
        @return none
         */
        list[row][column] = CellValue.ALIVE;
    }

    public int checkAdjacent(int row, int column, CellValue[][] list) {
        /*
        @param int row, int column, CellValue[][] list
        @return int that represents num of adjacent cells that are alive
        checks the status of the adjacent cells
         */

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
