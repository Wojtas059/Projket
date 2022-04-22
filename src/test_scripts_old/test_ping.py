from stm import send_message, cleanup, read_message
from management_pb2 import Ping


def test_connection_bidirectional(amount_of_pings: int, ping_delay: int = 0) -> int:
    ping = Ping()
    ping.expectedAmountOfPongs = 1
    ping.delayBetweenPongs = 0

    received_pongs: int = 0

    for i in range(1, amount_of_pings + 1):
        print(f"Sending ping # {i}")
        ping.pingID = i
        send_message(ping)
        pong = read_message(ping_delay, print_bytes=True)
        if pong is not None:
            if pong.pongID == ping.pingID:
                print(f"\tReceived pong: {pong}")
                received_pongs += 1
            else:
                print(f"Packet has invalid ID ({pong.pongID})!")
        else:
            print("Packet lost!")

    return received_pongs


def test_connection_rx(amount_of_pings: int, ping_delay: int = 0.1) -> int:
    ping = Ping()

    ping.pingID = 0
    ping.expectedAmountOfPongs = amount_of_pings
    ping.delayBetweenPongs = int(ping_delay * 1000)

    received_pongs: int = 0
    lost_pongs: int = 0

    print(f"Sending ping: {ping}")
    send_message(ping)

    for i in range(0, amount_of_pings):
        pong = read_message(ping_delay + 0.5)
        if pong is not None:
            print(f"\tReceived pong: {pong}")
            received_pongs += 1
        else:
            print("Packet lost!")
            lost_pongs += 1

            if lost_pongs > 10:
                break

    return received_pongs


def run_test_bidirectional(pings_to_send: int):
    received_pongs = test_connection_bidirectional(pings_to_send, 0.2)
    print(
        "\nPackets received: {0}, packet loss: {1:.2f}%".format(
            received_pongs, (1 - (received_pongs / pings_to_send)) * 100
        )
    )


def run_test_rx(pings_to_send: int, ping_delay: float):
    received_pongs = test_connection_rx(pings_to_send, ping_delay)
    print(
        "\nPackets received: {0}, packet loss: {1:.2f}%".format(
            received_pongs, (1 - (received_pongs / pings_to_send)) * 100
        )
    )


if __name__ == "__main__":
    run_test_bidirectional(500)
    # run_test_rx(1000, 0.02)

    cleanup()
