# py-aharef Makefile
# For building and testing the html structure render engine
PROJECT=py-aharef
.PHONY=all dep

test:
	nosetests tests

dep:
	pip3 install -r requirements.txt

all:
	dep
	test
	install

install:
	@echo TODO: create a convenient package, i.e. rpm
	#rpmbuild -ba $(PROJECT).spec
	# python setup.py build
  # python setup.py register
	# python setup.py --sign upload
