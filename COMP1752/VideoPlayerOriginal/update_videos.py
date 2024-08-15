import tkinter as tk
import tkinter.scrolledtext as tkst

import font_manager as fonts
import video_library as lib

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class UpdateVideos:
    def __init__(self, window):
        window.geometry("550x450")
        window.title("Update Videos")

        enter_video_number_lbl = tk.Label(window, text="Enter Video Number")
        enter_video_number_lbl.grid(row=0, column=0, padx=24, pady=24)

        self.video_number_txt = tk.Entry(window, width=4)
        self.video_number_txt.grid(row=0, column=1, padx=24, pady=24)

        enter_video_new_rating_lbl = tk.Label(window, text="Enter Video New Rating")
        enter_video_new_rating_lbl.grid(row=1, column=0, padx=24, pady=24)

        self.new_rating_txt = tk.Entry(window, width=4)
        self.new_rating_txt.grid(row=1, column=1, padx=24, pady=24)

        update_new_video_btn = tk.Button(window, text="Update Video", command=self.update_video_clicked)
        update_new_video_btn.grid(row=0, column=2, padx=24, pady=24)

        list_videos_btn = tk.Button(window, text="List Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=2, column=2, padx=10, pady=10)

        self.info_txt = tkst.ScrolledText(window, width=36, height=12, wrap="none")
        self.info_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="Status", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)


    def update_video_clicked(self):
        video_number = self.video_number_txt.get()
        new_rating = self.new_rating_txt.get()
        video_name = lib.get_name(video_number)
        self.status_lbl.configure(text="Update Video button was clicked!")
        try:
            new_rating = int(new_rating)
        except ValueError:
            set_text(self.info_txt, "Invalid Value!")
            return
        if video_name is not None:
            lib.set_rating(video_number, new_rating)
            set_text(self.info_txt, f"Video {video_number} rating has changed to {new_rating}!")
        else:
            set_text(self.info_txt, f"Video {video_number} not found!")



    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.info_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")


if __name__ == "__main__":  
    window = tk.Tk()  
    fonts.configure()  
    UpdateVideos(window)  
    window.mainloop()