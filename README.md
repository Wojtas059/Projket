# IMPORTANT
## REQUIREMENTS:
- python version>=3.9 && version<3.10
- flake8  4.0.1 (mccabe: 0.6.1, pycodestyle: 2.8.0, pyflakes: 2.4.0) CPython 3.9.4 on Windows
- isort   VERSION 5.10.1
- black 22.1.0 (compiled: yes)
- bcrypt             3.2.0
- Kivy               2.0.0
- kivy-garden.graph  0.4.0
- serial pyserial-3.5
- pytest             7.0.1
##  How to generate/update python files from proton:
Go in terminal to protos_dir then use for example:
python -m grpc_tools.protoc -I./protos_base_station_com --python_out=./protos_base_station_com/ --grpc_python_out=./protos_base_station_com/ ./protos_base_station_com/client_base_station.proto
if your protos is in diffrent dir then:
python -m grpc_tools.protoc -I./your_dir --python_out=./your_dir/ --grpc_python_out=./your_dir/ ./your_dir/your_protos.proto

# STM32 <-> PC communication example - Python project

This project contains example code that can be used to communicate with STM32 via Protobuf API.

The communication is done via UART peripheral, accesible via USB thanks to UART-to-USB converter implemented on STLink/V2 debugger, since i'm using Nucleo board - however, any UART-to-USB converter supported by your OS will do the job here.

The version of Python i'm using is 3.9, and i don't intend to support any other. However, it should work just fine on slightly newer or older versions (you may need to change the version in `Pipfile`, if you're not using 3.9)

## Running the project with pipenv

If you wanna use prepared virtualenv for this project, run `pipenv run main.py [SERIAL PORT]` - everything should set-up automatically and the script should run, talking to STM32 and printing the results in console. Replace `[SERIAL PORT]` with STM32 port path, for example `COM3` or `/dev/ttyACM0`. This script will always list available COM devices, so you can run it without providing serial port name to check which port is the STM32.

If you've configured different baudrate, pass it as optional argument `--baud`, for example: `pipenv run main.py /dev/ttyACM0 --baud 921600`. The default baudrate is `115200`, and script will always print currently used baudrate.

## Running the project manually

Install the dependencies manually, via `pip`, or other package manager. This script requires only `pyserial` and `protobuf` to run.

