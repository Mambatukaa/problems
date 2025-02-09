""""
Given a file and assume that you can only read the file using a given method read, implement a method
read to read n characters. Your method read may be called multiple times.
Method read4:
The API read4 reads four consecutive characters from file, then writes those characters into the buffer
array buf4.
The return value is the number of actual characters read.
Note that read() has its own file pointer, much like FILE *p in C.


Example 1:

Input: file = "abc", queries = [1,2,11
Output: [1,2,01

    Explanation: The test case represents the following scenario:
    File file("abc");
    Solution sol;
    sol. read(buf, 1); // After calling your read method, buf should contain "a" • We
    read a total of 1 character from the file, so return 1.
    sol. read (buf, 2); // Now buf should contain "bc". We read a total of 2 characters
    from the file, so return 2.
    sol. read (buf, 1); // We have reached the end of file, no more characters can be
    read. So return 0.
    Assume buf is allocated and guaranteed to have enough space for storing all
    characters from the file.
"""

