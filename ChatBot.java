import java.util.Scanner;

public class ChatBot {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("=== Rule Based AI ChatBot ===");

        while (true) {
            System.out.print("You: ");
            String input = sc.nextLine().toLowerCase();

            if (input.equals("hi") || input.equals("hello")) {
                System.out.println("Bot: Hello! Nice to meet you.");
            }
            else if (input.equals("how are you")) {
                System.out.println("Bot: I am doing great!");
            }
            else if (input.equals("what is your name")) {
                System.out.println("Bot: My name is DecodeBot.");
            }
            else if (input.equals("bye") || input.equals("exit")) {
                System.out.println("Bot: Goodbye! Have a nice day.");
                break;
            }
            else {
                System.out.println("Bot: Sorry, I don't understand that.");
            }
        }

        sc.close();
    }
}