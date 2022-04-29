


class ManageSensor:
    def __init__(self) -> None:
        self.quantity_sensor: int = None
        self.data_sensor: dict = {}
        self.list_sensor_ip: list = []

    def getQuantityDataSensor(self)-> int:
        return self.quantity_sensor
    
    def setQuantityDataSensor(self, quantity: int):
        self.quantity_sensor = quantity

    def getDataSensor(self)->dict:
        return self.data_sensor
    
    def setDataSensor(self, data_sensor:dict):
        self.data_sensor = data_sensor
    
    def addKeyValueDataSensor(self, name: str, value: list):
        self.data_sensor[name] = value

    def addIpAddressSensor(self, ip_address: str):
        self.list_sensor_ip.append(ip_address)
    
    def getIpAddressSensor(self)-> list:
        return self.list_sensor_ip

    def deleteKeyValueDataSensor(self, key_name: str):
        del self.data_sensor[key_name]