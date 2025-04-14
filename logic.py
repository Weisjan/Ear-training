import random
import pygame

pygame.init()

INTERVALS = {
    1: "sekunda mała",
    2: "sekunda wielka",
    3: "tercja mała",
    4: "tercja wielka",
    5: "kwarta czysta",
    6: "tryton",
    7: "kwinta czysta",
    8: "seksta mała",
    9: "seksta wielka",
    10: "septyma mała",
    11: "septyma wielka",
    12: "oktawa czysta"
}

notes = ['G#', "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"]

SOUNDS = [f"notes/{note}{octave}.mp3" for octave in range(3, 6) for note in notes]

first_sound_index = None
second_sound_index = None

def play_sound(filename):
    sound = pygame.mixer.Sound(filename)
    sound.play()

def generate_interval():
    global first_sound_index, second_sound_index
    max_interval = 12

    first_sound_index = random.randint(0, len(SOUNDS) - max_interval - 1)
    second_sound_index = random.randint(first_sound_index + 1, first_sound_index + max_interval)

    play_sound(SOUNDS[first_sound_index])
    pygame.time.wait(700)
    play_sound(SOUNDS[second_sound_index])

    interval = abs(second_sound_index - first_sound_index)

    return INTERVALS.get(interval, None)

def replay_interval():
    if first_sound_index is not None and second_sound_index is not None:
        play_sound(SOUNDS[first_sound_index])
        pygame.time.wait(700)
        play_sound(SOUNDS[second_sound_index])

def check_answer(user_interval, correct_interval):
    return user_interval.strip().lower() == correct_interval.strip().lower()
