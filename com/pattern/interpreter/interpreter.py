#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

class AbstractExpression(object):

    def interpreter(self, context):
        pass


class TerminalExpression(AbstractExpression):

    def interpreter(self, context):
        print "terminal",context


class NotTerminalExpression(AbstractExpression):

    def interpreter(self, context):
        print "non terminal",context


class Context(object):

    def __init__(self):
        self.name = ""

if __name__ == "__main__":
    context = Context()
    context.name = 'Andy'
    arr_list = [NotTerminalExpression(),TerminalExpression(),TerminalExpression()]
    for entry in arr_list:
        entry.interpreter(context)