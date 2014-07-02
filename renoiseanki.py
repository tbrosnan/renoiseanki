import xml.etree.ElementTree as ET
import sys

def usage():
    print "Usage: ankirenoise infile outfile"


if len(sys.argv) < 3:
    usage()
    sys.exit()

infile = sys.argv[1]
outfile = sys.argv[2]

try:
    tree = ET.parse(infile)
except IOError as e:
    print "Could not open KeyBindings file:" + infile
    sys.exit()

root = tree.getroot()

with open(outfile,'w') as f:
    for binding in root.iter('KeyBinding'):
        b = binding.find("Binding")
        k = binding.find("Key")
        t = binding.find("Topic")
        if k is not None:
            f.write(b.text + "," + k.text + "," + t.text + "\n")

