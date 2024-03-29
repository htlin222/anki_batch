# ANKI batch

[中文說明](README_zh-tw.md)

## TLDR

1. create a folder with many markdown files in it
2. will treat each markdown file as a deck
3. each markdown file should be formated as:
   - the front will start from the h2 `## title`
   - the back will start after `---`
   - h1 `# title` will be the deck name

```
# deckname

## card 1

---

back

## card 2

---

back
```

4. Install python packages

```bash
pip install -r requirements.txt
```

5. run

```bash
make DECK=your_folder_name
```

6. you will get the `.apkg` file from each markdown

## Supplementary

- Any file with the name containing 'index' will be ignored.
  - Especially useful for: creating a `note_index.md` using wikilinks to connect various documents.
- Images should be added in markdown format like `![alt](img.jpg)` or `![alt](https://i.imgur.com/abc123)`.
- You can modify the `theme.css` to adjust the card styles.
