#!/usr/bin/python3

import os
import xml.sax
import xml.dom.minidom


class PersonHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.firstname = ""
        self.surname = ""
        self.title = ""
        self.nick = ""
        self.email = ""
        self.jobtitle = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "person":
            print("*****Person*****")

   # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "firstname":
            print("First name:", self.firstname)
        elif self.CurrentData == "surname":
            print("Surname:", self.surname)
        elif self.CurrentData == "title":
            print("Title:", self.title)
        elif self.CurrentData == "nick":
            print("Nick:", self.nick)
        elif self.CurrentData == "email":
            print("Email:", self.email)
        elif self.CurrentData == "jobtitle":
            print("Job title:", self.jobtitle)
        self.CurrentData = ""

   # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "firstname":
            self.firstname = content
        elif self.CurrentData == "surname":
            self.surname = content
        elif self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "nick":
            self.nick = content
        elif self.CurrentData == "email":
            self.email = content
        elif self.CurrentData == "jobtitle":
            self.jobtitle = content


def use_dom(path):
    # Open XML document using minidom parser
    DOMTree = xml.dom.minidom.parse(path)
    collection = DOMTree.documentElement
    if collection.hasAttribute("shelf"):
        print("Root element : %s" % collection.getAttribute("shelf"))

    # Get all the movies in the collection
    people = collection.getElementsByTagName("person")

    # Print detail of each movie.
    for person in people:
        print("*****Person*****")
        firstname = person.getElementsByTagName('firstname')[0]
        print("First name: %s" % firstname.childNodes[0].data)
        surname = person.getElementsByTagName('surname')[0]
        print("Surname: %s" % surname.childNodes[0].data)
        title = person.getElementsByTagName('title')[0]
        print("Title: %s" % title.childNodes[0].data)
        nick = person.getElementsByTagName('nick')[0]
        print("Nick: %s" % nick.childNodes[0].data)
        email = person.getElementsByTagName('email')[0]
        print("Email: %s" % email.childNodes[0].data)
        jobtitle = person.getElementsByTagName('jobtitle')[0]
        print("Job title: %s" % jobtitle.childNodes[0].data)


def use_sax(path):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = PersonHandler()
    parser.setContentHandler(Handler)
    parser.parse(path)


if (__name__ == "__main__"):

    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "example.xml"  # load file
    abs_file_path_read = os.path.join(script_dir, rel_path)

    print("\nUSING SAX:\n")
    use_sax(abs_file_path_read)
    print("\nUSING DOM:\n")
    use_dom(abs_file_path_read)
