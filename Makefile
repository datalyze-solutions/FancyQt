UI_FILES = \
	examples/dummy.py \

COMPILED_RESOURCE_FILES = \
	fancyqt/firefox_rc.py \

RESOURCE_SRC=$(shell grep '^ *<file' resources.qrc | sed 's@</file>@@g;s/.*>//g' | tr '\n' ' ')

default: compile

compile: $(UI_FILES) $(COMPILED_RESOURCE_FILES)

%_rc.py : %.qrc $(RESOURCES_SRC)
	pyrcc4 -o $*_rc.py  $<

%.py : %.ui
	pyuic4 -o $@ $<