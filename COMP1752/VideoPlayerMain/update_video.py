# An existed module of Python to work as forming a Window-like application
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.scrolledtext as tkst
import video_library as lib


# Insert a function textarea for searching content.
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


# This class is for the third button functionality in the video_player main program to update rating stars
class UpdateVideos:
    def __init__(self, window):
        window.geometry("600x400") # Windowed displayed size
        window.title("Update Videos") # The title
        window.configure(background= "#008080") # Background color


# A labeled text for showing Enter Video textbox is next to it, to type number
        video_number_lbl = tk.Label(window, text="Enter Video Number", background="#F88379")
        video_number_lbl.pack()


# The text box used for search out specific video to proceed changing rating score
        self.video_number_entry = tk.Entry(window, background="#FF00FF")
        self.video_number_entry.pack()


# A labeled text for showing Enter Video New Rating next to it, also type number to change the new rating of the specific video
        rating_lbl = tk.Label(window, text="Enter New Video Rating", background="#F88379")
        rating_lbl.pack()


# This text box is after successfully browse the right video then it will adjust the rating score when a new nubmer is typed down
        self.rating_entry = tk.Entry(window, background="#FF00FF")
        self.rating_entry.pack()


# The button is for clarification the whole process, so as a message box will pop-up to notice whether the syntax is correct or wrong
        update_btn = tk.Button(window, text="Update Video Rating", command=self.update_video_rating, background="#F88379")
        update_btn.pack()


# A minor fixed and replicated code line from the check_video file to show list in the database
        show_current_video_list_btn = tk.Button(window, text="Show Current Video List", command=self.show_current_video_list_clicked, background="#F88379")
        show_current_video_list_btn.pack()


# For the last one, after the show_current_video_list information function above clicked, the data will appear in the textarea
        self.video_txt = tkst.ScrolledText(window, width=40, height=10, wrap="none", background="#FF00FF")
        self.video_txt.pack()

# Not to important section, but this code line works independently as making the word font clearer to read
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), background="#FF00FF")
        self.status_lbl.pack()


# The primary function for the operation works
    def update_video_rating(self):
        video_number = self.video_number_entry.get() # Getting video number result when write down
        rating = self.rating_entry.get() # Applying for the new rating 
        # Every possible error if the user type down wrongfully
        if not video_number.isdigit():
            self.show_error_message("Invalid video number input!") # If video number is not an integer
            return
        name = lib.get_name(video_number)
        if name is None:
            self.show_error_message(f"Video {video_number} not found!") # If it is blank
            return
        if not rating.isdigit():
            self.show_error_message("Invalid rating input!") # If rating case not an integer
            return
        # Save to Database and when type correctly, it will appear a success message
        rating = int(rating)
        play_count = lib.get_play_count(video_number)
        lib.update_rating(video_number, rating)
        lib.save_video_library() # A new applied code from lib file to save the data has altered
        self.status_lbl.configure(text="Update Video Rating button was clicked!")
        self.show_info_message(f"Video: {name}\nNew Rating: {rating}") # The display


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


# Seperated operation of this file
if __name__ == "__main__":
    window = tk.Tk()
    UpdateVideos(window)
    window.mainloop()