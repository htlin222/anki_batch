#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: add_yaml
# date: "2023-08-25"
import os
import re
import shutil

source_file = "theme.css"


def process_md_file(content, title):
    # Find the index of the first h2 heading
    content = re.sub(
        r"^(## .+)",
        r'<div data-question markdown="block">\n\n\1',
        content,
        flags=re.MULTILINE,
    )
    # Use regex to replace '---' at the beginning of a line
    content = re.sub(r"^---$", r"\n</div>\n", content, flags=re.MULTILINE)
    content = content.replace("</div>", f"\n`deck: 📚 {title}`\n\n</div>")
    return content


def main(folder_name):
    # Create a list to hold processed content of all .md files

    # Iterate through .md files in the specified folder
    for file_name in os.listdir(folder_name):
        if file_name.endswith(".md") and "index" not in file_name.lower():
            file_path = os.path.join(folder_name, file_name)
            with open(file_path, "r") as file:
                content = file.read()
            match = re.search(r"^#\s(.*)", content, re.MULTILINE)
            if match:
                title = match.group(1)
                processed_content = content.replace(match.group(0), "", 1)
                print(f"📖 Title: {title}")
            else:
                title = os.path.basename(folder_name)
                print("No h1 header found")
            processed_content = process_md_file(content, title)
            added_yaml_content = f"---\ncss: theme.css\n---\n\n# {os.path.basename(folder_name)}::{title}\n\n{processed_content}\n"
            tmp_folder = f"./{os.path.basename(folder_name)}.tmp"
            os.makedirs(tmp_folder, exist_ok=True)
            # Replace non-letter and non-underscore characters with underscores
            title_cleaned = re.sub(r"[^a-zA-Z_]", "_", title)

            # Replace colons, forward slashes, and backslashes with underscores
            title_cleaned = re.sub(r"[:/\\]", "_", title_cleaned)
            with open(
                    f"{tmp_folder}/{os.path.basename(folder_name)}_{title_cleaned}.md",
                    "w") as output_file:
                output_file.write(added_yaml_content)

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
