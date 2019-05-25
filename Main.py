from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
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

        song_title = Label(original_frame, text="Artist - Song Name", anchor=CENTER, background=self.widgetbackground)
        song_title.place(relx=0.5, rely=0.5, width=400, relheight=0.1, anchor=CENTER)

        scroll_track_time = Scale(original_frame, orient=HORIZONTAL)
        scroll_track_time.place(relx=0.5, rely=0.6, width=400, relheight=0.1, anchor=CENTER)

        equalizer = Label(original_frame, text="There will be equalizer", anchor=CENTER, background=self.widgetbackground)
        equalizer.place(relx=0.5, rely=0.7, width=400, relheight=0.1, anchor=CENTER)

        buttons_frame = Frame(original_frame, style='TFrame')
        buttons_frame.place(relx=0.5, rely=0.8, width=400, height=50, anchor=CENTER)

        play_button = Button(buttons_frame, text="PLAY")
        play_button.config(command=self.playsong)
        play_button.place(relx=0, rely=0, relwidth=0.08, relheight=1)

        pause_button = Button(buttons_frame, text="PAUSE")
        pause_button.config(command=self.pausesong)
        pause_button.place(relx=0.125, rely=0, relwidth=0.08, relheight=1)

        stop_button = Button(buttons_frame, text="STOP")
        stop_button.config(command=self.stop)
        stop_button.place(relx=0.250, rely=0, relwidth=0.08, relheight=1)

        echo_button = Button(buttons_frame, text="ECHO")
        echo_button.config(command=self.echo_effect)
        echo_button.place(relx=0.375, rely=0, relwidth=0.08, relheight=1)

        volume_button = Button(buttons_frame, text="VOLUME")
        volume_button.bind("<Enter>",self.volume)
        volume_button.place(relx=0.500, rely=0, relwidth=0.08, relheight=1)

        mute_button = Button(buttons_frame, text="Mute")
        mute_button.config(command=self.mute)
        mute_button.place(relx=0.625, rely=0, relwidth=0.08, relheight=1)

        open_file_button = Button(buttons_frame, text="Find", style="TButton")
        open_file_button.config(command=self.extract_files)
        open_file_button.place(relx=0.750, rely=0, relwidth=0.08, relheight=1)

        configuration_button = Button(buttons_frame, text="Change")
        configuration_button.config(command=self.sound_configuration)
        configuration_button.place(relx=0.875, rely=0, relwidth=0.8, relheight=1)

    def playsong(self):
        self.player = vlc.MediaPlayer(self.filename)
        self.player.play()

    def pausesong(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def echo_effect(self):
        filename = self.filename


    @staticmethod
    def volume(event=None):
        volume_window = Toplevel(window)
        wid = event.widget
        try:
            if volume_window.winfo_exists(): return
        except:
            pass
        volume_var = IntVar(value=50)
        volume_window.wm_overrideredirect(False)
        volume_window.resizable(0,0)
        volume_window.lift()
        volume_window.attributes('-alpha', 0.6)
        volume_window.attributes('-topmost', 1)
        scale = Scale(volume_window, from_=0, to=100, variable=volume_var, orient='horizontal', bg='black', fg='white')
        scale.pack()
        width = int((scale.winfo_reqwidth() - wid.winfo_width()) / 2)
        volume_window.geometry('+%s+%s' % (wid.winfo_windowx() - width, wid.winfo_windowy() - scale.winfo_reqheight()))
        volume_window.focus()
        volume_window.bind("<Leave>", volume_window.destroy())

    def mute(self):
        self.player.audio_set_mute(True)

    def sound_configuration(self):
        equalizer_window = Toplevel(window)
        equalizer = vlc.AudioEqualizer()


    def extract_files(self):
        self.filename = askopenfilename(filetypes=[("Mp3 Files", "*.mp3;*.wav;")])
        self.filename = os.path.abspath(self.filename)
        print(self.filename)
        return self.filename


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
