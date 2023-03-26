import os
import re
import shutil

from conf.Config import Config
from util import PrintUtil


def backup():
    if not os.path.isdir(input_dir):
        print(input_dir + ' is not directory')
        return

    manga_dir_list = os.listdir(input_dir)
    length = len(manga_dir_list)
    i = 0

    for manga_name in manga_dir_list:
        i += 1
        source_manga_path = os.path.join(input_dir, manga_name)

        # 判断是否漫画
        if not re.match(r'[0-9]+-', manga_name):
            PrintUtil.print_progress_bar_message(PrintUtil.COPY_MESSAGE_TYPE, source_manga_path, i, length, PrintUtil.DIR_NOT_MANAGE)
            continue

        # 默认文件夹名字 - other
        author_name = 'other'
        # 匹配第一个中括号
        square_bracket_list = re.findall(r'[/[](.*?)]', manga_name)
        if len(square_bracket_list) > 0:
            match_str = square_bracket_list[0]
            # 匹配中括号内的第一个小括号, 如果有则里面是作者的名字, 如果没有则取中括号的内容作为作者名
            parentheses_list = re.findall(r'[/(](.*?)[/)]', match_str)
            if len(parentheses_list) > 0:
                author_name = parentheses_list[0]
            else:
                # TODO 可能会和FANBOX之类的冲突
                author_name = match_str

        # 如果不是全量备份且作者没在备份名单内(此处嵌套一层, 忽略大小写), 则不备份
        if not (config.is_backup_all or author_name.lower() in config.author_dict.keys()):
            PrintUtil.print_progress_bar_message(PrintUtil.COPY_MESSAGE_TYPE, source_manga_path, i, length,  PrintUtil.AUTHOR_NOT_COPY)
            continue

        # 拼接输出路径
        for output_dir in config.output_dir_list:
            # 获取当前作者的保存路径
            author_path = config.author_dict[author_name.lower()] \
                if author_name.lower() in config.author_dict \
                else author_name.lower()
            author_path = os.path.join(output_dir, author_path)
            # 具体漫画保存路径
            manga_path = os.path.join(author_path, manga_name)
            # 判断是否覆盖复制
            if os.path.exists(manga_path):
                if not config.is_overwrite:
                    PrintUtil.print_progress_bar_message(PrintUtil.COPY_MESSAGE_TYPE, source_manga_path, i, length, PrintUtil.MANGA_EXIST_NOT_COPY)
                    continue
                else:
                    shutil.rmtree(manga_path)
            shutil.copytree(source_manga_path, manga_path)
            PrintUtil.print_progress_bar_message(PrintUtil.COPY_MESSAGE_TYPE, source_manga_path, i, length)

        # 备份完删除源文件
        if config.is_delete_after_backup:
            shutil.rmtree(source_manga_path)


if __name__ == '__main__':
    print('=============== backup begin ===============')
    config = Config()
    for input_dir in config.input_dir_list:
        backup()
    print('=============== backup finish ===============')
