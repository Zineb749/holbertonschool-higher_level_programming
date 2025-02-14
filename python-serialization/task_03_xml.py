#!/usr/bin/python3
"""3. Serializing and Deserializing with XML"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize python dictionary into XML"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """read the XML data from that file,
     and return a deserialized Python dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()

    _dict = {}
    for child in root:
        _dict[child.tag] = child.text
    return _dict
