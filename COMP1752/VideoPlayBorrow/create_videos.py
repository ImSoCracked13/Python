import tkinter as tk
import tkinter.scrolledtext as tkst

import font_manager as fonts
import video_library as lib
import tkinter.messagebox as messagebox

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class CreateVideos:
    def __init__(self,window):
        window.geometry("800x400")
        window.title("Create Videos")

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=5)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        add_playlist_btn = tk.Button(window, text="Add", command=self.add_playlist_clicked)
        add_playlist_btn.grid(row=0, column=2, padx=10, pady=10)

        play_playlist_btn = tk.Button(window, text="Play", command=self.play_playlist_clicked)
        play_playlist_btn.grid(row=0, column=3, padx=10, pady=10)

        reset_playlist_btn = tk.Button(window, text="Reset", command=self.reset_playlist_clicked)
        reset_playlist_btn.grid(row=0, column=4, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.playlist = []

        # self.list2_txt = tk.Text(window, width=48, height=1, wrap="none")
        # self.list2_txt.grid(row= 2, column= 0, padx= 10, pady= 10 )

        self.list2_txt = tk.Label(window, text="", font=("Helvetica", 10))
        self.list2_txt.grid( row= 2, column= 0, padx= 10, pady= 10)


    def add_playlist_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            self.playlist.append(name)
            video_details = f"{name}\n"
            self.list_txt.insert(1.0, video_details)
        else:
            set_text(self.list_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Add button was clicked!")


    def play_playlist_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            videoname = lib.get_name(key)
            play_count = lib.increment_play_count(key)
            video_details = f"{videoname}: {play_count}"
            set_text(self.list_txt, videoname)
            self.list2_txt.configure(text= video_details)
        else:
            messagebox.showerror("Invalid Video")
        self.status_lbl.configure(text="Play button was clicked!")

    def reset_playlist_clicked(self):
        self.playlist.clear()

        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            self.list_txt.delete("1.0", tk.END)
            #self.list2_txt.delete("1.0", tk.END)
            self.list2_txt.configure(text="")
            lib.library["01"].play_count = 0
            lib.library["02"].play_count = 0
            lib.library["03"].play_count = 0
            lib.library["04"].play_count = 0
            lib.library["05"].play_count = 0
            self.status_lbl.configure(text="Reset button was clicked")
        else:
            self.list_txt.delete("1.0", tk.END)
            self.status_lbl.configure(text="Reset button was clicked")
            messagebox.showinfo("Playlist already clear")




if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    CreateVideos(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc