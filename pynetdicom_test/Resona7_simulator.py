#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from pydicom import dcmread
from pydicom.uid import ImplicitVRLittleEndian

from pynetdicom import AE, VerificationPresentationContexts
from pynetdicom.sop_class import CTImageStorage, MRImageStorage

logger = logging.getLogger('Resona7_simulator')

ae = AE(ae_title=b'Resona7')
# We can also do the same thing with the requested contexts
ae.requested_contexts = VerificationPresentationContexts
# Or we can use inbuilt objects like CTImageStorage.
# The requested presentation context's transfer syntaxes can also
#   be specified using a str/UID or list of str/UIDs
ae.add_requested_context(CTImageStorage,
                         transfer_syntax=ImplicitVRLittleEndian)
# Adding a presentation context with multiple transfer syntaxes
ae.add_requested_context(MRImageStorage,
                         transfer_syntax=[ImplicitVRLittleEndian,
                                          '1.2.840.10008.1.2.1'])

# assoc = ae.associate(addr, port)
assoc = ae.associate('192.168.0.6', 2345)
logger.info('simulator')
print('simulator')
if assoc.is_established:
    dataset = dcmread('./MRI.dcm')
    logger.info('assoc is established')
    print('assoc is established')
    # `status` is the response from the peer to the store request
    # but may be an empty pydicom Dataset if the peer timed out or
    # sent an invalid dataset.
    status = assoc.send_c_store(dataset)
    assoc.release()
else:
    print('no assoc')
