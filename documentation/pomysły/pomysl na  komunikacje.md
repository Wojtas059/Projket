## Jak  stworzyć komunikację

1.  Opracowanie standardu komunikacji: propozycja protos, z ustalonym nagłówkiem i długością, aby sprawnie odczytywać
2.  Przekazać do odpowiedniej funkcji decydującej co dalej zrobić z odebraną paczką
3.  odczytanie zawartości paczki w adekwatnej funkcji
4.  przekazanie do funkcji wykonawczej 
5.  Bezpieczne wątkowo, pewnie kolejka
6.  Opracować zarządzanie danymi, do bazy, sposób zapisu
7.  Oddzielna tabela dla każdego zapisu
8.  metody komunikacji, parsowanie komunikatów z jednego do drugiego urządzenia.
9.  Ustalenie procedur zachowania urządzenia w zależności od stanu:przesył danych z czujników itp, do określenia.
10. opracować uml, najlepiej
11. działanie na zasadzie deamona
12. okresowe spawdzenia stanu połączenia