# Python-Markdown makefile

.PHONY : install
install:
	python setup.py install

.PHONY : deploy
deploy:
	python setup.py register
	python setup.py sdist --formats zip,gztar upload

.PHONY : build
build:
	python setup.py sdist --formats zip,gztar

.PHONY : build-win
build-win:
	python setup.py bdist_wininst

.PHONY : docs
docs:
	python setup.py build_docs --force
	cd build/docs && zip -r ../docs.zip .

.PHONY : test
test:
	tox

.PHONY : update-tests
update-tests:
	python run-tests.py update

.PHONY : clean
clean:
	rm -f MANIFEST
	rm -f test-output.html
	rm -f *.pyc
	rm -f markdown/*.pyc
	rm -f markdown/extensions/*.pyc
	rm -f *.bak
	rm -f markdown/*.bak
	rm -f markdown/extensions/*.bak
	rm -f *.swp
	rm -f markdown/*.swp
	rm -f markdown/extensions/*.swp
	rm -rf build
	rm -rf dist
	rm -rf tmp
	# git clean -dfx'
