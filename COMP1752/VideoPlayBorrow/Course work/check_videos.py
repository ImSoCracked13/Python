import tkinter as tk         # import tkinter
import tkinter.scrolledtext as tkst     # import tkinter.scrolledtext

from PIL import Image, ImageTk

import font_manager as fonts   # import font manager
import video_library as lib     # import video Library


def set_text(text_area, content):  # inserts content into the text_area 
    text_area.delete("1.0", tk.END)# first the existing content is deleted
    text_area.insert(1.0, content)# then the new content is inserted


class CheckVideos():  # Create a class to define the content
    def __init__(self, window):  # Self define in window
        window.geometry("750x350") # Size of window
        window.title("Check Videos") # Title of window

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked) # Button to list all videos
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10) # Styling the button

        enter_lbl = tk.Label(window, text="Enter Video Number")       # using label.tk as text
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)     # styling the text

        self.input_txt = tk.Entry(window, width=3)       # using input.tk as text field
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)    # styling the text field

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)   # using button.tk as button
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)     # styling the button

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")     # using list that can scrolled
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)     # styling the list

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")   # using text field as an output
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)     # styling the text field

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))     # To show the status
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)   # styling the status

        self.image_lbl = tk.Label(window)     # A label to show the image
        self.image_lbl.place(x=535, y=165)      # set the place by using x and y

        self.list_videos_clicked()  # show that list video button is clicked

    def check_video_clicked(self):   # FUnction to define check_video_clicked
        key = self.input_txt.get()  # convert input_txt to key
        name = lib.get_name(key)    # key access to video library
        if name is not None:    # If / Else statement to print output
            director = lib.get_director(key)   # the key allocate to director element from lib
            rating = lib.get_rating(key)       # the key allocate to rating element from lib
            play_count = lib.get_play_count(key)    # the key allocate to rating element from lib
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"     # video_details as output to show all the located element
            set_text(self.video_txt, video_details)     # output from located video_txt element to video_details
        else:   # Else statement
            set_text(self.video_txt, f"Video {key} not found")  # if key not found, print video {key} not found
        self.status_lbl.configure(text="Check Video button was clicked!")   # print status for Check Video button was clicked

        self.image = Image.open("Course work/img/tomandjerry.jpg")       # getting image from image's directory
        self.resize1 = self.image.resize((125, 125), Image.LANCZOS)     # style the image
        self.image1 = ImageTk.PhotoImage(self.resize1)                 # creating a PhotoImage

        self.image2 = Image.open("Course work/img/naruto.jpg")         # getting image from image's directory
        self.resize2 = self.image2.resize((125, 125), Image.LANCZOS)   # style the image
        self.image3 = ImageTk.PhotoImage(self.resize2)                # creating a PhotoImage

        self.image4 = Image.open("Course work/img/conan.jpg")        # getting image from image's directory
        self.resize3 = self.image4.resize((125, 125), Image.LANCZOS) # style the image
        self.image5 = ImageTk.PhotoImage(self.resize3)               # creating a PhotoImage

        self.image6 = Image.open("Course work/img/onepiece.jpg")       # getting image from image's directory
        self.resize4 = self.image6.resize((125, 125), Image.LANCZOS)   # style the image
        self.image7 = ImageTk.PhotoImage(self.resize4)                 # creating a PhotoImage

        self.image8 = Image.open("Course work/img/doraemon.jpg")                 # getting image from image's directory
        self.resize5 = self.image8.resize((125, 125), Image.LANCZOS)           # style the image
        self.image9 = ImageTk.PhotoImage(self.resize5)                        # creating a PhotoImage

        if key == "01":   # check if the key matches the video key "01"
            self.image_lbl.configure(image=self.image1)    # display the image associated with video key "01"

        elif key == "02":# check if the key matches the video key "02"
            self.image_lbl.configure(image=self.image3)    # display the image associated with video key "02"

        elif key == "03":# check if the key matches the video key "03"
            self.image_lbl.configure(image=self.image5)    # display the image associated with video key "03"

        elif key == "04":# check if the key matches the video key "04"
            self.image_lbl.configure(image=self.image7)    # display the image associated with video key "04"

        elif key == "05":# check if the key matches the video key "05"
            self.image_lbl.configure(image=self.image9)    # display the image associated with video key "05"

        else:
            set_text(self.video_txt, f"Video {key} not found") # display a message in the video text widget
            self.image_lbl.configure(image="") # clear the image label by configuring it with an empty image

    def list_videos_clicked(self):     # how to define list_videos_clicked
        video_list = lib.list_all()     # video_list get element from lib.list_all()
        set_text(self.list_txt, video_list)     # output from located list_txt to video_list
        self.status_lbl.configure(text="List Videos button was clicked!")    # print status for List Videos button was clicked


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    CheckVideos(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc
