#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from pydicom import dcmread
from pydicom.uid import ImplicitVRLittleEndian, UID

from pynetdicom import AE, build_context, VerificationPresentationContexts
from pynetdicom.sop_class import CTImageStorage, MRImageStorage,\
    UltrasoundMultiframeImageStorage

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("storage_scu_log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(handler)
logger.addHandler(console)

ae = AE(ae_title=b'MY_STORAGE_SCU')
# We can also do the same thing with the requested contexts
# ae.requested_contexts = VerificationPresentationContexts
# Or we can use inbuilt objects like CTImageStorage.
# The requested presentation context's transfer syntaxes can also
#   be specified using a str/UID or list of str/UIDs
# ivus_cx = build_context('1.2.840.10008.1.1', ['1.2.840.10008.5.1.4.1.1.3.1',])
# ivus_cx = build_context('1.2.840.10008.5.1.4.1.1.3.1')
# ae.add_requested_context('1.2.840.10008.5.1.4.1.1.3.1')
ae.add_requested_context(UID('1.2.840.10008.5.1.4.1.1.3.1'))
# ae.add_requested_context(UltrasoundMultiframeImageStorage)
# ae.add_requested_context(UltrasoundMultiframeImageStorage,
#                          transfer_syntax=['1.2.840.10008.5.1.4.1.1.3.1'])
ae.add_requested_context(CTImageStorage,
                         transfer_syntax=ImplicitVRLittleEndian)
# Adding a presentation context with multiple transfer syntaxes
ae.add_requested_context(MRImageStorage,
                         transfer_syntax=[ImplicitVRLittleEndian,
                                          '1.2.840.10008.1.2.1'])

for cx in ae.requested_contexts:
    print(cx)

# assoc = ae.associate(addr, port)
# assoc = ae.associate('192.168.0.6', 2345)
# assoc = ae.associate('192.168.1.102', 4100)
# assoc = ae.associate('192.168.0.6', 104)
assoc = ae.associate('192.168.3.5', 4100)
if assoc.is_established:
    logger.info('assoc is established')
    # dataset = dcmread('./MRI.dcm')
    dataset = dcmread('./IMG00001')
    # `status` is the response from the peer to the store request
    # but may be an empty pydicom Dataset if the peer timed out or
    # sent an invalid dataset.
    status = assoc.send_c_store(dataset)
    assoc.release()
else:
    logger.info('no assoc')
