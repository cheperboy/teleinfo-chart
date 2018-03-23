# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division

import time
from datetime import datetime, timedelta
from flask import current_app
from app import db

def dump_timestamp(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return int(time.mktime(value.timetuple())*1000)

def totimestamp(value):
    return time.mktime(value.timetuple())

class TeleinfoMinute(db.Model):
    __bind_key__ = 'teleinfo_minute'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    base = db.Column(db.Integer)
    papp = db.Column(db.Integer)
    iinst1 = db.Column(db.Float)
    iinst2 = db.Column(db.Float)
    iinst3 = db.Column(db.Float)

    def __repr__(self):
        return self.timestamp
        
class TeleinfoHour(db.Model):
    __bind_key__ = 'teleinfo_hour'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    base = db.Column(db.Integer)
    papp = db.Column(db.Integer)
    iinst1 = db.Column(db.Float)
    iinst2 = db.Column(db.Float)
    iinst3 = db.Column(db.Float)

    def __repr__(self):
        return self.timestamp
        
    
class Teleinfo(db.Model):
    __bind_key__ = 'teleinfo'
#    __tablename__ = 'teleinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    base = db.Column(db.Integer)
    papp = db.Column(db.Integer)
    iinst1 = db.Column(db.Integer)
    iinst2 = db.Column(db.Integer)
    iinst3 = db.Column(db.Integer)
        
    def __init__(self, timestamp, base=1, papp=1, iinst1=1, iinst2=1, iinst3=1):
        self.timestamp = timestamp
        self.base = base
        self.papp = papp
        self.iinst1 = iinst1
        self.iinst2 = iinst2
        self.iinst3 = iinst3

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<Teleinfo {0} {1} : {2}, {3}>'.format(self.id, self.timestamp, self.base, self.papp)

    def tolist(self):
        """Return Object data in list format"""
        return [
            dump_timestamp(self.timestamp),
            self.base,
            self.papp,
            self.iinst1,
            self.iinst2,
            self.iinst3,
            self.id
       ]

    def papptolist(self):
        """Return Object data in list format"""
        return [
            dump_timestamp(self.timestamp),
            self.papp,
       ]

    def alltolist(self):
        mylist = list()
        for entry in self.query.order_by(Teleinfo.timestamp).limit(500).all():
            mylist.append(entry.tolist())
        return mylist
       
    @staticmethod
    def all_byday(self, num_hours):
        mylist = list()
        ts = datetime.now() - timedelta(hours=num_hours)
        for entry in self.query\
                         .order_by(Teleinfo.timestamp)\
                         .filter(Teleinfo.timestamp >= ts)\
                         .all():
            mylist.append(entry.tolist())
        return mylist
    
