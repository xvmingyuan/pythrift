# coding:utf-8

__author__ = '作者'

from py.thrift.generated import ttypes

class PersonServiceImpl:
    def getPersonByUsername(self,username):
        print("Got client param: "+username)

        person = ttypes.Person()
        person.username = username
        person.age = 24
        person.married = False

        return person
    def savePerson(self,person):
        print 'Got client param'

        print person.username
        print person.age
        print person.married
        print '------------'