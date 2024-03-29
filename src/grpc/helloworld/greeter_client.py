# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import helloworld_pb2
import helloworld_pb2_grpc

import grpc


def run():
    channel = grpc.insecure_channel("192.168.1.107:50051")
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)


def run_1():
    channel = grpc.insecure_channel("192.168.1.107:50051")
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    while True:
        print("Wybierz opcje:")
        print("1 - SayHello")
        print("2 - SayHelloAgain")
        i = input()
        if i == "1":
            run()
        else:
            run_1()
