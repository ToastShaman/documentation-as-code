SLIDES_SRC := $(shell find . -name "*.md")
SLIDES_PDF := $(addsuffix .pdf, $(basename $(SLIDES_SRC)))
PWD := $(shell pwd)

pdf: clean $(SLIDES_PDF)

%.pdf: %.md
	docker run --rm --init -v $(PWD):/home/marp/app/ -e LANG=EN marpteam/marp-cli $< -o ./build/$(notdir $@)

clean:
	rm -rf ./build && mkdir ./build
.PHONY: clean
