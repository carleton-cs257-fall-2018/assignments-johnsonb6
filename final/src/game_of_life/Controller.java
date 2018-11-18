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
    @FXML private CellView cellView;
    private CellModel cellModel;
    private Timer timer;

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
    private void startTimer() {
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
        this.timer.cancel();
    }

    @Override
    public void handle(KeyEvent keyEvent) {
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
