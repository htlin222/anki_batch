#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: combine
# date: "2023-08-21"
# author: Hsieh-Ting Lin, the Lizard 🦎
import os
import re
import shutil

source_file = "theme.css"


def process_md_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    # Find the index of the first h2 heading
    match = re.search(r"##\s.+", content)
    if match:
        index = match.start()
        content = content[index:]
    # Use regex to replace h2 titles at the beginning of a line
    content = re.sub(
        r"^(## .+)",
        r'<div data-question markdown="block">\n\n\1',
        content,
        flags=re.MULTILINE,
    )
    # Use regex to replace '---' at the beginning of a line
    content = re.sub(r"^---$", r"\n</div>\n", content, flags=re.MULTILINE)
    # Add "---" if no match found
    if not re.search(r"^---$", content, flags=re.MULTILINE):
        content += "\n---\n\n(no back)"
    return content


def main(folder_name):
    # Create a list to hold processed content of all .md files
    combined_content = []

    # Iterate through .md files in the specified folder
    for file_name in os.listdir(folder_name):
        if file_name.endswith(".md") and "index" not in file_name.lower():
            file_path = os.path.join(folder_name, file_name)
            processed_content = process_md_file(file_path)
            combined_content.append(processed_content)

    # Combine all processed content into one string
    combined_content_str = "\n".join(combined_content)

    # Add the folder name as the first line
    combined_content_str = f"---\ncss: theme.css\n---\n\n# {os.path.basename(folder_name)}\n\n{combined_content_str}\n"

    # Create a 'foldername.tmp' folder if it doesn't exist
    tmp_folder = f"./{os.path.basename(folder_name)}.tmp"
    os.makedirs(tmp_folder, exist_ok=True)

    # Write the combined content to 'foldername.md' in the 'foldername.tmp' folder
    # with open(f"{tmp_folder}/{os.path.basename(folder_name)}.md",
    with open(f"{tmp_folder}/{os.path.basename(folder_name)}.md",
              "w") as output_file:
        output_file.write(combined_content_str)

    shutil.copy(source_file, tmp_folder)


def copy_img(folder_name):
    # Create a temporary folder with the name of the source folder
    tmp_folder = f"./{os.path.basename(folder_name)}.tmp"
    os.makedirs(tmp_folder, exist_ok=True)

    # Define a list of valid image file extensions
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif"]

    # Iterate through the files in the source folder
    for filename in os.listdir(folder_name):
        # Check if the file has a valid image extension (case-insensitive)
        file_extension = os.path.splitext(filename)[-1].lower()
        if file_extension in valid_extensions:
            # Build the full paths for the source and destination files
            src_path = os.path.join(folder_name, filename)
            dest_path = os.path.join(tmp_folder, filename)

            # Copy the image file to the temporary folder
            shutil.copy2(src_path, dest_path)

    # Return the path of the temporary folder
    print(f"Images copied to temporary folder: {tmp_folder}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python combine.py foldername")
    else:
        folder_name = sys.argv[1]
        main(folder_name)
        copy_img(folder_name)
