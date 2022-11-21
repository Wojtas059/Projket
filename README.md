# IMPORTANT
## REQUIREMENTS:
- python version>=3.9 && version<3.10 komputer diagnosty
- python version == 3.7 stacja bazowa
W pliku requirements.txt zostały umieszczone wszystkie narzędzia jakie były wykorzystywane w toku pracu nad aplikacją i stacją bazową, która wymagała mniejszej liczy, jednkaże jak było napisane w cześniej, to jest świadectwo wykorzystywanych narzędzi.
W pliku requirements_pred.txt są narzędzia potrzebne do uruchamienia narzędzia predykcji.

Instalowanie wymaganych zależności:
pip install -r  <nazwa_pliku>.<rozszerzenie> 

Jeśli są problemy z nazwą zmienić na typowe requirements.txt


## Jak uruchomić aplikacje:


Z głównego folderu python -m src.apps.main_app

## Ważne!

Zalecamy korzystać z środowiska wirtualnego.

## Jak można generować pliki dla grpc/protobuf, przykład jaki my wykorzystwaliśmy:

Przejść w terminalu do folderu grpc/protos_dir i  wywołać komendę:
python -m grpc_tools.protoc -I./protos_base_station_com --python_out=./protos_base_station_com/ --grpc_python_out=./protos_base_station_com/ ./protos_base_station_com/client_base_station.proto


## Jak do tej pory eksportowaliśmy aplikację
Komenda:
w folderze z repozytorium komenda:
pyinstaller --noconfirm --onefile --windowed --name "<nazwa do wyeksportowania>"  --paths "<ścieżka do folderu z paczkami w środowisku wirtualnym>\<nazwa folderu z środowiska wirtualnego>\Lib\site-packages" --hidden-import "PyQt6.sip"  --hidden-import pyqtgraph.graphicsItems.ViewBox.axisCtrlTemplate_pyqt6 --hidden-import pyqtgraph.graphicsItems.PlotItem plotConfigTemplate_pyqt6 --hidden-import sqlite3  --hidden-import pyqtgraph.imageview.ImageViewTemplate_pyqt6 "<ścieżka do foldoru z repozytorium>\src\apps\main_app.py"

Powyższa komenda powinna być w jednej linii.
## Kod do predykcji został wykonany jako POC(proof of concept) - obrazuje on jako można go w pełni wdrożyć z pewnymi poprawkami, na ten moment po udanym wykaniu predykcji należy zabić terminal.

Uruchomienie należy przeprowadzić z folderu pred i wywołać odpowiedni plik w terminalu.

## Ostatnia uwaga

To co jest w <> należy uzupełnić własnymi danymi
