# Define a variable for the folder name
DECK := $(folder_name)

# Define the default target
all: add_yaml img_to_local mdankideck

add_yaml:
	python add_yaml.py $(DECK) #加入yaml，加入anki的樣式

combine:
	python combine.py $(DECK)

img_to_local:
	python img_to_local.py $(DECK).tmp #下載圖片

mdankideck:
	mdankideck $(DECK).tmp . #產生apkg

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
