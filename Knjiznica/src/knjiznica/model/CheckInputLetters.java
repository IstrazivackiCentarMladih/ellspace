package knjiznica.model;

public class CheckInputLetters {
	
	private static char[] letters = {'A', 'a', 'B', 'b', 'C', 'c', '�', '�', '�', '�', 'D', 'd', '�', '�', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'R', 'r', 'S', 's', '�', '�', 'T', 't', 'U', 'u', 'V', 'v', 'Z', 'z', '�', '�', 'Q', 'q', 'W', 'w', 'X', 'x', 'Y', 'y', ' ', '-'};	
	public static boolean check(String wordIn) {
		boolean isPossible = true;
		boolean checkLetter;
		
		for(int i = 0; i < wordIn.length(); ++i) {
			checkLetter = false;
			for(int j = 0; j < letters.length; ++j) {
				if ((i == 0 || i == wordIn.length() - 1) && wordIn.charAt(i) == '-') {
					isPossible = false;
				}
				if (wordIn.charAt(i) == letters[j]) {
					checkLetter = true;
				}
			}
			if (!checkLetter) {
				isPossible = false;
				break;
			}
		}
		return isPossible;
	}
	
}
