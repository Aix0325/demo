# -*- coding: utf-8 -*-
import os
import yaml

from Mysql import Mysql


def main():
    config_database = read_database_configuration('./config.yaml')
    remain_links = read_links_configuration('./remain_links.txt')
    mysql = Mysql(config_database)
    count = mysql.count()
    data = mysql.get()

    print(f'--------------------需要处理的条数:{count}----------------------')

    ids = []
    for item in data:
        full_name = config_database['domain'] + item['post_name'] + ".html"
        print(full_name)
        if full_name in remain_links:
            ids.append(item['id'])

    if len(ids) == 0:
        print("-------------------------没有需要修改的数据-------------------------------")

    else:
        print(f'---------------------待改变状态的ID列表:{ids}------------------------')
        mysql.update(ids)
        print(f'-------------------更新成功，修改了{len(ids)}条数据-------------------')


def read_database_configuration(path):
    with open(path, 'r', encoding='utf-8') as f:
        try:
            file_content = f.read()
            database_config = yaml.load(file_content, yaml.FullLoader)
            return database_config
        except FileNotFoundError as error:
            print("---------config.yaml 不存在" + error + "---------")
            os.system('pause')


def read_links_configuration(path):
    links_config = []
    with open(path, "r", encoding='utf-8') as f:
        try:
            file_lines = f.readlines()
            for line in file_lines:
                line = line.replace('\n', '')
                links_config.append(line)
            return links_config
        except FileNotFoundError as error:
            print("---------remain_links.txt 不存在" + error + "---------")
            os.system('pause')


if __name__ == '__main__':
    main()
    os.system('pause')
