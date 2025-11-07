AIM:
To develop a python program that could search the text in a file for phone numbers
(+919900889977) and email addresses (sample@gmail.com)
ALGORITHM:
1. Start
2. Open the text file in read mode
3. Read the content of the file into a string
4. Import the re module for regular expressions
5. Define:
a) Regex pattern for phone numbers: r"\+91\d{10}"
b) Regex pattern for email addresses: r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
6. Use re.findall() to find all matches of phone numbers
7. Use re.findall() to find all matches of email addresses
8. Display the extracted phone numbers and email addresses
9. Close the file
10. End
PROGRAM:
import re
def extract_contacts(filename):
# Open and read the file
with open(filename, 'r') as file:
content = file.read()
# Regex patterns
phone_pattern = r"\+91\d{10}"
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# Finding all phone numbers and emails
phones = re.findall(phone_pattern, content)
emails = re.findall(email_pattern, content)
# Display results
print("Phone Numbers Found:")
for phone in phones:
print(phone)
print("\nEmail Addresses Found:")
for email in emails:
print(email)
# Example usage
extract_contacts("sample.txt") # Make sure this file exists with test data
SAMPLE CONTENT OF SAMPLE.TXT
Here are some contacts:
Call me at +919900889977 or +918888123456.
You can also email me at sample@gmail.com or contact_hr@example.co.in
OUTPUT:
Phone Numbers Found:
+919900889977
+918888123456
Email Addresses Found:
sample@gmail.com
contact_hr@example.co.in
