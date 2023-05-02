import os

import yaml


# 配置类
class Config:
    # 输入目录
    input_dir_list = []
    # 输出目录
    output_dir_list = []
    # 是否覆盖
    is_overwrite = False
    # 是否在复制前先压缩全部文件
    is_zip_all_before_backup = True
    # todo 是否复制完后压缩对应漫画
    is_zip_single_after_backup = False
    # 是否备份全部
    is_backup_all = False
    # 是否备份完后删除已备份的文件
    is_delete_after_backup = False
    # 作者(包含别名)及对应的输出目录
    author_dict = {}

    def __init__(self):
        self.load_config()

    def load_config(self):
        yaml_config = yaml.load(open('conf' + os.sep + 'config.yaml', 'r', encoding='utf-8').read(),
                                Loader=yaml.FullLoader)
        self.load_common_config(yaml_config['common'])
        self.load_authors(yaml_config['authors'])
        self.load_output_dir()

    # 读取普通配置
    def load_common_config(self, common_config):
        self.input_dir_list = common_config['input_dir_list']
        self.output_dir_list = common_config['output_dir_list']
        self.is_overwrite = common_config['is_overwrite']
        self.is_zip_all_before_backup = common_config['is_zip_all_before_backup']
        self.is_zip_single_after_backup = common_config['is_zip_single_after_backup']
        self.is_backup_all = common_config['is_backup_all']
        self.is_delete_after_backup = common_config['is_delete_after_backup']

    # 读取作者及输出目录的配置(存的都是小写)
    def load_authors(self, authors):
        for author_name, author_attr in authors.items():
            # 判断有没有写输出文件夹名字
            if author_attr is not None:
                out_put_dir = author_attr['out_put_dir'] if 'out_put_dir' in author_attr else author_name
                self.author_dict[author_name.lower()] = out_put_dir
                # 判断有没有别名
                if 'alias' in author_attr and len(author_attr['alias']) > 0:
                    self.author_dict.update([(alias.lower(), out_put_dir) for alias in author_attr['alias']])
            else:
                out_put_dir = author_name
                self.author_dict[author_name.lower()] = out_put_dir
            print(author_name + ": " + out_put_dir)

    # 读取输出目录文件夹, 获取需要备份的作者名
    def load_output_dir(self):
        for output_dir in self.output_dir_list:
            file_list = os.listdir(output_dir)
            self.author_dict.update(
                [(file_name, file_name) for file_name in file_list if file_name not in self.author_dict and os.path.isdir(os.path.join(output_dir, file_name))])

# if __name__ == '__main__':
#     c = Config()
#     print(c.author_dict)
