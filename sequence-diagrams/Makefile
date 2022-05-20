DIAGRAMS_SRC := $(shell find . -name "*.plantuml")
DIAGRAMS_PNG := $(addsuffix .png, $(basename $(DIAGRAMS_SRC)))
DIAGRAMS_SVG := $(addsuffix .svg, $(basename $(DIAGRAMS_SRC)))
PWD := $(shell pwd)

png: build $(DIAGRAMS_PNG)
svg: build $(DIAGRAMS_SVG)

%.png: %.plantuml
		cat $< | docker run -v $(PWD):/work -w /work --rm -i toastshaman/plantuml -tpng > ./build/$(notdir $@)

%.svg: %.plantuml
		cat $< | docker run -v $(PWD):/work -w /work --rm -i toastshaman/plantuml > ./build/$(notdir $@)

build: clean
		docker build -f ./Dockerfile --build-arg plantuml_version=1.2022.5 -t toastshaman/plantuml:latest .

clean:
	rm -rf ./build && mkdir ./build

.PHONY: build png svg clean
