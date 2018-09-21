clean:
	@find . -name "*.pyc" -delete

dependencies: pytest

pytest:
	@python -c 'import pytest' 2>/dev/null || pip install pytest

test: dependencies clean
	@pytest .
