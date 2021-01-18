#coding=utf-8
from functools import wraps
import pymysql

class MYSQL():
    connect=None

    def _Connect(self,):
        self.connect = pymysql.connect("localhost", "root", "123456", "spider")

    def _CheckStatus(func):
        @wraps(func)
        def WrapFunc(self,*args,**kwargs):
            if not self.connect:
                print('数据库连接')
                self._Connect()

            res=func(self,*args,**kwargs)
            print('数据库断开')
            self.connect.close()
            return res
        return WrapFunc
    @_CheckStatus
    def Creat(self):
        cursor = self.connect.cursor()
        sqlCmd = r"""
        CREATE TABLE  `douban`(
           `topicId` INT NOT NULL AUTO_INCREMENT ,
           `title` text,
           `website` varchar(100),
           `author` text,
           `authorsite` varchar(100),
           PRIMARY KEY (`topicId`),
           UNIQUE KEY `repeat` (`website`)
        ) character set = utf8;
        """
        print(sqlCmd)
        cursor.execute(sqlCmd)
        data = cursor.fetchall()
        print(list(data))


    @_CheckStatus
    def Insert(self,content):
        cursor = self.connect.cursor()
        # sqlCmd = r"""
        # Insert into douban (title,website,author,authorsite) values
        # ({})
        # """.format(content)
        sqlCmd = r"""
        Insert ignore into  douban (title,website,author,authorsite) values
        ({})
        """.format(content)
        print(sqlCmd)
        cursor.execute(sqlCmd)
        self.connect.commit()
        data = cursor.fetchall()
        print(list(data))


    @_CheckStatus
    def ShowALl(self):
        cursor = self.connect.cursor()
        sqlCmd = r"""
                select * from douban;
                """
        print(sqlCmd)
        cursor.execute(sqlCmd)
        # self.connect.commit()
        data = cursor.fetchall()
        print(list(data))


class STRINGPROCESS():



    def __init__(self,astr):
        self.sourceStr=astr
        self.resultStr=astr


    def DropWhiteChar(self):
        self.resultStr=self.resultStr.replace('\n','')
        self.resultStr=self.resultStr.strip()

    def OutPut(self):

        return  self.resultStr


if __name__=='__main__':
    a=MYSQL()
    # a.Creat()
    a.ShowALl()
    # a.Insert("'1','2','3','4'")