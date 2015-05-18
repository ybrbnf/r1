#!/usr/bin/python
#coding: utf-8
import datetime
date=datetime.date.today()
month=date.month
day=date.day
date=date.strftime('%d.%m')
class NewYearError(Exception): pass
try:
    if month!=12 and day!=31:
        raise NewYearError(date)
except NewYearError, date:
    print 'Сегодня {}. Нового Года не будет :('.format (date)
