from stm import send_message, read_message
from management_pb2 import StartBioZMeasurementsRequest, StopMeasurementsRequest
from measurements_pb2 import BioZData, BioZDataRequest

def start_measurements():
    request = StartBioZMeasurementsRequest()
    request.type = StartBioZMeasurementsRequest.BIOZ
    request.rate = StartBioZMeasurementsRequest.RATE_64HZ
    request.gain = StartBioZMeasurementsRequest.GAIN_20VV
    request.analogHighPassFilterCutoff = StartBioZMeasurementsRequest.CUTOFF_800HZ
    request.digitalHighPassFilterCutoff = StartBioZMeasurementsRequest.DHPF_CUTOFF_BYPASS
    request.digitalLowPassFilterCutoff = StartBioZMeasurementsRequest.CUTOFF_4HZ
    request.currentGeneratorFrequency = StartBioZMeasurementsRequest.CURRENT_GEN_80KHZ
    request.currentGeneratorMagnitude = StartBioZMeasurementsRequest.CURRENT_GEN_32UA

    send_message(request)
    
    return True

def read_next_packet(get_next: bool = True):
    request = BioZDataRequest()
    request.nextPacketRequested = get_next
    send_message(request)
    
    data = read_message(wait_time=0.5, print_bytes=False)
    return data

def print_bioz_data(packet: BioZData, print_data: bool = True):
    if print_data:
        print("Received packet {} with data:".format(packet.sampleID))
        for impedance in packet.biozImpedance:
            print("\t{}Ohm".format(impedance))
    else:
        print(f"{packet.sampleID} ", end="", flush=True)

received_packets = 0
last_received_packet_id = 0

def process_packet(packet: BioZData):
    global received_packets, last_received_packet_id
    if isinstance(packet, BioZData):
        if packet.sampleID != 0 and packet.isValidPacket == True:
            received_packets += 1
            last_received_packet_id = packet.sampleID
            print_bioz_data(packet, True)
            return True
        
    print(".", end="")
    return False

if __name__ == "__main__":
    start_measurements()
    # exit(0)
    while True:
        try:
            bioz_data = read_next_packet()
            i = 0
            while i < 5 and not process_packet(bioz_data):
                i += 1
                bioz_data = read_next_packet(False)
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