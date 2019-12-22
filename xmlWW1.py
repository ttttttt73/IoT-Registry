from lxml import etree
 
# Data
values =  ["22", "24", "17", "18"]
albums = [ ["EP 1집", "Season of Glass"],  ["EP 2집", "Flower Bud"],
           ["EP 3집", "Snowflake"],        ["정규 1집", "LOL"] ]
 
# Create XML 
root = etree.Element("data")
 
# Set name
x_name = etree.Element("device")
x_name.text = "WeMosD1"
x_name.set("name", "ARDUINO")
 
# Set members
x_value = etree.Element("value")
for value in values:
    x_value = etree.SubElement(x_values, "value")
    x_value.text = member
 
# Set albums
x_albums = etree.Element("albums")
for album in albums:
    x_album = etree.SubElement(x_albums, "album")
    x_album.text = album[1]
    x_album.set("order", album[0])
 
# Append elements
root.append(x_name)
root.append(x_members)
root.append(x_albums)
 
# Print
x_output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
x_header = '<?xml version="1.0" encoding="UTF-8"?>\n'
print(x_header + x_output.decode('utf-8') )

# Write to xml file
x_output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
x_header = '<?xml version="1.0" encoding="UTF-8"?>\n'
ff=open('./sample.xml', 'w', encoding="utf-8")
ff.write(x_header + x_output.decode('utf-8') )
