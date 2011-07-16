clean:
	@find . -name "*.pyc" -delete

test: clean
	@nosetests --nocapture --with-coverage --cover-erase --cover-inclusive --cover-package=htmlentities
