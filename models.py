from peewee import *

identify = open("parameter.txt", "r")
login = identify.readlines()
identify.close()

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase(login[0], user=login[0])


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class School(BaseModel):
    name = CharField()


class City(BaseModel):
    name = CharField()
    related_school = ForeignKeyField(School, related_name="cities")


class Mentor(BaseModel):
    name = CharField()
    related_school = ForeignKeyField(School, related_name="workplaces")


class Applicant(BaseModel):
    name = CharField()
    city = ForeignKeyField(City, related_name="homes")
    status = CharField()
    code = CharField()
    school = ForeignKeyField(School, related_name="registered_school")


class InterviewSlot(BaseModel):
    start = DateTimeField()
    end = DateTimeField()
    reserved = BooleanField()
    mentor = ForeignKeyField(Mentor, related_name="mentors")


class Interview(BaseModel):
    applicant = ForeignKeyField(Applicant, related_name="interviews")
    interviewslot = ForeignKeyField(InterviewSlot, related_name="interviews")
