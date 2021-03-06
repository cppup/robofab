# robofab manual
# Info object
# usage examples

from robofab.world import CurrentFont

f = CurrentFont()
print f.info.postscriptFullName
print f.info.openTypeNameDesigner

f.info.openTypeNameDesigner = "Jan van Krimpen"
print f.info.openTypeNameDesigner
print f.info.openTypeOS2VendorID
print f.info.unitsPerEm
print f.info.xHeight
print f.info.openTypeNameLicenseURL

# but you can set the values as well
f.info.postscriptUniqueID = 4309359
f.info.openTypeNameDesigner = "Eric Gill"

