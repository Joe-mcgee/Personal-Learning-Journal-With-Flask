from peewee import *

DATABASE = SqliteDatabase('journal.db')


class Entry(Model):
    title = CharField()
    date = DateField()
    timeSpent = CharField()
    whatILearned = CharField()
    ResourcesToRemember = CharField()

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)
    DATABASE.close()