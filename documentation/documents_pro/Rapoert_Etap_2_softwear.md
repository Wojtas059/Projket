## Raport Etapu 2
#### Niniejszy raport dotyczy podsumowania zrealizowanych zadań z Etapu 2 (Trello-Aplikacja-Etap 2)
> #### Wojciech Maj, Piotr Łach

#### Założenia

Głównych założeń aplikacji jest prowadzenie akwizycji danych podczas sesji treningowych lub rehabilitacyjnych. Dodatkowo aplikacja ma zadanie umożliwić wyświetlenie historii pomiarowej użytkownika lub użytkowników (w przypadku użytkownika zaawansowanego).

#### Realizacja

Praca nad stworzeniem aplikacji jest podzielona na 4 etapy. 
Etap 2 miał zostać ukończony do 17 stycznia ( Znaczne przesunięcie), który składa się z następujących zadań:
*  Obsługa bazy danych: dane pomiarowe
*  Widoki trybu Auto
*  Widoki trybu Manual
*  Widoki pomocy
*  Implementacja modułu pomiarowego
*  Implementacja modułu pomocy

Wszytskie zadania udało się zrealizować

#### Problemy

Ten etap był bardzo obfity w pojawianie się problemów, począwszy od tego że długi czas oczekiwania na otrzymanie stacji bazowej i modułu akwizycji danych.
Dodatkowo pojawił się znaczny problem w doborze biblioteki `Kivy`, która nie dość że mocno dołożyła nam pracy to całkowicie się nie sprawdziła na etapie wizualizacji sygnału. 
Dlatego ten czas zostal wydłużony o ponową implementację całego widoku z wykorzystaniem innej bibliteki `PyQt6`, gdzie musieliśmy ponownie przeprowadzić etap 1, co skutkowało dodatkowym nakładem pracy.


### GUI trybów pomiarowych

Rozpoczęcei pomiaru dla trybu gość
<img src='img/1.png'>


Wybór aktywności
<img src='img/2.png'>
Wybór sylwetki
<img src='img/3.png'>

Wybór liczby taśm pomiarowych TRYB AUTO
<img src='img/4.png'>
<img src='img/5.png'>

Połaczenie się z taśmami TRYB AUTO
<img src='img/6.png'>

Rozpoczęcie pomiaru referencyjnego
<img src='img/7.png'>

Film video z ćwiczeniem - pomiar referencyjny
<img src='img/8.png'>

Rozpoczęcie ćwiczenia - pomiar referencyjny
<img src='img/9.png'>

Rozpoczęcie badania
<img src='img/10.png'>

Badanie w trakcie
<img src='img/11.png'>

Podgląd wykresu dla wybranej taśmy
<img src='img/12.png'>

Wybór liczby taśm - TRYB MANUAL
<img src='img/13.png'>

Wybór użytkownika i typu mięśni badanych
<img src='img/14.png'>

Łączenie się z taśmami  - TRYB MANUAL
<img src='img/15.png'>

Badanie w trakcie - TRYB MANUAL
<img src='img/16.png'>
Podgląd wykresu jednej z wybranych taśm
<img src='img/17.png'>

POMOC 
<img src='img/18.png'>



#### Komunikacja

Do komunikacji wykorzystaliśmy protokół `GRPC`, gdzie łączymy się po sieci lan z stacją bazową i przesyłanie wyników następuje za pomocą biblioteki `Protobuf`

Klasa stacji bazowej(serverowa)
<img src='img/19.png'>

Klasa klienta(komputer diagnosty)
<img src='img/20.png'>

Protobuf wynikowy
<img src='img/21.png'>


#### Baza danych

Dodatno strukturę tabeli, która bęzie osobna do każego badania pomiarowego
<img src='img/24.png'>
<img src='img/25.png'>
