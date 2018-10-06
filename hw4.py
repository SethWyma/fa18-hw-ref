"""
CS 196 FA18 HW4
Prepared by Andrew, Emilio, and Prithvi

You might find certain default Python packages immensely helpful.
"""

# Good luck!

"""
most_common_char

Given an input string s, return the most common character in s.
"""
def most_common_char(s):

	myString, dict = s.lower(), {}

	for n in range(len(myString)):
		if not myString[n] in dict:
			dict[myString[n]] = 1
		else: dict[myString[n]] += 1

	mostCommon = ['', 0]
	for key, value in dict.items():
		if value > mostCommon[1]:
			mostCommon[0], mostCommon[1] = key, value

	return mostCommon[0]


"""
alphabet_finder

Given an input string s, return the shortest prefix of s (i.e. some s' = s[0:i] for some 0 < i <= n)
that contains all the letters of the alphabet.
If there is no such prefix, return None.
Your function should recognize letters in both cases, i.e. "qwertyuiopASDFGHJKLzxcvbnm" is a valid alphabet.

Example 1:
	Argument:
		"qwertyuiopASDFGHJKLzxcvbnm insensitive paella"
	Return:
		"qwertyuiopASDFGHJKLzxcvbnm"

Example 2:
	Argument:
		"aardvarks are cool!"
	Return:
		None
"""


def alphabet_finder(s):
	alphabet = list(map(chr, range(97, 123)))

	for i in range(len(s)):
		if s[i].lower() in alphabet:
			alphabet.remove(s[i].lower())
			if not alphabet: return s[0:i + 1]

	return None


"""
longest_unique_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that arr[a:a+b] is the longest unique subarray.
That is to say, all the elements of arr[a:a+b] must be unique,
and b must be the largest value possible for the array.
If multiple such subarrays exist (i.e. same b, different a), use the lowest value of a.

Example:
	Argument:
		[1, 2, 3, 1, 4, 5, 6]
	Return:
		[1, 6]
"""

def longest_unique_subarray(arr):
	longest, bestA = -1, 0
	for a in range(len(arr)):
		for b in range(len(arr) - a + 1):
			if len(set(arr[a:a+b])) == len(arr[a:a+b]):
				if b > longest: bestA, longest = a, b
			else: break
		if longest > len(arr) - a: break
	return [bestA, longest]


"""
string_my_one_true_love

A former(?) CA for this course really like[d] strings that have the same occurrences of letters.
This means the staff member likes "aabbcc", "ccddee", "abcabcabc", etcetera.

But the person who wrote all of your homework sets wants to trick the staff with really long strings,
that either could be the type of string that the staff member likes,
or a string that the CA would like if you remove exactly one character from the string.

Return True if it's a string that the homework creator made, and False otherwise.
Don't treat any characters specially, i.e. 'a' and 'A' are different characters.

Ungraded food for thought:
Ideally, your method should also work on integer arrays without any modification.

Example 1:
	Argument:
		"abcbabcdcdda"
		There are 3 a's, 3 b's, 3 c's, and 3 d's. That means it is a very likable string!
	Return:
		True

Example 2:
	Argument:
		"aaabbbcccddde"
		There are 3 a's, 3 b's, 3 c's, and 3 d's. We have 1 e, which we can remove.
	Return:
		True

Example 3:
	Argument:
		"aaabbbcccdddeeffgg"
		This string is similar to the other ones, except with 2 e's, f's and g's at the end.
		To make this string likable, we need to remove the 2 e's, f's, and g's or we can remove
		one a, b, c, and d. However all of these require more than one removal, so it becomes invalid.
	Return:
		False
"""
def string_my_one_true_love(s):
	myString, dict = s, {}
	for n in range(len(myString)):
		if not myString[n] in dict:
			dict[myString[n]] = 1
		else: dict[myString[n]] += 1

	if len(set(dict.values())) == 1: return True

	for key, value in dict.items():
		dict[key] -= 1
		if len(set(dict.values())) == 1: return True
		if value == 0 and len(set(dict.values())) == 2: return True
		dict[key] += 1

	return False


"""
alive_people

You are given a 2-dimensional list data. Each element in data is a list [birth_year, age_of_death].
Assume that the person was alive in the year (birth_year + age_of_death).
Given that data, return the year where the most people represented in the list were alive.
If there are multiple such years, return the earliest year.

Example:
	Argument:
		[[1920, 80], [1940, 22], [1961, 10]]
	Return:
		1961
"""
def alive_people(data):
	candidateYears = [[item[0], 0] for item in data]
	for year in candidateYears:
		for item in data:
			if item[0] <= year[0] <= item[0] + item[1]:
				year[1] += 1
	candidateYears.sort(key = lambda elem: (elem[1], elem[0]))
	return candidateYears[-1][0]


#alive_people([[1920, 80], [1940, 22], [1961, 10], [1965, 17], [1944, 19], [1900, 90], [2000, 18], [1944, 55]])

"""
three_sum

Given an input list of integers arr, and a constant target t,
is there a triplet of distinct elements [a,b,c] so that a + b + c = t?

Return a 2-dimensional list of all the unique triplets as defined above.
Each inner list should be a triplet as we defined above.
We don't care about the order of triplets, nor the order of elements in each triplet.

Example:
	Arguments:
		[-1, 0, 1, 2, -1, -4], 0
	Return:
		[
			[-1, 0, 1],
			[-1, -1, 2]
		]
"""
def three_sum(arr, t):
	pass


"""
happy_numbers

Given an input integer n > 0, return the number of happy integers between 1 and n, bounds inclusive.
https://en.wikipedia.org/wiki/Happy_number

Example 1:
	Argument:
		8
		The happy numbers between 1 and 8 are 1 and 7 (7 -> 49 -> 97 -> 130 -> 10 -> 1)
	Return:
		2468 // 1234 (i.e., 2)
Example 2:
	Argument:
		15
	Return:
		4294967296 ** (1 / 16) (i.e., 4)
"""
def happy_numbers(n):
	happyNums = {1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100}
	squares = {'0': 0, '1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}
	amount = 0

	for num in range(1, n + 1):
		while num > 100:
			num = sum(squares.get(digit) for digit in list(str(num)))
		if num in happyNums:
			amount += 1

	return amount


"""
zero_sum_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that sum(arr[a:a+b]) == 0.
In plain English, give us the location of a subarray of arr that starts at index a
and continues for b elements, so that the sum of the subarray you indicated is zero.
If multiple such subarrays exist, use the lowest valid a, and then lowest valid b,
in that order of priority.
If no such subarray exists, return None.

Ungraded food for thought:
Think about how to generalize your solution to any arbitrary target sum.

Example 1:
	Argument:
		[0, 1, 2, 3, 4, 5]
		Clearly, the first element by itself forms a subarray with sum == 0.
	Return:
		[0, 1]

Example 2:
	Argument:
		[10, 20, -20, 3, 21, 2, -6]
		In this case, arr[1:3] = [20, -20], so there is a zero sum subarray.
	Return:
		[1, 2]
"""
def zero_sum_subarray(arr):
	for a in range(len(arr)):
		for b in range(len(arr) - a):
			if sum(arr[a:a + b + 1]) == 0:
				return [a,b + 1]
	return None

#myArr = [-56, 76, 29, -7, 12, -31, -4, 34, 56, -9, 5, 17, 62, -44, -2, 11, -27, 9, 10, 43]