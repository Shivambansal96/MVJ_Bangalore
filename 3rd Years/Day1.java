
class Day1 {

    public static void main(String[] args) {
        // System.out.print("HeLL\nHello");

        // System.out.println("*\n * *\n * * *\n * * * *\n * * * * *");
        // int a = 5; // var0 = 5
        // int b = 10; // var1 = 10
        // a = 1; // var2 = 1
        // System.out.print(a + b);
        // Scanner sc = new Scanner(System.in);
        // String firstName = sc.next();  // Shivam Bansal
        // sc.nextLine();
        // int marks = sc.nextInt();
        // System.out.println(firstName);
        // System.out.println(marks);
        // int a = 5;
        // a = a + 5;
        // a *= 5;
        // a = 10;
        // System.out.print(a == 5 ? "Match" : "Not matched");
        // // System.out.println(a);
        // // Write a program to categorize Minor, Adult, Senior Citizen and Super Senior Citizen // //
        // int age = 165;
        // if(age < 18)
        //     System.out.println("Minor");
        // else if (age >= 18 && age < 60) 
        //     System.out.println("Adult");
        // else if (age >= 60 && age < 80) 
        //     System.out.println("Senior Citizen");
        // else 
        //     System.out.println("Super Senior Citizen");

        // int age = 94;

        // if (age >= 18) {
        //     if (age >= 60) {
        //         if (age >= 80) {
        //             System.out.println(" Super Senior Citizen");
        //         } else {
        //             System.out.println("Senior Citizen");
        //         }
        //     } else {
        //         System.out.println("Adult");
        //     }

        // } else {
        //     System.out.println("Minor");
        // }


        int num = 123;
        int originalNum = num;

        int revNum = 0;
        while(num != 0) {
            int r = num % 10;
            revNum = (revNum * 10) + r;
            num /= 10;
        }

        System.out.println("Reversed Number: " + revNum);
        System.out.println(originalNum == revNum ? "Palindrome" : "NOT Palindrome");



    }
}
