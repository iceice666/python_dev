## tools
一個小軟體

Made by KSHSlime & iceice666

### 如何使用
#### 註：`[   ]` 內的名稱需自行代換為你的程式資料夾的名稱

STEP 1：在projects資料夾新增一個資料夾 名子為 `[project_id]`
[Imgur](https://i.imgur.com/9zfDyL7.png)

STEP 2：將 程式or軟體or捷徑or可執行檔...等等 放入`[project_id]`資料夾中
[Imgur](https://i.imgur.com/cAt9S0z.png)

STEP 3：進入 data 資料夾 打開 settings.json
[Imgur](https://i.imgur.com/lJYqM0y.png)

STEP 4：[在這裡](https://i.imgur.com/fXAkc6q.png) 輸入下列文字

```
"[project_id]": {
  "path": "[run_path]",
  "name": "[project_name]"
}
```

其中

- `[project_id]` ：每個project專屬的id

---

+ `[run_path]` ：要執行的檔案的路徑（包括副檔名）:
+ `[project]\\[run_file]` 
+ `[project]`為此工具的跟目錄
+ `[run_file]`為執行的的名稱 （此檔案必須在`[project]`中 且必須在`[project]`中的最上層）
        
        [project]
            │
            ├─ [run_file]
            │
            ├─ [run_dir]
            │
            └─ [other_file]
        
---

- `[project_name]` ：在軟體中要顯示的名稱

