import tkinter as tk
import tkinter.scrolledtext as tkst


import font_manager as fonts
import video_library as lib


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class CreateVideoList():
    def __init__(self, window, playlist_video_name=[], playlist_video_number=[]):
        window.geometry("800x500")
        window.title("Create Video List") 


        self.playlist_video_number = playlist_video_number 
        self.playlist_video_name = playlist_video_name 


        list_video_btn = tk.Button(window, text="List Videos", command=self.list_videos_clicked)
        list_video_btn.grid(row=0, column=0, padx=10, pady=10)


        enter_a_number_lbl = tk.Label(window, text="Enter Video Number")
        enter_a_number_lbl.grid(row=0, column=1, padx=10, pady=10)


        self.number_txt = tk.Entry(window, width=2)
        self.number_txt.grid(row=0, column=2, padx=10, pady=10)


        add_video_btn = tk.Button(window, text="Add Video", command=self.add_video_clicked)
        add_video_btn.grid(row=0, column=3, padx=10, pady=10)


        reset_video_playlist_btn = tk.Button(window, text="Reset Playlist", command=self.reset_playlist_clicked)
        reset_video_playlist_btn.grid(row=2, column=2, padx=10, pady=10)


        play_video_playlist_btn = tk.Button(window, text="Play Playlist", command=self.play_playlist_clicked)
        play_video_playlist_btn.grid(row=2, column=3, padx=10, pady=10)


        self.playlist_txt = tkst.ScrolledText(window, width=40, height=20, wrap="none")
        self.playlist_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)


        self.info_txt = tk.Text(window, width=40, height=20, wrap="none")
        self.info_txt.grid(row=1, column=3, sticky="W", padx=10, pady=10)


        self.status_lbl = tk.Label(window, text="Status", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)


    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.info_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")


    def add_video_clicked(self):
        video_number = self.number_txt.get() 
        video_name = lib.get_name(video_number)
        if video_name is not None:
            self.playlist_video_number.append(video_number)
            self.playlist_video_name.append(video_name)
            set_text(self.info_txt, f"Added Video {video_name}!")
        else:
            set_text(self.info_txt, f"Video {video_number} not found")
        video_name = lib.get_name(video_number)
        self.playlist_txt.insert(tk.END, video_name + "\n")
        self.status_lbl.configure(text="Add Video button was clicked!")


    def play_playlist_clicked(self):
        for video_number in self.playlist_video_number:
            lib.increment_play_count(video_number) 
        set_text(self.info_txt, "List played!")
        self.status_lbl.configure(text="Play Video Playlist button was clicked!") 


    def reset_playlist_clicked(self):
        set_text(self.playlist_txt, "")
        set_text(self.info_txt, "Playlist reset!")
        self.status_lbl.configure(text="Reset Playlist button was clicked!")


if __name__ == "__main__":  
    window = tk.Tk()  
    fonts.configure()  
    CreateVideoList(window) 
    window.mainloop() 