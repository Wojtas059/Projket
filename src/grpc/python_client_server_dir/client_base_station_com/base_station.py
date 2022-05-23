import logging
from concurrent import futures
from queue import Queue
from threading import Thread
import grpc
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer
from file.mygrid import Connect as ConnectSTM32
from src.python_class.medical_research.ecg_tests import ECGTests 

class BaseStation(Servicer.ClientBaseStationServicer):
    def __init__(self) -> None:
        super().__init__()
        self._my_status = "Active"
        self._stm_status = ""
        self._stm_manager = ConnectSTM32()
        self._spirit_manager = ECGTests()
        

    def checkConnection(self, request, context):
        return ServicerMethods.ConnectionStats(stats=self._my_status)

    def checkSTMConnection(self, request, context):
        return ServicerMethods.ConnectionStats(stats=self._stm_status)

    def stopSTMSampling(self, request, context):
        self._stm_manager.stop()
        self._stm_status = request.order
        return ServicerMethods.ConnectionStats(stats=self._stm_status)

    def startSTMSampling(self, request, context):
        self._stm_manager.start()
        Thread(target=self.sendSpiritData).start()
        self._stm_status = request.order
        print(self._stm_status)
        return ServicerMethods.ConnectionStats(stats=self._stm_status)

    def sendSTMData(self, request, context):
        
        while True:
            if self._stm_status == "Sampling":
                if self._spirit_manager.queqe_data.qsize() > 0:
                    data_stm = self._spirit_manager.queqe_data.get()
                    
                    yield ServicerMethods.STMData(data=data_stm)
    #TODO: Function returning the rest of the queue, update proto...

    def sendSpiritData(self):
        self._spirit_manager.start_test_measurements()
        while True:
            try:
                self._spirit_manager.ecg_data = self._spirit_manager.read_next_packet()
                if self._spirit_manager.ecg_data is None:
                    self._spirit_manager.ecg_data = self._spirit_manager.read_next_packet(False, wait_time=4) 
                i = 0
                while i < 5 and not self._spirit_manager.process_packet( self._spirit_manager.ecg_data):
                    i += 1
                    self._spirit_manager.ecg_data = self._spirit_manager.read_next_packet(False)
            except KeyboardInterrupt:
                print("Received {} packets".format(self._spirit_manager.received_packets))
                print("Last received packet had ID = {}".format(self._spirit_manager.last_received_packet_id))
                print(
                    "We lost {} packets, which is {:.2f}%".format(
                        self._spirit_manager.last_received_packet_id - self._spirit_manager.received_packets,
                        (1 - (self._spirit_manager.received_packets / self._spirit_manager.last_received_packet_id)) * 100,
                    )
                )




def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    Servicer.add_ClientBaseStationServicer_to_server(BaseStation(), server)
    server.add_insecure_port("[::]:50051")
    
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    start_server()
