#coding=utf-8
from functools import wraps
import pymysql

class MYSQL():
    connect=None

    def _Connect(self,):
        self.connect = pymysql.connect(host="172.17.0.2", user="root", password="123456", database="spider")
        # self.connect = pymysql.connect(host="localhost", user="root", password="123456", database="spider")

    # def __init__(self, host=None, user=None, password="",
    #              database=None, port=0, unix_socket=None,
    #              charset='', sql_mode=None,
    #              read_default_file=None, conv=None, use_unicode=None,
    #              client_flag=0, cursorclass=Cursor, init_command=None,
    #              connect_timeout=10, ssl=None, read_default_group=None,
    #              compress=None, named_pipe=None,
    #              autocommit=False, db=None, passwd=None, local_infile=False,
    #              max_allowed_packet=16 * 1024 * 1024, defer_connect=False,
    #              auth_plugin_map=None, read_timeout=None, write_timeout=None,
    #              bind_address=None, binary_prefix=False, program_name=None,
    #              server_public_key=None):


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
        Insert ignore into  douban (title,website,author,authorsite,replytime,replycount) values
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