DIAGRAMS_SRC := $(shell find . -name "*.py")
DIAGRAMS_PNG := $(addsuffix .png, $(basename $(DIAGRAMS_SRC)))
PWD=$(shell pwd)

png: build $(DIAGRAMS_PNG)

%.png: %.py
	cat $< | docker run -i --rm -v $(PWD)/build:/diagrams diagrams

build: clean
	docker build . -t diagrams:latest -t diagrams

clean:
	rm -rf ./build && mkdir ./build

.PHONY: build clean png