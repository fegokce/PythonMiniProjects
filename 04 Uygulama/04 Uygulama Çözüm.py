from tkinter import *
import os
import time

class CopyTextFile(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.root = parent
        self.initUI()


    def initUI(self):
        self.label_head = Label(self, text = 'Copy Text File', bg = 'blue', fg = 'white', anchor = CENTER , font = ('', '20', 'bold'))
        self.label_head.pack(fill=X)

        self.label_input_file = Label(self, text = 'Input File Full Path:',font = ('', '14'))
        self.label_input_file.pack(pady = (5,0))

        self.input_file = Entry(self, width = 50)
        self.input_file.pack()

        self.label_output_file = Label(self, text = 'Output File Name:', font = ('','14'))
        self.label_output_file.pack(pady = (20,0))

        self.output_file = Entry(self, width = 50)
        self.output_file.pack()

        self.spell_check_button = Button(self, text = 'Copy', font = ('', '12'), command = self.copy)
        self.spell_check_button.pack(pady = (15, 0))

        self.progress_label = Label(self, text = 'Progress:',font = ('', '14'))
        self.progress_label.pack(pady = (20,0))

        self.progress_bar = Canvas(self, bg='grey', width =300, height = 20, borderwidth=2, relief='sunken')
        self.progress_bar.pack()




    def copy(self):
        input_file = self.input_file.get()
        output_file = self.output_file.get()
        file_size = os.path.getsize(input_file)

        piece_size = 1024 # 1 KiB
        step = 300 / float(file_size / piece_size) # progress size for each iteration


        with open(input_file, "rb") as in_file, open(output_file, "wb") as out_file:
            progress = 0
            while True:
                if progress >= (step * (file_size/piece_size)):
                    return
                piece = in_file.read(piece_size) # read 1024 byte from the input file
                progress += step  # update the progress



                progress_label = 'Progress: %f completed' %progress  #progress label updated
                self.progress_label.configure(text= progress_label)

                #drawing the rectangle
                self.progress_bar.create_rectangle(0, 0, progress, 25, fill="blue")  # 0,0 = sol ust , 0,0 = sag alt


                self.update() #update the frame


                out_file.write(piece) #write 1024 kb each step
                time.sleep(0.00001) # to see the progress


def main():
    root = Tk()
    root.title('Copy Text File')
    root.geometry('800x600')
    app = CopyTextFile(root)
    app.pack(fill = BOTH, expand = True)
    root.mainloop()


main()