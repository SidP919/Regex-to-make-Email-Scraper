import re

text = "A random string."

pattern = re.compile("A random string.")

result = pattern.search(text)#search only finds the first occurence of the pattern and not all of them in a given text
print(result)
print()

pattern2 = re.compile("[Ab]")#find the occurence of either A or b in the string

result2 = pattern2.search(text)#search will only find the occurence of "A" in text and not b's.
print(result2)
print()

pattern3 = re.compile("[a-s0-7]")#find the occurence of either a, b, c,..., r, s or 0, 1, 2, ..., 8, 9 whichever comes first
result3 = pattern3.search(text)
print(result3)
print()

#what happens if we add a + to the regex in pattern:
pattern4 = re.compile("[a-s0-7]+")
result4  = pattern4.search(text)
print(result4)
#as you see now it not only finds the first occurence of any of the a-s or 0-7 but also keeps on finding the occurence of a-s or 0-7 until the text keeps on satisfying the pattern, like after "random" there's a space which doesn't match the pattern we provided, so it breaks there.
print()
print()
print()

#Email Scraper:------------------->
text2 = "A random string. Myname123@gmail.com More random string. YourName128@yahoo.com also His_Name-88.8@tcs.com"
print("Email Scrapper in action on following Text: ")
print(text2)
print()
print()
pattern5 = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-z]+")
result5 = pattern5.search(text2)
print("With search function and Pattern6: ")
print(result5)
print()
result6 = pattern5.findall(text2)
print("With findAll function and Patttern6: ")
print(result6)
print()
pattern6 = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-z]+")
result7 = pattern6.findall(text2)
print("With findAll function and Pattern7: ")
print(result7)
print()