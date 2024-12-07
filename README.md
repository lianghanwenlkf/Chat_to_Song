# Chat_to_Song
## 1.数据准备
### 1.1 聊天记录csv文件
#### 使用“留痕”软件导出微信聊天记录的csv文件，第三列是消息类型，第八列是消息内容，第十列是微信备注名。可以导出对方的单聊以及包含对方的群聊的聊天记录，并把文件路径添加至csv_files列表中。
#### 留痕官网：https://memotrace.cn/
### 1.2 歌词txt文件
#### 在网上搜索想要制作歌曲的歌词，新建txt文件保存歌词，一行为一句歌词。可以批量新建歌词文件，并把文件路径添加至lyrics_files列表中。
### 1.3 中文字体文件
#### 代码中有绘制的功能，需要中文字体，可下载字体ttf文件，并把路径添加到font_path中。
## 2.保存路径设置
### 2.1 查找结果文件
#### 代码会根据每句歌词，逐字查找聊天记录中匹配的字符，并在查找到所有符合条件的聊天记录消息中，随机挑选一句保存。若聊天记录中无对应字符，则直接保存单字。所有查找结果会以txt文件保存，需要在output_path中指定保存路径。
### 2.2 聊天记录覆盖率图
#### 在每一句歌词中，定义聊天记录中覆盖到的字符除以歌词字数，为覆盖率。计算每一首歌的每一句歌词的覆盖率，并绘制覆盖率曲线。曲线图像回忆png格式保存，需要在pic_path中指定保存路径。
