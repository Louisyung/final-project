## 使用提示:

1. 每次更改前請先pull下來確保本地端與github上不會產生衝突(使用自己的分支)

2. 將本地端push到github上後確認是否有pull requests

3. 建立pull requests並將分支的更動merge到main
***
## 常用指令:

### 一、查詢狀態  
1. git status : 查詢目前倉庫的狀態(包含當前所在分支及是否有add或commit)

2. git branch : 查看本地分支(所在分支)

3. git log : 查看目前分支的所有提交紀錄(會轉換到分頁式閱讀介面)

> 分頁式閱讀指令
* *(重要)* Q : 離開分頁式閱讀介面
* J(或向下) : 下一行
* K(或向上) : 上一行
* 空白鍵 : 向下翻一頁
* B : 向上翻一頁

4. git remote -v : 查看遠端URL

### 二、協作方式
1. git add : 將檔案的更改加入暫緩區(可使用git add . 將所有改動加入暫緩區)

2. git commit -m "敘述文字" : 將更改寫入本地.git紀錄中

3. git push -u origin 分支名(首次推送使用) : 推送並建立追蹤關係

4. git push(已建立追蹤關係) : 把當前的分支推送到對應的遠端分支


    

