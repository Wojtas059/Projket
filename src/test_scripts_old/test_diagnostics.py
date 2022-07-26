from distutils.command.clean import clean

from management_pb2 import DiagnosticsRequest
from stm import cleanup, send_message_until_response_or_timeout


def send_diagnostics_message(checkMAX: bool) -> object | None:
    msg = DiagnosticsRequest()
    msg.checkMAX30001 = checkMAX

    return send_message_until_response_or_timeout(msg, 2)


if __name__ == "__main__":
    print(send_diagnostics_message(True))
    print(send_diagnostics_message(False))
    cleanup()
