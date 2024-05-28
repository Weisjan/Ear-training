# Ear Training

Prosta aplikacja do treningu słuchu, która pomaga użytkownikowi ćwiczyć rozpoznawanie interwałów muzycznych. Aplikacja odtwarza dwa dźwięki jeden po drugim, a użytkownik musi zidentyfikować interwał między nimi.

## Wymagania

* Python 3.10
* Pygame 2.0.0
* Tkinter

## Struktura plików

```
Ear-training
├── notes
│   ├── A#3.mp3
│   ├── A#4.mp3
│   ├── A#5.mp3
│   └── ...
├── logic.py
├── gui.py
└── README.md
```

| Nr | Plik/Katalog    | Opis |
|----|-----------------|------|
| 1  | `notes`        | Katalog zawierający pliki dźwiękowe nut (format mp3) |
| 2  | `logic.py`      | Zawiera główną logikę aplikacji |
| 3  | `gui.py`        | Implementacja graficznego interfejsu użytkownika (GUI) |
| 4  | `README.md`     | Plik Readme |

## Instalacja

1. Sklonuj repozytorium:
   ```sh
   git clone https://github.com/Weisjan/Ear-training.git
   ```
2. Uruchom `gui.py`

## Opis działania

1. **Generowanie pytania**: Aplikacja odtwarza dwa dźwięki jeden po drugim. Użytkownik musi zidentyfikować interwał muzyczny między tymi dźwiękami.
2. **Zatwierdzenie odpowiedzi**: Użytkownik wybiera interwał z menu rozwijanego i zatwierdza swoją odpowiedź. Aplikacja sprawdza odpowiedź i aktualizuje wynik.
3. **Ponowne odtworzenie interwału**: Jeśli użytkownik chce ponownie usłyszeć dźwięki, może kliknąć przycisk "Odtwórz ponownie", aby ponownie odtworzyć dźwięki.
4. **Nowy interwał**: Użytkownik może w każdej chwili wygenerować nowy interwał, klikając przycisk "Nowy interwał".

- **`logic.py`**:
  - Zawiera funkcje do obsługi głównej logiki, w tym generowanie interwałów, odtwarzanie dźwięków i sprawdzanie odpowiedzi.
  - Funkcje:
    - `play_sound(filename)`: Odtwarza dany plik dźwiękowy.
    - `generate_interval()`: Generuje nowy interwał.
    - `replay_interval()`: Ponownie odtwarza bieżący interwał.
    - `check_answer(user_interval, correct_interval)`: Sprawdza, czy odpowiedź użytkownika jest poprawna.

- **`gui.py`**:
  - Implementuje GUI przy użyciu Tkinter.
  - Tworzy przyciski i menu rozwijane do interakcji z użytkownikiem.
  - Funkcje:
    - `new_interval()`: Generuje nowy interwał.
    - `submit_answer()`: Zatwierdza odpowiedź użytkownika i aktualizuje wynik.
    - `replay_interval()`: Ponownie odtwarza bieżący interwał.

## Uwagi

- Możesz dostosować aplikację do swoich potrzeb, na przykład dodając więcej nut lub interwałów.

## Autor

[Jan Weis](https://github.com/Weisjan)
