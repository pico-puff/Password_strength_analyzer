import re
print("Password Strength Analyzer")
password=input("Enter password: ")
score=sum([len(password)>=8,bool(re.search(r'[A-Z]',password)),bool(re.search(r'[a-z]',password)),bool(re.search(r'\d',password)),bool(re.search(r'[^A-Za-z0-9]',password))])
print("Strong" if score>=5 else "Medium" if score>=3 else "Weak")
