from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
from PIL import ImageTk
import os
import vlc


window = Tk()


class PyMediaPlayer(Frame):

    appbackground = '#e6ecf0'
    widgetbackground = '#ffffff'
    activewidgetbackground = '#737678'
    logocolor = '#0184b4'
    activelogocolor = '#0084b4'

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.create_ui()
        self.extract_files()
        self.create_player()

    def create_ui(self):

        self.parent.title("PyMediaPlayer")
        self.place(relwidth=1, relheight=1)

        style = Style()
        style.configure("TFrame", bg=self.appbackground)
        style.configure("TButton", bg=self.widgetbackground, bd=0)

        original_frame = Frame(window, style='TFrame')
        original_frame.place(relx=0, rely=0, width=400, relheight=1)

        album_logo = Label(original_frame, text="Logo of your Album", anchor=CENTER, background=self.widgetbackground)
        album_logo.place(relx=0.5, rely=0.25, width=300, height=250, anchor=CENTER)

        song_tittle = "{} - {}".format(vlc.Meta.Artist, vlc.Meta.Title)
        title_label = Label(original_frame, text=song_tittle, anchor=CENTER, background=self.widgetbackground)
        title_label.place(relx=0.5, rely=0.5, width=400, relheight=0.1, anchor=CENTER)

        scroll_track_time = Scale(original_frame, orient=HORIZONTAL)
        scroll_track_time.place(relx=0.5, rely=0.6, width=400, relheight=0.1, anchor=CENTER)

        equalizer = Label(original_frame, text="There will be equalizer", anchor=CENTER, background=self.widgetbackground)
        equalizer.place(relx=0.5, rely=0.7, width=400, relheight=0.1, anchor=CENTER)

        buttons_frame = Frame(original_frame, style='TFrame')
        buttons_frame.place(relx=0.5, rely=0.85, width=400, height=50, anchor=CENTER)

        self.play_image = ImageTk.PhotoImage(file='play.png')
        play_button = Button(buttons_frame, image=self.play_image)
        play_button.config(command=self.playsong)
        play_button.place(relx=0, rely=0, width=50, height=50)

        self.pause_image = ImageTk.PhotoImage(file='pause.png')
        pause_button = Button(buttons_frame, image=self.pause_image)
        pause_button.config(command=self.pausesong)
        pause_button.place(relx=0.125, rely=0, width=50, height=50)

        self.stop_image = ImageTk.PhotoImage(file='stop.png')
        stop_button = Button(buttons_frame, image=self.stop_image)
        stop_button.config(command=self.stop)
        stop_button.place(relx=0.250, rely=0, width=50, height=50)

        self.echo_image = ImageTk.PhotoImage(file='reverb.png')
        echo_button = Button(buttons_frame, image=self.echo_image)
        echo_button.config(command=self.echo_effect)
        echo_button.place(relx=0.375, rely=0, width=50, height=50)

        self.volume_image = ImageTk.PhotoImage(file='volume.png')
        volume_button = Button(buttons_frame, image=self.volume_image)
        volume_button.bind("<Enter>", self.volume)
        volume_button.place(relx=0.500, rely=0, width=50, height=50)

        self.mute_image = ImageTk.PhotoImage(file='mute.png')
        mute_button = Button(buttons_frame, image=self.mute_image)
        mute_button.config(command=self.mute)
        mute_button.place(relx=0.625, rely=0, width=50, height=50)

        self.search_image = ImageTk.PhotoImage(file='search.png')
        open_file_button = Button(buttons_frame, image=self.search_image, style="TButton")
        open_file_button.config(command=self.extract_files)
        open_file_button.place(relx=0.750, rely=0, width=50, height=50)

        self.equalizer_image = ImageTk.PhotoImage(file='equalizer.png')
        configuration_button = Button(buttons_frame, image=self.equalizer_image)
        configuration_button.config(command=self.sound_configuration)
        configuration_button.place(relx=0.875, rely=0, width=50, height=50)

    def extract_files(self):
        self.filename = askopenfilename(filetypes=[("Mp3 Files", "*.mp3;*.wav;")])
        self.filename = os.path.abspath(self.filename)
        print(self.filename)
        return self.filename

    def create_player(self):
        self.player = vlc.MediaPlayer(self.filename)

    def playsong(self):
        self.player.play()

    def pausesong(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def echo_effect(self):
        yield

    def volume(self):
        yield

    def mute(self):
        self.player.audio_set_mute(True)

    def sound_configuration(self):
        equalizer_window = Toplevel(window)
        equalizer_window.geometry('300x200')




def main():

    width_monitor = window.winfo_screenwidth()
    height_monitor = window.winfo_screenheight()
    width_monitor = width_monitor // 2
    height_monitor = height_monitor // 2
    width_monitor = width_monitor - 200
    height_monitor = height_monitor - 250
    window.geometry('400x500+{}+{}'.format(width_monitor, height_monitor))
    window.minsize(400, 500)
    window.resizable(True, True)

    app = PyMediaPlayer(window)
    app.mainloop()


if __name__ == '__main__':
    main()
