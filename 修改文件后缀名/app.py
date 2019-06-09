##python批量更换后缀名

import os
import sys
path0=r"F:\\云南\\云南-手机"
path1=r"F:\\云南\\云南-手机"+'\\'

sys.path.append(path1)
print(sys.path)

# 列出当前目录下所有的文件
files = os.listdir(path0)
print('files',files)

for filename in files:
	portion = os.path.splitext(filename)
	if portion[1] == ".jpg": 
		
		newname = portion[0] + ".png" 
		filenamedir=path1 +filename
		newnamedir=path1+newname
		
		os.rename(filenamedir,newnamedir)
