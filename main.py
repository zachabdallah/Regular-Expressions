import re

text = "Hello Myra, you can email me at automata907@alaska.org or visit the website at alaska.org/automata and learn about the theory of computing!  Or call me at 907.786.1234.  Another way to learn about automata is to visit 192.229.210.176/automata_theory/index.htm or to go to https://en.wikipedia.org/wiki/Automata_theory for more information.  Mr.Foo posted in section 999.10.34.997 about the equivalence between finite state automata and regular expressions.  He regularly updates www.automata.com with the latest developments."

#url_pattern = r'(?:(?:http://|www\.)\S+|(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\S+)|(?:\S+\.(?:com|org|edu|net|gov)))'
# Find all matches in the text
#matches = re.findall(url_pattern, text)
#for match in matches:
    #print(match)
http_patterns = re.findall(r"\shttp[\S]*", text)
ZeroToTwoHundredFiftyFive = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"#basically an expression we don't have to copy
IP_patterns = re.findall(fr"(\s{ZeroToTwoHundredFiftyFive}\.{ZeroToTwoHundredFiftyFive}\.{ZeroToTwoHundredFiftyFive}\.{ZeroToTwoHundredFiftyFive}[\S]*)", text)
#f allows us to reference a variable in curly brackets
domain_name = r"\s[^\s^@]*"
domain_extension = r"[\S]*"
website_patterns = re.findall(fr"({domain_name}\.com{domain_extension}|{domain_name}\.edu{domain_extension}|{domain_name}\.org{domain_extension}|{domain_name}\.net{domain_extension}|{domain_name}\.gov{domain_extension})", text)
#for match in http_patterns:
    #print(match) #not necessary
for match in IP_patterns[0]:
     if (len(match) > 3):
         print(match)
for match in website_patterns:
    print(match)
