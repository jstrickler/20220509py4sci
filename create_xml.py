import lxml.etree as et

person_list = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

root = et.Element('people')
for first_name, last_name, product, dob in person_list:
    person_element = et.SubElement(root, 'person', dob=dob)
    first_name_element = et.SubElement(person_element, 'first_name')
    first_name_element.text = first_name
    et.SubElement(person_element, 'last_name').text = last_name
    et.SubElement(person_element, 'product').text = product

xml = et.tostring(root, xml_declaration=True,
                  pretty_print=True).decode()

print("xml: {}".format(xml))
doc = et.ElementTree(root)
doc.write('people.xml', xml_declaration=True, pretty_print=True)




