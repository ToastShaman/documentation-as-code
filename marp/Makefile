DIAGRAMS_SRC := $(shell find . -name "*.md")
DIAGRAMS_PNG := $(addsuffix .pdf, $(basename $(DIAGRAMS_SRC)))
PWD := $(shell pwd)

pdf: clean $(DIAGRAMS_PNG)

%.pdf: %.md
	docker run --rm --init -v $(PWD):/home/marp/app/ -e LANG=EN marpteam/marp-cli $< -o ./build/$(notdir $@)

clean:
	rm -rf ./build && mkdir ./build
.PHONY: clean
