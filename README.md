# Linked-List-Music-Player-GUI
# Linked List Music Player GUI

## Short Description

A simple desktop music player built with Python 3.12 using a linked list to manage the playlist. Features a Tkinter GUI and pygame for audio playback.

---

## Description

This is a desktop music player application built using Python 3.12. It features a graphical user interface (GUI) created with Tkinter and uses pygame for audio playback. The playlist is managed using a doubly linked list, allowing you to add, delete, and navigate through songs efficiently.

## Features

* Add songs using a file dialog
* Play, Pause, and Resume songs
* Navigate through the playlist using Next and Previous buttons
* Shuffle songs randomly
* Delete songs from the playlist
* Playlist displayed in a GUI Listbox showing all added songs

## Requirements

* Python 3.12 (recommended, newer versions may not fully support pygame)
* pygame library

Install pygame using pip:

```
pip install pygame
```

## Usage

1. Run the Python file:

```
python music.py
```

2. Use the GUI buttons to:

   * **Add Song**: Select a .mp3 file to add to the playlist
   * **Play**: Play the selected song from the playlist
   * **Pause**: Pause the currently playing song
   * **Resume**: Resume playback
   * **Next / Previous**: Navigate through songs
   * **Shuffle**: Play a random song from the playlist
   * **Delete**: Remove a selected song from the playlist

3. The status label shows the currently playing song or current action

## Project Structure

```
MusicPlayer/
├─ music.py                     # Main Python file with GUI and playlist logic
├─ musica/                      # Optional folder for storing .mp3 songs
└─ README.md                     # README file with instructions
```

## Notes

* Ensure .mp3 files are accessible and not corrupted
* Playlist uses a linked list internally, preserving the order of songs added
* Works on desktop platforms where Python 3.12 and pygame are supported
