import tkinter as tk
from tkinter import filedialog
import pygame
import os
import random

# Initialize pygame mixer
pygame.mixer.init()

# Linked list node for songs
class SongNode:
    def __init__(self, song_path):
        self.song_path = song_path
        self.next = None
        self.prev = None

# Doubly linked list playlist
class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, song_path):
        new_node = SongNode(song_path)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node

    def delete_song(self, node):
        if not node:
            return
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        # Move current if needed
        if self.current == node:
            self.current = node.next or node.prev

    def play_song(self, node):
        if node:
            self.current = node
            pygame.mixer.music.load(node.song_path)
            pygame.mixer.music.play()
            return os.path.basename(node.song_path)
        return None

    def next_song(self):
        if self.current and self.current.next:
            return self.play_song(self.current.next)
        return None

    def prev_song(self):
        if self.current and self.current.prev:
            return self.play_song(self.current.prev)
        return None

    def shuffle_song(self):
        # Collect all nodes in a list
        nodes = []
        temp = self.head
        while temp:
            nodes.append(temp)
            temp = temp.next
        if nodes:
            node = random.choice(nodes)
            return self.play_song(node)
        return None

    def list_nodes(self):
        # Returns a list of nodes
        nodes = []
        temp = self.head
        while temp:
            nodes.append(temp)
            temp = temp.next
        return nodes

# GUI
root = tk.Tk()
root.title("Linked List Music Player")

playlist = Playlist()

# Tkinter widgets
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

status_label = tk.Label(root, text="No song playing", fg="blue")
status_label.pack(pady=5)

# Functions
def add_song():
    path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if path:
        node = playlist.add_song(path)
        listbox.insert(tk.END, os.path.basename(path))

def play_selected():
    try:
        index = listbox.curselection()[0]
        node = playlist.list_nodes()[index]
        song_name = playlist.play_song(node)
        if song_name:
            status_label.config(text=f"Playing: {song_name}")
    except IndexError:
        pass

def pause_song():
    pygame.mixer.music.pause()
    status_label.config(text="Paused")

def resume_song():
    pygame.mixer.music.unpause()
    if playlist.current:
        status_label.config(text=f"Playing: {os.path.basename(playlist.current.song_path)}")

def next_song():
    song_name = playlist.next_song()
    if song_name:
        status_label.config(text=f"Playing: {song_name}")

def prev_song():
    song_name = playlist.prev_song()
    if song_name:
        status_label.config(text=f"Playing: {song_name}")

def shuffle_song():
    song_name = playlist.shuffle_song()
    if song_name:
        status_label.config(text=f"Playing: {song_name}")

def delete_song():
    try:
        index = listbox.curselection()[0]
        node = playlist.list_nodes()[index]
        playlist.delete_song(node)
        listbox.delete(index)
        status_label.config(text="Song deleted")
    except IndexError:
        pass

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Add Song", command=add_song).grid(row=0, column=0)
tk.Button(frame, text="Play", command=play_selected).grid(row=0, column=1)
tk.Button(frame, text="Pause", command=pause_song).grid(row=0, column=2)
tk.Button(frame, text="Resume", command=resume_song).grid(row=0, column=3)
tk.Button(frame, text="Next", command=next_song).grid(row=1, column=0)
tk.Button(frame, text="Previous", command=prev_song).grid(row=1, column=1)
tk.Button(frame, text="Shuffle", command=shuffle_song).grid(row=1, column=2)
tk.Button(frame, text="Delete", command=delete_song).grid(row=1, column=3)

root.mainloop()
