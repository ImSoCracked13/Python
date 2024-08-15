# An existed module of Python to work as forming a Window-like application
import tkinter as tk

# Linkage files inside the folder to act as supporting Classes to operate this file 
import font_manager as fonts
from check_videos import CheckVideos
from create_video_list import CreateVideoList
from update_video import UpdateVideos

# First button command to link 
def check_videos_clicked():
    status_lbl.configure(text="Check Videos button was clicked!")
    CheckVideos(tk.Toplevel(window))
# Second button command to link 
def create_video_list_clicked():
    status_lbl.configure(text="Create Video List button was clicked!")
    CreateVideoList(tk.Toplevel(window))
# Third button command to link 
def update_video_clicked():
    status_lbl.configure(text="Update Video button was clicked!")
    UpdateVideos(tk.Toplevel(window))
# The main window
window = tk.Tk()
window.geometry("520x150")
window.title("Video Player")
window.configure(background= "#008080")
# Fonts
fonts.configure()
# Header
header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below", background="#ff00ff")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# First button to Check Videos
check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked, background="#F88379")
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)
# Second button to create a video list
create_video_list_btn = tk.Button(window, text="Create Video List", command=create_video_list_clicked, background="#F88379")
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)
# Third button to update any video rating
update_videos_btn = tk.Button(window, text="Update Videos", command=update_video_clicked, background="#F88379")
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)
# Word font, not significant but quite useful for clear words
status_lbl = tk.Label(window, text="", font=("Helvetica", 10), background="#FF00FF")
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10, )
# Program Launcher
window.mainloop()