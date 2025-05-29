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
> * *(重要)* Q : 離開分頁式閱讀介面
> * J(或向下) : 下一行
> * K(或向上) : 上一行
> * 空白鍵 : 向下翻一頁
> * B : 向上翻一頁

4. git remote -v : 查看遠端URL

### 二、協作方式
1. git add : 將檔案的更改加入暫緩區(可使用git add . 將所有改動加入暫緩區)

2. git commit -m "敘述文字" : 將更改寫入本地.git紀錄中

3. git push -u origin 分支名(首次推送使用) : 推送並建立追蹤關係

4. git push(已建立追蹤關係) : 把當前的分支推送到對應的遠端分支
***
## 專案介紹
> 🎬AI 電影AI小助手
本專案旨在打造一個AI小助手，結合 LLM 模型訓練能力以及 Dify嵌入agent，讓使用者可以透過簡單的操作介面，自由的提問方式，藉由跟AI小助手聊天得到一些電影推薦。

我們的目標是讓使用者避免劇荒或者需要人來聊聊電影時，沒有人給出好的建議或閒話家常的情況，隨時都有小助手陪你聊電影。

## 使用者介面
>>介紹畫面

![image](https://github.com/user-attachments/assets/a26eb74f-ef1e-4742-8e0d-a3f9a1c85c25)
>簡單介紹小助手的功能還有一些簡單注意事項👆


![image](https://github.com/user-attachments/assets/22b58a72-eb98-4dc3-85c2-154b18670e74)
>想要開始體驗小助手就需要點擊這個按鈕👆


![image](https://github.com/user-attachments/assets/cb43395a-c261-4bfa-a975-5b6bcf681f50)
>點擊按鈕後進入登入介面👆









    

