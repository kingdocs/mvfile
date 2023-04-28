import os
import shutil

# 原始目录路径
# src_dir = r'D:\Temp\filetest\XX000002'
src_dir = input("请输入源目录路径：")

# 目标目录路径
# dst_dir = r'D:\Temp\filetest\t'
dst_dir = input("请输入目标目录路径：")

print("正在运行……")
# 遍历原始目录
# 遍历原始文件夹下的所有子目录
for root, dirs, files in os.walk(src_dir):
    # 如果当前目录没有子目录，则说明是最后一层子目录
    if not dirs:
        # 获取当前目录的相对路径
        rel_path = os.path.relpath(root, src_dir)
        # 拼接目标文件夹路径和当前目录的相对路径
        substrings = rel_path.split("\\")
        last_substring = substrings[-1]
        dst_path = os.path.join(dst_dir, last_substring)
        # 创建目标文件夹
        os.makedirs(dst_path, exist_ok=True)
        # 遍历当前目录下的所有文件
        for file in files:
            # 拼接当前文件的路径
            src_file = os.path.join(root, file)
            # 拼接目标文件的路径
            dst_file = os.path.join(dst_path, file)
            # 移动文件到目标文件夹
            shutil.move(src_file, dst_file)