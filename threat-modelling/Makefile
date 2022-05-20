DIAGRAMS_SRC := $(shell find . -name "*.py")
DIAGRAMS_PNG := $(addsuffix .png, $(basename $(DIAGRAMS_SRC)))

png: clean $(DIAGRAMS_PNG)

%.png: %.py
	python3 $< --dfd | dot -Tpng -o ./build/$(notdir $@)
	python3 $< --report docs/template.md > ./build/$(notdir $@).md && sed -i '' 's/sample.png/$(notdir $@)/g' ./build/$(notdir $@).md

clean:
	rm -rf ./build && mkdir ./build
.PHONY: clean
