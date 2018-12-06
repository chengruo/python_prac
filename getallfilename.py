import os
import os.path
import sys
rootdir = "C:\\Users\\Utsc0990\Desktop\HaiNan\externalxml"                                   # 指明被遍历的文件夹

externalfile = open("externalfile.txt",'w')
sys.stdout = externalfile
for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
      for filename in filenames:
          print(filename)
