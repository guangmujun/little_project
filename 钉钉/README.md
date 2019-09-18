### 通过调用钉钉机器人向钉钉的群组发送消息

1. 手机端，建立群组，在群组设置中添加自定义的机器人
2. PC端，点击“头像-机器人管理”，点击已添加的机器人，复制webhook内容
3. 编写程序

参考：

开发文档：https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq



说明：

1. 进入到项目文件目录 /home/pyproj/dingding
2. 后台运行程序``nohup python3 dingding.py &``

补充：

1. 查看后台进程``ps -A``
2. 结束进程``keill PID``(PID指进程号)