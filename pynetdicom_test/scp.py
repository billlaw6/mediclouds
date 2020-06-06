import logging

from pynetdicom import AE, evt, debug_logger
from pynetdicom.sop_class import VerificationSOPClass

# Setup logging to use the StreamHandler at the debug level
debug_logger()

ae = AE(ae_title=b'MY_ECHO_SCP')
ae.add_supported_context(VerificationSOPClass)

# Implement the EVT_C_ECHO handler
def handle_echo(event, logger):
    """Handle a C-ECHO service request.

    Parameters
    ----------
    event : evt.Event
        The C-ECHO service request event, this parameter is always
        present.
    logger : logging.Logger
        The logger to use, this parameter is only present because we
        bound ``evt.EVT_C_ECHO`` using a 3-tuple.

    Returns
    -------
    int or pydicom.dataset.Dataset
        The status returned to the peer AE in the C-ECHO response.
        Must be a valid C-ECHO status value as either an ``int`` or a
        ``Dataset`` object containing an (0000,0900) *Status* element.
    """
    # Every *Event* includes `assoc` and `timestamp` attributes
    #   which are the *Association* instance the event occurred in
    #   and the *datetime.datetime* the event occurred at
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    msg = (
        "Received C-ECHO service request from ({}, {}) at {}"
        .format(requestor.address, requestor.port, timestamp)
    )
    logger.info(msg)

    # Return a *Success* status
    return 0x0000

# By binding using a 3-tuple we can pass extra arguments to
#   the handler
handlers = [(evt.EVT_C_ECHO, handle_echo, [logging.getLogger('pynetdicom')])]

# Start the SCP in non-blocking mode
# scp = ae.start_server(('', 11116), block=False, evt_handlers=handlers)
scp = ae.start_server(('', 11116), block=False)

# Associate and send a C-ECHO request to our own Verification SCP
ae.add_requested_context(VerificationSOPClass)
assoc = ae.associate('localhost', 11116)
if assoc.is_established:
    status = assoc.send_c_echo()
    assoc.release()

# Shutdown the SCP
# scp.shutdown()
