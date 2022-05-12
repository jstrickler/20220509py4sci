import lxml.etree as et

doc = et.parse('DATA/solar.xml')

print("doc: {}".format(doc))

root = doc.getroot()

print("root: {}".format(root))

for sub_element in root:
    if sub_element.tag.endswith('planets'):
        for planet in sub_element.findall('planet'):
            print(planet.get('planetname'))
print('-' * 60)

earth = doc.find('.//planet[@planetname="Earth"]')
et.SubElement(earth, 'moon').text = 'Death Star'

for planet in doc.findall('.//planet'):
    planet_name = planet.get('planetname')
    print(planet_name)

    for moon in planet.findall('moon'):
        print(f"    {moon.text}")


doc.write('newsolar.xml', pretty_print=True, xml_declaration=True)
