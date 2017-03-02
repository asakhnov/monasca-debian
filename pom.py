#!/usr/bin/env python
import argparse
import xml.etree.ElementTree as ET
import yaml

POM_BASE = '{http://maven.apache.org/POM/4.0.0}'


def load_xml(path):
    with open(path, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def create_xml_tree(pom):
    ET.register_namespace('', 'http://maven.apache.org/POM/4.0.0')
    ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    ET.register_namespace('schemaLocation', 'http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd')
    tree = ET.parse(pom)
    return tree


def data_element(data):
    e = ET.Element('%sdata' % POM_BASE)
    for k, v in data.iteritems():
        s = ET.SubElement(e, '%s%s' % (POM_BASE, k))
        s.text = v
    return e


def generate_pom(pom, helper):
    tree = create_xml_tree(pom)
    root = tree.getroot()
    plugins = root.find('%sbuild' % POM_BASE)[0]
    for plugin in plugins:
        if plugin.find('%sartifactId' % POM_BASE).text == 'jdeb':
            break
    configuration = plugin.find('%sexecutions' % POM_BASE)[0].find('%sconfiguration' % POM_BASE)
    dataset = configuration.find('%sdataSet' % POM_BASE)

    helper = load_xml(helper)
    for d in helper:
        data = data_element(d)
        dataset.append(data)

    tree.write(pom)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pom', type=str,
                        help='path to pom.xml')
    parser.add_argument('helper', type=str,
                        help='path to helper file')
    args = parser.parse_args()

    generate_pom(args.pom, args.helper)


if __name__ == '__main__':
    main()
