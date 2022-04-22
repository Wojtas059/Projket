from struct import pack
import serial
import time
from messages import serialize_message, parse_message

# STM_COM_PORT = "COM3"
STM_COM_PORT = "COM11"
STM_BAUDRATE = 921600

stm = serial.Serial(STM_COM_PORT, STM_BAUDRATE, timeout=None)


def send_message_until_response_or_timeout(
    message: object, timeout_s: float, time_step_s: float = 0.5
) -> object | None:
    stm.write(serialize_message(message))
    stm.flush()
    time.sleep(time_step_s)
    timeout_counter: float = time_step_s

    while stm.in_waiting == 0 and timeout_counter < timeout_s:
        stm.write(serialize_message(message))
        stm.flush()
        time.sleep(time_step_s)
        timeout_counter += time_step_s

    if timeout_counter >= timeout_s:
        return None

    packet_length = int.from_bytes(stm.read(), "big", signed=False)
    return parse_message(stm.read(packet_length))


def send_message(message: object) -> None:
    stm.write(serialize_message(message))
    stm.flush()


def read_message(
    wait_time: float = 0.1, wait_precision: float = 0.01, print_bytes: bool = False, print_size: bool = True
) -> object | None:
    total_wait_time: float = 0

    while stm.in_waiting == 0 and total_wait_time < wait_time:
        time.sleep(wait_precision)
        total_wait_time += wait_precision

    if total_wait_time >= wait_time:
        return None

    packet_length = int.from_bytes(stm.read(), "big", signed=False)
    data = stm.read(packet_length)
    if print_bytes:
        print(f"Received packet length: {packet_length}, data:")
        print(data)
    if print_size:
        print(f"Received packet length: {packet_length}")
    return parse_message(data)


def cleanup():
    stm.close()
