# import os
# import re
# import shutil
# import sys
# import getopt
#
# HELP_MESSAGE = "type in: python EhviewerBackup.py -i <ehviewer download directory> -o <backup directory>"
# PROGRESS_BAR_MESSAGE = "progress:{}/{}, current directory:{}"
#
#
# # print help message and exit
# def print_help_message():
#     print(HELP_MESSAGE)
#     sys.exit(2)
#
#
# # get input parameters
# def get_parameters(argv):
#     input_dir = ''
#     output_dir = ''
#     opts = []
#     try:
#         opts, args = getopt.getopt(argv[1:], "hi:o:", ["help", "input=", "output="])
#     except getopt.GetoptError:
#         print_help_message()
#     for opt, arg in opts:
#         if opt in ("-h", "--help"):
#             print_help_message()
#         elif opt in ("-i", "--input"):
#             input_dir = arg
#         elif opt in ("-o", "--output"):
#             output_dir = arg
#
#     if not input_dir.strip() or not os.path.exists(input_dir):
#         print("input directory not found")
#         sys.exit(2)
#
#     if not output_dir.strip():
#         print("output directory not found")
#         sys.exit(2)
#
#     return input_dir, output_dir
#
#
# # print progress bar
# def progress_bar(name, now, total):
#     print("\r", end="")
#     print(PROGRESS_BAR_MESSAGE.format(now, total, name), end="", flush=True)
#
#
# # backup files
# def backup(argv):
#     input_dir, output_dir = get_parameters(argv)
#     dirs = os.listdir(input_dir)
#     length = len(dirs)
#     i = 0
#
#     print("=========================== start ===========================")
#     for manga_name in dirs:
#         # when author not found, managa copy to other directory
#         author_name = "other"
#         source_manga_path = os.path.join(input_dir, manga_name)
#         i += 1
#         progress_bar(source_manga_path, i, length)
#
#         # match first square bracket
#         square_bracket_list = re.findall(r"[/[](.*?)]", manga_name)
#         if len(square_bracket_list) > 0:
#             match_str = square_bracket_list[0]
#             # match first parentheses
#             parentheses_list = re.findall(r"[/(](.*?)[/)]", match_str)
#             if len(parentheses_list) > 0:
#                 author_name = parentheses_list[0]
#             else:
#                 author_name = match_str
#
#         # author directory
#         author_path = os.path.join(output_dir, author_name)
#         # manga directory
#         manga_path = os.path.join(author_path, manga_name)
#
#         # if exist same manga then remove
#         if os.path.exists(manga_path):
#             shutil.rmtree(manga_path)
#         shutil.copytree(source_manga_path, manga_path)
#
#     print("\r")
#     print("===========================  end  ===========================")
#
#
# if __name__ == "__main__":
#     backup(sys.argv)
