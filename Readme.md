<div align="center">

# 🚀 MVJ College of Engineering

![Java](https://img.shields.io/badge/Java-Fundamentals%20%26%20OOP-ED8B00?style=flat-square&logo=java)
![Level](https://img.shields.io/badge/Level-Beginner-yellow?style=flat-square)
![Duration](https://img.shields.io/badge/Duration-4%20Days-brightgreen?style=flat-square)

### A four-day, hands-on journey from your first Java program to object-oriented programming

Build the foundations one concept at a time: write and run Java programs, solve problems with conditions and loops, work with arrays and strings, organize logic into methods, understand recursion, and model real-world ideas with classes and objects.

[Java Presentation](https://canva.link/4ut64mrfxt4cx83) · [Presentation Questions](https://canva.link/revlaa5terj13w4) · [Practice Portal](https://skill.campuscredential.com)

</div>

---

## 📚 Quick Navigation

- [Course outcomes](#-what-you-will-learn)
- [Before you begin](#-before-you-begin)
- [Four-day roadmap](#-four-day-roadmap)
- [Day 1: Java foundations](#day-1-java-foundations)
- [Day 2: Decisions, loops, arrays, and strings](#day-2-decisions-loops-arrays-and-strings)
- [Day 3: Methods and recursion](#day-3-methods-and-recursion)
- [Day 4: Classes, objects, and OOP](#day-4-classes-objects-and-oop)
- [Practice plan](#-practice-plan)
- [How to use the Campus Credential portal](#-practice-on-the-campus-credential-portal)
- [Files and resources](#-files-and-resources)
- [Java quick reference](#-java-quick-reference)
- [Troubleshooting](#-common-errors-and-how-to-debug)

## 🎯 What You Will Learn

By the end of these four days, you should be able to:

- Explain what the JDK, JVM, and a Java program do at a beginner level.
- Write, compile, and run a Java class with a `main` method.
- Store data in variables, choose suitable types, and use operators.
- Read input and display clear output.
- Use `if`/`else`, `switch`, loops, arrays, and strings to solve small problems.
- Break a problem into methods, pass arguments, return results, and trace recursion.
- Create objects from classes and understand fields, methods, constructors, and `this`.
- Describe the purpose of encapsulation, inheritance, polymorphism, and abstraction.
- Test solutions with normal, boundary, and invalid inputs, and explain your approach.

This is an intensive introduction. The goal is to leave with a strong foundation and a repeatable way to learn—not to memorize every Java API in four days.

## 🧰 Before You Begin

### You need

- A computer with a JDK and a Java editor/IDE (VS Code with Java support, IntelliJ IDEA, or Eclipse).
- A browser and access to the class practice portal: [skill.campuscredential.com](https://skill.campuscredential.com).
- A notebook or document for recording mistakes, test cases, and questions.

No previous Java experience is required. Basic computer use and a willingness to try, debug, and try again are enough.

### First setup check

Open a terminal and check that Java is available:

```text
java -version
javac -version
```

Create a file named `Hello.java`:

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
```

The public class name and filename must match (`Hello.java`). In a terminal, compile and run it with:

```text
javac Hello.java
java Hello
```

An IDE can compile and run the program for you, but understanding what these commands do will make errors easier to diagnose.

## 🗓️ Four-Day Roadmap

| Day | Main focus | By the end of the day |
|---|---|---|
| **1** | Java setup, program structure, variables, types, operators, input/output, conditions | Write small programs that read data, make decisions, and solve number problems |
| **2** | Loops, nested loops, patterns, arrays, and strings | Repeat work safely and process a collection of values |
| **3** | Methods, parameters, return values, scope, and recursion | Decompose problems and trace iterative and recursive solutions |
| **4** | Classes, objects, constructors, `this`, and OOP principles | Model a simple real-world entity and explain the core OOP ideas |

Use the day sections as a checklist. The lesson source files are examples and class notes; the exercises on the portal provide additional practice and may include questions not represented in those files.

---

## Day 1: Java Foundations

### 1. How a Java program runs

- **Source code** is written in a `.java` file.
- The **compiler** (`javac`) translates source code into bytecode (`.class` files).
- The **JVM** runs bytecode on the current operating system.
- The **JDK** includes the tools needed to develop Java programs, including the compiler.

Remember the basic program shape:

```java
public class DayOne {
    public static void main(String[] args) {
        System.out.println("Program starts here");
    }
}
```

`main` is the entry point used to start this application. Java is case-sensitive, statements usually end in `;`, and braces group a class or method body.

### 2. Output, comments, variables, and types

```java
int age = 20;
double percentage = 86.5;
char grade = 'A';
boolean enrolled = true;
String name = "Asha";

System.out.println("Name: " + name);
System.out.println("Age: " + age);
```

- Use `System.out.print(...)` to keep output on the same line and `println(...)` to finish the line.
- Use `//` for a single-line comment and `/* ... */` for a block comment.
- Java primitive types include `byte`, `short`, `int`, `long`, `float`, `double`, `char`, and `boolean`. `String` is a reference type.
- Choose descriptive names such as `totalMarks`, not `x1`, when the meaning matters.
- A variable's type determines which values it can store. Converting between types may require a cast; conversions that can lose information should be done deliberately.

### 3. Operators and expressions

Practice arithmetic (`+`, `-`, `*`, `/`, `%`), comparisons (`==`, `!=`, `<`, `<=`, `>`, `>=`), logical operators (`&&`, `||`, `!`), assignment operators (`=`, `+=`, `-=`), and increment/decrement (`++`, `--`).

Integer division drops the fractional part: `7 / 2` is `3`, while `7.0 / 2` is `3.5`. Use parentheses when they make the order of an expression easier to understand.

### 4. Input with `Scanner`

```java
import java.util.Scanner;

public class ReadInput {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter your age: ");
        int age = input.nextInt();

        System.out.println("Next year you will be " + (age + 1));
        input.close();
    }
}
```

Common `Scanner` methods include `nextInt()`, `nextDouble()`, `next()`, and `nextLine()`. `next()` reads one token; `nextLine()` reads the rest of a line. When mixing numeric reads with `nextLine()`, consume the pending newline before asking for the next full line.

### 5. Conditions

```java
if (age < 18) {
    System.out.println("Minor");
} else if (age < 60) {
    System.out.println("Adult");
} else {
    System.out.println("Senior");
}
```

Conditions are evaluated in order. Decide which ranges are inclusive, and test values exactly at each boundary. A `switch` can be useful when choosing among a fixed set of values.

### Day 1 practice

1. Read two numbers and print their sum, difference, product, quotient, and remainder.
2. Read a person's age and classify it using clearly defined ranges.
3. Read a number and check whether it is even or odd.
4. Reverse the digits of a positive integer.
5. Check whether a number is a palindrome (for example, `121`).

**Lesson file:** [Day1.java](<3rd Years/Day1.java>)

---

## Day 2: Decisions, Loops, Arrays, and Strings

### 1. Loops

Use a `for` loop when the number of repetitions is known or controlled by a counter. Use `while` when repetition depends on a condition. A `do`/`while` loop always runs its body at least once.

```java
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}
```

Before running a loop, identify its starting value, stopping condition, and update. Check that the update moves toward stopping; otherwise the loop may never end.

### 2. Nested loops and patterns

A loop inside another loop is useful for rows and columns, tables, and simple patterns:

```java
for (int row = 1; row <= 4; row++) {
    for (int column = 1; column <= row; column++) {
        System.out.print("* ");
    }
    System.out.println();
}
```

For pattern questions, first determine the number of rows. Then work out how many spaces or symbols belong on each row before writing the nested loops.

### 3. Arrays

An array stores a fixed number of values of one type. Its indexes start at `0`; for an array of length `n`, valid indexes are `0` through `n - 1`.

```java
int[] marks = {82, 91, 76};

for (int i = 0; i < marks.length; i++) {
    System.out.println("marks[" + i + "] = " + marks[i]);
}
```

Practice creating an array, reading its values, traversing it forward and backward, finding its sum/minimum/maximum, and counting values that meet a condition. Accessing an index outside the valid range causes an `ArrayIndexOutOfBoundsException`.

### 4. Strings

Strings represent text. Useful beginner operations include `length()`, `charAt(index)`, `equals(...)`, and `substring(...)`. Use `equals` to compare string contents; `==` compares object references, not whether two strings contain the same text.

Strings are immutable: methods that change or trim text return a string rather than changing the original string.

### Day 2 practice

1. Print the multiplication table for a number.
2. Print all even numbers in a chosen range.
3. Find the sum and maximum of an array.
4. Count how many array values are positive, negative, or zero.
5. Reverse a string and check whether it is a palindrome.
6. Print a right triangle, an inverted triangle, and a number pattern.

**Lesson file:** [Day2.java](<3rd Years/Day2.java>) · **Pattern reference:** [Pattern Program In java.pdf](<resources/Pattern Program In java.pdf>)

---

## Day 3: Methods and Recursion

### 1. Write reusable methods

A method gives a name to a unit of work. Its parameters are inputs; a return value is the result sent back to the caller.

```java
public static int add(int first, int second) {
    return first + second;
}
```

Call it from another method with `int total = add(4, 6);`. A method declared `void` does not return a value. The method signature includes the name and parameter types; methods can be overloaded by using different parameter lists.

### 2. Scope and `static`

- A local variable is available only within the block or method where it is declared.
- A parameter receives a value when the method is called.
- A `static` method belongs to the class and can be called without creating an object.
- Keep each method focused: validate input, calculate a result, or display output rather than doing everything in one long method.

### 3. Recursion

A recursive method calls itself on a smaller version of the problem. Every correct recursive solution needs:

1. A **base case** that stops recursion.
2. A **recursive case** that makes progress toward the base case.
3. A correct way to combine the smaller result with the current work.

Example: sum the integers from `1` through `n`:

```java
public static int sumTo(int n) {
    if (n <= 0) {
        return 0;
    }
    return n + sumTo(n - 1);
}
```

For factorial, the recursive relationship is `n * factorial(n - 1)`, with `factorial(0) = 1`. Multiplying by `n` is important: adding would calculate a different result. Trace a small input by hand and watch how calls return in reverse order. Deep recursion can use a lot of call-stack space.

### 4. Iteration or recursion?

Many problems can be solved either way. A loop is often simpler and uses constant call-stack space; recursion can make a naturally self-similar problem easier to express. For example, Fibonacci numbers can be defined recursively, but the straightforward two-call version repeats work. An iterative version is more efficient for larger inputs.

### Day 3 practice

1. Write methods for a maximum of two numbers, a number's factorial, and the sum from `1` to `n`.
2. Create a method that checks whether a number is prime.
3. Write iterative and recursive versions of factorial.
4. Generate the first `n` Fibonacci numbers iteratively; compare with the simple recursive definition.
5. Calculate permutation `nPr = n! / (n-r)!` and combination `nCr = n! / (r! * (n-r)!)`; check that `0 <= r <= n`.
6. Check a strong number by summing the factorials of its digits (for example, `145 = 1! + 4! + 5!`).

**Lesson file:** [Day3.java](<3rd Years/Day3.java>)

---

## Day 4: Classes, Objects, and OOP

### 1. Classes and objects

A **class** describes a kind of thing; an **object** is one instance of that class. Fields hold an object's state, and methods describe its behavior.

```java
class Student {
    String name;

    Student(String name) {
        this.name = name;
    }

    void introduce() {
        System.out.println("Hi, I am " + name);
    }
}

public class Main {
    public static void main(String[] args) {
        Student student = new Student("Asha");
        student.introduce();
    }
}
```

`new Student("Asha")` creates an object. The constructor initializes it. `this.name` refers to the current object's field; the `name` on the right is the constructor parameter.

### 2. The four OOP principles

- **Encapsulation:** keep state and the operations on it together; protect fields and expose intentional methods. A common pattern is `private` fields with validated getters/setters.
- **Inheritance:** define a specialized class from a more general class with `extends`. Use inheritance when the relationship genuinely is-a; call a parent constructor with `super(...)` where needed.
- **Polymorphism:** a parent-class or interface reference can point to different implementing objects. Overridden instance methods use the actual object's implementation at runtime.
- **Abstraction:** describe what an object can do while hiding implementation details, commonly with an interface or an abstract class.

These ideas support code that is easier to understand and change. Prefer composition (one object uses another) when it models the relationship better than inheritance.

### 3. Related Java concepts

- **Access modifiers:** `private`, package-private (no modifier), `protected`, and `public` control visibility.
- **Constructor overloading:** a class can provide more than one constructor with different parameter lists.
- **Method overloading:** same method name, different parameter lists. Changing only the return type is not enough.
- **Method overriding:** a subclass provides a compatible implementation of an inherited instance method; use `@Override` so the compiler can check it.
- **`static`:** belongs to the class rather than a particular object. Use it for class-level behavior or shared constants, not as a substitute for object state.
- **`final`:** can prevent reassignment of a variable, overriding of a method, or extension of a class, depending on where it is used.
- **Interfaces:** define a contract that a class can implement. A class can implement multiple interfaces.

### 4. Think in objects

For a simple `BankAccount` model, ask:

- What is its state? (For example, account holder and balance.)
- What should be hidden? (The balance should not be changed arbitrarily.)
- What operations are allowed? (Deposit and withdrawal.)
- What input rules must each operation enforce? (For example, reject a negative deposit.)
- What should each operation return or report?

**Lesson file:** [Day4OOP.java](<3rd Years/Day4OOP.java>)

### Day 4 practice

1. Create a `Book` class with a title, author, and a method that prints its details.
2. Create a `Student` class with fields, a constructor, and a method that calculates a simple grade from marks.
3. Create a `BankAccount` with a private balance and deposit/withdraw methods that reject invalid amounts.
4. Make a base `Shape` type and two concrete shapes that each provide their own area calculation. Explain where inheritance, overriding, and polymorphism appear.
5. Represent a capability such as `Printable` with an interface, then implement it in two different classes.

---

## ✅ Practice Plan

For every problem, follow this sequence:

1. **Understand:** restate the task and identify the input and required output.
2. **Work an example:** solve one small case by hand.
3. **Plan:** write the steps or pseudocode before coding.
4. **Implement:** use clear names and one responsibility per method.
5. **Test:** try a typical case, a boundary case (such as `0` or an empty array), and an invalid case if relevant.
6. **Debug:** read the first compiler/runtime error, inspect the relevant line, and check variable values.
7. **Explain:** describe why the solution works and what its limitations are.

Do not just read a solution and move on. Close it, reproduce the idea yourself, and then compare. Keep a small “mistakes I will not repeat” list.

## 🌐 Practice on the Campus Credential Portal

Use [skill.campuscredential.com](https://skill.campuscredential.com) as the class practice and question portal:

1. Sign in using the access details provided for your class.
2. Open the Java course or assigned class activity.
3. Attempt each question before checking a solution or hint.
4. Compile and run your code against the sample cases, then test additional edge cases.
5. Revisit incorrect or incomplete submissions after reviewing the relevant day's source file and notes.

The questions and solved examples on the portal complement this repository; not every classroom exercise is copied into the README. If a link, login, or assignment is unavailable, check the instructions shared by your instructor.

## 📁 Files and Resources

### Class source files

- [Day1.java](<3rd Years/Day1.java>) — first programs, variables, conditions, and reversing/checking a number.
- [Day2.java](<3rd Years/Day2.java>) — input, loops, arrays, and strings examples.
- [Day3.java](<3rd Years/Day3.java>) — methods, factorial, recursion, Fibonacci, and number-problem examples.
- [Day4OOP.java](<3rd Years/Day4OOP.java>) — a first class, object, and constructor.

Some lesson files contain commented examples from class. Uncomment or copy one example at a time, then compile and run it. A `.class` file is generated output; the `.java` file is the source to read and edit.

### Reference material

- [Pattern Program In java.pdf](<resources/Pattern Program In java.pdf>) — additional Java pattern exercises.
- [Java Presentation](https://canva.link/4ut64mrfxt4cx83)
- [Presentation Questions](https://canva.link/revlaa5terj13w4)
- [Campus Credential practice portal](https://skill.campuscredential.com)

The repository also contains advanced DSA and placement resources. Those are optional follow-up material, not prerequisites for this four-day Java fundamentals and OOP course.

## ☕ Java Quick Reference

| Need | Example |
|---|---|
| Print a line | `System.out.println("Hello");` |
| Declare an integer | `int count = 0;` |
| Compare values | `if (count == 0) { ... }` |
| Repeat a known number of times | `for (int i = 0; i < n; i++) { ... }` |
| Traverse an array | `for (int value : values) { ... }` |
| Declare a method | `static int square(int n) { return n * n; }` |
| Create an object | `Student student = new Student("Asha");` |
| Compare string contents | `first.equals(second)` |

## 🛠️ Common Errors and How to Debug

| Symptom | Check |
|---|---|
| `';' expected` or `cannot find symbol` | Spelling, capitalization, semicolons, braces, and whether the name is declared in scope |
| Public class/filename error | The public class name must match the `.java` filename exactly |
| `ArrayIndexOutOfBoundsException` | Array indexes start at `0`; the last valid index is `length - 1` |
| `InputMismatchException` | The entered value must match the type requested by `Scanner` |
| A loop never ends | Check its condition and make sure its update moves toward termination |
| A recursive method overflows the stack | Confirm a reachable base case and progress toward it |
| Text comparison behaves unexpectedly | Compare string contents with `.equals(...)`, not `==` |
| A result is unexpectedly truncated | Check whether integer division is being used |

Read compiler messages from the top and fix the first relevant error before chasing later messages; one syntax error can produce several follow-on errors.

---

**Maintained by**: Java Instructor  ([Shivam Bansal](https://shivambansal.co.in))

## <a href="https://whatsapp.com/channel/0029Vb74kBaL2ATzZBnRka19" target="_blank">✨ **Shine_Beyond_Syntax** ✨</a>

[![WhatsApp Channel](https://img.shields.io/badge/Join%20My-WhatsApp%20Channel-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029Vb74kBaL2ATzZBnRka19)
