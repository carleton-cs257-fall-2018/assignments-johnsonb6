package game_of_life;
/*
Created by Brennan Johnson and Silas Monahan, 2018
part of MVC. CellView is what the user sees. It is updated by CellModel, which is updated by user input into Controller
 */

import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

public class CellView extends Group {
    public final static double CELL_WIDTH = 20.0;

    @FXML private int rowCount;
    @FXML private int columnCount;
    public Rectangle[][] cellViews;

    public CellView() {
    }

    public int getRowCount() {
        return this.rowCount;
    }

    public void setRowCount(int rowCount) {
        this.rowCount = rowCount;
        this.initializeGrid();
    }

    public int getColumnCount() {
        return this.columnCount;
    }

    public void setColumnCount(int columnCount) {
        this.columnCount = columnCount;
        this.initializeGrid();
    }

    private void initializeGrid() {
        if (this.rowCount > 0 && this.columnCount > 0) {
            this.cellViews = new Rectangle[this.rowCount][this.columnCount];
            for (int row = 0; row < this.rowCount; row++) {
                for (int column = 0; column < this.columnCount; column++) {
                    Rectangle rectangle = new Rectangle();
                    rectangle.setX((double) column * CELL_WIDTH);
                    rectangle.setY((double) row * CELL_WIDTH);
                    rectangle.setWidth(CELL_WIDTH);
                    rectangle.setHeight(CELL_WIDTH);
                    this.cellViews[row][column] = rectangle;
                    this.getChildren().add(rectangle);
                    //added these next two rows
                    this.cellViews[row][column].setFill(Color.BLACK);
                    this.cellViews[row][column].setStroke(Color.WHITE);
                }
            }
        }
    }

    public void setDeadColor(int row, int column, Rectangle[][] rectangleList) {
        rectangleList[row][column].setFill(Color.BLACK);
    }
    public void setAliveColor(int row, int column, Rectangle[][] rectangleList) {
        rectangleList[row][column].setFill(Color.YELLOW);
    }



    public void nextGeneration(CellModel model) {
        assert model.getRowCount() == this.rowCount && model.getColumnCount() == this.columnCount;
        CellModel.CellValue[][] tempCells = new CellModel.CellValue[this.rowCount][this.columnCount];
        for (int row = 0; row <this.rowCount; row++){
            for (int col = 0; col <this.columnCount; col++){
                tempCells[row][col] = model.cells[row][col];
            }
        }
        for (int row = 0; row < this.rowCount; row++) {
            for (int column = 0; column < this.columnCount; column++) {
                CellModel.CellValue cellValue = model.getCellValue(row, column, model.cells);
                if (cellValue == CellModel.CellValue.DEAD) {
                    if (model.checkAdjacent(row, column, model.cells) == 3) {
                        model.setCellAlive(row, column, tempCells);
                    }
                } else { //if it is alive
                    if (model.checkAdjacent(row, column, model.cells) > 3 || model.checkAdjacent(row, column, model.cells) < 2) {
                        model.setCellDead(row, column, tempCells);
                    }
                }
            }
        }

        model.cells = tempCells;
        for (int row = 0; row < this.rowCount; row++) {
            for (int column = 0; column < this.columnCount; column++) {
                CellModel.CellValue cellValue = model.getCellValue(row, column, model.cells);
                if (cellValue == CellModel.CellValue.ALIVE) {
                    this.cellViews[row][column].setFill(Color.YELLOW);
                }
                if (cellValue == CellModel.CellValue.DEAD) {
                    this.cellViews[row][column].setFill(Color.BLACK);
                }
            }
        }
    }
}