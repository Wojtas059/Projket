# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import client_base_station_pb2 as client__base__station__pb2


class ClientBaseStationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.checkConnection = channel.unary_unary(
                '/ClientBaseStation/checkConnection',
                request_serializer=client__base__station__pb2.CheckConnection.SerializeToString,
                response_deserializer=client__base__station__pb2.ConnectionStats.FromString,
                )
        self.checkSTMConnection = channel.unary_unary(
                '/ClientBaseStation/checkSTMConnection',
                request_serializer=client__base__station__pb2.CheckConnection.SerializeToString,
                response_deserializer=client__base__station__pb2.ConnectionStats.FromString,
                )
        self.startSTMSampling = channel.unary_unary(
                '/ClientBaseStation/startSTMSampling',
                request_serializer=client__base__station__pb2.OrderSTM.SerializeToString,
                response_deserializer=client__base__station__pb2.ConnectionStats.FromString,
                )
        self.stopSTMSampling = channel.unary_unary(
                '/ClientBaseStation/stopSTMSampling',
                request_serializer=client__base__station__pb2.OrderSTM.SerializeToString,
                response_deserializer=client__base__station__pb2.ConnectionStats.FromString,
                )
        self.sendSTMData = channel.unary_stream(
                '/ClientBaseStation/sendSTMData',
                request_serializer=client__base__station__pb2.Void.SerializeToString,
                response_deserializer=client__base__station__pb2.STMData.FromString,
                )


class ClientBaseStationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def checkConnection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def checkSTMConnection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def startSTMSampling(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stopSTMSampling(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendSTMData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientBaseStationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'checkConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.checkConnection,
                    request_deserializer=client__base__station__pb2.CheckConnection.FromString,
                    response_serializer=client__base__station__pb2.ConnectionStats.SerializeToString,
            ),
            'checkSTMConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.checkSTMConnection,
                    request_deserializer=client__base__station__pb2.CheckConnection.FromString,
                    response_serializer=client__base__station__pb2.ConnectionStats.SerializeToString,
            ),
            'startSTMSampling': grpc.unary_unary_rpc_method_handler(
                    servicer.startSTMSampling,
                    request_deserializer=client__base__station__pb2.OrderSTM.FromString,
                    response_serializer=client__base__station__pb2.ConnectionStats.SerializeToString,
            ),
            'stopSTMSampling': grpc.unary_unary_rpc_method_handler(
                    servicer.stopSTMSampling,
                    request_deserializer=client__base__station__pb2.OrderSTM.FromString,
                    response_serializer=client__base__station__pb2.ConnectionStats.SerializeToString,
            ),
            'sendSTMData': grpc.unary_stream_rpc_method_handler(
                    servicer.sendSTMData,
                    request_deserializer=client__base__station__pb2.Void.FromString,
                    response_serializer=client__base__station__pb2.STMData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ClientBaseStation', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClientBaseStation(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def checkConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientBaseStation/checkConnection',
            client__base__station__pb2.CheckConnection.SerializeToString,
            client__base__station__pb2.ConnectionStats.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def checkSTMConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientBaseStation/checkSTMConnection',
            client__base__station__pb2.CheckConnection.SerializeToString,
            client__base__station__pb2.ConnectionStats.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def startSTMSampling(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientBaseStation/startSTMSampling',
            client__base__station__pb2.OrderSTM.SerializeToString,
            client__base__station__pb2.ConnectionStats.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stopSTMSampling(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientBaseStation/stopSTMSampling',
            client__base__station__pb2.OrderSTM.SerializeToString,
            client__base__station__pb2.ConnectionStats.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendSTMData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ClientBaseStation/sendSTMData',
            client__base__station__pb2.Void.SerializeToString,
            client__base__station__pb2.STMData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
