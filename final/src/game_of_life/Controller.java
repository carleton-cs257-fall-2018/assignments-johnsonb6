package game_of_life;
/*
Created by Brennan Johnson and Silas Monahan, 2018
part of MVC. User interacts with Controller, which manipulates CellModel, which relays changes to CellView.
 */
import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.input.MouseEvent;
import static game_of_life.CellModel.*;
import static game_of_life.CellView.*;
import java.util.Timer;
import java.util.TimerTask;

public class Controller implements EventHandler<KeyEvent> {
    /*
    @author Brennan Johnson & Silas Monahan
     */
    @FXML private CellView cellView;
    private CellModel cellModel;
    private Timer timer;

    public Controller() {
    }

    public void initialize() {
        /*
        @param none
        @return none
         */
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
        /*
        @param none
        @return double that represents the width of the board (num columns)
         */
        return CELL_WIDTH * this.cellView.getColumnCount();
    }

    public double getBoardHeight() {
        /*
        @param none
        @return double that represents height of board (num rows)
         */
        return CELL_WIDTH * this.cellView.getRowCount();
    }

    private void nextGeneration() {
        /*
        @param none
        @return none
         */
        this.cellView.nextGeneration(this.cellModel);
    }
    private void startTimer() {
        /*
        @param none
        @return none
         */
        this.timer = new java.util.Timer();
        TimerTask timerTask = new TimerTask() {
            public void run() {
                nextGeneration();
            }
        };

        long frameTimeInMilliseconds = (long)(500.0);
        this.timer.schedule(timerTask, 0, frameTimeInMilliseconds);
    }
    private void pauseTimer() {
        /*
        @param none
        @return none
         */
        this.timer.cancel();
    }

    @Override
    public void handle(KeyEvent keyEvent) {
        /*
        @param KeyEvent from user, represents intended action to be applied
        @return none
         */
        KeyCode code = keyEvent.getCode();

        String s = code.getChar();
        if (s.equals("N")) {
            this.nextGeneration();
        }
        if (s.equals("G")) {
            this.pauseTimer();
            this.cellModel.startSimulation();
            this.nextGeneration();
        }
        if (s.equals("R")) {
            this.startTimer();
        }
        if (s.equals("P")) {
            this.pauseTimer();
        }
    }

    public void handleMouseEvent(MouseEvent mouseEvent) {
        /*
        @param MouseEvent that represents a click of the mouse on the game board
        @return none
         */
        int rowCount = cellModel.cells.length;
        int columnCount = cellModel.cells[0].length;

        double mouseX = mouseEvent.getSceneX() - 10;
        double mouseY = mouseEvent.getSceneY() - 45;

        for (int row = 0; row < rowCount; row++) {
            for (int column = 0; column < columnCount; column++) {
                if (cellView.cellViews[row][column].contains(mouseX, mouseY)) {
                    if (cellModel.cells[row][column] == CellValue.DEAD) {
                        cellModel.setCellAlive(row, column, cellModel.cells);
                        cellView.setAliveColor(row, column, cellView.cellViews);
                    }
                    else {
                        cellModel.setCellDead(row, column, cellModel.cells);
                        cellView.setDeadColor(row, column, cellView.cellViews);
                    }
                }
            }
        }
    }
}
