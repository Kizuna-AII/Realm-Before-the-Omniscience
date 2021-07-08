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

4. 电梯门向上的按钮的图片

5. 三个区域的logo

6. 字母A-H，数字1-16（8进制下）的长宽比1：1贴图（现在的电梯按钮字体不一样不太好康）


