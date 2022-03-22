import os

import pymysql


class Mysql(object):

    def __init__(self, config_database):
        try:

            self.config_database = config_database
            self.connect = pymysql.connect(host=config_database["host"],
                                           user=config_database["user"],
                                           port=config_database["port"],
                                           password=config_database["password"],
                                           database=config_database["database"])

            self.cursor = self.connect.cursor()
            self.cursor.execute(f"USE {config_database['database']}")

        except Exception as error:
            print(f"---------数据库连接失败:{error}--------")
            os.system('pause')

        print("---------数据库连接成功---------")

    def get_index_dict(self):
        index_dict = dict()
        index = 0
        for desc in self.cursor.description:
            index_dict[desc[0]] = index
            index = index + 1
        return index_dict

    def get(self):
        get_sql = f"SELECT `id`, `guid`, `post_content`, `post_type`, `post_name`  FROM `{self.config_database['table']}` WHERE `post_status` = 'publish' AND `post_type` = 'post' ORDER BY id DESC"
        self.cursor.execute(get_sql)
        data = self.cursor.fetchall()
        index_dict = self.get_index_dict()
        res = []
        for i in data:
            resi = dict()
            for ii in index_dict:
                resi[ii] = i[index_dict[ii]]
            res.append(resi)
        return res

    def count(self):
        count_sql = f"SELECT COUNT(*) FROM `{self.config_database['table']}` WHERE `post_status` = 'publish' AND `post_type` = 'post'"
        self.cursor.execute(count_sql)
        data = self.cursor.fetchone()
        return data[0]

    def update(self, ids):
        update_sql = f"UPDATE {self.config_database['table']} SET `post_status` = 'pending' Where `id` in {tuple(ids)}"
        self.cursor.execute(update_sql)
        self.connect.commit()
