package game_of_life;



public class CellModel {
    public enum CellValue {
        DEAD, ALIVE
    };


    // Note that runnerRow, runnerColumn, and dalekCount are all redundant with
    // the contents of cells, so we have to be careful throughout to keep them
    // coherent. We maintain this redundancy to avoid lags for large boards.
    private CellValue[][] cells;
    private int numberOfAliveCells;
    private int numberOfGenerations;


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

    public CellValue getCellValue(int row, int column) {
        assert row >= 0 && row < this.cells.length && column >= 0 && column < this.cells[0].length;
        return this.cells[row][column];
    }


    public int getRowCount() {
        return this.cells.length;
    }

    public int getColumnCount() {
        assert this.cells.length > 0;
        return this.cells[0].length;
    }



    public void setCellDead(int row, int column) {
        // sets cell to dead
    }

    public void setCellAlive(int row, int column) {
        // sets cell to alive
    }

    public void checkAdjacent() {
        // checks the status of the adjacent cells
        int rowCount = this.cells.length;
        int columnCount = this.cells[0].length;

        for (int row = 0; row < rowCount; row++) {
            for (int column = 0; column < columnCount; column++) {

            }
        }
    }

}