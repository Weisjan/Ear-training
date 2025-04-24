# Ear Training

A simple application for ear training that helps users practice recognizing musical intervals. The app plays two notes one after the other, and the user must identify the interval between them.

## Requirements

* Python 3.10  
* Pygame 2.0.0  
* Tkinter (built-in with Python)

## File Structure

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

| No | File/Folder     | Description                                  |
|----|------------------|----------------------------------------------|
| 1  | `notes`          | Folder containing note audio files (mp3)     |
| 2  | `logic.py`       | Contains the core application logic          |
| 3  | `gui.py`         | Implements the graphical user interface      |
| 4  | `README.md`      | This README file                             |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Weisjan/Ear-training.git
   ```

2. Run `gui.py`

## How It Works

1. **Generate a Question**: The app plays two notes in sequence. The user must identify the musical interval between them.
2. **Submit Answer**: The user selects the interval from a dropdown menu and confirms the answer. The app checks it and updates the score.
3. **Replay Interval**: The user can click the "Replay" button to hear the interval again.
4. **New Interval**: The user can generate a new interval at any time by clicking the "New Interval" button.

- **`logic.py`**:
  - Contains functions for the main logic, including interval generation, sound playback, and answer checking.
  - Functions:
    - `play_sound(filename)`: Plays a sound file.
    - `generate_interval()`: Creates a new interval.
    - `replay_interval()`: Replays the current interval.
    - `check_answer(user_interval, correct_interval)`: Validates the user’s answer.

- **`gui.py`**:
  - Implements the GUI using Tkinter.
  - Creates buttons and dropdowns for user interaction.
  - Functions:
    - `new_interval()`: Generates a new interval.
    - `submit_answer()`: Validates user input and updates the score.
    - `replay_interval()`: Replays the current interval.

## Notes

- You can customize the app by adding more notes or interval types.

## Author

[Jan Weis](https://github.com/Weisjan)
