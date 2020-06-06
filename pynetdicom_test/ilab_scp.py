#!/usr/bin/env python3
# -*- coding:utf-8 _-*-

import logging
from pynetdicom import (
    AE, debug_logger, evt, AllStoragePresentationContexts,
    ALL_TRANSFER_SYNTAXES
)
from pynetdicom.sop_class import VerificationSOPClass

debug_logger()
# logger = logging.getLogger('pynetdicom')
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("storage_scu_log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)

def handle_open(event):
    """Print """
    msg = 'Connected with remote at {}'.format(event.address)
    logger.info(msg)

def handle_accepted(event, arg1, arg2):
    logger.info("Extra args: '{}' and '{}'".format(arg1, arg2))

def handle_store(event):
    """Handle EVT_C_STORE events."""
    ds = event.dataset
    ds.file_meta = event.file_meta
    ds.save_as(ds.SOPInstanceUID, write_like_original=False)

    return 0x0000


handlers = [
    (evt.EVT_CONN_OPEN, handle_open),
    (evt.EVT_ACCEPTED, handle_accepted, ['optional', 'parameters']),
    (evt.EVT_C_STORE, handle_store)
]

# ae = AE()
ae = AE(ae_title=b'abc')

storage_sop_classes = [
    cx.abstract_syntax for cx in AllStoragePresentationContexts
]
for uid in storage_sop_classes:
    ae.add_supported_context(uid, ALL_TRANSFER_SYNTAXES)

ae.start_server(('', 4100), block=True, evt_handlers=handlers)
