# SQL_project0x1

ver 0.6 完成登入&註冊帳號的部分

ver 0.7 部分函式拆分完成

ver 0.8 增加管理員

ver 1.0 重構code 並將 管理員 介面設置完成

ver 1.1 建立新課表 部分完成

ver 2.11 優化管理員介面

ver 2.4 完成加退選 函示 加入預設課表匯入

ver 2.5 完成課表導入 & 優化 整體學分數計算 將選課介面完成至60%

ver 2.6 系統爆掉重load

ver 2.7 把選課部分完成 新增可否選擇外系學分 暫時移除照片功能

ver 2.8 再次優化選課成功介面 並且修正 系外判定異常

ver 2.81 補sql data黨

ver 2.9 介面分割 + 預選 + 退選時裝 待補預退選

ver 2.94 修正登入 / 加選 型別錯誤 及各類狀態

ver 2.96 問題修正資料庫再修改

ver 3.0 正式版 ver1.0

#目前優先完成
~~1.選課列表回傳判定~~
    ~~a.同名課程~~
    ~~b.擋修課程~~
    ~~c.學分數判定~~
    ~~d.本系課程~~
~~2.退選部分 完全尚未開工 估計 1 Day~~
~~考慮加入課程名稱至課表中~~

待補功能:
1.忘記密碼

~~a. 加選： 同學可以加選課程，課程加選須滿足以下限制：~~
   ~~(i) 同學只能加選本系的課程；~~
   ~~(ii) 人數已滿的課程不可加選；~~
   ~~(iii) 不可加選衝堂的課程；~~
   (iv) 不可加選與已選課程同名的課程；
   ~~(v) 加選後學分不可超過最高學分限制 (30 學分)。~~

~~b. 退選：同學可以退選課程，課程退選須滿足下列限制：~~
    ~~(i) 退選後學分不可低於最低學分限制 (9 學分)；~~
    ~~(ii) 退選必修課需提出警告。~~

~~c. 功課表：列出同學已選課程之課號、名稱、課程時間 (可條列或者以功課表方式表示)，且系統應根據每個同學的系所、年級，將其必修課預選進其功課表中；~~

非必要功能：
a. 可選課列表：列出該同學可選的課程清單；
~~b. 關注抽籤功能：對於人數已滿的課程，可以關注，當該課程有人退選導致有空額出現時，由所有關注該課程的同學亂數抽選一人加選該課程，唯同學不能關注部可加選的課程；~~

上述為加分項目，然3 人以上組別，每多一人須從上述非必要需求中選擇一項實作列為基礎項目，不另行加分。

其他非必要功能：

~~(i) 登入/登出；~~
~~(ii) 擋修限制；~~
(iii)  任何其他與選課系統相關的額外功能。(?)


額外提醒 可每堂課是以16進未去進行儲存
ex monday_13節 -> 1d
ex sunday_7 節 -> 77
因此判定需先將 時間戳記欄位 導入後抓長度/2 並開始取value