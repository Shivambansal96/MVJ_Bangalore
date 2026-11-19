
// class Student {
//     String myName;
//     String role;
//     Student(String a, String role) {
//         this.myName = a;
//         this.role = role;
//     }
// }
// class Circle {
//     float radius;
//     Circle(float r) {
//         this.radius = r;
//     }
//     public void area() {
//         float area = (this.radius * this.radius * 22) / 7;
//         System.out.println("Area of Circle = " + area);
//         // return area;
//     }
//     public void perimeter() {
//         float p = (2 * this.radius * 22) / 7;
//         System.out.println("Perimeter of Circle = " + p);
//     }
// }
// class Student {
//     String name;
//     int m1;
//     int m2;
//     int m3;
//     Student(String name, int m1, int m2, int m3) {
//         this.name = name;
//         this.m1 = m1;
//         this.m2 = m2;
//         this.m3 = m3;
//     }
//     public float average() {
//         float avg = (this.m1 + this.m2 + this.m3) / 3.0f;
//         System.out.println("Average of " + this.name + ": " + avg);
//         return avg;
//     }
// }
// ================= INHERITANCE =============== //
// class Shape {
//     int sides = 1;
//     String color = "red";
//     public void nothing() {
//         System.out.println("Shape Printed....");
//     }
// }
// class Triangle extends Shape {
//     int side = 3;
// }
// class equilateralTriange extends Triangle {
//     String sides = "equal";
// }
// ================= INHERITANCE =============== //
class Employee {

    String role;
    String department;
    int salary;

    public Employee(String role, String dept, int salary) {
        this.role = role;
        this.department = dept;
        this.salary = salary;
    }

    public void showDetails() {
        System.out.println("Role: " + this.role);
        System.out.println("Department: " + this.department);
        System.out.println("Salary: " + this.salary);

        System.out.println(" ----------------- ");
    }
}

class Engineer extends Employee {

    String name;
    int age;

    public Engineer(String name, int age, String role, int salary, String dept) {
        super(role, dept, salary);
        this.name = name;
        this.age = age;
    }

    @Override
    public void showDetails() {
        System.out.println("Name: " + this.name);
        System.out.println("Age: " + this.age);
        super.showDetails();
    }
}

// abstract class Animal {
//     abstract void sound();
// }
// class Dog extends Animal {
//     void sound() {
//         System.out.println("Dog Barks");
//     }
// }
// class Cat extends Animal {
//     void sound() {
//         System.out.println("can walk on 4 legs");
//     }
// }
class Bank {

    String accNum;
    private String pass;

    Bank(String accNum, String pass) {
        this.accNum = accNum;
        this.pass = pass;
    }

    private void getPass() {
        System.out.println("Password = " + this.pass);
    }

    private void setPass() {
        // System.out.println("Password = " + this.pass);
        this.pass = "passWord CHanged!!!";
    }

    public void setAgain() {
        this.setPass();
    }
}

public class Day4OOPs {

    public static void main(String[] args) {

        Bank b1 = new Bank("14380100115559", "Shivam123");

        // System.out.println("Account Number: " + b1.accNum);
        b1.setAgain();

        // Dog d1 = new Dog();
        // d1.sound();
        // Animal a1 = new Animal();
        // ============================================== //
        // s1.name = "<Mohihi>";
        // System.out.println(s2.name);
        // Student s3 = new Student(); // Object Created
        // s3.name = "Sejal";
        // System.out.println(s3.name);
        // s1.printSomething();
        // s1.name = "Shivam";
        // s1.role = "Trainer";
        // Student s2 = new Student(); // Object Created
        // s2.name = "Mohini";
        // s2.role = "SDE";
        // System.out.println(s1.name);
        // System.out.println(s2.name);
        // Student s1 = new Student("Shiv", "Trainer"); // Object Created
        // System.out.println(s1.myName);
        // Student s2 = new Student("Mohini", "SDE"); // Object Created
        // System.out.println(s2.myName);
        // ============================================== //
        // Circle c1 = new Circle(5);
        // c1.area();
        // c1.perimeter();
        // ============================================== //
        // Student s1 = new Student("Shivam", 90, 95, 100);
        // s1.average();
        // System.out.println("Average of " + s1.name + ": " + s1.average());
        // System.out.println(s1.average());
        // s1.average();
        // Student s2 = new Student("Mohini", 100, 100, 100);
        // s2.average();
        // Triangle t1 = new Triangle();
        // System.out.println(t1.color);
        // t1.nothing();
        // ======================= //
        // Employee e1 = new Employee("Trainer", "IT", 999);
        // e1.showDetails();
        // Engineer eng1 = new Engineer("Shivam", 207,  "IT Trainer", 99, "CS");
        // eng1.showDetails();
        // ======================= //
    }

}
