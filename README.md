# ANKI batch

[中文說明](README_zh-tw.md)

## TLDR

1. create a folder with many markdown files in it
2. will treat each markdown file as a card
3. each markdown file should be formated as:
   - the front will start from the h1 `# title`
   - the back will start after `---`
   - will omit yaml and any text before h1

```
---
title: wow
date: 2023-08-21
author: Hsieh-Ting Lin
---

> text before h1 will be delete

# note1

front

---

back
```

4. run make DECK=your_folder_name
5. you will get the `.apkg` file
