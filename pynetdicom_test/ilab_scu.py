#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import logging
from pydicom import dcmread
from pynetdicom import AE, VerificationPresentationContexts,\
    StoragePresentationContexts
from pynetdicom.sop_class import VerificationSOPClass
# import pdb

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("storage_scu_log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s\
                              - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)

ds = dcmread('/Volumes/Transcend/mediclouds/PACS/MRI.dcm')
# ds = dcmread('/Volumes/Transcend/mediclouds/PACS/IMG00001')
ae = AE(ae_title=b'ilab_scu')

ae.requested_contexts = StoragePresentationContexts
# ae.add_requested_context(VerificationPresentationContexts)
# ae.add_requested_context(VerificationSOPClass)

# for cx in ae.requested_contexts:
#     print(cx)

assoc = ae.associate('192.168.3.5', 4100, ae_title=b'lkjds')

if assoc.is_established:
    logger.info('assoc is established')
    dataset = dcmread('./MRI.dcm')
    # dataset = dcmread('./IMG00001')
    # `status` is the response from the peer to the store request
    # but may be an empty pydicom Dataset if the peer timed out or
    # sent an invalid dataset.
    status = assoc.send_c_store(ds, 1, 1)
    assoc.release()
else:
    logger.info('no assoc')

# if assoc.is_established:
#     print('Association connected')
#     status = assoc.send_c_echo()
#     if status:
#         print('ok')
#     else:
#         print('no')
# else:
#     print('Association rejected, aborted or never connected')
