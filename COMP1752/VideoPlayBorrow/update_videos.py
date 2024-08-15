import tkinter as tk

import font_manager as fonts
import video_library as lib
import tkinter.messagebox as messagebox


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateVideos:
    def __init__(self,window):
        window.geometry("415x350")
        window.title("Update Videos")

        enter_lbl = tk.Label(window, text="Enter Video Number:")
        enter_lbl.grid(row=1, column=0, padx=0, pady=0)

        self.input_txt = tk.Entry(window, width=5)
        self.input_txt.grid(row=1, column=1, padx=0, pady=0)

        enter_lbl = tk.Label(window, text="Enter New Rating    :")
        enter_lbl.grid(row=2, column=0, padx=0, pady=5)

        self.input_rating_txt = tk.Entry(window, width=5)
        self.input_rating_txt.grid(row=2, column=1, padx=0, pady=0)

        update_btn = tk.Button(window, text="Update", width=30, command=self.update_btn_clicked)
        update_btn.grid(row=3, column=0, padx=0, pady=10)

        self.list_txt = tk.Text(window, width=43, height=8, wrap="none")
        self.list_txt.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=4, column=0, columnspan=4, sticky="W", padx=10, pady=10)

    def update_btn_clicked(self):
        key = self.input_txt.get()
        rating = self.input_rating_txt.get()
        name = lib.get_name(key)

        try: 
            rating = int(rating)
            # if rating < 1 or rating > 10:
            #     messagebox.showerror("Error", "Invalid rating")
            #     return
        except ValueError:
            set_text(self.list_txt, "Invalid rating")
            return

        if name is not None:
            lib.set_rating(key,rating)
            director = lib.get_director(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}\n"
            set_text(self.list_txt, video_details)
        else:
            set_text(self.list_txt, f"Video {key} not found")
            self.status_lbl.configure(text="Update button was clicked!")




if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    UpdateVideos(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc