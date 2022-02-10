from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import module


dark_theme = "#2B2B2B"
light_theme = "#F0F0F0"
dark_entrytheme = "#3D3D3D"
light_entrytheme = 'white'
convert_btn_darktheme = "#B5B5B5"
convert_btn_lighttheme = 'white'#"#CBCBCB"
theme = light_theme
entry_theme = light_entrytheme
convert_btn_theme=convert_btn_lighttheme
get_sql = 1

root = Tk()
root.geometry("400x265") #600x400
root.resizable(False, False)
root.title("dicom to nifti")
root.config(bg=theme)

path0 = StringVar()
path_out = StringVar()

darkmode_button_ico = PhotoImage(file="darkmode.png")
lightmode_button_ico = PhotoImage(file="lightmode.png")

lightmode_search_ico = PhotoImage(file="serach_icon_light.png")
darkmode_search_ico = PhotoImage(file="search_icon_dark.png")

btn_theme = lightmode_button_ico
search_theme = lightmode_search_ico


frame1 = Frame(root, bg=theme)
frame1.grid(row=0, column=0, sticky='w', pady=0)
subframe11 = Frame(frame1, bg=theme)
subframe11.grid(row=1, column=0, sticky='w', padx=25)
subframe12 = Frame(frame1, bg=theme)
subframe12.grid(row=3, column=0, sticky='w', padx=25)
frame2 = Frame(root, bg=theme)
frame2.grid(row=1, column=0, sticky='w', pady=10)
subframe21 = Frame(frame2, bg=theme)
subframe21.grid(row=0, column=0, sticky='w', padx=25)
subframe22 = Frame(frame2)
subframe22.grid(row=1, column=0, sticky='w', padx=25)

label1 = Label(frame1, text="Input directory", font = ('Bahnschrift', '22'), bg=theme)
label1.grid(row=0, column=0, sticky='w')

entry1 = Entry(subframe11, bg=entry_theme, exportselection=0, font = ('Bahnschrift', '13'), relief='flat', textvariable=path0)
entry1.grid(row=0, column=0, ipadx=75)

label2 = Label(frame1, text="Output directory", font = ('Bahnschrift', '22'), bg=theme)
label2.grid(row=2, column=0, sticky='w')

entry2 = Entry(subframe12, bg=entry_theme, exportselection=0, font = ('Bahnschrift', '13'), relief='flat', textvariable=path_out)
entry2.grid(row=0, column=0, ipadx=75)

cb_style = ttk.Style()
cb_style.configure("light.TCheckbutton")
cb_style.configure("dark.TCheckbutton", background='#2B2B2B', selectcolor='#FFFFFF')
if theme == light_theme:
    check_style="light.TCheckbutton"
else:   
    check_style='dark.TCheckbutton'
sql_check = ttk.Checkbutton(subframe21, takefocus=0, style=check_style)
sql_check.grid(row=0, column=0, sticky='w', pady=0)
sql_check.invoke()
sql_check.invoke()

label3 = Label(subframe21, text="Get a sql file with dicoms datas", font = ('Bahnschrift', '14'), bg=theme)
label3.grid(row=0, column=1, sticky='sw')

gz_check = ttk.Checkbutton(subframe22, takefocus=0, style=check_style)
gz_check.grid(row=0, column=0, sticky='nw', pady=7)
gz_check.invoke()
gz_check.invoke()

label4 = Label(subframe22, text="gzip compression", font = ('Bahnschrift', '14'), bg=theme)
label4.grid(row=0, column=1, sticky='nw')


def switch_themebutton() :
    global theme,entry_theme
    if theme == light_theme :
        theme=dark_theme
        entry_theme=dark_entrytheme
        fontcolor = "white"
        btn_theme = lightmode_button_ico
        search_theme = darkmode_search_ico
        check_style = "dark.TCheckbutton"
        convert_btn_theme = convert_btn_lighttheme        
    else :
        theme = light_theme
        entry_theme = light_entrytheme
        fontcolor = "black"
        btn_theme = darkmode_button_ico
        search_theme = lightmode_search_ico
        check_style = "light.TCheckbutton"
        convert_btn_theme = convert_btn_darktheme
    root.config(bg=theme)
    frame1.config(bg=theme)
    frame2.config(bg=theme)
    subframe11.config(bg=theme)
    subframe12.config(bg=theme)
    subframe21.config(bg=theme)
    subframe22.config(bg=theme)  
    label1.config(bg=theme, fg=fontcolor)
    label2.config(bg=theme, fg=fontcolor)
    label3.config(bg=theme, fg=fontcolor)
    label4.config(bg=theme, fg=fontcolor)
    entry1.config(bg=entry_theme, fg=fontcolor)
    entry2.config(bg=entry_theme, fg=fontcolor)
    print(btn_theme.configure())
    btn_search1.config(bg=theme, activebackground=theme, image=search_theme)
    btn_search2.config(bg=theme, activebackground=theme, image=search_theme)
    sql_check.config(style=check_style)
    sql_check.config(style=check_style)
    btn_convert.config(bg=convert_btn_theme)
    btn_theme.config(image=search_theme)

def path0_browse():
    '''Allow user to select a directory and store it in global var called folder_path'''
    global path0
    filename = filedialog.askdirectory()
    path0.set(filename)
def path_out_browse():
    '''Allow user to select a directory and store it in global var called folder_path'''
    global path_out
    filename = filedialog.askdirectory()
    path_out.set(filename)

btn_search1 = Button(subframe11, borderwidth=0, command=path0_browse, image=search_theme, bg=theme)
btn_search1.grid(row=0, column=1)

btn_search2 = Button(subframe12, borderwidth=0, command=path_out_browse, image=search_theme, bg=theme)
btn_search2.grid(row=0, column=1)

btn_theme = Button(subframe22, relief='flat', command=switch_themebutton, bg=theme, image=btn_theme)
btn_theme.grid(row=0, column=2, padx=100, pady=10)

def convert_btn_func():
    input_dict = entry1.get()
    output_dict = entry2.get()
    format='.nii'
    if len(gz_check.state())==1 :
        format='.nii.gz'
    sql=False
    if len(sql_check.state())==1:
        sql=True
    module.d2n(input_dict, output_dict, format, sql)

btn_convert = Button(root, relief='flat', text='Convert', font = ('Bahnschrift', '14'), bg=convert_btn_darktheme, command=convert_btn_func)
btn_convert.place(relx=0.1, rely=0.8)

root.mainloop()