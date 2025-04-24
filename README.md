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
> 🎬AI 劇本創作助手：角色個性 + 劇本風格，自動生成提示打造原創劇本！

本專案旨在打造一個創作工具，結合 DeepSeek 模型訓練能力，讓使用者可以透過簡單的操作介面，自由選擇角色個性、劇本風格，系統便會根據這些條件自動生成提示語，進一步引導 AI 進行劇本創作。

我們的目標是簡化劇本開發流程，讓創作者不需具備專業編劇或 prompt 設計知識，也能輕鬆打造高質感的原創劇情。

## 使用者介面
>主畫面

![image](https://github.com/user-attachments/assets/50fdc63f-6d14-42f0-b367-214e20fc11bb)
>使用者可選擇推薦的劇情類型或者自行設定劇情類型

![image](https://github.com/user-attachments/assets/9507e5bc-e224-4ffb-b084-473da841addf)
>在設定玩劇情類型後會出現新增角色的按鈕

![image](https://github.com/user-attachments/assets/fe744b25-8916-4e17-9d85-438f87081766)
>點擊後能夠在此新增角色並進行刪除或更改管理

![image](https://github.com/user-attachments/assets/2367d655-09cd-412f-919c-35ce3a92cd0a)
>當設定完角色及個性後，彈出劇情提式的視窗(可輸入)

![image](https://github.com/user-attachments/assets/88fec569-2a85-4497-8bd9-c1c47a56351e)
>確認完後會列出這次劇本會有的角色及一些相關提式訊息，AI就會開始幫你生成劇本啦!

![image](https://github.com/user-attachments/assets/5e151385-1499-4546-bb1e-c895d82f3818)







    

