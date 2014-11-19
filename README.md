Brute-Force-using-Python
========================

Script to attack brute force using python language. This was made for personal use.

It works perfectly fine, but I would recommend not to use this directly as its not time efficient.

I would work on same and make more efficient.

Requirements:

1. Python version >= 2.7

2. module mechanize - Stateful programmatic web browsing

3. module socket

4. module urlparse

5. module httplib 

6. module cookielib

7. module itertools

HOW TO USE:

Suppose there is a site named example.com and its has form at index 0 and having fields email and pass, and you want to bruteforce the password.

from bruteforce import BruteForce

ob = BruteForce()

print ob.call_brute_force('abcdef', 'http://www.example.com', 'http://www.example.com', [4,6], {'email':'random@gmail.com'}, 'pass', form_by_index = 0)

