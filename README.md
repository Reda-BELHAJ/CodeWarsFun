# CodeWarsFun
I have provided my approach to solving CodeWars problems here to help others through the questions. I would love your feedback and questions on my thought process.

Here's my CodeWars Profile: https://www.codewars.com/users/RedaBELHAJ

My current codewars rank:

<img src = "https://www.codewars.com/users/RedaBELHAJ/badges/small" />

<br>

# Simple Pig Latin
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay <br/>
pig_it('Hello world !')     # elloHay orldway ! <br/>

<br>

# Find the next perfect square!
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144 <br/>
findNextSquare(625) --> returns 676 <br/>
findNextSquare(114) --> returns -1 since 114 is not a perfect 

<br>

# Create Phone Number
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890" <br/>
The returned format must be correct in order to complete this challenge. <br/>
Don't forget the space after the closing parentheses! <br/>

<br>

# Is a number prime?
Define a function that takes an integer argument and returns logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Requirements

You can assume you will be given an integer input. <br/>
You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0). <br/>
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to n, or n/2, will be too slow. <br/>

Example

is_prime(1)  /* false */ <br/>
is_prime(2)  /* true  */ <br/> 
is_prime(-1) /* false */ <br/>
 
<br>

# IP Validation
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Input to the function is guaranteed to be a single string.

Examples:

#### Valid inputs:

1.2.3.4
123.45.67.89

#### Invalid inputs:

1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Note that leading zeros (e.g. 01.02.03.04) are considered invalid.

<br>

# Get the Middle Character
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#### Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"

#### Input

A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

#### Output

The middle character(s) of the word represented as a string.

<br>

# Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

#### Example:

"abcde" -> 0 # no characters repeats more than once <br/>
"aabbcde" -> 2 # `a` and `b` <br/>
"aabBcde" -> 2 # `a` occurs twice and `b` twice (`b` and `B`) <br/>
"indivisibility" -> 1 # `i` occurs six times <br/>
"Indivisibilities" -> 2 # `i` occurs seven times and `s` occurs twice <br/>
"aA11" -> 2 # `a` and `1` <br/>
"ABBA" -> 2 # `A` and `B` each occur twice <br/>

<br>

# Descending Order
Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

#### Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

<br>

# +1 Array
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

#### Examples
For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]

<br>

# Street Fighter 2 - Character Selection
https://www.codewars.com/kata/5853213063adbd1b9b0000be
