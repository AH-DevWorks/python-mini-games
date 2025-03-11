
# python-mini-games

## 簡介
   + 這個倉庫(Repository)包含我在學習和實踐 Python 過程中的參考課程、資源、建立的各種基礎小型遊戲專案以及成果等。
   + 這些專案都是基於線上課程中的教學內容進一步延伸、擴充而成，每個專案都展示了部份的 Python 概念和技術，反映我個人的學習和技能成長歷程。
   + 此倉庫集中於遊戲類專案，其他演算法專案請見另一倉庫: [python-algorithms](https://github.com/AH-DevWorks/python-algorithms)

## 課程參考
+ Udemy - [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)
  + 課程涵蓋了 Python 從基礎語法、流程控制及演算法、網頁開發，到資料科學、AI等進階主題知識。
+ Udemy - [以 SQLite 入門 SQL | Introduction to SQL with SQLite](https://www.udemy.com/course/introduction-to-sql-with-sqlite)
  + 課程從 SQL 基本觀念、實作到測驗循序漸進，內容涵蓋建立學習環境、資料表選擇、運算符與函數的應用、排序、篩選、條件邏輯、分組與聚合、子查詢以及資料表關聯，學習在自己的電腦上建立 SQLite 環境，並掌握關聯式資料庫與 SQL 查詢語法等基礎技能。
+ Udemy - [机器学习 A-Z (Machine Learning A-Z in Chinese)](https://www.udemy.com/course/machinelearningchinese/)
  + 學習機器學習的完整知識體系，從資料前處理、回歸、分類、聚類、關聯規則，到強化學習、自然語言處理、深度學習、降維與模型選擇等各個面向；透過 Python 和 R 的程式碼範本及案例，掌握構建並運用機器學習模型的能力
+ 線上資源 - [《Hello 演算法》](https://www.hello-algo.com/zh-hant/)

## 專案列表
+ 依完成日期排序（遞減）
> 執行方式： 1. 下載或 clone 此倉庫； 2. 進入對應的資料夾，如：`cd "子資料夾名稱"`； 3. 在該資料夾中使用命令提示字元 (CMD) 或終端機執行 Python 檔案，如： `python (檔名).py`。
>> 另可參考各專案資料夾內執行截圖檔案。

1. [TurtleCrossing](./TurtleCrossing)
  + **Turtle Crossing Game 烏龜過馬路遊戲**
    + 類 Jumping frog / Frog Crossing 遊戲
    + 玩家操縱一隻烏龜，必須找時機穿越充滿移動中車輛的道路
    + 抵達終點、level up後，烏龜會回到起始點，進行下一關卡。
    + 隨著關卡等級提昇，難度（車子數量、速度）將會隨之增加。
  + **使用的主要技術/概念**
    + 主要以python內建之[turtle — Turtle graphics](https://docs.python.org/3/library/turtle.html)進行開發
    + 以GUI及OOP概念，將player、場景、計分、車輛等項目拆分，進行模組化(modularize)，利於管理
  + 完成日期: *[2025-03-11]*
  + <span style="color: darkorange">未來預計延伸/改進：</span>
    + 增加豐富度，如隨機車輛大小，或關卡第二階段（過河——踩上浮木隨之移動）等

2. [Blackjack](./Blackjack)
  + **Blackjack 撲克遊戲**
    + 仿製常見之Blackjack（二十一點）遊戲
    + 初始玩家及莊家（電腦）皆有兩張牌，玩家可看見自己的所有手牌以及電腦的第一張牌
    + 玩家可持續叫牌或選擇pass，pass後玩家回合結束，進入莊家階段，若莊家手牌點數不足17點，則莊家會持續叫牌
    + Ace（1）卡牌可視為1點或11點；JQK皆視為10點
    + 勝利條件：
      1. 若雙方手牌皆未超過21點，點數大者勝。
      2. 若玩家手上點數恰好21點則Blackjack，無論莊家點數，皆為玩家獲勝
      3. 若玩家手牌已滿5張且未bust（超過21點）則屬於「Five-Card Charlie」，無論莊家點數，皆為玩家獲勝
  + **使用的主要技術/概念**
    + 將deal card、calculate score、show hand等遊戲各階段拆分為不同functions，利於管理
    + 以if-else、while loop等進行遊戲流程管理
  +  完成日期: *[2025-03-04]*
  + <span style="color: darkorange">未來預計延伸/改進：</span>
    + 轉以OOP呈現，讓程式結構更直觀，便於維護擴展

3. [Treasure of Tunes](./Treasure%20of%20Tunes)
  + **簡易尋寶遊戲——Treasure of Tunes**
    + 玩家是個冒險者，來到 Muse Island 尋找失落的旋律（lost melody）
    + 玩家必須透過輸入自己的選擇，成功抵達Happy Ending。過程中只要稍有疏失，立刻就會Game Over
    + 可重新「接關」從失敗的地方重新開始
    + 防呆設計，避免無效或複數輸入（如輸入指定範圍以外的文字）
    + 搭配簡單的ASCII Art增加視覺豐富度
  + **使用的主要技術/概念**
    + 以while loop搭配conditions進行防呆設計，避免使用者不合理的輸入
    + 搭配錯誤提示文字，讓使用者重新輸入直到合理為止
  + 完成日期: *[2025-02-26]*
  + <span style="color: darkorange">未來預計延伸/改進：</span>
    + 把遊戲的不同階段包裝成不同的Funcitons，提昇易讀性且方便管理
    + 考慮將Game Over玩家選擇重新開始遊戲時，是跳回遊戲最初階段而非階段性的起點
    + 擴展遊戲內容，增加豐富度與吸引力
    + 增加GUI界面；或把程式變成網頁版 WEB 應用程式

4. [待持續更新]




*首次建立：[2025-02-26]*  
*最後更新: [2025-03-11]*


