import socket
import urllib.request
import xml.etree.ElementTree as ET

#https://www.youtube.com/watch?v=8DvywoWv6fI&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&index=4
#!Networked programs
#*write a web browser using sockets
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
mysock.close()

#*write a web browser using urllib
##since HTTP is so common, we have a library (urllib) 
##that does all the sockets work for us and makes web pages look like a file
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

#!Data on the web
"""
.WIth the HTTP Request/Response well understood and well supprted, 
there was a natural move toward exchanging data between programs using these protocols

.We needed to come up with an agreed way to represent data
going between applications and accross networks

.there are two commonly used formats : XML and JSON

.Serialization/Deserialization: Convert data in one program into a common format
than can be stored and/or transmitted between systems in a programming langage-independentmanner	

"""

#!XML Schema
"""
.Description of the legal format of an XML document

.Expressed in terms of constraints on the structure and contentt of documents

.often used to specify a "contract" between systems-"My system will only accept XML that conforms to this particular schema

.If a particular piece of XML meets the specification of the schema it is said to "validate"
There are manu xml schema langages but we're gonna look at xsd langage (or W3C Schema) because very common

example of basic xml:
<person>
<lastname>John</lastname>
<age>17</age>
<dateborn>14-05-2001</dateborn>
</person>

example of xml schema:
<xs:complexType name="person">
    <xs:sequence>
        <xs:element name="lastname" type="xs:string"/>
        <xs:element name="age" type="xs:integer"/>
        <xs:element name="dateborn" type="xs:date"/>
    </xs:sequence>
</xs:complexType>
"""
