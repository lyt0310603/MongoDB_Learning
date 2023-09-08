# MongoDB_Learning

## 資料來源
### 使用爬蟲爬取ptt CFantasy，取出作者 時間 連結 標題 跟推數，並將結果寫入資料庫，然而檢查過後發現資料有點小瑕疵，因此複製一份表單並嘗試修復他

### 複製表單的指令 ![](https://cdn.discordapp.com/attachments/1148965438886256764/1148965524080963694/2023-09-06_203748.png)

# 表單問題: 
* 在日期欄位中有些會帶有空白
* push_num(推數)欄位中是字串而非數字，且有些為 "爆" 或 "" ，其中 "爆" 代表推數超過一定值， "" 則代表該文沒有任何推
* 網址連接欄位缺少https://www.ptt.cc/

## 日期欄位含有空白

### 總共有57494筆資料須修正![](https://cdn.discordapp.com/attachments/1148965438886256764/1149265365642260500/2023-09-07_164954.png)

### 使用pymongo，用find找出所有日期含有空白的文章，再用迴圈個別更新，結果極其耗時。另外用迴圈遍歷的方式update的話即使中斷還是會更新已經update的，因為沒有用transaction的關係![](https://cdn.discordapp.com/attachments/1148965438886256764/1149294980498718842/image.png)

### 使用command方法相當快速，因為aggregate尚不支援explain，所以僅憑體感不到一秒，圖片上update區段使用aggregate方法![](https://cdn.discordapp.com/attachments/1148965438886256764/1149301294922735626/image.png)

## 推數轉換
### 使用command，分成三步驟
#### 1. 將一般數字從string轉成int ![](https://cdn.discordapp.com/attachments/1148965438886256764/1149630141874581565/image.png)
#### 2. 將 "" 轉成0 ![](https://cdn.discordapp.com/attachments/1148965438886256764/1149631356754726922/2023-09-08_170356.png)
#### 3. 將 "爆" 轉成數字，先找出最大值 ![](https://cdn.discordapp.com/attachments/1148965438886256764/1149633660480393216/image.png)  可以推斷推數超過99就會被替換成爆，因此將 "爆" 替換成100 ![](https://cdn.discordapp.com/attachments/1148965438886256764/1149634418084945951/image.png)
#### 利用$type，檢查有沒有漏掉，2代表string![](https://cdn.discordapp.com/attachments/1148965438886256764/1149635588589371462/image.png)

## 網址補全
### 使用command，利用$concat連接 ![](https://cdn.discordapp.com/attachments/1148965438886256764/1149644832894103572/image.png)