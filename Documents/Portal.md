所有功能使用下列参数即可完成：

![](../Photos/Portal.png)

- Destination Actor: 传送目的地的actor
- Gate Mat：本传送门的材质，一般选择某个M_Portal_CameraCube_X，该材质应当是其他Portal的Render Target的Texture
- Render Target：将本传送门摄像机捕获的内容关联到该Render Target上，生成Texture
- Target Relative Offset：人物传送后的偏移位置，防止人物传送之后直接被传回来
- Camera Rotate：摄像机绕Z轴的旋转角度，需要手动调整确保传送前后画面连续