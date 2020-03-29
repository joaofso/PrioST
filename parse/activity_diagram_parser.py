import xml.sax

from model.activity_diagram import *


class ActivityDiagramHandler(xml.sax.ContentHandler):
    """
    CurentData is the type of tag the parser getting
    ActivityDiagram is the activity diagram being parsed
    """

    def __init__(self):
        self.CurrentData = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "mxCell":
            id = attributes.get("id")
            parent = attributes.get("parent")
            style = attributes.get("style")
            if attributes.get("vertex") == "1":
                value = attributes.get("value")

                vertex = Vertex(id, value, parent, style)
                activityDiagram.add_vertex(vertex)
                if style == "ellipse;whiteSpace=wrap;html=1;aspect=fixed;":
                    activityDiagram.start_node = vertex
            elif attributes.get("edge") == "1":
                source = attributes.get("source")
                target = attributes.get("target")

                edge = Edge(id, parent, style, source, target)
                activityDiagram.add_edge(edge)

    # Call when an elements ends
    def endElement(self, tag):
        self.CurrentData = ""


if (__name__ == "__main__"):

    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = ActivityDiagramHandler()
    parser.setContentHandler(Handler)

    directory = "../resources/xml/"
    print("Type the name of the activity diagram file:")
    file = str(input())

    activityDiagram = ActivityDiagram(file)
    parser.parse(directory + file + ".xml")
    activityDiagram.convert_to_alts()