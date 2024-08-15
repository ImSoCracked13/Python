# An existed module of Python to work as forming a Window-like application
import tkinter as tk
import tkinter.scrolledtext as tkst


# Linkage files inside the folder to act as supporting Classes to operate this file 
import font_manager as fonts
import video_library as lib

# Insert a function textarea for searching content.
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

# This the class as the first button for checking in the library music database
class CheckVideos():
    def __init__(self, window):
        window.geometry("750x350") # Size of the window when running
        window.title("Check Videos") # The title of the window, located at the top left next to a favicon
        window.configure(background= "#008080") # Additional background color setting


        # A button to list videos
        list_videos_btn = tk.Button(window, text="Show Current Video List", command=self.show_current_video_list_clicked, background="#F88379")
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)


        # A labeled text for knowing to type the video number
        enter_lbl = tk.Label(window, text="Enter Video Number", background="#F88379")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)


        # A text box inserted for entering Number to navigate the corresponding information provided in the database
        self.input_txt = tk.Entry(window, width=3, background="#FF00FF")
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)


        # Having a function written to find the same information when the search textbox entered.
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked, background="#F88379")
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)


        # This is a textarea but having a function to scroll down when having more data provided in the limit, it will automatically add more space to see underneath
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none", background="#FF00FF")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)


        # A side textarea contains the information when searched out succesffully in the database
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none", background="#FF00FF")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)


        # Word font for every typed words in the window, including displayed words.
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), background="#FF00FF")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)


# This function provided for listing every data included in the lib file
    def show_current_video_list_clicked(self):
        self.list = lib.list_all() # A callback from video_library file to list all videos in the database
        name = lib.get_name(list) 
        list_description = self.list # Getting information from the database
        if name is not None:
            director = lib.get_director(list_description)
            rating = lib.get_rating(list_description)
            play_count = lib.get_play_count(list_description)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.list_txt, video_details) # The displayed information is provided in the list textarea
        else:
            set_text(self.list_txt, f"{list_description}")
        self.status_lbl.configure(text="Show Current Video List button was clicked!")


# A syntax function for checking whether the search is correct or incorrect, in order to notice the user they are typing the right information
    def check_video_clicked(self):
        key = self.input_txt.get() # The text when write on, will return its exact wanted results
        name = lib.get_name(key) # Getting the data from the library
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"Video: {name}\nArtist: {director}\nRating: {rating}\nPlays: {play_count}"
            set_text(self.video_txt, video_details) # The display when the number type down correctly
        else:
            set_text(self.video_txt, f"Video {key} not found") # Incorrect case when the text write down is invalid
        self.status_lbl.configure(text="Check Video button was clicked!")


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    CheckVideos(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc

