from management_pb2 import StartECGMeasurementsRequest, StopMeasurementsRequest
from measurements_pb2 import ECGData, ECGDataRequest
from stm import read_message, send_message


def start_test_measurements() -> bool:
    request = StartECGMeasurementsRequest()
    request.type = StartECGMeasurementsRequest.TEST
    request.rate = StartECGMeasurementsRequest.RATE_128HZ
    request.gain = StartECGMeasurementsRequest.GAIN_20VV
    request.lowPassFilterCutoff = StartECGMeasurementsRequest.CUTOFF_DISABLED
    request.highPassFilterEnabled = False

    send_message(request)

    return True


def stop_test_measurements() -> bool:
    request = StopMeasurementsRequest()
    send_message(request)

    response = read_message(1)
    print(type(response))
    return True


# def read_samples() -> None:
#     samples = read_message(1, print_bytes=True)
#     print(type(samples))
#     if samples is not None:
#         try:
#             print("Sample no. {}".format(samples.sampleID))
#             for voltage in samples.ecgVoltage:
#                 print("\t{}V".format(voltage))
#         except AttributeError:
#             print("Invalid message received!")


def read_next_packet(get_next: bool = True):
    # Send request packet
    request = ECGDataRequest()
    request.nextPacketRequested = get_next
    send_message(request)
    data = read_message(wait_time=0.2, print_bytes=False)
    return data


def print_ecg_data(packet: ECGData, print_data: bool = True) -> None:
    print("Received packet no. {} with readings:".format(packet.sampleID))
    if print_data:
        for voltage in ecg_data.ecgVoltage:
            print("\t{}V".format(voltage))


received_packets = 0
last_received_packet_id = 0


def process_packet(packet: ECGData) -> bool:
    global received_packets, last_received_packet_id
    if isinstance(packet, ECGData):
        if packet.sampleID != 0 and packet.isValidPacket == True:
            received_packets += 1
            last_received_packet_id = packet.sampleID
            print_ecg_data(packet)
            return True

    print(".", end="")
    return False


if __name__ == "__main__":
    start_test_measurements()
    while True:
        try:
            ecg_data = read_next_packet()
            i = 0
            while i < 5 and not process_packet(ecg_data):
                i += 1
                ecg_data = read_next_packet(False)
        except KeyboardInterrupt:
            print("Received {} packets".format(received_packets))
            print("Last received packet had ID = {}".format(last_received_packet_id))
            print(
                "We lost {} packets, which is {:.2f}%".format(
                    last_received_packet_id - received_packets,
                    (1 - (received_packets / last_received_packet_id)) * 100,
                )
            )
            exit(0)
    # time.sleep(1)
    # stop_test_measurements()
