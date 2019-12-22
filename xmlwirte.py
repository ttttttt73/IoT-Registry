from xml.etree.ElementTree import Element, dump, ElementTree, SubElement, dump, parse, tostring
import xml.etree.ElementTree as ET



root = Element("devlist")

node1 = Element("dev", name="Arduino")
root.append(node1)

#arduino
node1sub1 = SubElement(node1, "value", name="Smoke")
node1sub1.text = "100"

node1sub2 = SubElement(node1, "time")
node1sub2.text = "2019-05-03"

#rpi
node2 = Element("dev", name="RPi")
root.append(node2)

node2sub1 = SubElement(node2, "value", name="Temperature")
node2sub1.text = "23"

node2sub3 = SubElement(node2, "value", name="Humidity")
node2sub3.text = "45"

node2sub2 = SubElement(node2, "time")
node2sub2.text = "2019-05-03"


def indent(elem, level=0): #자료 출처 https://goo.gl/J8VoDK
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
indent(root)
dump(root)

# Write to xml file
'''
x_output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
x_header = '<?xml version="1.0" encoding="UTF-8"?>\n'
ff=open('./sample.xml', 'w', encoding="utf-8")
ff.write(x_header + x_output.decode('utf-8') )'''


ElementTree(root).write("note.xml", "utf-8")

#tt = ElementTree(root)
#print(tt)

test = dump(root)
print(test)
