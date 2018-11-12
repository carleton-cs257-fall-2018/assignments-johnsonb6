package game_of_life;

import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.input.MouseEvent;

public class Controller implements EventHandler<MouseEvent> {
    @FXML private Label scoreLabel;
    @FXML private Label messageLabel;
    @FXML private CellView cellView;
    private CellModel cellModel;

    public Controller() {
    }

    public void initialize() {
        this.cellModel = new CellModel(this.cellView.getRowCount(), this.cellView.getColumnCount());
        this.nextGeneration();
    }

    public double getBoardWidth() {
        return CellView.CELL_WIDTH * this.cellView.getColumnCount();
    }

    public double getBoardHeight() {
        return CellView.CELL_WIDTH * this.cellView.getRowCount();
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

    @Override
    public void handle(MouseEvent mouseEvent) {
        //Need to only handle mouse clicked
        //change the status of the clicked on cell to dead or alive, whichever it is not
    }
}
