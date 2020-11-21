from tkinter import *
from tkinter.ttk import Combobox
import random

class ColorGame(Frame):
    def __init__(self, parent):
        self.parent = parent
        Frame.__init__(self, parent)
        self.colors_list = ['red', 'green', 'blue']
        self.user_score = 0
        self.user_color = StringVar()
        self.stop = False
        self.initUI()

    def initUI(self):
        self.var = StringVar()
        self.var.set('e')

        Label(self, text='Renk Oyunu', font='Arial 19', bg='blue').pack(fill=X)
        color_entry_frame = Frame(self)
        color_entry_frame.pack(pady=10)
        Label(color_entry_frame, text='Renginizi Seçiniz:').pack(side=LEFT)
        Entry(color_entry_frame, textvariable=self.user_color).pack(side=LEFT)
        Label(color_entry_frame, text='Bir tanesini girin-->("red", "blue", "green")').pack(side=LEFT)

        speed_frame = Frame(self)
        speed_frame.pack(pady=10)
        Label(speed_frame, text='Hız:').pack(side=LEFT)
        self.combobox = Combobox(speed_frame, values=('Hızlı', 'Normal', 'Yavaş'), state='readonly')
        self.combobox.pack(side=LEFT)

        start_stop_frame = Frame(self)
        start_stop_frame.pack(pady=10)
        Button(start_stop_frame, text='Başlat', width=5, command=self.game_start).pack(side=LEFT, padx=5)
        Button(start_stop_frame, text='Durdur', width=5, command=self.stop_function).pack(side=LEFT, padx=5)

        self.user_color_button = Label(self, text='Renginiz')
        self.user_color_button.pack(pady=10)

        play_buttons_frame = Frame(self)
        play_buttons_frame.pack(pady=10)

        self.box_1 = Button(play_buttons_frame, text='1', width=5, height=2, command=self.getValue_Color1)
        self.box_1.pack(side=LEFT, padx=5)

        self.box_2 = Button(play_buttons_frame, text='2', width=5, height=2, command=self.getValue_Color2)
        self.box_2.pack(side=LEFT, padx=5)

        self.box_3 = Button(play_buttons_frame, text='3', width=5, height=2, command=self.getValue_Color3)
        self.box_3.pack(side=LEFT, padx=5)

        score_frame = Frame(self)
        score_frame.pack(pady=10)

        Label(score_frame, text='Skor: ').pack(side=LEFT)
        self.score_button = Label(score_frame, text='0')
        self.score_button.pack(side=LEFT)

        self.pack(fill=BOTH, expand=True)

    def game_start(self):
        speed = self.combobox.get()
        if speed == 'Hızlı':
            self.speed= 500
        if speed == 'Normal':
            self.speed = 1000
        if speed == 'Yavaş':
            self.speed = 2000
        self.user_color_button.configure(bg=self.user_color.get())
        self.stop = False
        self.game_main()

    def game_main(self):
        if self.stop:
            return
        scor_list = [random.randint(1,100), random.randint(1,100),random.randint(1,100)]
        colors_list = [random.choice(self.colors_list), random.choice(self.colors_list), random.choice(self.colors_list)]
        max_list = [0]
        order = 0
        for color in colors_list:
            if color == self.user_color.get():
                max_list.append(scor_list[order])
            order +=1
        self.max = max(max_list)
        self.box_1.configure(bg=colors_list[0], text=scor_list[0], font=('','12','bold'))
        self.box_2.configure(bg=colors_list[1], text=scor_list[1], font=('','12','bold'))
        self.box_3.configure(bg=colors_list[2], text=scor_list[2], font=('','12','bold'))
        self.update_idletasks()

        self.updating = self.after(self.speed, self.game_main)

    def getValue_Color1(self):
        if self.box_1.cget('text') == self.max and self.box_1.cget('bg') == self.user_color.get():
            self.user_score += 10
        else:
            self.user_score -= 5
        self.score_button.configure(text=str(self.user_score))

    def getValue_Color2(self):
        if self.box_2.cget('text') == self.max and self.box_2.cget('bg') == self.user_color.get():
            self.user_score += 10
        else:
            self.user_score -= 5
        self.score_button.configure(text=str(self.user_score))

    def getValue_Color3(self):
        if self.box_3.cget('text') == self.max and self.box_3.cget('bg') == self.user_color.get():
            self.user_score += 10
        else:
            self.user_score -= 5
        self.score_button.configure(text=str(self.user_score))
    def stop_function(self):
        self.stop = True

def main():
    root = Tk()
    root.title('Renk Oyunu')
    root.geometry('600x350')
    app = ColorGame(root)
    root.mainloop()
main()
