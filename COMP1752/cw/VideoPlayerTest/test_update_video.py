# An existed module of Python to work as forming a Window-like application
import tkinter as tk
import tkinter.messagebox as messagebox
import test_video_library as lib


# This class is for the third button functionality in the video_player main program to update rating stars
class UpdateVideos:
    def __init__(self, window):
        window.geometry("600x200") # Windowed displayed size
        window.title("Update Videos") # The title
        window.configure(background= "#008080") # Background color


# A labeled text for showing Enter Video textbox is next to it, to type number
        video_number_lbl = tk.Label(window, text="Enter Video Number", background="#F88379")
        video_number_lbl.grid(row=0, column=0, padx=10, pady=10)


# The text box used for search out specific video to proceed changing rating score
        self.video_number_entry = tk.Entry(window, background="#FF00FF")
        self.video_number_entry.grid(row=0, column=2, padx=10, pady=10)


# A labeled text for showing Enter Video New Rating next to it, also type number to change the new rating of the specific video
        rating_lbl = tk.Label(window, text="Enter Video New Rating", background="#F88379")
        rating_lbl.grid(row=1, column=0, padx=10, pady=10)


# This text box is after successfully browse the right video then it will adjust the rating score when a new nubmer is typed down
        self.rating_entry = tk.Entry(window, background="#FF00FF")
        self.rating_entry.grid(row=1, column=2, padx=10, pady=10)


# The button is for clarification the whole process, so as a message box will pop-up to notice whether the syntax is correct or wrong
        update_btn = tk.Button(window, text="Update Video", command=self.update_video, background="#F88379")
        update_btn.grid(row=2, column=1, padx=10, pady=10)


# The primary function for the operation works
    def update_video(self):
        video_number = self.video_number_entry.get() # Getting video number result when write down
        rating = self.rating_entry.get() # Applying for the new rating 
        # Every possible error if the user type down wrongfully
        if not video_number.isdigit():
            messagebox.showerror("Error!", "Invalid video number!") # If video number is not an integer
            return
        name = lib.get_name(video_number)
        if name is None:
            messagebox.showerror("Error!", f"Video {video_number} not found!") # If it is blank
            return
        if not rating.isdigit():
            messagebox.showerror("Error!", "Invalid rating!") # If rating case not an integer
            return
        # Save to Database and when type correctly, it will appear a success message
        rating = int(rating)
        play_count = lib.get_play_count(video_number)
        lib.update_rating(video_number, rating)
        lib.save_video_library() 
        messagebox.showinfo("Success!", f"Video: {name}\nNew Rating: {rating}\nPlay Count: {play_count}")


# Seperated operation of this file
if __name__ == "__main__":
    window = tk.Tk()
    UpdateVideos(window)
    window.mainloop()