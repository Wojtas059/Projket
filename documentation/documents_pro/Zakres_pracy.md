### Zakres pracy

> Wojciech Maj, Piotr Łach

Głównym celem pracy Wojciecha i Piotra jest stworzenie oprogramowania aplikacji  na potrzeby projektu.

### Wykaz funkcjonalności

#### Gość

##### Badanie
1. Przeprowadzenie badania w trybie AUTO

##### Zarządzanie kontem
1. Rejestracja
2. Logowanie 

##### Pomoc
1. Dostęp do pomocy

#### Użytkownik (podstawowy)
##### Badanie
1. Przeprowadzenie badania w trybie AUTO*
2. Przegląd historii badań(swoich)
   
##### Zarządzanie kontem
1. Wylogowanie się
2. Przegląd danych osobistych
3. Manualne przypisanie do trenera

##### Pomoc
1. Dostęp do pomocy

#### Użytkownik (wykwalifikowany)
##### Badanie
1. Przeprowadzenie badania w trybie MANUAL*
2. Przegląd historii badań wszystkich użytkowników podlegających*

##### Zarządzanie użytkownikami
1. Dodawanie nowych użytkowników(?)
2. Usuwanie nowych użytkowników
3. Modyfikacja danych użytkowników podlegających*
   
##### Zarządzanie kontem
1. Wylogowanie się
2. Przegląd i modyfikacja danych osobistych

##### Pomoc
1. Dostęp do pomocy



#### Moduł Logowania
1. Rejestracja 
2. Logowanie



#### Moduł Pomiarowy
1. Wybór użytkownika (istniejący)
2. Wybór metody pomiarowej
3. Wybór partii mięśni 
4. Wybór liczby taśm
5. Panel zarządzania taśmami
6. Rozpoczęcie pomiaru referencyjnego
7. Zapoznanie się z opisem ćwiczeń
8. Zakończenie pomiaru referencyjnego
9. Rozpoczęcie badania właściwego
10. Panel pomiarowy
> Powyższy moduł występuję w postaci dwóch trybów Auto i Manual, z czego pierwszy tryb jest ograniczony co do ilości użytkowników i ilości taśm sensorycznych (1 osoba, 2 taśmy).
> Wraz z niniejszym dokumentem załączonym jest dokument User_manuak_UML.pdf, który szczegółowo przedstawia powyższe tryby pomiarowe.

#### Moduł Bazy danych 
1. Stworzenie struktury bazy danych
2. Wdrożenie bazy danych
3. Przygotowanie skryptów bazo danowych

#### Moduł Analizy
1. Stworzenie algorytmu uczenia maszynowego*
2. Wdrożenie algorytmu uczenia maszynowego*




#### Moduł Pomocy
1. Wybór instrukcji obsługi
2. Wybór procedury pomiarowej
3. Wybór chatbota

| Np. |Element aplikacji | Przynależność | Odpowiedzialność | Przybliżony czas pracy |
|---|---|---|---|---|
|  | <b>Rozpoczęcie Etapu I</b> | || 
| 1.| Ekran logowania się aplikacji | GUI | W. Maj | 22.12.2021 |
| 2.| Obsługa bazy danych: logowania | Moduł Bazy danych | P.Łach | 22.12.2021|
| 3.| Widok Gościa | GUI | W. Maj |22.12.2021|
| 4.| Widok Użytkownika | GUI |P.Łach|22.12.2021|
| 5.| Widok Użytkownika (wykwalifikowanego) | GUI| W. Maj|22.12.2021|
| 6.| Implementacja modułu gościa z wyłączeniem. badań | Moduł Gościa |P.Łach|22.12.2021|
| 7.| Implementacja modułu użytkownika z wyłączeniem. badań | Moduł Użytkownika | W. Maj|22.12.2021|
| 8.| Implementacja modułu użytkownika (wykwalifikowanego) z wyłączeniem. badań | Moduł Użytkownika(wykwalifikowanego) |P.Łach|22.12.2021|
|| Przygotowanie raportu z Etapu I |Dokumentacja |W.Maj P.Łach|22.12.2021|
| | <span style="color:red">Zakończenie Etapu I</span> |||
| | <b>Rozpoczęcie Etapu II</b>||||
| 9.| Obsługa bazy danych: dane pomiarowe | Moduł Bazy danych | W.Maj | 15.01.2022|
|10.| Widoki trybu Auto |GUI | P.Łach|15.01.2022|
|11.| Widoki trybu Manual | GUI| W.Maj|15.01.2022|
|12.| Widoki pomocy | GUI| P.Łach|15.01.2022|
|13.| Implementacja modułu pomiarowego  | Moduł Pomiarowy | W.Maj|15.01.2022|
|15.| Implementacja modułu pomocy | Moduł Pomocy|P.Łach |15.01.2022|
|| Przygotowanie raportu z Etapu II |Dokumentacja |W.Maj P.Łach|17.01.2022|
| | <span style="color:red">Zakończenie Etapu II</span> |||
| | <b>Rozpoczęcie Etapu III</b>||||
|16.| Wdrożenie algorytmu klasyfikacji  | Moduł Analizy |W.Maj |3.02.2022|
|17.| Integracja sytemu | Aplikacja | P.Łach|3.02.2022|
|| Przygotowanie raportu z Etapu III  | Dokumentacja |W.Maj P.Łach|3.02.2022|
| | <span style="color:red">Zakończenie Etapu III</span> |||
| | <b>Rozpoczęcie Etapu IV</b>||||
|18.| Przeprowadzeni testów penetracyjnych| Bezpieczeństwo Bazy danych |W.Maj|28.02.2022|
|19.| Testy jednostkowe | Poprawność wykonywanych funkcji |  P.Łach|23.02.2022|
|20.| Testy integracyjne | Poprawność wykonywanych modułów | W.Maj|23.02.2022|
|21.| Testy użytkowe | Poprawność integracji aplikacji/systemu |W.Maj |23.02.2022|
|22.| Testy wydajnościowe | Badanie wydajności aplikacji oraz zasobów systemowych | P.Łach|23.02.2022|
|| Przygotowanie raportu z Etapu IV |Dokumentacja |W.Maj P.Łach|23.02.2022|
| | <span style="color:red">Zakończenie Etapu IV</span> |||
|| Przygotowanie raportu końcowego, podsumowanie wytwarzania aplikacji desktopowej |Dokumentacja |W.Maj P.Łach|26.02|
| | <span style="color:red">Zakończenie projektu</span> |||28.02.2022|




#### Legenda
> definicje pojęć oznaczonych: *

<i><b> Użytkownik podlegający </b></i>- osoba, która podlega pod danego trenera/lekarza itp. co daje możliwość także przeglądanie historii wyników badań a także modyfikacja danych podlegających użytkowników.

<i><b> Tryb AUTO </b></i>- podstawowy tryb badania jednej osoby, charakteryzujący się prostotą, dodatkowo polega na przeprowadzenie pomiarów za pomocą maksymalnie dwóch taśm sensorycznych.

<i><b> Tryb MANUAL </b></i>- Jest to rozszerzenie trybu AUTO dla większej ilości osób badanych i z możliwością wykorzystania większej ilości taśm sensorycznych przeznaczonych dla jednej osoby.


