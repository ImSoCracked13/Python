from tkinter import *
import tkinter.scrolledtext as tkst

import video_library as lib

def set_text(text_area, content):
    text_area.delete("1.0", END)
    text_area.insert(1.0, content)


class CreateVideoList():
    def __init__(self, window):
        window.geometry("1600x900")
        window.title("Check Videos")
        window.configure(background= "#333333")

        self.playlist = []

        enter_playlist_name_lbl = Label(window, text="Enter Playlist's name", background="#458B74")
        enter_playlist_name_lbl.grid(row=0, column=0, padx=24, pady=24)

        self.name_txt = Entry(window, width=30)
        self.name_txt.grid(row=0, column=1, padx=24, pady=24)

        create_video_list_btn = Button(window, text="Create Video List", background="#458B74", command=self.create_playlist_clicked)
        create_video_list_btn.grid(row=0, column=2, padx=24, pady=24)

        list_videos_btn = Button(window, text="List All Videos in the library", command=self.list_videos_clicked,  background="#458B74")
        list_videos_btn.grid(row=0, column=3, padx=24, pady=24)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=9, pady=9)

        enter_video_to_add_lbl = Label(window, text="Enter Video Number to add to new playlist",  background="#458B74")
        enter_video_to_add_lbl.grid(row=2, column=0, padx=24, pady=24)

        self.input_vide0_add_txt = Entry(window, width=7)
        self.input_vide0_add_txt.grid(row=2, column=1, padx=9, pady=9)

        add_button = Button(window, text="Add", background="#458B74", command=self.add_video_to_playlist)
        add_button.grid(row=2, column=2, padx=9, pady=9)

        self.playlist_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.playlist_txt.grid(row=1, column=2, columnspan=3, sticky="W", padx=9, pady=9)


    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)


    def create_playlist_clicked(self):
        playlist_name = self.name_txt.get()
        if playlist_name == None:
            raise ValueError("Name cannot be NULL")
        set_text(self.playlist_txt, playlist_name)


    def add_video_to_playlist(self):
        number_to_add = self.input_vide0_add_txt.get()
        video_to_add = lib.get_name(number_to_add)
        if video_to_add is not None:
            self.playlist.append(video_to_add)
            set_text(self.playlist_txt, self.playlist)
        else:
            set_text(self.playlist_txt, f"Video {number_to_add} not found")
