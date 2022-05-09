"""
string quoting examples

blah blah blah-dy blah
"""
s1 = "spam\n"
print(len(s1))
s2 = 'spam\n'
print(len(s2))
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r'spam\n'  # raw string
print("len(s5): {}".format(len(s5)))

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')

print("""Guido's The ex-"BDFL" of Python""")

query = """
select c.id, c.fname, c.lname
from customers c
where c.zipcode == '90392'
"""

print(r"\\_o_//")


