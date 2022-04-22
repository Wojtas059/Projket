import src.test_scripts.management_pb2 as management
import src.test_scripts.measurements_pb2 as measurements
from enum import IntEnum
from google.protobuf.message import DecodeError


class MessageID(IntEnum):
    PING = 0x01
    PONG = 0x02
    DIAGNOSTICS_REQUEST = 0x03
    DIAGNOSTICS_RESPONSE = 0x04
    STOP_MEASUREMENTS_REQUEST = 0x05
    STOP_MEASUREMENTS_RESPONSE = 0x06
    START_ECG_MEASUREMENTS_REQUEST = 0x20
    START_ECG_MEASUREMENTS_RESPONSE = 0x21
    ECG_DATA = 0x60
    ECG_DATA_REQUEST = 0x61
    TEST_DATA = 0x90
    TEST_DATA_REQUEST = 0x91

    ERROR_RESPONSE = 0xFF


_MESSAGE_IDS_LIST = set(item.value for item in MessageID)


def get_message_id(message_data: bytes):
    """Return the ID of the message, or None if the ID is invalid"""
    if len(message_data) == 0:
        return None

    messageIDByte = int(message_data[0])
    print(f"Message ID byte: {messageIDByte}")
    if messageIDByte not in _MESSAGE_IDS_LIST:
        return None
    return MessageID(messageIDByte)


def parse_message(message_data: bytes):
    """Return the parsed message, or None if parsing has failed or message is invalid"""
    message_id = get_message_id(message_data)
    if message_id is None:
        return None


    message = None

    


       # match message_id:
    #     case MessageID.PONG:
    #         message = management.Pong()
    #     case MessageID.DIAGNOSTICS_RESPONSE:
    #         message = management.DiagnosticsResponse()
    #     case MessageID.STOP_MEASUREMENTS_RESPONSE:
    #         message = management.StopMeasurementsResponse()
    #     case MessageID.START_ECG_MEASUREMENTS_RESPONSE:
    #         message = management.StartECGMeasurementsResponse()
    #     case MessageID.ECG_DATA:
    #         message = measurements.ECGData()
    #     case MessageID.ERROR_RESPONSE:
    #         message = management.ErrorResponse()
    #     case MessageID.TEST_DATA:
    #         message = measurements.BandwidthTestData()

    if message_id is MessageID.PONG:
        message = management.Pong()
    if message_id is MessageID.DIAGNOSTICS_RESPONSE:
        message = management.DiagnosticsResponse()
    if message_id is MessageID.STOP_MEASUREMENTS_RESPONSE:
        message = management.StopMeasurementsResponse()
    if message_id is MessageID.START_ECG_MEASUREMENTS_RESPONSE:
       message = management.StartECGMeasurementsResponse()
    if message_id is MessageID.ECG_DATA:
        message = measurements.ECGData()
    if message_id is MessageID.ERROR_RESPONSE:
        message = management.ErrorResponse()
    if message_id is MessageID.TEST_DATA:
        message = measurements.BandwidthTestData()

    if message is None:
        return None

    try:
        message.ParseFromString(message_data[1:])
    except DecodeError:
        return None

    return message


def serialize_message(message: object):
    message_id = None
    if isinstance(message, management.Ping):
        message_id = MessageID.PING
    elif isinstance(message, management.DiagnosticsRequest):
        message_id = MessageID.DIAGNOSTICS_REQUEST
    elif isinstance(message, management.StopMeasurementsRequest):
        message_id = MessageID.STOP_MEASUREMENTS_REQUEST
    elif isinstance(message, management.StartECGMeasurementsRequest):
        message_id = MessageID.START_ECG_MEASUREMENTS_REQUEST
    elif isinstance(message, measurements.ECGDataRequest):
        message_id = MessageID.ECG_DATA_REQUEST

    return bytes([message_id]) + message.SerializeToString()
