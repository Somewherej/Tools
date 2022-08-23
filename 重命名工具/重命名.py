import os
import sys

def rename(filePath):
    """
    :param filePath: 文件夹的路径
    :return:
    """
    # 文件筛选条件
    condition_input = ('input')
    condition_output = ('output')
    #os.walk 查找文件
    #root  表示正在访问的当前目录
    #dirs  表示root当前目录下包含的子目录
    #files 表示root当前目录下包含的文件
    for root, dirs, files in os.walk(filePath):
        # 文件夹名字
        mark = root.split('\\')[-1]

        #for循环遍历文件名字
        for fileName in files:
            #排除rename文件自己
            if fileName != sys.argv[0]:
               if fileName.startswith(condition_input):
                    #len(input1.txt) == 10
                    if len(fileName) == 10:
                        os.rename(os.path.join(root, fileName),os.path.join(root, fileName[-5] + '.' + "in"))
                    # len(input10.txt) == 11
                    if len(fileName) == 11:
                        os.rename(os.path.join(root, fileName),os.path.join(root, fileName[-6] + fileName[-5] + '.' + "in"))

               if fileName.startswith(condition_output):
                   # len(output1.txt) == 11
                   if len(fileName) == 11:
                       os.rename(os.path.join(root, fileName), os.path.join(root, fileName[-5] + '.' + "out"))
                   # len(output10.txt) == 12
                   if len(fileName) == 12:
                       os.rename(os.path.join(root, fileName),
                                 os.path.join(root, fileName[-6] + fileName[-5] + '.' + "out"))
    print("重命名成功")



#当前文件所在的目录os.path.dirname(__file__)
print(rename(os.path.dirname(__file__)))
