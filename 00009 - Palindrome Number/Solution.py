class Solution:
    def isPalindrome(self, x: int) -> bool:
        # a negative will never be a palindrome
        if x < 0:
            return False
        # get temp value to store reversed x as we build number
        temp = x
        # value to store reversed value to check with later
        reversed_num = 0

        while temp != 0:
            # get the last digit of temp
            digit = temp % 10
            # store it in reversed. As you build reversed, it will get multiplied by 10 repeatedly, putting it at the reverse spot
            # ex, 201, 1 *10 repeatedly ends up with 102
            reversed_num = reversed_num * 10 + digit
            # hard divide by 10 to get the next digit in place
            temp //= 10
        # if our reverse number equals the original, return true
        return reversed_num == x

