# An existed module of Python to work as forming a Window-like application
import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.messagebox as messagebox


# Linkage files inside the folder to act as supporting Classes to operate this file 
import test_font_manager as fonts
import test_video_library as lib


# Insert a function textarea for searching content.
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


# A class associated with the second main function for the creating video list.
class CreateVideoList():
    def __init__(self, window):
        window.geometry("1600x900") # Size of the window when running
        window.title("Create Video List") # The title
        window.configure(background= "#008080") # Addition background color configuration for the aesthetic

        self.playlist = [] # An array for later playlist function to operate
        self.playlist_video_number = [] # Another array for setting video number


# A minor fixed and replicated code line from the check_video file to show list in the database
        show_current_video_list_btn = tk.Button(window, text="Show Current Video List", command=self.show_current_video_list_clicked, background="#F88379")
        show_current_video_list_btn.grid(row=0, column=0, padx=10, pady=10)


# A default labeled text to notify user where to type next
        enter_a_name_lbl = tk.Label(window, text="Enter a Number/Name of the Video", background="#FF00FF")
        enter_a_name_lbl.grid(row=0, column=1, padx=10, pady=10)



        self.name_txt = tk.Entry(window, width=16, background="#FF00FF")
        self.name_txt.grid(row=0, column=2, padx=10, pady=10)


# After done typing down the wanted video to add in the list, this clickable works as an aftermath result to fill all the data in the textarea
        add_video_to_list_btn = tk.Button(window, text="Add Video to List", command=self.add_video_to_list_clicked, background="#F88379")
        add_video_to_list_btn.grid(row=0, column=3, padx=10, pady=10)


# The button operate as a simulation as for videos in the list_txt has already added the desirable list. so as it will show a message box to know whether the current included videos run.
        play_btn = tk.Button(window, text="Play the video Playlist", command=self.play_video_playlist, background="#F88379")
        play_btn.grid(row=0, column=4, padx=10, pady=10)


# This button is use for erasing all the added video in the list textarea 
        reset_btn = tk.Button(window, text="Reset the Video Playlist", command=self.reset_video_playlist, background="#F88379")
        reset_btn.grid(row=0, column=5, padx=10, pady=10)


# This textarea is when the add_video_to_list clicked as having the same wording for the browsing in the database, it will simultenaously link then appear in it; then the message box will also notify
        self.list_txt = tkst.ScrolledText(window, width=80, height=40, wrap="none", background="#FF00FF")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)


# For the last one, after the show_current_video_list information function above clicked, the data will appear in the textarea
        self.video_txt = tk.Text(window, width=40, height=20, wrap="none", background="#FF00FF")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)


# Not to important section, but this code line works independently as making the word font clearer to read
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), background="#FF00FF")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)


# This function is for adding the video when typed down correctly number of the video, it will added successfully in the list textarea
    def add_video_to_list_clicked(self):
        video_number = self.name_txt.get()
        video_name = lib.get_name(video_number)
        if video_name is not None:
            self.playlist.append(video_name)
            self.playlist_video_number.append(video_number)
            self.update_playlist_text()
            self.show_info_message("Video Added!")
            self.status_lbl.configure(text="Add Video to List button was clicked!")
        else:
            self.show_error_message(f"Video {video_number} not found! Or text cannot be blank!")


# By having the wanted listed add in the list textarea and then play the list, this function is for the play button accumulates number of play counts every videos in the list.
    def play_video_playlist(self):
        for video_number in self.playlist_video_number:
            lib.increment_play_count(video_number) # Updating the play count
        self.show_info_message("Video in Playlist played!")
        lib.save_video_library()
        
        self.status_lbl.configure(text="Play the Video Playlist button was clicked!")


# To delete every displayed that video has added to the textarea, this is the function
    def reset_video_playlist(self):
        self.playlist = []
        self.update_playlist_text()
        self.status_lbl.configure(text="Reset the Video Playlist button was clicked!")


# After by one another video added in the textarea, this function works as a sub-operator to automatically break the line to down the underneath line.
    def update_playlist_text(self):
        self.list_txt.delete("1.0", tk.END)
        for video_name in self.playlist:
            self.list_txt.insert(tk.END, video_name + "\n")


# This is an editted and yet mostly reused function from the check_video class to make clear browse to add video to list correctly 
    def show_current_video_list_clicked(self):
        self.list = lib.list_all()
        name = lib.get_name(list)
        list_description = self.list # Getting information from the database
        if name is not None:
            director = lib.get_director(list_description)
            rating = lib.get_rating(list_description)
            play_count = lib.get_play_count(list_description)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"{list_description}")
        self.status_lbl.configure(text="Show Current Video List button was clicked!")


# An imported function from messagebox module to work as a pop-up Error Notification
    def show_error_message(self, message):
        messagebox.showerror("Error", message)


# An imported function from messagebox module to work as a pop-up Positive Notification
    def show_info_message(self, message):
        messagebox.showinfo("Information", message)


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    CreateVideoList(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc