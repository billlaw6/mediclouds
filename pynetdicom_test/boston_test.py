#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from pydicom.dataset import Dataset

logger = logging.getLogger('pynetdicom')
from pynetdicom import (
    AE, evt,
    StoragePresentationContexts,
    PYNETDICOM_IMPLEMENTATION_UID,
    PYNETDICOM_IMPLEMENTATION_VERSION
)

# Implement a handler evt.EVT_C_STORE
def handle_store(event):
    """Handle a C-STORE request event."""
    # Decode the C-STORE request's *Data Set* parameter to a pydicom Dataset
    ds = event.dataset

    # Add the File Meta Information
    ds.file_meta = event.file_meta

    # Save the dataset using the SOP Instance UID as the filename
    ds.save_as(ds.SOPInstanceUID, write_like_original=False)

    # Return a 'Success' status
    return 0x0000

handlers = [(evt.EVT_C_STORE, handle_store)]

# Initialise the Application Entity
ae = AE()

# Add the supported presentation contexts
ae.supported_contexts = StoragePresentationContexts

# Start listening for incoming association requests
ae.start_server(('', 2345), evt_handlers=handlers)
