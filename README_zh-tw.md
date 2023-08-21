# 中文說明

## 快速上手

1. 建立一個資料夾
2. 裡面每一個 md 檔，都是一張卡片
3. 卡片格式如下
   - 正面都是用一級標題開頭 h1 `# 標題`
   - 正反用`---` 分開
   - 一級標題以前的內容都會被刪掉 e.g. yaml 內容

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

4. 執行 `make DECK=your_folder_name`
5. 就會得到 `.apkg` 檔了
