from tkinter import *
from check_videos import CheckVideos
from create_video_list import CreateVideoList


window = Tk()
window.geometry('1000x1000')
window.title('Media Player')
window.configure(background= "#333333")


#Check video button function
def Check_video_clicked():
    # Toplevel object which will be treated as a new window
    Check_video_window = Toplevel(window)
    CheckVideos(Check_video_window)


#Create video list
def Create_video_list_clicked():
    # Toplevel object which will be treated as a new window
    Create_video_list_window = Toplevel(window)
    CreateVideoList(Create_video_list_window)

    




#main buton from the main GUI
labelA = Label(window, text= 'Select an option by clicking one of the buttons below')
labelA.place(x = 300, y=10)

#check video button
Check_video_button = Button(window, text= 'Check videos', width=20, height=5, background="#458B74", command=Check_video_clicked)
Check_video_button.place(x=50, y=50)

#create video list button
Create_video_list_button = Button(window, text= 'Create video list', width=20, height=5, background="#458B74", command=Create_video_list_clicked)
Create_video_list_button.place(x=360, y=50)

#update video button
Update_video_button = Button(window, text= 'Update videos', width=20, height=5, background="#458B74")
Update_video_button.place(x=670, y=50)


window.mainloop()


