from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry('256x144')
window.title('Cinema')

def cbMovies_clicked():
    movie_name = cbMovies.get()
    info = movies[movie_name][0]
    rotten_tomatoes_score = movies[movie_name][1]
    lblInfo.config(text='Movie info: ' + str(info))
    lblRottenTomatoes.config(text='Rotten Tomatoes score: ')

def btnBuy_clicked():
    


lblMovie = Label(window, text='Select a movie', justify=LEFT)
lblMovie.grid(column=0, row=0, sticky='w')
cbMovies = Combobox(window, change=cbMovies_clicked)
cbMovies.bind("<<Combobox Selected>>", cbMovies_clicked)
cbMovies['values'] = ['Jujutsu Kaisen 0', 'Kimetsu No Yaiba: Mugen Kessha-sen', 'Shingeki No Kyojin: Owari-hen', 'Kaifuku no Yarinaoshi: Hentai-sen']
movies = [('Jujutsu Kaisen 0': ('Directed by Sunghoo Park', 91%)),('Kimetsu No Yaiba: Mugen Kessha-sen': ('Directed by Haruo Sotozaki': 90%))]
cbMovies.current(0)
cbMovies.grid(column=1, row=0, sticky='w')

lblInfo = Label(window, text='Movie Info')
lblInfo.grid(column=0, row=1, sticky='w')
lblRottenTomatoes = Label(window, text='Rotten Tomatoes rating')
lblRottenTomatoes.grid(column=0, row=2, sticky='w')

lblTickets = Label(window, text='Number of tickets')
lblTickets.grid(column=0, row=3, sticky='w')
txtTickets = Entry(window, width=10)
txtTickets.grid(column=0, row=4, sticky='w')
btnBuy = Button(window, text='Buy', command=btnBuy_clicked()













