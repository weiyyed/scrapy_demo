# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.utils import spider
from scrapy.utils.project import get_project_settings

class Boss(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position = scrapy.Field(serializer=str)  # 招聘职位
    salary = scrapy.Field(serializer=str)  # 薪资
    addr = scrapy.Field(serializer=str)  # 工作地址
    years = scrapy.Field(serializer=str)  # 工作年限
    education = scrapy.Field(serializer=str)  # 学历
    company = scrapy.Field(serializer=str)  # 招聘公司
    industry = scrapy.Field(serializer=str)  # 行业
    nature = scrapy.Field(serializer=str)  # 性质：是否上市
    scale = scrapy.Field(serializer=str)  # 规模：人数
    publisher = scrapy.Field(serializer=str)  # 招牌者
    publisherPosition = scrapy.Field(serializer=str)  # 招聘者岗位
    publishDateDesc = scrapy.Field(serializer=str)  # 发布时间
class BossItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_title = scrapy.Field()  # 岗位
    compensation = scrapy.Field()  # 薪资
    company = scrapy.Field()  # 公司
    address = scrapy.Field()  # 地址
    seniority = scrapy.Field()  # 工作年薪
    education = scrapy.Field()  # 教育程度
    company_type = scrapy.Field()  # 公司类型
    company_finance = scrapy.Field()  # 融资
    company_quorum = scrapy.Field()  # 公司人数
class ToutiaoItem(scrapy.Item):
    url=scrapy.Field()
class MingyanItem(scrapy.Item):
    description=scrapy.Field()
