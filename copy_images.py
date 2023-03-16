import os
import shutil

from past.builtins import raw_input

# paths = ['C:\\Users\\2023011\\Downloads\\XT\\img']  # 原文件路径
temp = raw_input(u"请输入文件目录:")
paths = []
paths.append(temp)

savePath = raw_input(u"请输入保存目录:")

# paths = ['./']  # 原文件路径
# savePath = './all_images'  # 目标路径
postfix = ['.jpg', '.JPG', '.PNG', '.png', '.jpeg', '.JPEG']  # 指定文件后缀名

if not os.path.exists(savePath):
    os.mkdir(savePath)


def copyFile(sourcePath, savePath):
    items = os.listdir(sourcePath)
    for item in items:
        filePath = os.path.join(sourcePath, item)
        if os.path.isfile(filePath):
            if os.path.splitext(filePath)[1] in postfix:  # 后缀名判断
                shutil.copyfile(filePath, os.path.join(savePath, item))  # 复制文件到目标文件夹
                print(' 复制成功 ' + filePath)
            else:
                continue
        elif os.path.isdir(filePath):
            copyFile(filePath, savePath)  # 如果是文件夹，则再次调用此函数，递归处理
        else:
            print('不是目标文件或文件夹 ' + filePath)


if __name__ == '__main__':
    for path in paths:
        sourcePath = path
        copyFile(sourcePath, savePath)