build: venv
	$(VENV)/python build_with_local_node.py
.PHONY: build

docker: venv
	$(VENV)/python build.py
.PHONY: build

include Makefile.venv
