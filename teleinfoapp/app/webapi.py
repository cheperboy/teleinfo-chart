# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Blueprint, jsonify, make_response
import json, time
from datetime import datetime, timedelta
from random import random

from app.auth import auth
from app.models import Teleinfo

webapi = Blueprint("webapi", __name__, url_prefix='/webapi')

@webapi.route('/conso_by_date/<int:year>/<int:month>/<int:day>', methods=['GET'])
def conso_by_date(year, month, day):
    entries = list()
    ts = datetime.now() - timedelta(hours=25)
    for entry in Teleinfo.query\
                     .order_by(Teleinfo.timestamp)\
                     .filter(Teleinfo.timestamp >= ts)\
                     .all():
        entries.append(entry.papptolist())
    return jsonify(entries), 200

@webapi.route('/fakedata', defaults={'hours': 1}, methods=['GET'])
@webapi.route('/fakedata/<int:hours>', methods=['GET'])
def fakedata(hours):
    entries = Teleinfo.all_byday(Teleinfo, hours)
    return jsonify(entries), 200

@webapi.route('/fakedataall', methods=['GET'])
def fakedataall():
    entries = Teleinfo.alltolist(Teleinfo)
    ts = datetime.now() - timedelta(minutes=len(entries))
    for entry in entries:
        ts = ts + timedelta(minutes=1)
        entry[0] = time.mktime(ts.timetuple())*1000
    return jsonify(entries), 200

@webapi.route('/live.json')
def live_json():
    # Create a PHP array and echo it as JSON
    data = [time.time() * 1000, random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

