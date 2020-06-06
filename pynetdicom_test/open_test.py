#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import logging

from pynetdicom import AE, evt
from pynetdicom.sop_class import VerificationSOPClass

LOGGER = logging.getLogger('pynetdicom')

def handle_open(event):
    """Print the remote's (host, port) when connected."""
    msg = 'Connected with remote at ({})'.format(event.address)
    LOGGER.info(msg)

handlers = [(evt.EVT_CONN_OPEN, handle_open)]

ae = AE()
ae.add_requested_context(VerificationSOPClass)
assoc = ae.associate('', 11112, evt_handlers=handlers)

if assoc.is_established:
    assoc.release()

