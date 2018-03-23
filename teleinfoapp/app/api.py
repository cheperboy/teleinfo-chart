import os
import sys
#basedir = os.path.abspath(os.path.dirname(__file__))
#sys.path.append(os.path.join(basedir,'app'))
from app.models import Teleinfo
from app import db
from datetime import datetime

from flask import Blueprint
import json, time
from datetime import datetime, timedelta
from random import random

api = Blueprint("api", __name__, url_prefix='/api')


def createti(timestamp, base, papp, iinst1, iinst2, iinst3):
    ret = 'NOK'
    try:
        entry = Teleinfo(datetime.now())
        db.session.add(entry)
        db.session.commit()
    except RuntimeError,e:
        print e.message
"""
    teleinfo = Teleinfo(
        timestamp,
        1,
        papp,
        iinst1,
        iinst2,
        iinst3
    )
    try:
        db.session.add(teleinfo)
        db.session.commit()
        ret = True
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print "Error: %s" % e
    finally:
        return ret
"""
#except exc.SQLAlchemyError as e:
#ret = False

#print createti(datetime.now(), 3, 2, 2, 2, 3)