# alarm.py
# Generates and plays a beep alarm — no audio file needed!

import pygame
import numpy as np

pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)


def generate_beep(frequency=1000, duration=1.5, volume=0.9):
    """
    Creates a beep sound using a sine wave.
    frequency : pitch in Hz  (higher = shriller)
    duration  : length in seconds
    volume    : 0.0 to 1.0
    """
    sample_rate = 44100
    n_samples   = int(sample_rate * duration)

    t    = np.linspace(0, duration, n_samples, endpoint=False)
    wave = (np.sin(2 * np.pi * frequency * t) * 32767 * volume).astype(np.int16)

    return pygame.sndarray.make_sound(wave)


# Pre-load alarm sound once so it plays instantly
ALARM_SOUND = generate_beep(frequency=1000, duration=1.5, volume=0.9)


def play_alarm():
    """Plays alarm if not already playing."""
    if not pygame.mixer.get_busy():
        ALARM_SOUND.play()


def stop_alarm():
    """Stops the alarm."""
    pygame.mixer.stop()