INFO
================================

**Autor: Lissu**

**Prosty bot Discord do wyświetlania liczby graczy na serwerze MTA za pomocą ServerProject API.**

WYMAGANIA
=========
- Python 3.8+
- Konto Discord Developer
- Serwer MTA na ServerProject
- Klucz API ServerProject

INSTALACJA
==========

1. Zainstaluj zależności:
   pip install discord.py python-dotenv aiohttp

2. Skonfiguruj plik `.env`:
   Utwórz plik `.env` w tym samym folderze co `bot.py`:
   
   DISCORD_TOKEN=twój_token_discord
   API_KEY=twój_serverproject_api_key
   VOICE_CHANNEL_ID=id_kanału_głosowego

KONFIGURACJA
============

Discord Bot:
1. Wejdź na Discord Developer Portal
2. Stwórz nową aplikację
3. Przejdź do "Bot" → "Reset Token"
4. Skopiuj token do `.env`
5. Zaproś bota na serwer z uprawnieniem "Zarządzaj kanałami"

ServerProject API:
1. Zaloguj się do panelu ServerProject
2. Przejdź do swojego serwera MTA
3. Znajdź i skopiuj Public API Key
4. Wklej do `.env` jako `API_KEY`

ID Kanału:
1. Włącz tryb dewelopera w Discord
2. Kliknij PPM na kanale głosowym → "Kopiuj ID"
3. Wklej do `.env` jako `VOICE_CHANNEL_ID`

URUCHOMIENIE
============
python bot.py

DZIAŁANIE
=========
- Interwał: Co 10 minut (bezpieczny limit Discord)
- Sprawdzanie: Pobiera dane z ServerProject API
- Aktualizacja: Zmienia nazwę kanału tylko gdy liczba graczy się zmieni
- Format: Emoji + liczba graczy

WYŚWIETLANE STATUSY
===================
🟡 👥 Online: 0      - Serwer pusty
🟢 👥 Online: 5      - 1-9 graczy
🔵 👥 Online: 12     - 10-14 graczy
🔥 👥 Online: 20     - 15+ graczy
🔴 Serwer offline    - Serwer wyłączony

RATE LIMITING
=============
Discord ma surowe limity na zmianę nazw kanałów:
- Maksymalnie: 2 zmiany na 10 minut
- Bezpiecznie: 1 zmiana na 10 minut
- Ten bot: 1 zmiana na 10 minut (gdy się zmienia)

Bot zapamiętuje ostatnią liczbę graczy i aktualizuje tylko gdy:
1. Minęło 10 minut od ostatniej zmiany
2. Liczba graczy się zmieniła

ROZWIĄZYWANIE PROBLEMÓW
=======================

"Invalid Token"
- Sprawdź czy token w `.env` jest poprawny
- Upewnij się że nie ma spacji na początku/końcu

"Missing Access"
- Dodaj bota z uprawnieniem "Zarządzaj kanałami"
- Upewnij się że bot ma wyższą rolę niż kanał

"wrong_key" (API Error)
- Sprawdź czy klucz API jest poprawny
- Upewnij się że to Public API Key
- Skontaktuj się z supportem ServerProject

Bot nie aktualizuje kanału
- Sprawdź czy minęło 10 minut od ostatniej zmiany
- Sprawdź czy liczba graczy się zmieniła
- Sprawdź logi w konsoli

LOGI
====
Bot wyświetla informacje w konsoli:
✅ NICKBOTA#1234 - Bot uruchomiony
⏰ Aktualizacja co 10 minut (bezpieczny limit)
📝 14:30 - 👥 Online: 5
📝 14:40 - 🔵 👥 Online: 12

STRUKTURA PLIKÓW
================
/
├── bot.py              # Kod bota
├── .env               # Konfiguracja (NIE udostępniaj!)
├── requirements.txt   # Zależności (opcjonalnie)
└── README.md         # Ten plik

BEZPIECZEŃSTWO
==============
- NIGDY nie udostępniaj pliku `.env`
- Token Discord daje pełny dostęp do bota
- Klucz API daje dostęp do danych serwera
- Używaj osobnego konta Discord dla bota

WSPARCIE
========
W przypadku problemów:
1. Sprawdź czy wszystkie dane w `.env` są poprawne
2. Upewnij się że serwer MTA jest włączony
3. Sprawdź czy bot ma odpowiednie uprawnienia
4. Sprawdź logi w konsoli

ZMIANA INTERWAŁU
================
Aby zmienić interwał aktualizacji, zmień linię w kodzie:
@tasks.loop(minutes=10)  # Zmień 10 na inną wartość

Uwaga: Discord może zbanować bota za zbyt częste zmiany!

LICENCJA
========
Wolne użycie. Podaj autora jeśli modyfikujesz.

Wersja: 1
Ostatnia aktualizacja: Styczeń 2026
