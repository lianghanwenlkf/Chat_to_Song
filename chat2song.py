import random
import pandas as pd
from matplotlib import font_manager, pyplot as plt


# 批量读取聊天记录CSV文件并处理数据
def process_csv(files, target_str):
    result = []

    for file in files:
        # 读取 CSV 文件
        df = pd.read_csv(file)

        # 遍历每一行数据
        for index, row in df.iterrows():
            # 检查第三列（消息类型）和第十列（微信备注名）的条件
            if row[2] == 1 and row[9] == target_str:
                # 保存第八列（消息内容）的内容到结果列表
                result.append(str(row[7]).replace('\n', ' '))

    return result


# 读取歌词文件并将每一行添加到列表
def process_txt(lyrics_files):
    result = []

    for file_path in lyrics_files:
        try:
            # 打开文件进行读取
            with open(file_path, 'r', encoding='utf-8') as file:
                # 逐行读取文件，并添加到列表中
                lines = file.readlines()
            # 去掉每行的换行符
            lines = [line.strip() for line in lines]
            result.append(lines)
        except FileNotFoundError:
            print(f"文件 {file_path} 未找到.")
        except Exception as e:
            print(f"发生错误: {e}")

    return result


# 查找聊天记录中是否包含歌词字符
def find_elements_in_lyrics(lyrics_list, data_list, lyrics_files, output_path, pic_path, font_prop):
    content = ''
    for i, lyrics in enumerate(lyrics_list):
        content += (f'======================================\n'
                    f'第{i + 1}首歌：{lyrics_files[i][40:-4]}\n'
                    f'======================================')
        count_x = []
        count_y = []
        lyric_total = 0
        char_total = 0
        for j, lyric in enumerate(lyrics):
            content += f'\n\n歌词{j+1}：{lyric}'
            lyric_length = 0
            char_length = 0
            count_x.append(j+1)
            for char in lyric:
                if char != " ":
                    lyric_length += 1
                    char_results = []
                    for data in data_list:
                        if char in data:
                            char_results.insert(0, data.replace(char, f"【{char}】"))
                    if len(char_results) > 0:
                        content += f'\n{random.choice(char_results)}'
                        char_length += 1
                    else:
                        content += f'\n【{char}】'
            count_y.append(char_length/lyric_length)
            lyric_total += lyric_length
            char_total += char_length
        content += f'\n\n\n'

        # 创建折线图
        plt.plot(count_x, count_y, marker='o', color='b', linestyle='-', label='Line')

        # 添加标题和标签
        plt.xlabel('歌词句数', fontproperties=font_prop)
        plt.ylabel('聊天记录覆盖率', fontproperties=font_prop)

        # 显示图例
        plt.legend()

        # 保存图像到文件
        plt.savefig(pic_path + f'_{lyrics_files[i][40:-4]}.png')
        plt.clf()

        print(f'第{i + 1}首歌：{lyrics_files[i][40:-4]}   歌词总字数：{lyric_total}   聊天记录覆盖的字数：{char_total}   '
              f'覆盖率：{round(char_total/lyric_total*100, 2)}%')

    try:
        # 以写模式打开文件，如果文件不存在会自动创建
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print("文件保存成功")
    except Exception as e:
        print(f"保存文件时发生错误: {e}")


def main():
    # 本地中文字体路径
    font_path = r'D:\GameBoxPro\2项目\Code\WebUpdate\fonts\微软雅黑.ttf'
    font_prop = font_manager.FontProperties(fname=font_path)

    # 目标对象微信备注名
    target_string = '张翼'

    # 微信聊天记录导出文件路径
    csv_files = [
        r'D:\GameBoxPro\2项目\Code\WebUpdate\data\张翼.csv',
        r'D:\GameBoxPro\2项目\Code\WebUpdate\data\pico_park_gogogo!.csv',
        r'D:\GameBoxPro\2项目\Code\WebUpdate\data\乒乓集结号！.csv',
        r'D:\GameBoxPro\2项目\Code\WebUpdate\data\南京赴川西新质生产力发展考察团.csv',
        r'D:\GameBoxPro\2项目\Code\WebUpdate\data\大草坪的快乐聚会.csv',
        r'D:\GameBoxPro\2项目\Code\WebUpdate\data\校庆行动小组.csv',
        r'D:\GameBoxPro\2项目\Code\WebUpdate\data\歌友会.csv',
        r'D:\GameBoxPro\2项目\Code\WebUpdate\data\今晚鹅鸭杀.csv'
    ]

    # 歌词文件路径
    lyrics_files = [
        r'D:\GameBoxPro\2项目\Code\WebUpdate\lyrics\一人行.txt',
        r'D:\GameBoxPro\2项目\Code\WebUpdate\lyrics\一生所爱.txt',
        r'D:\GameBoxPro\2项目\Code\WebUpdate\lyrics\银河系梦游指南.txt'
    ]

    # 查找结果文件保存路径
    output_path = rf'D:\GameBoxPro\2项目\Code\WebUpdate\lyrics_output\{target_string}.txt'
    # 聊天记录覆盖率图表保存路径
    pic_path = rf'D:\GameBoxPro\2项目\Code\WebUpdate\lyrics_output\{target_string}'

    # 获取处理结果
    data_list = process_csv(csv_files, target_string)
    lyrics_list = process_txt(lyrics_files)

    # 查找歌词中包含的元素
    find_elements_in_lyrics(lyrics_list, data_list, lyrics_files, output_path, pic_path, font_prop)


if __name__ == '__main__':
    main()
