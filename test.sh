cd test
nosetests --with-coverage --cover-package cutecharts --cover-package test && cd .. && flake8 --exclude build --max-line-length 89 --ignore=F401
