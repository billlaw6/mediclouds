#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pynetdicom import AE
from pynetdicom.sop_class import VerificationSOPClass

# Initialise the Application Entity
ae = AE()

# Add a requested presentation context
ae.add_requested_context(VerificationSOPClass)

# Associate with peer AE at IP 127.0.0.1 and port 11112
assoc = ae.associate('192.168.1.101', 4100)
# assoc = ae.associate('192.168.1.101', 4100)

if assoc.is_established:
    # Use the C-ECHO service to send the request
    # returns the response status a pydicom Dataset
    status = assoc.send_c_echo()

    # Check the status of the verification request
    if status:
        # If the verification request succeeded this will be 0x0000
        print('C-ECHO request status: 0x{0:04x}'.format(status.Status))
    else:
        print('Connection timed out, was aborted or received invalid response')

    # Release the association
    assoc.release()
else:
    print('Association rejected, aborted or never connected')
