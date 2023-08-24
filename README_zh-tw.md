# 中文說明

## 快速上手

1. 建立一個資料夾
2. 裡面每一個 md 檔，都是一張卡片
3. 卡片格式如下
   - 正面都是用一級標題開頭 h2 `## 標題`
   - 正反用`---` 分開
   - 一級標題為卡片的牌堆名稱

```
# deckname

## card 1

---

back

## card 2

---

back
```

4. 安裝 python 套件

```bash
pip install -r requirements.txt
```

5. 執行

```bash
make DECK=your_folder_name
```

5. 就會得到 `.apkg` 檔了

## 補充

- 任何檔名包含`index` 的檔案會被忽略
  - 特別適用於：用 wikilink 建了一個 `note_index.md` 來連到各個文件
- 圖片以 markdown 的格式加入 `![alt](img.jpg)` 或 `![alt](https://i.imgur.com/abc123)`
- 可以修改 `theme.css` 來調整卡片樣式
