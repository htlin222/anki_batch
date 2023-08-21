# Define a variable for the folder name
DECK := $(folder_name)

# Define the default target
all: combine img_to_local mdankideck

combine:
	python combine.py $(DECK)

img_to_local:
	python img_to_local.py $(DECK).tmp

mdankideck:
	mdankideck $(DECK).tmp .

# Specify that these targets do not create actual files
.PHONY: combine img_to_local mdankideck

# Clean up temporary files
clean:
	rm -rf $(DECK).tmp

env:
	pip install -r requirements.txt

# Define a target for cleaning and then running all tasks again
rebuild: clean all

# By default, just run the 'all' target
default: all
