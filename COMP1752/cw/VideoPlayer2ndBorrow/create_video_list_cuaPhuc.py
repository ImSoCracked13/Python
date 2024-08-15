import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class CreateVideoList():
    def __init__(self, window):
        window.geometry("1600x900")
        window.title("Create Video List")

        create_video_list_btn = tk.Button(window, text="Create Video List", command=self.create_video_list_clicked)
        create_video_list_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_a_name_lbl = tk.Label(window, text="Enter a Name")
        enter_a_name_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.name_txt = tk.Entry(window, width=16)
        self.name_txt.grid(row=0, column=2, padx=10, pady=10)

        enter_a_number_lbl = tk.Label(window, text="Enter a Number")
        enter_a_number_lbl.grid(row=0, column=3, padx=10, pady=10)

        self.number_txt = tk.Entry(window, width=2)
        self.number_txt.grid(row=0, column=4, padx=10, pady=10)

        enter_rating_lbl = tk.Label(window, text="Enter Rating")
        enter_rating_lbl.grid(row=0, column=5, padx=10, pady=10)

        self.rating_txt = tk.Entry(window, width=2)
        self.rating_txt.grid(row=0, column=6, padx=10, pady=10)

        add_video_to_list_btn = tk.Button(window, text="Add Video to List", command=self.add_song_to_list_clicked)
        add_video_to_list_btn.grid(row=0, column=7, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=80, height=40, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(window, width=40, height=20, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.create_video_list_clicked()
        self.add_song_to_list_clicked()

    def enter_a_name_condition(self):
        self.name_txt == ""
        if self.name_txt is not None:
            raise ValueError("Name must not be empty!")

    def enter_a_number_condition(self):
        self.number_txt == int
        if self.number_txt is not int:
            raise ValueError("Number must be an integer!")

    def enter_a_rating_condition(self):
        self.rating_txt == "*"
        if self.rating_txt is not "*":
            raise ValueError("Rating must type as an asterisk")
        elif self.rating_txt("*") > 5 or  self.rating_txt("*") <= 0:
            raise ValueError("Rating stars must be in the range of 0 to 5!")

    def add_song_to_list_clicked(self):
        self.list = [self.name_txt, self.number_txt, self.rating_txt]
        self.list.append()
        self.list = f"{self.name_txt} - {self.number_txt} {self.rating_txt}" 
        self.status_lbl.configure(text="Add Video to List button was clicked! Video has been added to the list")

    def create_video_list_clicked(self):
        self.list = lib.list_all()
        name = lib.get_name(list)
        list_description = self.list
        if name is not None:
            director = lib.get_director(list_description)
            rating = lib.get_rating(list_description)
            play_count = lib.get_play_count(list_description)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"{list_description}")
        self.status_lbl.configure(text="Create Video List button was clicked!")

#if __name__ == "__main__":  # only runs when this file is run as a standalone
#    window = tk.Tk()  # create a TK object
#   CreateVideoList(window)  # open the CheckVideo GUI
#   window.mainloop()  # run the window main loop, reacting to button presses, etc