# Python Documentation

# Luhn Algorithm Card Validator

This Python script validates a card number using the Luhn Algorithm, also known as the "modulus 10" or "mod 10" algorithm, which is a simple checksum formula used to validate a variety of identification numbers.

## How it works

The script asks the user to input a card number. It then applies the Luhn Algorithm to the card number to determine if it is valid or not. If the card number is valid, it prints "This is a valid card number." If the card number is not valid, it prints "This is not a valid card number." The user can quit the program by entering 'q'.

## Code Explanation

The script consists of two main functions: `luhn_algorithm` and `is_luhn_valid`.

### luhn_algorithm

This function takes a card number as input and applies the Luhn Algorithm to it. It first converts the card number into a list of its digits. It then separates the digits into two groups: those at odd indices and those at even indices. It sums up the digits at odd indices. For the digits at even indices, it doubles each digit and then sums up the digits of the result. It adds these two sums together to get the checksum. The function returns the remainder when the checksum is divided by 10.

### is_luhn_valid

This function takes a card number as input and returns True if the card number is valid according to the Luhn Algorithm and False otherwise. It does this by calling the `luhn_algorithm` function and checking if the result is 0.

## Libraries

This script does not import any libraries. It only uses built-in Python functions and methods.

---

# C# Documentation

# CSharp Number Validation Script

This script is written in CSharp and is used to validate a number entered by the user. The validation is based on the Luhn algorithm, which is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers and Canadian Social Insurance Numbers.

## Code Explanation

The script begins by prompting the user to enter a number. This number is then passed to the `IsValid` function, which checks if the number is valid or not based on the Luhn algorithm. If the number is valid, the script prints "Valid", otherwise it prints "Invalid".

### Imported Libraries

The script uses the `System` namespace, which is a fundamental library in CSharp. It provides classes that are used for a wide variety of tasks such as input/output via streams, string manipulation, exception handling, and more.

Here is a brief explanation of the classes used from the `System` namespace:

- `Console`: This class is used for reading from and writing to the console. In this script, it is used to prompt the user to enter a number and to print whether the number is valid or not.

## Function Explanation

- `Main`: This is the entry point of the script. It prompts the user to enter a number and then calls the `IsValid` function with the entered number.

- `IsValid`: This function implements the Luhn algorithm to check if the entered number is valid or not. It iterates over the digits of the number from right to left, doubling every second digit. If the doubled digit is greater than 9, it subtracts 9 from it. The function then sums up all the digits. If the total modulo 10 is equal to 0, then the number is valid; otherwise, it is not.

## Usage

To use this script, you need to have a CSharp compiler installed on your system. You can then compile the script using the `csc` command and run the resulting executable. The script will prompt you to enter a number, and it will then print whether the number is valid or not.

---

# Java Documentation

# Java Number Validator

This Java script is designed to validate a number input by the user. The validation process is based on the Luhn algorithm, which is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers and Canadian Social Insurance Numbers.

## Script Overview

The script first prompts the user to enter a number. It then checks if the number is valid or not based on the Luhn algorithm and finally, it prints out the result.

## Code Breakdown

The script is divided into two main parts: the `main` method and the `isValid` method.

### Main Method

The `main` method is the entry point of the script. It does the following:

1. Creates a `Scanner` object to read the user's input.
2. Prompts the user to enter a number.
3. Calls the `isValid` method to validate the entered number.
4. Prints out whether the number is valid or not.

### isValid Method

The `isValid` method implements the Luhn algorithm to validate the number. It does the following:

1. Initializes a sum to 0 and a boolean flag `alternate` to false.
2. Iterates over the digits of the number from right to left.
3. Doubles every second digit and if this doubling results in a number greater than 9, it adds the digits of the number.
4. Adds the resulting number to the sum.
5. After all digits have been processed, it checks if the total sum is a multiple of 10. If it is, the number is valid.

## Imported Libraries

The script imports the following Java library:

- `java.util.Scanner`: This library is used to read the user's input. The `Scanner` class is a simple text scanner which can parse primitive types and strings using regular expressions. In this script, it is used to read the number entered by the user.

## Usage

To use this script, simply run it in a Java environment, enter a number when prompted, and the script will tell you whether the number is valid or not based on the Luhn algorithm.

---
