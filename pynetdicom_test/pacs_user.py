#!/usr/bin/env python3
#-*- coding=utf-8 -*-

from pydicom import dcmread
from pynetdicom import AE
from pynetdicom.sop_class import CTImageStorage, MRImageStorage
import pdb

# Initialise the Application Entity
ae = AE(ae_title=b'WHTM-116')

# Add a requested presentation context
ae.add_requested_context(CTImageStorage)
ae.add_requested_context(MRImageStorage)

# Read in our DICOM CT dataset
ds = dcmread('/Volumes/Transcend/mediclouds/PACS/MRI.dcm')
# Associate with peer AE at IP 127.0.0.1 and port 11112
pdb.set_trace()
assoc = ae.associate('127.0.0.1', 3333 ,ae_title=b'UIHPACSSERVER')

if assoc.is_established:
    # Use the C-STORE service to send the dataset
    # returns the response status as a pydicom Dataset
    status = assoc.send_c_store(ds)
    # Check the status of the storage request
    if status:
        # If the storage request succeeded this will be 0x0000
        print('C-STORE request status: 0x{0:04x}'.format(status.Status))
    else:
        print('Connection timed out, was aborted or received invalid response')
    # Release the association
    assoc.release()
else:
    print('Association rejected, aborted or never connected')
