# -*- coding: utf-8 -*-
import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        db=pymysql.connect(host="localhost",user="root",password="123456",db="dd")
        for i in range(0,len(["title"])):
            #获取数据库行游标
            cur=db.cursor()
            title=item["title"][i]
            link=item["link"][i]
            comment=item["comment"][i]
            sql_insert="insert into books(title,link,comment) values('"+title+"','"+link+"','"+comment+"')"
            try:
                #提交数据库sql语句
                cur.execute(sql_insert)
                db.commit()
                print(title+"插入成功")
                print(link+"插入成功")
                print(comment+"插入成功")
            except Exception as e:
                db.rollback()
            finally:
                db.close()
        return item
