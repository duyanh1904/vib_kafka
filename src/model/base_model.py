from peewee import *

db = MySQLDatabase('my_app', user='root', passwd='test')

class BaseModel(Model):
    class Meta:
        database = db

class CustProfile(BaseModel):
    cust_id = AutoField()
    cust_name = CharField()
    cust_card = CharField()

    class Meta:
        table_name = 'cust_profile'

db.create_tables([CustProfile])

#
# i = 1
#
# while i < 10000:
#     CustProfile.create(cust_name = 'bayner', cust_card = 'visa')
#     i += 1

# print(CustProfile.select().count())

