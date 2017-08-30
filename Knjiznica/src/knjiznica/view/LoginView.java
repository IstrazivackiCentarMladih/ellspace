package knjiznica.view;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import org.postgresql.util.PSQLException;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;

public class LoginView {

	@FXML
	private TextField usernameText;
	
	@FXML
	private PasswordField passwordText;
	
	@FXML
	private Label errorLabel;
		
	@FXML 
	private BorderPane root;
	
	public void login() {

	}
	
	public void initialize() {
		root.setId("pane");
	}
	
	@FXML
	private void activateLogin() {
		String username = usernameText.getText();
		String password = passwordText.getText();
		
        try {
        	@SuppressWarnings("unused")
			Connection con = DriverManager.getConnection(
					"jdbc:postgresql://localhost:5432/TestFill", username, password);
		} catch (PSQLException e) {
			errorLabel.setVisible(true);
			passwordText.setText("");
		} catch (SQLException e) {
			e.printStackTrace();
		}

		System.out.println(username + '\t' + password);
		
		//errorLabel.setText("Successful login!");
		//errorLabel.setVisible(true);
				
		//close window / view
		
	}
	
}