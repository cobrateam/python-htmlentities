clean:
	@find . -name "*.pyc" -delete

dependencies: nose coverage

nose:
	@python -c 'import nose' 2>/dev/null || pip install nose==1.0.0

coverage:
	@python -c 'import coverage' 2>/dev/null || pip install coverage==3.5

test: dependencies clean
	@nosetests --nocapture --with-coverage --cover-erase --cover-inclusive --cover-package=htmlentities
