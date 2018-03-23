# -*- coding: utf-8 -*-
from __future__ import absolute_import
from app import create_app
import config

def run():
    app = create_app()
    app.run(host="0.0.0.0", port=config.PORT, debug=True, threaded=True)

if __name__ == '__main__':
    run()
