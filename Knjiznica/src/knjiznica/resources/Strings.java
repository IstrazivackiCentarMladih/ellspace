package knjiznica.resources;

public class Strings {
	
	private static String link = "jdbc:postgresql://localhost:5432/TestFill";
	private static String username = null;
	private static String password = null;
	
	public static String getLink() { 
		return link;
	}
	
	public static String getPassword() {
		return password;
	}
	
	public static void setPassword(String password) {
		Strings.password = password;
	}

	public static String getUsername() {
		return username;
	}

	public static void setUsername(String username) {
		Strings.username = username;
	}
	
}