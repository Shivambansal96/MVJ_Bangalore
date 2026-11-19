public class Day3 {

    public static String teacherName() {
        String name = "Shivam";
        System.out.println("Shivam Bansal");
        return name;
    }

    public static int addition(int f, int n) {
        int a = 5;
        int b = 5;
        int add = a + b;

        int newDesign = add * f;
        return newDesign;
    }

    public static int factorial(int n) {
        int fact = 1;

        for (int i = 1; i <= n; i++) {
            fact *= i;
        }

        // System.out.println(fact);
        return fact;
    }

    public static void rec(int n) {

        if(n == 0) {     // BASE CASE
            return;
        }

        System.out.println("INSIDE Fn BEFORE Rec, n = " + n);
        rec(n-1);      // Recursive Case
        System.out.println("INSIDE Fn AFTER Rec, n = " + n);
    }



    public static void recursive(int n) {

        if(n == 0) {     // BASE CASE
            return;
        }

        System.out.println(n);
        rec(n-1);      // Recursive Case
    }

    public static void print1To5(int n, int i) {
        if(i == n + 1) {
            return;
        }
        
        System.out.println(i);
        print1To5(n, i+1);

    }

    public static int sumOfNaturalNumbers(int n) {

        if(n == 0 || n == 1)
            return n;

        return n + sumOfNaturalNumbers(n-1);
    }

    public static int factorialRecursive(int n) {

        if(n == 0 || n == 1)
            return n;

        return n + factorialRecursive(n-1);
    }

    public static int fib(int n) {

        if (n == 0 || n == 1) {
            return n;
        }

        return fib(n - 1) + fib(n - 2);
    }

    public static void main(String[] args) {

        // int n = 5;
        // int fact = 1;
        // for(int i = 1; i <= n; i++) {
        //     fact *= i;
        // }
        // System.out.println("Factorial of " + n + " = " + fact);
        //     int n = 5;
        //     int total = 0;
        //     for (int i = 1; i <= n; i++) {
        //         total += i;
        //     }
        //     System.out.println("Sum of " + n + " Natural nums = " + total);
        // String name = teacherName();
        // System.out.println(name);
        // System.out.println("Shivam");
        // int p = 50;
        // System.out.println(addition(fact, p));
        // System.out.println(factorial());

        // BRUTE FORCE / LONG PROCESS FOR PREMUTATION / COMBINATION //
        // Permutation =  n! /(n -r)!

        // int n = 5;
        // int r = 2;
        // int fact = 1;

        // for (int i = 1; i <= n; i++) {
        //     fact *= i;
        // }
        
        // int numerator = fact;
        // // ---------------------------------------- //

        // fact = 1;

        // for (int i = 1; i <= (n-r); i++) {
        //     fact *= i;
        // }

        // int denominator = fact;

        // int perm = numerator / denominator;

        // System.out.println(perm);

        // BRUTE FORCE / LONG PROCESS FOR PREMUTATION / COMBINATION //



        // int n = 5;
        // int r = 2;


        // int num = factorial(n);
        // int denom = factorial(n-r);

        // int perm = num / denom;

        // denom = denom * factorial(r);

        // int comb = num / denom;
        
        // System.out.println("Permutation = " + perm);
        // System.out.println("Combination: " + comb);

        // BRUTE FORCE / LONG PROCESS FOR PREMUTATION / COMBINATION //


        // STRONG NUMBER 


        // input = 145;     
        // 1! + 4! + 5! = 145 (True) else False;

        // n = 15;
        // int oG = n;
        // int total = 0;

        // while(n != 0) {
        //     r = n % 10;
        //     total += factorial(r);
        //     n /= 10;
        // }

        // System.out.println((total == oG));

        
        // int n = 5;
        // System.out.println("CODE STARTS");
        // rec(n);
        // System.out.println("CODE ENDS");

        // int n = 1;

        // while(n <= 5) {
        //     System.out.println(n);

        //     n++;
        // }

        // print1To5(5, 1);



        // int n = 5;
        // int total = factorialRecursive(n);

        // System.out.println("Factorial of " + n + " = " + total);



        // =============== Fibonacci Series ======================= //



        // int n = 10;

        // int first = 0;
        // int second = 1;

        // for(int i = 1; i <= n; i++) {
        //     System.out.print(first + " ");
        //     int current = first + second;
        //     first = second;
        //     second = current;
        // }


        int a = fib(5);
        System.out.println(a);


    }

}



// public class Student { // Class

//     static String trainerName = "Shivam Bansal"; // Class Var

//     Student() {
//         System.out.println("Object created!!!");
//     }
//     public static void main(String[] args) {
//         System.out.println(trainerName);
//         Student s1 = new Student(); // Creating of an object
//     }



// }