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


# i = 1
#
# while i < 1000000:
#     CustProfile.create(cust_name = 'kafka_test', cust_card = 'debit_visa')
#     i += 1
#
# print(CustProfile.select().count())

