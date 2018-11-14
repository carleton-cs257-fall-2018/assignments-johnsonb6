package game_of_life;

import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

public class CellView extends Group {
    public final static double CELL_WIDTH = 20.0;

    @FXML private int rowCount;
    @FXML private int columnCount;
    private Rectangle[][] cellViews;

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

    /*
    public void nextGeneration(CellModel model) {
        assert model.getRowCount() == this.rowCount && model.getColumnCount() == this.columnCount;
        for (int row = 0; row < this.rowCount; row++) {
            for (int column = 0; column < this.columnCount; column++) {
                CellModel.CellValue cellValue = model.getCellValue(row, column);
                if (cellValue == CellModel.CellValue.DEAD) {
                    this.cellViews[row][column].setFill(Color.BLACK);
                    this.cellViews[row][column].setStroke(Color.WHITE);
                } else if (cellValue == CellModel.CellValue.ALIVE) {
                    this.cellViews[row][column].setFill(Color.WHITE);
                }
                //here is where we need to call the check adjacent method.
                // I put it in cellModel but maybe it could go in this file instead
            }

        }
    }*/

    public void nextGeneration(CellModel model) {
        assert model.getRowCount() == this.rowCount && model.getColumnCount() == this.columnCount;
        model.tempCells = model.cells;
        for (int row = 0; row < this.rowCount; row++) {
            for (int column = 0; column < this.columnCount; column++) {
                CellModel.CellValue cellValue = model.getCellValue(row, column);
                if (cellValue == CellModel.CellValue.DEAD) {
                    if (model.cells[row][column].checkAdjacent() == 3) {
                        model.setCellAlive(row, column, model.tempCells);
                    }
                } else if (cellValue == CellModel.CellValue.ALIVE) {
                    if (model.cells[row][column].checkAdjacent() > 3 || model.cells[row][column].checkAdjacent() < 2) {
                        model.setCellDead(row, column, model.tempCells);
                    }
                }
                //here is where we need to call the check adjacent method.
                // I put it in cellModel but maybe it could go in this file instead
            }

        }
        model.cells = model.tempCells;
        for (int row = 0; row < this.rowCount; row++) {
            for (int column = 0; column < this.columnCount; column++) {
                CellModel.CellValue cellValue = model.getCellValue(row, column);
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