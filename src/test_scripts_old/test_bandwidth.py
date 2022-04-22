from stm import read_message, send_message
from measurements_pb2 import BandwidthTestData, BandwidthTestDataRequest
from enum import Enum

PACKET_DATA_LENGTH = 60

class ValidationResult(Enum):
    OK = 0
    DATA_ERROR = 1
    ID_ERROR = 2
    INVALID_PACKET_TYPE = 3


def send_request_for_test_data(retransmit_last: bool = False):
    request = BandwidthTestDataRequest()
    request.nextPacketRequested = not retransmit_last

    send_message(request)


def validate_data_packet(
    packet: BandwidthTestData, expectedID: int
):
    if not isinstance(packet, BandwidthTestData):
        return (
            ValidationResult.INVALID_PACKET_TYPE,
            f"Invalid packet type: {type(packet).__name__}",
        )

    if packet.sampleID != expectedID:
        return (
            ValidationResult.ID_ERROR,
            f"Expected ID: {expectedID}, packet ID: {packet.sampleID}",
        )

    for i in range(0, PACKET_DATA_LENGTH):
        expectedValue = (expectedID + i) % 0x100
        if packet.testValues[i] != expectedValue:
            return (
                ValidationResult.DATA_ERROR,
                f"Byte {i} invalid, expected 0x{expectedValue:02x}, got 0x{packet.testValues[i]:02x}",
            )

    return (ValidationResult.OK, "")


def test_data_transmission(
    expected_id: int,
    retransmit_last: bool = False,
    wait_time: float = 0.5,
    current_retry: int = 1,
    max_retries: int = 5,
) -> bool:
    send_request_for_test_data(retransmit_last)

    data = read_message(wait_time)
    validation_result, validation_message = validate_data_packet(data, expected_id)

    if validation_result is ValidationResult.OK:
        print(f"Packet {expected_id} received!")
        return True
    else:
        print(validation_message)
        if current_retry <= max_retries:
            print(f"\tTrying retransmission [{current_retry}/{max_retries}]")
            return test_data_transmission(
                expected_id,
                retransmit_last=True,
                wait_time=wait_time,
                current_retry=(current_retry + 1),
                max_retries=max_retries,
            )
        else:
            print("\tMaximum retransmission tries reached, packet lost.")

    return False


def main():
    expectedPacketID = 1
    receivedPackets = 0

    while True:
        try:
            print(f"Requested packet {expectedPacketID}")
            packetReceived = test_data_transmission(expectedPacketID)
            if packetReceived:
                receivedPackets += 1

            expectedPacketID += 1

        except KeyboardInterrupt:
            lostPackets = expectedPacketID - receivedPackets
            lostPacketsRatio = (lostPackets / receivedPackets) * 100
            print(
                f"Received {receivedPackets} out of {expectedPacketID}. Lost {lostPackets} packets ({lostPacketsRatio:.2f}%)"
            )
            exit(0)


if __name__ == "__main__":
    main()
