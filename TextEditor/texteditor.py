from tkinter import *
import enchant

root = Tk()
dictionary = enchant.Dict("en_US")


def open_file():
    file_name = filedialog.askopenfilename()
    try:
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        f.close()
    except:
        messagebox.showerror(
            'Вопрос',
            'Файл не выбран.')     

def new_file():
    pass

def save_file():
    file_name = filedialog.asksaveasfilename(
        filetypes=(('TXT files', '*txt'), 
                   ('HTML files', '*.html;*.htm'), 
                   ('All files', '*.*')))
    try:
        f = open(file_name, 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()
    except:
        messagebox.showerror(
            'Вопрос',
            'Файл не выбран.')    

def new_file():
    save_current = messagebox.askyesno(title='Сохранить файл', message='Сохранить текущий файл?')
    if save_current:
        save_file()
        text.delete(1.0, END)
    else:
        text.delete(1.0, END)

def spell_check(event):

    index = text.search(r'\s', INSERT, backwards=True, regexp=True)
    print(index)

    word = text.get(index, INSERT)

    if word == "":
        index ="1.0"
    else:
        index = text.index("%s+1c" % index)
    
    word = text.get(index, INSERT)

    try:
        spell_is_correct = dictionary.check(word)
    except:
        spell_is_correct = True

    if spell_is_correct:
        text.tag_remove("misspelled", index, "%s+%dc" % (index, len(word)))

    else:
        text.tag_add("misspelled", index, "%s+%dc" % (index, len(word)))

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Открыть...', command=open_file)
filemenu.add_command(label='Новый', command=new_file)
filemenu.add_command(label='Сохранить...', command=save_file)
filemenu.add_command(label='Выход', command=root.destroy)

mainmenu.add_cascade(label='Файл', menu=filemenu)

text = Text(width='50', height='30')
text.tag_configure("misspelled", foreground="red", underline=True)
scroll = Scrollbar(command=text.yview)

text.bind('<space>', spell_check)

scroll.pack(side=RIGHT, fill=Y)
text.pack(side=TOP, fill=Y)
root.mainloop()