""""


Given a file and assume that you can only read the file using a given method read, implement a method to
read n characters.
Method read4:
The API read4 reads four consecutive characters from file, then writes those characters into the buffer
array buf4.
The return value is the number of actual characters read.
Note that read4() has its own file pointer, much like FILE *fp in C.


Example 1:

Input: file = "abc", n = 4
Output : 3
Explanation: After calling your read method, buf should contain "abc" • We read a
total of 3 characters from the file, so return 3.
Note that "abc" is the file's content, not buf. buf is the destination buffer that
you will have to write the results to.


"""


"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        copiedChars = 0
        readChars = 4
        buf4 = [""] * 4


        while copiedChars < n and readChars == 4:
            readChars = read4(buf4)

            for i in range(readChars):
                if copiedChars == n:
                    return copiedChars
                buf[copiedChars] = buf4[i]
                copiedChars += 1


        return copiedChars
