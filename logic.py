import random
import pygame

pygame.init()

INTERVALS = {
    "sekunda mała": 1,
    "sekunda wielka": 2,
    "tercja mała": 3,
    "tercja wielka": 4,
    "kwarta czysta": 5,
    "tryton": 6,
    "kwinta czysta": 7,
    "seksta mała": 8,
    "seksta wielka": 9,
    "septyma mała": 10,
    "septyma wielka": 11,
    "oktawa czysta": 12
}

SOUNDS = []
notes = ['G#', "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"]

for i in range(3):
    for note in notes:
        sound_filename = f"notes/{note}{i + 3}.mp3"
        SOUNDS.append(sound_filename)

first_sound_index = None
second_sound_index = None

def play_sound(filename):
    sound = pygame.mixer.Sound(filename)
    sound.play()

def get_interval_name(interval):
    for name, value in INTERVALS.items():
        if value == interval:
            return name
    return None

def generate_interval():
    global first_sound_index, second_sound_index
    first_sound_index = random.randint(0, len(SOUNDS) - 2)
    x = 12  # Zakres interwału, można zmienić
    if first_sound_index + x <= len(SOUNDS):
        second_sound_index = random.randint(first_sound_index + 1, first_sound_index + x)
    else:
        first_sound_index = 23
        second_sound_index = random.randint(first_sound_index + 1, len(SOUNDS) - 1)

    play_sound(SOUNDS[first_sound_index])
    pygame.time.wait(700)
    play_sound(SOUNDS[second_sound_index])

    interval = abs(second_sound_index - first_sound_index)
    interval_name = get_interval_name(interval)
    return interval_name

def replay_interval():
    if first_sound_index is not None and second_sound_index is not None:
        play_sound(SOUNDS[first_sound_index])
        pygame.time.wait(700)
        play_sound(SOUNDS[second_sound_index])

def check_answer(user_interval, correct_interval):
    return user_interval.lower() == correct_interval.lower()
