actor = "Chris Hemsworth"
print(type(actor), len(actor))

print("actor.upper(): {}".format(actor.upper()))

au = actor.upper()

print("actor.count('h'): {}".format(actor.count('h')))
print("actor.count('Hem'): {}".format(actor.count('Hem')))
print("actor.lower().count('h'): {}".format(actor.lower().count('h')))

print("actor.startswith('Chris'): {}".format(actor.startswith('Chris')))
print("actor.startswith('Liam'): {}".format(actor.startswith('Liam')))

print("actor.replace('Chris', 'Liam'): {}".format(actor.replace('Chris', 'Liam')))

print("actor.replace('s', 'X', 1): {}".format(actor.replace('s', 'X', 1)))

print("actor.find('Chris'): {}".format(actor.find('Chris')))
print("actor.find('Hem'): {}".format(actor.find('Hem')))
print("actor.find('Liam'): {}".format(actor.find('Liam')))

data = "1:George:Washington:VA"
fields = data.split(':')
print("fields: {}".format(fields))

question = "What is the airspeed of a swallow?"
words = question.split()
print("words: {}".format(words))

print("'Hem' in actor: {}".format('Hem' in actor))
print("'Spam' in actor: {}".format('Spam' in actor))

s1 = "       all my exes live in Texas     "
print("'|' + s1 + '|': {}".format('|' + s1 + '|'))
print("'|' + s1.lstrip() + '|': {}".format('|' + s1.lstrip() + '|'))
print("'|' + s1.rstrip() + '|': {}".format('|' + s1.rstrip() + '|'))
print("'|' + s1.strip() + '|': {}".format('|' + s1.strip() + '|'))
print()

s2 = "yxyxxyyyyyxall my exes live in Texasyyxxxyxxxxxxxyyyyyyyyxxyxxyxx"
print("'|' + s2 + '|': {}".format('|' + s2 + '|'))
print("'|' + s2.lstrip('xy') + '|': {}".format('|' + s2.lstrip('xy') + '|'))
print("'|' + s2.rstrip('xy') + '|': {}".format('|' + s2.rstrip('xy') + '|'))
print("'|' + s2.strip('xy') + '|': {}".format('|' + s2.strip('xy') + '|'))
print()

