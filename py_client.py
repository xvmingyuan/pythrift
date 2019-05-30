# coding:utf-8

__author__ = '作者'
from py.thrift.generated import PersonService
from py.thrift.generated import ttypes

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol


try:
    tSocket = TSocket.TSocket('localhost', 8899)
    tSocket.setTimeout(600)

    transport = TTransport.TFramedTransport(tSocket)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = PersonService.Client(protocol)

    transport.open()

    person  = client.getPersonByUsername("Python 汤姆".decode('utf-8'))

    print person.username
    print person.age
    print person.married

    print '-----------'

    person2 = ttypes.Person()
    person2.username = 'Python 杰克'.decode('utf-8')
    person2.age = 18
    person2.married = False

    client.savePerson(person2)

    transport.close()
except Thrift.TException, tx:
    print '%s' % tx.message
