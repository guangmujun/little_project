# 自动化监控网页变化

> 模拟登陆 https://blog.csdn.net/qq_22222499/article/details/52664110



> 网页变化监控 http://www.caorongduan.com/index.php/archives/3/ 



```Python 
userName: 
pwd: 
certCode: 
sb: sb     # 提交按钮
```

人文讲座预告网址：【选课系统】、【人文讲座】、【讲座预告】



问题：

缺乏Last-Modified参数 

How to work around missing 'last-modified' headers?

![1569740110639](E:\GitHub\little_project\little_project\网页变化监控\1569740110639.png)



尝试用缓存机制解决

替代方案：爬取页面，存储，定期爬取，存储对比



变化检测原理

提取讲座序号，得到最大的序号，存入全局变量

每次爬取得到最大的序号，和此序号比较

新的序号较大，将全部内容发送出来，否则...



https://blog.csdn.net/qwerty200696/article/details/78771448

获取验证码图片，弹出窗口，输入验证码，



