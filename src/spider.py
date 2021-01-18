#coding=utf-8
import requests
from lxml import etree

from interface import MYSQL,STRINGPROCESS

headers={'User-Agent': 'Safari/534.50'}

response=requests.get('https://www.douban.com/group/beijingzufang/',headers=headers,verify=False)


tree=etree.HTML(response.content)


# nodeTree=tree.xpath('//a[@href]')
# nodeTree=tree.xpath('/html/body/div[3]/')
# nodeTree=tree.xpath("//div[@id='content']/")
nodeTree=tree.xpath("//table//tr")
# nodeTree=tree.xpath('a')

def StringDetail(astr):
    STR=STRINGPROCESS(astr)
    STR.DropWhiteChar()
    return STR.OutPut()

def StoryData(content):
    MY=MYSQL()
    MY.Insert(content)



n=0
for node in nodeTree:
    contentNode=node.xpath(".//a")
    if len(contentNode)==2:
        TopicTitle=contentNode[0].text
        TopicHerf=contentNode[0].attrib['href']
        AuthorName=contentNode[1].text
        AuthorHerf=contentNode[1].attrib['href']
    else:
        continue

    TopicTitle=StringDetail(TopicTitle)
    AuthorName=StringDetail(AuthorName)

    StoryData("'{}','{}','{}','{}'".format(TopicTitle,TopicHerf,AuthorName,AuthorHerf))


    # b=AuthorHerf['href']
    # a=dict(AuthorHerf)
    # nodeText=node.text
    # nodeHref=node.attrib


    n+=1
    print(n)
    # print(n,nodeText)
    # print('herf:',nodeHref)
# print(response.status_code)
# print(response.text)
