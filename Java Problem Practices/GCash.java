/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
import java.util.*;

public class Main
{
    public class Account{
        private String username;
        private String password;
        
        public Account(String username, String password){
            this.username = username;
            this.password = password;
        }
        public String getUsername(){
            return username;
        }
        public String getPassword(){
            return password;
        }
        
    }
    
    static LinkedList<Account> accounts = new LinkedList<>();
    
	public static void main(String[] args) {
	    Scanner scan = new Scanner(System.in);
		System.out.println("GCash Me");
		
		loginSystem(scan);
		
		scan.close();
		
	}
	
	public static boolean loginSystem(Scanner scan){
	    System.out.println("1. Login");
		System.out.println("2. Register");
		int choice = scan.nextInt();
		scan.nextLine(); // Consume leftover newline
		if(choice == 1){
		    System.out.print("Input Username: ");
		    String username = scan.nextLine();
		    System.out.print("Input Password: ");
		    String password = scan.nextLine();
		    
		    
		}
		return false;
	}
}








