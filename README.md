# MongoDB_Learning
## The code that copy one collection to another ![](https://cdn.discordapp.com/attachments/1148965438886256764/1148965524080963694/2023-09-06_203748.png)

# Problems: 
* 1. contain blank(" ") in some article's date
* 2. type of push_num is string not int and some of them are '爆' or ''('爆' means this article is popular,'' means that no one give this article like)
* 3. url lack some part to use

## 第一題

### 總共有57494筆資料須修正![](https://cdn.discordapp.com/attachments/1148965438886256764/1149265365642260500/2023-09-07_164954.png)

### 使用pymongo，用find找出所有日期含有空白的文章，再用迴圈個別更新，結果極其耗時。另外用迴圈遍歷的方式update的話即使中斷還是會更新已經update的，因為沒有用transaction的關係![](https://cdn.discordapp.com/attachments/1148965438886256764/1149294980498718842/image.png)

### 使用command方法相當快速，因為aggregate尚不支援explain，所以僅憑體感不到一秒，圖片上update區段使用aggregate方法![](https://cdn.discordapp.com/attachments/1148965438886256764/1149301294922735626/image.png)