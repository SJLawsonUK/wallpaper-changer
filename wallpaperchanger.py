## Python3 app

from xml.dom.minidom import parse, parseString, Document
from os.path import expanduser
import os, io, struct

stulist = []
tran_time = "5.0"
dura_time = "195.0"
staticfile = "pic1.jpg"
fromfile = staticfile
tofile = "pic2.jpg"
firstfile = "first.jpg"

home = expanduser("~")
src_folder = home + "/Pictures"
xmlfile = src_folder + "/backgrounds.xml"

def is_image_file(file, extensions=['.jpg', '.jpeg', '.JPG']):
    return any(file.endswith(e) for e in extensions)

for path, dirs, files in os.walk(src_folder):
    for file in filter(is_image_file, files):
        stufile = (os.path.join(path, file))
        dafile = open((os.path.join(path, file)), 'rb')
        jpeg = io.BytesIO(dafile.read())
        try:

            type_check = jpeg.read(2)
            if type_check != b'\xff\xd8':
                print("\nNot a JPG .... \n", stufile)
                badlist.append(stufile)
            else:
                byte = jpeg.read(1)

                while byte != b"":

                    while byte != b'\xff': byte = jpeg.read(1)
                    while byte == b'\xff': byte = jpeg.read(1)

                    if (byte >= b'\xC0' and byte <= b'\xC3'):
                        jpeg.read(3)
                        h, w = struct.unpack('>HH', jpeg.read(4))
                        break
                    else:
                        jpeg.read(int(struct.unpack(">H", jpeg.read(2))[0])-2)

                    byte = jpeg.read(1)
                    
                stulist.append(stufile)
        finally:
            jpeg.close()



#create minidom-document
doc = Document()

# create base element
base = doc.createElement('background')
doc.appendChild(base)

# create an entry element
entry = doc.createElement('starttime')

# ... and append it to the base element
base.appendChild(entry)

# create another element 
year = doc.createElement('year')
year_content = doc.createTextNode('1970')
year.appendChild(year_content)
entry.appendChild(year)

month = doc.createElement('month')
month_content = doc.createTextNode('08')
month.appendChild(month_content)
entry.appendChild(month)

day = doc.createElement('day')
day_content = doc.createTextNode('04')
day.appendChild(day_content)
entry.appendChild(day)

hour = doc.createElement('hour')
hour_content = doc.createTextNode('00')
hour.appendChild(hour_content)
entry.appendChild(hour)

minute = doc.createElement('minute')
minute_content = doc.createTextNode('00')
minute.appendChild(minute_content)
entry.appendChild(minute)

second = doc.createElement('second')
second_content = doc.createTextNode('00')
second.appendChild(second_content)
entry.appendChild(second)


x = len(stulist)

for y in range(0, x-1):
    
    entry = doc.createElement('static')
    base.appendChild(entry)

    duration = doc.createElement('duration')
    duration_content = doc.createTextNode(dura_time)
    duration.appendChild(duration_content)
    entry.appendChild(duration)

    file = doc.createElement('file')
    file_content = doc.createTextNode(stulist[y])
    file.appendChild(file_content)
    entry.appendChild(file)

    entry = doc.createElement('transistion')
    base.appendChild(entry)

    duration = doc.createElement('duration')
    duration_content = doc.createTextNode(tran_time)
    duration.appendChild(duration_content)
    entry.appendChild(duration)

    xmlfrom = doc.createElement('from')
    xmlfrom_content = doc.createTextNode(stulist[y])
    xmlfrom.appendChild(xmlfrom_content)
    entry.appendChild(xmlfrom)

    xmlto = doc.createElement('to')
    xmlto_content = doc.createTextNode(stulist[y+1])
    xmlto.appendChild(xmlto_content)
    entry.appendChild(xmlto)

entry = doc.createElement('static')
base.appendChild(entry)

duration = doc.createElement('duration')
duration_content = doc.createTextNode(dura_time)
duration.appendChild(duration_content)
entry.appendChild(duration)

file = doc.createElement('file')
file_content = doc.createTextNode(stulist[y+1])
file.appendChild(file_content)
entry.appendChild(file)

entry = doc.createElement('transistion')
base.appendChild(entry)

duration = doc.createElement('duration')
duration_content = doc.createTextNode(tran_time)
duration.appendChild(duration_content)
entry.appendChild(duration)

xmlfrom = doc.createElement('from')
xmlfrom_content = doc.createTextNode(stulist[y+1])
xmlfrom.appendChild(xmlfrom_content)
entry.appendChild(xmlfrom)

xmlto = doc.createElement('to')
xmlto_content = doc.createTextNode(stulist[0])
xmlto.appendChild(xmlto_content)
entry.appendChild(xmlto)



pretty_xml = doc.toprettyxml()

file = open(xmlfile, "w")
file.write(pretty_xml)
file.close()


