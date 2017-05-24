
.PHONY=.virtualenv

.virtualenv:
	virtualenv -p python2 .virtualenv

notebook: .virtualenv
	.virtualenv/bin/jupyter notebook --notebook-dir=notebooks

	
