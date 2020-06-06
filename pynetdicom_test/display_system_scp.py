from pynetdicom import AE, evt
from pynetdicom.sop_class import DisplaySystemSOPClass

# from my_code import create_attribute_list

# Implement a handler evt.EVT_N_GET
def handle_get(event):
    """Handle an N-GET request event."""
    attr = event.request.AttributeIdentifierList
    # User defined function to generate the required attribute list dataset
    # implementation is outside the scope of the current example
    # We pretend it returns a pydicom Dataset
    dataset = create_attribute_list(attr)

    # Return success status and dataset
    return 0x0000, dataset

handlers = [(evt.EVT_N_GET, handle_get)]

# Initialise the Application Entity and specify the listen port
ae = AE()

# Add the supported presentation context
ae.add_supported_context(DisplaySystemSOPClass)

# Start listening for incoming association requests
ae.start_server(('', 11112), evt_handlers=handlers)
