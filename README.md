# Realm: Before the Omniscience

Project for ZJU-Game-2021

Collaborator:

3180101995 Haohan JIANG 	(River75731)

3180103009 Tianyun ZHONG (Kizuna-AII)

3180105261 Ningyuan YOU	(SilverNebula)

3180105438 Qingyi HE			 (FlazeNaive)



## Readme

程序源码：./Code/Code.uproject

Demo：./Release

演示视频：./Release

所有文档均在./Document下

设计文档：Design Book.md （后续设计有修改，会有更新）

概念文档：Concept Book.md

开发文档：Development Report (还有一些技术部分未更新，后续会有更新)

报告ppt：presentation.pptx

分工文档：Detailed Contribution.md



## Timeline

6.6 游戏概念文档

6.15 游戏策划书 Part1 

6.16 游戏策划书 Part2

6.17 游戏策划书 Part3

6.20 Part1

6.25 Part2

6.27 Part3



### 3 DAY TO PUBLISH!

**note**

room6里 BP door1，4是北边大厅的，BP door2，3是药房的（修改路线用）

River:
DAY 1: Room11实验室场景搭建，关卡蓝图及核心技术、所有收集品设置、Room2收集品修改
DAY 2: Room4场景搭建及关卡蓝图，无尽回廊搭建、Room8关卡蓝图、策划文档修改、Room8-12BGM
DAY 3: Room6关卡蓝图，合并，宣传视频



SilverN:
DAY 1: 难度调节、语言调节、画质调节接口（传送门清晰度），滚动字幕ending之后回到主菜单，infopic 调尺寸接口
DAY 2: 做宣传视频特效动画（想实现的效果是最后游戏logo缓慢开始旋转然后缓慢停下来，出现游戏名，参考其他游戏宣传片），找一些宣传片的音效，游戏主菜单按钮要不要改成无边框？
DAY 3: 音量调节（全局管理音量，现在我放的所有BGM是不受UI里的音量控制的），修下bug(例如电梯按钮有一个更黑、奇怪的纹理问题等、可以顺手把数字贴图全换了（现在0-9和10-16位置有点不太一样，微软雅黑不能商用）)



KizunaAI:

DAY1: 传送门给个清晰度接口，Room8场景搭建及核心技术（方向键/IJKL控制矩形的灯上下左右转，能投到墙壁上的那种，建议看下策划案里这里的谜题设计）

DAY2: 关卡流（1-6-7-8-9-10-11-12），改下前面的密码锁（Room2提示不够明显 最好把两个数字放到门的两边，然后把所有数字密码锁改成8进制），Room4现需要一个密码为BG(CITY)-F5(ZONE)-13(BLOCK)-15(FLOOR)的地方，设定是一个未来世界的去任意城市任意建筑的传送门，可以加入小彩蛋：如果输入BG-D3-06-10可以传送到Room1（可以从抽屉里的超市小票推出的自己家的地址），这里城市编码是A-H，zone是A-H,1-7，floor按键都是0-7，建议触发方式是按一个按键检测前面是否正确，若正确打开传送门至Room5/1

DAY3: 调整各个房间的光照（不出意外只有你能编译了），希望Room9能够更顺滑地过渡到Room10而不是直接闪现qwq，可以考虑加个没有门的门之类的，10加个壳和终点门吧让他顺利过渡到room11，9和10改成逆时针



Flaze:

DAY1：Room4素材，Room6素材（放在道场的地图），游戏logo，Room11素材（详见策划案），把带坐标的国际象棋棋盘obj放到Room3里（obj在群文件）

DAY2: Room6场景搭建（如果能调下光照就更好了呜呜）

DAY3: Room8、11所有物件，无尽回廊纹理调整，所有房间纹理调整统一每个部分画风





### Test to Release

Todos：

1. Room6光照
2. Collection2
3. Ending
4. 提示&反馈

tester的问题反馈：

1. room3的密码复用问题

   Solution：

   1. 直接4位改成2位密码
   2. 添加连线/别的提示引导密码复用（或直接将密码初始值设为35）
   3. 在room3添加新的线索（不复用，另一个视角是新密码）

2. 视角移速太快，晕3D问题（UI添加调节条？）

3. UI的bug

   ![](.\Photos\问题反馈-UI.jpg)

   “然后 ui这里 好像点了设置 敲esc 就会出问题（”



## Ending Text

### ENG

Realm : Before the Omniscience



Contributors

Master Planning : River75731

Concept Sketch : FlazeNaive, Kizuna_AII, River75731, SilverNebula

Concept Design : River75731

Level Design : River75731

User Interface : SilverNebula

Sound Effect : SilverNebula

Background Music : River75731

Art Supervisor : FlazeNaive

Scene Building : FlazeNaive, Kizuna_AII, River75731

Art Material : FlazeNaive, Kizuna_AII, River75731

Mechanic Implementation : Kizuna_AII



Art Material (Free Material in Unreal Market)

Edith Finch : Barbara Room

Edith Finch : Cannery and LowPoly Kingdom

Edith Finch : Classrooms and Bedrooms

Edith Finch : Edie Room

Edith Finch : Molly Room

Edith Finch : Sam Room

UE4 Starter Content



Music Material 

(Declaration : Some materials have not obtained commercial copyright. This work is for entertainment purposes only. Commercial activities in any form are not allowed.)

Aphex Twin - #3

Aphex Twin - #17 

Aphex Twin - T69 Collapse

Kikagaku Moyo - Amayadori

Kikagaku Moyo - Entrance

Re-TROS (Rebuilding the Rights of Statues) - 8+2+8 II

Re-TROS (Rebuilding the Rights of Statues) - THE LAST DANCE, W_

The Big Wave - Synth

发光曲线 (Glow Curve) - 死在旋转公寓

惘闻 (Wang Wen) - 独舞

超级市场 (The Supermarket) - 空4 (Empty #4)



Acknowledgement

Unreal Engine 4.26.2



### CHN

感知领域



制作者（按姓名首字母排序）

总策划：江昊翰

概念草案：贺情怡、江昊翰、游宁远、钟添芸

概念设计：江昊翰

关卡设计：江昊翰

UI界面：游宁远

音效 ： 游宁远

背景音乐 ：江昊翰

美术总监：贺情怡

场景搭建 ： 贺情怡、江昊翰、钟添芸

美术素材 ： 贺情怡、江昊翰、钟添芸

核心技术蓝图：钟添芸



素材提供

（注：部分素材未获得商用版权，本作品仅供娱乐使用，不允许将本作品以任何形式进行商业行为，违者必究）

美术素材（虚幻商城免费产品）

Edith Finch : Barbara Room

Edith Finch : Cannery and LowPoly Kingdom

Edith Finch : Classrooms and Bedrooms

Edith Finch : Edie Room

Edith Finch : Molly Room

Edith Finch : Sam Room

UE4 Starter Content



音乐素材（均未获得商用版权）

《#3》—— Aphex Twin (Room11 背景音乐)

《#17》—— Aphex Twin (Room7 背景音乐)

《T69 Collapse》 —— Aphex Twin (Room9 背景音乐)

《空4》—— 超级市场 (Room6 背景音乐)

《Synth》—— 大波浪 The Big Wave (Room8 背景音乐)

《死在旋转公寓》—— 发光曲线 (Room6 背景音乐)

《Amayadori》—— 幾何学模様 Kikagaku Moyo (Room3 背景音乐)

《Entrance》—— 幾何学模様 Kikagaku Moyo (主菜单背景音乐)

《独舞》—— 惘闻 (Room10 背景音乐)

《8+2+8 II》—— 重塑雕像的权力 Re-TROS (Room7 背景音乐)

《THE LAST DANCE, W_》 —— 重塑雕像的权力 Re-TROS (Room12 背景音乐)



特别鸣谢

虚幻引擎4.26.2





## Naming Rule

Level : Room1, Room2,...

Texture :  XX_Mat，XX_Mesh



## Map Design

在UE4中按照1m=100像素来设计



## Model List

全图：弧形墙壁、天花板、地板、自动门（类似电梯门那种左右打开的）、拼图（收集品）

### Room 1

卧室场景

衣柜、床、电脑桌、鼠标、键盘、显示器、窗户、灯管、门锁（密码锁）、置物架、挂在衣架上的衣服

### Room 2

类似厨房

油烟机、锅、灶台、柜子、冰箱、洗衣机、（烘干机）、盆栽、窗户、带抽屉的桌子、试卷

### Room 3

书房场景

书柜、各种书、仪器、沙发、显示屏、国际象棋棋盘

### Room 4

显示屏、密码板、奇怪的模型（应该可以用基础图形组合起来）、射灯

### Room 5

电梯门、电梯按钮、放在电梯旁边的盆栽

### Room 6

医院内的该有的东西

### Room 7

玻璃墙、迷宫中心的雕塑、屏幕、门上的指示器（参考谜题5-1）

### Room 8

射灯、控制台

### Room 9

### Room 10

### Room 11

### Room 12

前面都出现过了



## Material List

按重要性排序：

1. Room4两个屏幕上的画，草图：

   大意：左下角的王和后指代国际象棋中的王和后，坐标是D1和E1，左边是一张城市俯瞰地图，线条是马路，其他地方可以随意添加，只要不要和谜题混淆就行（图案是我随手糊的），右边是SOUND LAB位置，通过右边的图可以推断建筑物所在区块的应有的俯瞰图的样子，从而去左边找到对应的坐标F5，左边的图王和后可以换成类似图形的地方，例如修成皇冠图案的公园等，实在不行就使用地名标识，例如QUEEN'S PARK，教堂之类的。右边是一张SOUNDLAB宣传画，画出楼的样子，并用箭头指出SOUNDLAB的位置，位于第13层（但是不要写第13层几个字，让玩家自己数），不过密码是13。

   ![](./Photos/Room4_Wall_Draft.jpg)

2. Room6里面需要一个长得比较像蓝图一样的东西，就那种有点像建筑工地蓝图的蓝底白字，内容是Room6平面图（用于贴在道场上，指示玩家去哪里收集道具（我现在用的文字提示））

3. Room11也需要一个类似蓝图，不过画的是整个地图的平面图

5. 三个区域的logo

6. 字母A-H，数字1-16（8进制下）的长宽比1：1贴图（现在的电梯按钮字体不一样不太好康）


## 目前可用的UI

存读档:存档自动存所在level(关卡)，读档自动open level；有接口GetNowLevel()和SetNowLevel()可以手动存一个integer(可以用来记具体到了哪个room..?)

提示图像(小)：BP_Actor_Pickupable的子类可以设一个infoPic，当鼠标移上去时在准星旁边弹出图片；

提示图像(大)：调用UImanager的ShowItemInfo()接口可以在屏幕中央弹出一个有图片和文字的面板（带滚动条，可以放很多字），需要玩家手动关闭。

字幕：调用UImanager的ShowSubtitle接口可以以指定屏幕坐标、时长、字号、内容显示一行文字。

显示坐标：如有需要可以在玩家HUD上显示character的xyz坐标等属性。

进度条actor：可以在场景中放一个进度条，见UI/InterfaceActors/ProgressbarActor

显示屏actor：可以在场景中放一个显示屏，显示任意文字和图像。见UI/InterfaceActors/InterfaceActor