#!/usr/bin/python
# Required header that tells the browser how to render the text.
print "Content-Type: text/plain\n\n"
# Print a simple message to the display window.
print "Hello, World!\n"
print "test2\n"
print "cos jest nie tak"
exec(open("cms/controller.py").read())

import django
print django.get_version()

import cms.library as lb

lb.testFunc()
