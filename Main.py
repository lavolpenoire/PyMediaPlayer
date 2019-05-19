from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
import os
import vlc


class PyMediaPlayer(Frame):

    appbackground = '#d2d2d2'
    widgetbackground = '#a19c9c'
    activewidgetbackground = '#d4d8d4'
    logocolor = '#326ada'
    activelogocolor = '#433e90'

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.create_ui()

    def create_ui(self):

        self.parent.title("PyMediaPlayer")
        self.pack(fill=BOTH, expand=1)

        style = Style()
        style.configure("TFrame", bg=self.appbackground)
        style.configure("TButton", bg=self.widgetbackground)

        album_logo = Label(self, text="Logo of your Album", anchor=CENTER, background=self.widgetbackground)
        album_logo.place(relx=0.125, rely=0, relwidth=0.75, relheight=0.5)

        song_title = Label(self, text="Artist - Song Name", anchor=CENTER, background=self.widgetbackground)
        song_title.place(relx=0.5, rely=0.5, width=400, relheight=0.1, anchor=CENTER)

        scroll_track_time = Scale(self, orient=HORIZONTAL)
        scroll_track_time.place(relx=0.5, rely=0.6, width=400, relheight=0.1, anchor=CENTER)

        equalizer = Label(self, text="There will be equalizer", anchor=CENTER, background=self.widgetbackground)
        equalizer.place(relx=0.5, rely=0.7, width=400, relheight=0.2, anchor=CENTER)

        play_button = Button(self, text="PLAY")
        play_button.config(command=self.playsong)
        play_button.place(relx=0, rely=0.9, relwidth=0.08, relheight=0.08)

        pause_button = Button(self, text="PAUSE")
        pause_button.config(command=self.pausesong)
        pause_button.place(relx=0.125, rely=0.9, relwidth=0.08, relheight=0.08)

        stop_button = Button(self, text="STOP")
        stop_button.config(command=self.stop)
        stop_button.place(relx=0.250, rely=0.9, relwidth=0.08, relheight=0.08)

        echo_button = Button(self, text="ECHO")
        echo_button.config(command=self.echo_effect)
        echo_button.place(relx=0.375, rely=0.9, relwidth=0.08, relheight=0.08)

        volume_button = Button(self, text="VOLUME")
        volume_button.config()
        volume_button.place(relx=0.500, rely=0.9, relwidth=0.08, relheight=0.08)

        mute_button = Button(self, text="Mute")
        mute_button.config(command=self.mute)
        mute_button.place(relx=0.625, rely=0.9, relwidth=0.08, relheight=0.08)

        open_file_button = Button(self, text="Find", style="TButton")
        open_file_button.config(command=self.extract_files)
        open_file_button.place(relx=0.750, rely=0.9, relwidth=0.08, relheight=0.08)

        configuration_button = Button(self, text="Change")
        configuration_button.config()
        configuration_button.place(relx=0.875, rely=0.9, relwidth=0.1, relheight=0.08)

    def playsong(self):
        self.player = vlc.MediaPlayer(self.filename)
        self.player.play()

    def pausesong(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def echo_effect(self):
        vlc.libvlc_audio_set_delay(self.player, 1000)
        vlc.libvlc_audio_get_delay(self.player)

    def mute(self):
        self.player.audio_set_mute(True)

    def sound_configuration(self):
        yield
        #vlc.AudioEqualizer

    def extract_files(self):
        self.filename = askopenfilename(filetypes=[("Mp3 Files", "*.mp3;*.wav;")])
        self.filename = os.path.abspath(self.filename)
        print(self.filename)
        return self.filename


def main():
    window = Tk()

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
