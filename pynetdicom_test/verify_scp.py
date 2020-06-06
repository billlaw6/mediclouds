from pynetdicom import AE, evt
from pynetdicom.sop_class import VerificationSOPClass

# Implement a handler for evt.EVT_C_ECHO
def handle_echo(event):
    """Handle a C-ECHO request event."""
    print('request received')
    return 0x0000

handlers = [(evt.EVT_C_ECHO, handle_echo)]

# ae = AE()
# ae = AE(ae_title=b'abc')
ae = AE(ae_title='abc')
ae.add_supported_context(VerificationSOPClass)
ae.start_server(('', 4100), evt_handlers=handlers)
# ae.start_server(('192.168.1.100', 4100), evt_handlers=handlers)
