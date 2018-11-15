package game_of_life;

import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;

import static game_of_life.CellModel.*;
import static game_of_life.CellView.*;

public class Controller implements EventHandler<KeyEvent> {
    @FXML private Label scoreLabel;
    @FXML private Label messageLabel;
    @FXML private CellView cellView;
    private CellModel cellModel;

    public Controller() {
    }

    public void initialize() {
        this.cellModel = new CellModel(this.cellView.getRowCount(), this.cellView.getColumnCount());

        this.cellView.addEventFilter(MouseEvent.MOUSE_PRESSED, new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent mouseEvent) {
                handleMouseEvent(mouseEvent);
            }
        });
        this.nextGeneration();
    }

    public double getBoardWidth() {
        return CELL_WIDTH * this.cellView.getColumnCount();
    }

    public double getBoardHeight() {
        return CELL_WIDTH * this.cellView.getRowCount();
    }

    private void nextGeneration() {
        this.cellView.nextGeneration(this.cellModel);
    }

    @Override
    public void handle(KeyEvent keyEvent) {
        boolean keyRecognized = true;
        KeyCode code = keyEvent.getCode();

        String s = code.getChar();
        if (s.length() > 0) {
            char theCharacterWeWant = s.charAt(0);
        }
        if (s.equals("N")) {
            this.nextGeneration();
        }
    }

    public void handleMouseEvent(MouseEvent mouseEvent) {
        int rowCount = cellModel.cells.length;
        int columnCount = cellModel.cells[0].length;

        double mouseX = mouseEvent.getSceneX() - 10;
        double mouseY = mouseEvent.getSceneY() - 45;

        for (int row = 0; row < rowCount; row++) {
            for (int column = 0; column < columnCount; column++) {
                if (cellView.cellViews[row][column].contains(mouseX, mouseY)) {
                    if (cellModel.cells[row][column] == CellValue.DEAD) {
                        CellModel.setCellAlive(row, column, cellModel.cells);
                        cellView.setAliveColor(row, column);
                    }
                    if (cellModel.cells[row][column] == CellValue.ALIVE) {
                        CellModel.setCellDead(row, column, cellModel.cells);
                        cellView.setDeadColor(row, column);
                    }
                }
            }
        }
    }
}
