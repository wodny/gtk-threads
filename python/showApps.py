#!/usr/bin/python

import pyatspi
r = pyatspi.Registry
print("Desktop count: {0}".format(r.getDesktopCount()))
d = r.getDesktop(0)

MAXLEVEL=1

def showChildren(a, level = 1):
    if level > MAXLEVEL:
        return
    for i in range(a.childCount):
        showProps(a.getChildAtIndex(i), level)
        showChildren(a.getChildAtIndex(i), level + 1)

def showProps(a, level=0):
    print("{0}{2:12}({3:2}) {1}".format("    "*level, a.name, a.getRoleName(), a.childCount))
    if a.getRoleName() == "link":
        print("+++++++++++++++ {0}".format(a.queryHyperlink().getURI(0)))

for a in d:
    showProps(a)
    print("    {0}, {1}, {2}".format(a.toolkitName, a.version, a.id))
    showChildren(a)
