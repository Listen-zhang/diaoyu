from xml.dom.minidom import parse
import  xml.dom.minidom

DomTree = xml.dom.minidom.parse("po.xml")
collection = DomTree.documentElement
movies = collection.getElementsByTagName("person")
for i in movies :
    print(i)
    type = i.getElementsByTagName('name')[0].childNodes[0].data
    print(type)
import  xml.sax