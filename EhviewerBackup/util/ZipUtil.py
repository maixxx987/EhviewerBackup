import os
import zipfile


# 压缩多个文件
def zip_multi_dir(file_path_list):
    with zipfile.ZipFile('out.zip', 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for file_path in file_path_list:
            zip_dir(file_path, zip_file)


# 递归判断是否子文件夹
def zip_dir(file_path, zip_file):
    if os.path.isdir(file_path):
        child_files = os.listdir(file_path)
        for child_file in child_files:
            child_file_path = file_path + os.sep + child_file
            if os.path.isdir(child_file_path):
                zip_dir(child_file_path, zip_file)
            else:
                zip_file.write(child_file_path)
    else:
        zip_file.write(file_path)