import queue

from src.test_scripts.management_pb2 import (
    StartECGMeasurementsRequest,
    StopMeasurementsRequest,
)
from src.test_scripts.measurements_pb2 import ECGData, ECGDataRequest
from src.test_scripts.stm import read_message, send_message


class ECGTests:
    def __init__(self) -> None:
        self.received_packets = 0
        self.last_received_packet_id = 0
        self.ecg_data = None
        self.queqe_data = queue.Queue()

    def start_test_measurements(self) -> bool:
        request = StartECGMeasurementsRequest()
        request.type = StartECGMeasurementsRequest.TEST
        request.rate = StartECGMeasurementsRequest.RATE_128HZ
        request.gain = StartECGMeasurementsRequest.GAIN_20VV
        request.lowPassFilterCutoff = StartECGMeasurementsRequest.CUTOFF_DISABLED
        request.highPassFilterEnabled = False

        send_message(request)

        return True

    def stop_test_measurements(self) -> bool:
        request = StopMeasurementsRequest()
        send_message(request)

        response = read_message(1)
        print(type(response))
        return True

    def read_next_packet(self, get_next: bool = True, *, wait_time: float = 0.2):
        # Send request packet
        request = ECGDataRequest()
        request.nextPacketRequested = get_next
        send_message(request)
        data = read_message(wait_time=wait_time, print_bytes=False)
        return data

    def print_ecg_data(self, packet: ECGData, print_data: bool = True) -> None:
        print("Received packet no. {} with readings:".format(packet.sampleID))
        if print_data:
            for voltage in self.ecg_data.ecgVoltage:
                print("\t{}V".format(voltage))
                self.queqe_data.put(voltage)

    def process_packet(self, packet: ECGData) -> bool:
        self.received_packets, self.last_received_packet_id
        if isinstance(packet, ECGData):
            if packet.sampleID != 0 and packet.isValidPacket == True:
                self.received_packets += 1
                self.last_received_packet_id = packet.sampleID
                self.print_ecg_data(packet)
                return True

        print(".", end="")
        return False
