import sys

HELP_MESSAGE = 'type in: python EhviewerBackup.py -i <ehviewer download directory> -o <backup directory>'

# 输出类型
ZIP_MESSAGE_TYPE = 1
ZIP_MESSAGE = 'zip'

COPY_MESSAGE_TYPE = 2
COPY_MESSAGE = 'copy'

# 输出类型: 输出消息
MESSAGE_DICT = {ZIP_MESSAGE_TYPE: ZIP_MESSAGE,
                COPY_MESSAGE_TYPE: COPY_MESSAGE}

# 开始消息
BEGIN_MESSAGE = '================ {} progress begin ================'
# 进度条消息
PROGRESS_BAR_MESSAGE = '{} progress:{}/{}, current directory:{}'
SKIP_DIR_NOT_MANAGE_MESSAGE = PROGRESS_BAR_MESSAGE + ', is not manga directory, skip'
SKIP_AUTHOR_NOT_COPY_MESSAGE = PROGRESS_BAR_MESSAGE + ', author do not need to copy, skip'
MANGA_EXIST_NOT_COPY_MESSAGE = PROGRESS_BAR_MESSAGE + ', manga exist, do not need to copy, skip'

DIR_NOT_MANAGE = 1
AUTHOR_NOT_COPY = 2
MANGA_EXIST_NOT_COPY = 3

PROGRESS_BAR_SKIP_MESSAGE_DICT = {DIR_NOT_MANAGE: SKIP_DIR_NOT_MANAGE_MESSAGE,
                                  AUTHOR_NOT_COPY: SKIP_AUTHOR_NOT_COPY_MESSAGE,
                                  MANGA_EXIST_NOT_COPY: MANGA_EXIST_NOT_COPY_MESSAGE}
# 结束消息
END_MESSAGE = '================ {} progress finish ================'


# print help message and exit
# def print_help_message():
#     print(HELP_MESSAGE)
#     sys.exit(2)

# get input parameters
# def get_parameters(argv):
#     input_dir = ''
#     output_dir = ''
#     opts = []
#     try:
#         opts, args = getopt.getopt(argv[1:], 'hi:o:', ['help', 'input=', 'output='])
#     except getopt.GetoptError:
#         print_help_message()
#     for opt, arg in opts:
#         if opt in ('-h', '--help'):
#             print_help_message()
#         elif opt in ('-i', '--input'):
#             input_dir = arg
#         elif opt in ('-o', '--output'):
#             output_dir = arg
#
#     if not input_dir.strip() or not os.path.exists(input_dir):
#         print('input directory not found')
#         sys.exit(2)
#
#     if not output_dir.strip():
#         print('output directory not found')
#         sys.exit(2)
#
#     return input_dir, output_dir


# 输出进度条
def print_progress_bar_message(message_type, name, now, total, skip_type=0):
    message_type = MESSAGE_DICT[message_type]
    # if now == 1:
    #     # 开始
    #     print(BEGIN_MESSAGE.format(message_type))
    # print('\r', end='')

    # 进度条类型
    process_bar_message = PROGRESS_BAR_MESSAGE
    if skip_type != 0:
        process_bar_message = PROGRESS_BAR_SKIP_MESSAGE_DICT[skip_type]
    print(process_bar_message.format(message_type, now, total, name))

    # if now != total:
    #     print(process_bar_message.format(message_type, now, total, name), end='', flush=True)
    # else:
    #     # 结束
    #     print(process_bar_message.format(message_type, now, total, name), flush=True)
    #     print(END_MESSAGE.format(message_type))
