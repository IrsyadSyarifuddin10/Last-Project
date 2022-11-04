from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import pandas as pd
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
from datetime import date

#=================================================================================================================================================================================================#
#===============================================   LOGIN  DONE  =====================================================================================================================================#
#login
def login_display():
    global login_window
    login_window = Tk()
    login_window.title("LOGIN")
    login_window.resizable(0, 0)
    window_height = 500
    window_width = 350

    #centering window
    def center_screen():
        """ gets the coordinates of the center of the screen """
        global screen_height, screen_width, x_cordinate, y_cordinate

        screen_width = login_window.winfo_screenwidth()
        screen_height = login_window.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        login_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    center_screen()

    #background
    j = 0
    r = 0
    for i in range(100):
        c = str(222222 + r)
        Frame(login_window, width=10, height=500, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1

    #white container
    Frame(login_window, width=250, height=400, bg="white").place(x=50, y=50)

    # label username
    labeluser = Label(login_window, text="Username", bg="white")
    l = ("consolas", 13)  # font, text, size
    labeluser.config(font=l)
    labeluser.place(x=80, y=200)

    #entry user
    entryuser = Entry(login_window, width=20, border=0)
    entryuser.config(font=l)
    entryuser.place(x=80, y=230)

    # label password
    labelpassword = Label(login_window, text="Password (max 8 digit)", bg="white")
    l = ("consolas", 13)  # font, text, size
    labelpassword.config(font=l)
    labelpassword.place(x=75, y=280)

    #entry password
    entrypassword = Entry(login_window, width=20, border=0)
    entrypassword.config(font=l,  show='*')
    entrypassword.place(x=80, y=310)

    #one line under entry
    Frame(login_window, width=180, height=2, bg="#141414").place(x=80, y=250)
    Frame(login_window, width=180, height=2, bg="#141414").place(x=80, y=330)

    #logo login
    imagelog = Image.open("loginlogo.jpg")
    imagelog.thumbnail((150, 150))
    imagelogin = ImageTk.PhotoImage(imagelog)

    label_logo_login = Label(image=imagelogin , border=0 , justify=CENTER)
    label_logo_login.place(x = 96, y = 50)

    def regis():
        login_window.destroy()
        add_admin_display()


    def cmd():
        username = entryuser.get()
        passw = entrypassword.get()

        if username == '' and passw == '':
            messagebox.showerror("Error!", "Isi username dan password untuk login")
        else:
            try:
                database = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    database='siac'
                )
                cursordb = database.cursor()
                cursordb.execute('select * from admin where nama_admin = %s and password = %s', (username, passw))
                akun_admin = cursordb.fetchone()
                if akun_admin == None:
                    messagebox.showerror('Error', 'Salah username dan password')
                else:
                    messagebox.showinfo('Login Success', 'Login sukses')
                    database.close()
                    login_window.destroy()
                    main_menu_display()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    # login button
    Button(login_window, width=20, height=2, fg='white', bg='#994422', border=0, command=cmd, text='LOGIN').place(x=100, y=355)
    Button(login_window, width=20, height=2, fg='white', bg='#994422', border=0, command=regis, text='TAMBAH ADMIN').place(x=100, y=400)

    login_window.mainloop()


#===============================================   ADD ADMIN DONE   =================================================================================================================================#

#add admin
def add_admin_display():
    global add_admin_window
    add_admin_window = Tk()
    add_admin_window.title("ADD ADMIN")
    add_admin_window.resizable(0, 0)
    window_height = 500
    window_width = 350

    #centering window
    def center_screen():
        """ gets the coordinates of the center of the screen """
        global screen_height, screen_width, x_cordinate, y_cordinate

        screen_width = add_admin_window.winfo_screenwidth()
        screen_height = add_admin_window.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        add_admin_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    center_screen()

    #background
    j = 0
    r = 0
    for i in range(100):
        c = str(222222 + r)
        Frame(add_admin_window, width=10, height=500, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1

    #white container
    Frame(add_admin_window, width=250, height=400, bg="white").place(x=50, y=50)

    # label username
    labeluserreg = Label(add_admin_window, text="Username", bg="white")
    l = ("consolas", 13)  # font, text, size
    labeluserreg.config(font=l)
    labeluserreg.place(x=80, y=200)

    #entry user
    entryuserreg = Entry(add_admin_window, width=20, border=0)
    entryuserreg.config(font=l)
    entryuserreg.place(x=80, y=230)

    # label password
    labelpasswordreg = Label(add_admin_window, text="Password (max 8 digit)", bg="white")
    l = ("consolas", 13)  # font, text, size
    labelpasswordreg.config(font=l)
    labelpasswordreg.place(x=75, y=280)

    #entry password
    entrypasswordreg = Entry(add_admin_window, width=20, border=0)
    entrypasswordreg.config(font=l,  show='*')
    entrypasswordreg.place(x=80, y=310)

    #one line under entry
    Frame(add_admin_window, width=180, height=2, bg="#141414").place(x=80, y=250)
    Frame(add_admin_window, width=180, height=2, bg="#141414").place(x=80, y=330)

    def login_page():
        add_admin_window.destroy()
        login_display()


    def cmd_add_admin():
        usernamereg = entryuserreg.get()
        passwreg = entrypasswordreg.get()

        if usernamereg == '' and passwreg == '':
            messagebox.showerror("Error!", "Isi username dan password")
        else:
            try:
                database = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    database='siac'
                )
                cursordb = database.cursor()
                cursordb.execute('insert into admin(nama_admin, password) values (%s, %s)', (usernamereg, passwreg))
                messagebox.showinfo('Success', 'Sukses menambah admin. Akun bisa digunakan.')
                database.commit()
                database.close()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    # login button
    Button(add_admin_window, width=20, height=2, fg='white', bg='#994422', border=0, command=cmd_add_admin, text='Add Admin').place(x=100, y=355)
    Button(add_admin_window, width=20, height=2, fg='white', bg='#994422', border=0, command=login_page, text='Back').place(x=100, y=400)


#===============================================   MAIN MENU kurang 1 menu adn 1 tabel  =============================================================================================================#

#main menu
def main_menu_display():
    global main_menu_window
    main_menu_window = Tk()
    main_menu_window.title("AWONG CELL")
    main_menu_window.resizable(0, 0)
    window_height = 500
    window_width = 350

    # centering window
    def center_screen():
        """ gets the coordinates of the center of the screen """
        global screen_height, screen_width, x_cordinate, y_cordinate

        screen_width = main_menu_window.winfo_screenwidth()
        screen_height = main_menu_window.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        main_menu_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    center_screen()

    # background
    j = 0
    r = 0
    for i in range(100):
        c = str(222222 + r)
        Frame(main_menu_window, width=10, height=500, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1

    # white container
    Frame(main_menu_window, width=250, height=400, bg="white").place(x=50, y=50)

    #header
    header_main_menu = Label(main_menu_window, text='AWONG CELL', bg='white')
    config_header = ('consolas', 20)
    header_main_menu.config(font=config_header)
    header_main_menu.place(x=98, y=60)

    #sub header
    sub_header_main_menu = Label(main_menu_window, text='Main Menu', bg='white')
    config_sub_header = ('consolas', 16)
    sub_header_main_menu.config(font=config_sub_header)
    sub_header_main_menu.place(x=119, y=165)

    #def tombol-tombol
    def go_to_spk():
        main_menu_window.destroy()
        spk_display()

    def go_to_daftar_hp():
        main_menu_window.destroy()
        daftar_hp_display()

    #def riwayat spk
    def go_to_riwayat_spk():
        main_menu_window.destroy()
        riwayat_spk()

    #tombol spk
    Button(main_menu_window, width=30, height=2, fg='white', bg='#994422', border=0, command=go_to_spk, text='Sistem Pendukung Keputusan').place(x=70, y=250)
    Button(main_menu_window, width=30, height=2, fg='white', bg='#994422', border=0, command=go_to_daftar_hp, text='Daftar HP').place(x=70, y=320)
    Button(main_menu_window, width=30, height=2, fg='white', bg='#994422', border=0, command=go_to_riwayat_spk, text='Riwayat SPK').place(x=70, y=390)


# ===============================================   SPK display DONE   =========================================================================================================#

#SPK
def spk_display():
    global spk_window
    spk_window = Tk()
    spk_window.title('Awong Cell')
    window_height = 600
    window_width = 350

    def center_screen():
        """ gets the coordinates of the center of the screen """
        global screen_height, screen_width, x_cordinate, y_cordinate

        screen_width = spk_window.winfo_screenwidth()
        screen_height = spk_window.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        spk_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    center_screen()

    # background
    j = 0
    r = 0
    for i in range(100):
        c = str(222222 + r)
        Frame(spk_window, width=1900, height=1000, bg="#" + c).place(x=j, y=0)
        j = j + 8000
        r = r + 800

    Frame(spk_window, width=300, height=550, bg="white").place(x=25, y=25)
    Frame(spk_window, width=290, height=500, bg="grey").place(x=30, y=70)

    # label header
    label_header_spk_display = Label(spk_window, text='AWONG CELL', bg='white')
    l = ('consolas', 20)
    label_header_spk_display.config(font=l)
    label_header_spk_display.place(x=100, y=30)

    # label sub header
    label_sub_header_spk_display = Label(spk_window, text='Sistem Pendukung Keputusan\n Pembelian Smartphone',
                                         bg='grey', fg='white')
    l = ('consolas', 14)
    label_sub_header_spk_display.config(font=l)
    label_sub_header_spk_display.place(x=40, y=80)

    # config label input
    l3 = ('consolas', 13)

    # label nama_pelanggan
    label_nama_pelanggan = Label(spk_window, text='Nama Pelanggan', bg='grey', fg='white')
    label_nama_pelanggan.config(font=l3)
    label_nama_pelanggan.place(x=45, y=150)

    # entry nama pelanggan
    entry_nama_pelanggan = Entry(spk_window, width=28, border=0, bg='grey', fg='white')
    entry_nama_pelanggan.config(font=l3)
    entry_nama_pelanggan.place(x=45, y=180)

    # garis dibawah entry nama pelanggan
    Frame(spk_window, width=255, height=2, bg="white").place(x=45, y=203)

    # label antutu score
    label_antutu_score = Label(spk_window, text='Antutu Score', bg='grey', fg='white')
    label_antutu_score.config(font=l3)
    label_antutu_score.place(x=45, y=220)

    # entry antutu score
    entry_antutu_score = Entry(spk_window, width=28, border=0, bg='grey', fg='white')
    entry_antutu_score.config(font=l3)
    entry_antutu_score.place(x=45, y=250)

    # garis dibawah entry antutu score
    Frame(spk_window, width=255, height=2, bg="white").place(x=45, y=273)

    # label ram
    label_ram = Label(spk_window, text='RAM', bg='grey', fg='white')
    label_ram.config(font=l3)
    label_ram.place(x=45, y=293)

    # entry ram
    entry_ram = Entry(spk_window, width=28, border=0, bg='grey', fg='white')
    entry_ram.config(font=l3)
    entry_ram.place(x=45, y=323)

    # garis dibawah entry ram
    Frame(spk_window, width=255, height=2, bg="white").place(x=45, y=343)

    # label internal storage
    label_internal_storage = Label(spk_window, text='Internal Storage', bg='grey', fg='white')
    label_internal_storage.config(font=l3)
    label_internal_storage.place(x=45, y=363)

    # entry internal storage
    entry_internal_storage = Entry(spk_window, width=28, border=0, bg='grey', fg='white')
    entry_internal_storage.config(font=l3)
    entry_internal_storage.place(x=45, y=393)

    # garis dibawah entry internal storage
    Frame(spk_window, width=255, height=2, bg="white").place(x=45, y=413)

    # def tombol calculate
    def calculate():
        data_nama_pelanggan = entry_nama_pelanggan.get()
        data_entry_antutu = entry_antutu_score.get()
        data_entry_ram = entry_ram.get()
        data_entry_internal = entry_internal_storage.get()
        if len(data_nama_pelanggan)  == 0 or len(data_entry_antutu)  == 0 or len(data_entry_ram) == 0 or len(data_entry_internal) == 0:
            messagebox.showerror('Error!', 'Silahkan isi form nama_pelanggan, antutu_score, ram, dan internal storage terlebih dahulu!')
        else:
            database = mysql.connector.connect(
                host='localhost',
                user='root',
                database='siac'
            )
            cursordb = database.cursor()
            cursordb.execute('select * from stok')
            data_hp = cursordb.fetchall()
            data_hp = pd.DataFrame(data_hp,
                                   columns=['kode barang', 'tipe', 'merk', 'chipset', 'antutu score', 'ram', 'internal',
                                            'harga', 'stok','skor'])
            database.close()

            data_antutu_score = np.array(data_hp)
            data_antutu_score = data_antutu_score[:, 4]

            data_ram = np.array(data_hp)
            data_ram = data_ram[:, 5]

            data_internal_storage = np.array(data_hp)
            data_internal_storage = data_internal_storage[:, 6]

            def RangeSubjektif(_low, _high, _step):
                subjektif = np.arange(_low, _high, _step)
                return subjektif

            def AlgoritmaFuzzy(_rule, _range_subjektif, _titel):
                lo = fuzz.trimf(_range_subjektif, _rule[0])
                hi = fuzz.trimf(_range_subjektif, _rule[1])

                fig, ax = plt.subplots(nrows=1, figsize=(6, 3))
                ax.plot(_range_subjektif, lo, 'g', linewidth=1.5, label='Low')
                ax.plot(_range_subjektif, hi, 'b', linewidth=1.5, label='High')

                ax.set_title(_titel)
                ax.legend()

                ax.spines['top'].set_visible(False)
                ax.get_xaxis().tick_bottom()
                ax.get_yaxis().tick_left()

                plt.tight_layout()
                #plt.show()

                return lo, hi

            xantutu_score = RangeSubjektif(40000, 310000, 1)
            rantutu_score = np.array([
                [40000, 40000, 310000],
                [40000, 310000, 310000]
            ])

            xram = RangeSubjektif(1, 12, 1)
            rram = np.array([
                [1, 1, 12],
                [1, 12, 12]
            ])

            xinternal_storage = RangeSubjektif(8, 512, 1)
            rinternal_storage = np.array([
                [8, 8, 512],
                [8, 512, 512]
            ])

            xskor = RangeSubjektif(1, 100, 1)
            rskor = np.array([
                [1, 1, 100],
                [1, 100, 100]
            ])

            lo_antutu_score, hi_antutu_score = AlgoritmaFuzzy(rantutu_score, xantutu_score, 'Antutu Score')
            lo_ram, hi_ram = AlgoritmaFuzzy(rram, xram, 'RAM')
            lo_internal_storage, hi_internal_storage = AlgoritmaFuzzy(rinternal_storage, xinternal_storage,
                                                                      'Internal Storage')
            lo_skor, hi_skor = AlgoritmaFuzzy(rskor, xskor, 'Skor')

            def FungsiKeanggotaan(_range, _lo, _hi, _nilai):
                lo = fuzz.interp_membership(_range, _lo, _nilai)
                hi = fuzz.interp_membership(_range, _hi, _nilai)

                return lo, hi

            # fungsi keanggotaan
            panjang_data = len(data_hp)

            antutu_score_anggota = {}
            xxx = 0
            for x in range(panjang_data):
                xxx += 1
                antutu_score_anggota["antutu_score_anggota_{0}".format(xxx)] = FungsiKeanggotaan(xantutu_score,
                                                                                                 lo_antutu_score,
                                                                                                 hi_antutu_score,
                                                                                                 data_antutu_score[x])

            ram_anggota = {}
            yyy = 0
            for y in range(panjang_data):
                yyy += 1
                ram_anggota['ram_anggota_{0}'.format(yyy)] = FungsiKeanggotaan(xram, lo_ram, hi_ram, data_ram[y])

            internal_storage_anggota = {}
            zzz = 0
            for z in range(panjang_data):
                zzz += 1
                internal_storage_anggota['internal_storage_anggota_{0}'.format(zzz)] = FungsiKeanggotaan(
                    xinternal_storage, lo_internal_storage,
                    hi_internal_storage, data_internal_storage[z])

            # memisahkan anggota low and high
            a = 1
            for x, y in antutu_score_anggota.values():
                globals()['low_antutu_score_anggota_' + str(a)] = x
                globals()['high_antutu_score_anggota_' + str(a)] = y
                a += 1

            b = 1
            for xx, yy in ram_anggota.values():
                globals()['low_ram_anggota_' + str(b)] = xx
                globals()['high_ram_anggota_' + str(b)] = yy
                b += 1

            c = 1
            for xxx, yyy in internal_storage_anggota.values():
                globals()['low_internal_storage_anggota_' + str(c)] = xxx
                globals()['high_internal_storage_anggota_' + str(c)] = yyy
                c += 1


            # ALPHA semua
            # Rule
            # R1 antutu_score LOW RAM LOW INTERNAL LOW
            alpha_1_anggota = {}
            a = 1
            for x in range(panjang_data):
                alpha_1_anggota['alpha_1_anggota_{0}'.format(a)] = min(globals()['low_antutu_score_anggota_' + str(a)],
                                                                       globals()['low_ram_anggota_' + str(a)],
                                                                       globals()[
                                                                           'low_internal_storage_anggota_' + str(a)])
                a += 1
            # R2 antutu_score LOW RAM LOW INTERNAL HIGH
            alpha_2_anggota = {}
            b = 1
            for y in range(panjang_data):
                alpha_2_anggota['alpha_2_anggota_{0}'.format(b)] = min(globals()['low_antutu_score_anggota_' + str(b)],
                                                                       globals()['low_ram_anggota_' + str(b)],
                                                                       globals()['high_internal_storage_anggota_' + str(b)])
                b += 1
            # R3 antutu_score LOW RAM HIGH INTERNAL LOW
            alpha_3_anggota = {}
            c = 1
            for y in range(panjang_data):
                alpha_3_anggota['alpha_3_anggota_{0}'.format(c)] = min(globals()['low_antutu_score_anggota_' + str(c)],
                                                                       globals()['high_ram_anggota_' + str(c)],
                                                                       globals()[
                                                                           'low_internal_storage_anggota_' + str(c)])
                c += 1
            # R4 antutu_score LOW RAM HIGH INTERNAL HIGH
            alpha_4_anggota = {}
            d = 1
            for z in range(panjang_data):
                alpha_4_anggota['alpha_4_anggota_{0}'.format(d)] = min(globals()['low_antutu_score_anggota_' + str(d)],
                                                                       globals()['high_ram_anggota_' + str(d)],
                                                                       globals()[
                                                                           'high_internal_storage_anggota_' + str(d)])
                d += 1

            # R5 antutu_score HIGH RAM LOW INTERNAL LOW
            alpha_5_anggota = {}
            e = 1
            for xx in range(panjang_data):
                alpha_5_anggota['alpha_5_anggota_{0}'.format(e)] = min(globals()['high_antutu_score_anggota_' + str(e)],
                                                                       globals()['low_ram_anggota_' + str(e)],
                                                                       globals()[
                                                                           'low_internal_storage_anggota_' + str(e)])
                e += 1
            # R6 antutu_score HIGH RAM LOW INTERNAL HIGH
            alpha_6_anggota = {}
            f = 1
            for yy in range(panjang_data):
                alpha_6_anggota['alpha_6_anggota_{0}'.format(f)] = min(globals()['high_antutu_score_anggota_' + str(f)],
                                                                       globals()['low_ram_anggota_' + str(f)],
                                                                       globals()[
                                                                           'high_internal_storage_anggota_' + str(f)])
                f += 1
            # R7 antutu_score HIGH RAM HIGH INTERNAL LOW
            alpha_7_anggota = {}
            g = 1
            for zz in range(panjang_data):
                alpha_7_anggota['alpha_7_anggota_{0}'.format(g)] = min(globals()['high_antutu_score_anggota_' + str(g)],
                                                                       globals()['high_ram_anggota_' + str(g)],
                                                                       globals()[
                                                                           'low_internal_storage_anggota_' + str(g)])
                g += 1
            # R8 antutu_score HIGH RAM HIGH INTERNAL HIGH
            alpha_8_anggota = {}
            h = 1
            for xxx in range(panjang_data):
                alpha_8_anggota['alpha_8_anggota_{0}'.format(h)] = min(globals()['high_antutu_score_anggota_' + str(h)],
                                                                       globals()['high_ram_anggota_' + str(h)],
                                                                       globals()[
                                                                           'high_internal_storage_anggota_' + str(h)])
                h += 1

            # nilai z
            # Z1 turun
            z_1_anggota = {}
            a = 1
            for x in range(panjang_data):
                z_1_anggota['z_1_anggota_{0}'.format(a)] = ''
                if alpha_1_anggota['alpha_1_anggota_{0}'.format(a)] == 0:
                    z_1_anggota['z_1_anggota_{0}'.format(a)] = 100
                elif alpha_1_anggota['alpha_1_anggota_{0}'.format(a)] == 1:
                    z_1_anggota['z_1_anggota_{0}'.format(a)] = 1
                else:
                    z_1_anggota['z_1_anggota_{0}'.format(a)] = 100 - (
                                alpha_1_anggota['alpha_1_anggota_{0}'.format(a)] * (100 - 1))

                a += 1
            # Z2 turun
            z_2_anggota = {}
            b = 1
            for y in range(panjang_data):
                z_2_anggota['z_2_anggota_{0}'.format(b)] = ''
                if alpha_2_anggota['alpha_2_anggota_{0}'.format(b)] == 0:
                    z_2_anggota['z_2_anggota_{0}'.format(b)] = 100
                elif alpha_2_anggota['alpha_2_anggota_{0}'.format(b)] == 1:
                    z_2_anggota['z_2_anggota_{0}'.format(b)] = 1
                else:
                    z_2_anggota['z_2_anggota_{0}'.format(b)] = 100 - (
                                alpha_2_anggota['alpha_2_anggota_{0}'.format(b)] * (100 - 1))

                b += 1
            # Z3 turun
            z_3_anggota = {}
            c = 1
            for z in range(panjang_data):
                z_3_anggota['z_3_anggota_{0}'.format(c)] = ''
                if alpha_3_anggota['alpha_3_anggota_{0}'.format(c)] == 0:
                    z_3_anggota['z_3_anggota_{0}'.format(c)] = 100
                elif alpha_3_anggota['alpha_3_anggota_{0}'.format(c)] == 1:
                    z_3_anggota['z_3_anggota_{0}'.format(c)] = 1
                else:
                    z_3_anggota['z_3_anggota_{0}'.format(c)] = 100 - (
                                alpha_3_anggota['alpha_3_anggota_{0}'.format(c)] * (100 - 1))

                c += 1
            # Z4 turun
            z_4_anggota = {}
            d = 1
            for xx in range(panjang_data):
                z_4_anggota['z_4_anggota_{0}'.format(d)] = ''
                if alpha_4_anggota['alpha_4_anggota_{0}'.format(d)] == 0:
                    z_4_anggota['z_4_anggota_{0}'.format(d)] = 100
                elif alpha_4_anggota['alpha_4_anggota_{0}'.format(d)] == 1:
                    z_4_anggota['z_4_anggota_{0}'.format(d)] = 1
                else:
                    z_4_anggota['z_4_anggota_{0}'.format(d)] = 100 - (
                                alpha_4_anggota['alpha_4_anggota_{0}'.format(d)] * (100 - 1))

                d += 1

            # Z5 turun
            z_5_anggota = {}
            e = 1
            for yy in range(panjang_data):
                z_5_anggota['z_5_anggota_{0}'.format(e)] = ''
                if alpha_5_anggota['alpha_5_anggota_{0}'.format(e)] == 0:
                    z_5_anggota['z_5_anggota_{0}'.format(e)] = 100
                elif alpha_5_anggota['alpha_5_anggota_{0}'.format(e)] == 1:
                    z_5_anggota['z_5_anggota_{0}'.format(e)] = 1
                else:
                    z_5_anggota['z_5_anggota_{0}'.format(e)] = 100 - (
                                alpha_5_anggota['alpha_5_anggota_{0}'.format(e)] * (100 - 1))

                e += 1
            # Z6 turun
            z_6_anggota = {}
            f = 1
            for zz in range(panjang_data):
                z_6_anggota['z_6_anggota_{0}'.format(f)] = ''
                if alpha_6_anggota['alpha_6_anggota_{0}'.format(f)] == 0:
                    z_6_anggota['z_6_anggota_{0}'.format(f)] = 100
                elif alpha_6_anggota['alpha_6_anggota_{0}'.format(f)] == 1:
                    z_6_anggota['z_6_anggota_{0}'.format(f)] = 1
                else:
                    z_6_anggota['z_6_anggota_{0}'.format(f)] = 100 - (
                                alpha_6_anggota['alpha_6_anggota_{0}'.format(f)] * (100 - 1))

                f += 1
            # Z7 naik
            z_7_anggota = {}
            g = 1
            for xxx in range(panjang_data):
                z_7_anggota['z_7_anggota_{0}'.format(g)] = ''
                if alpha_7_anggota['alpha_7_anggota_{0}'.format(g)] == 0:
                    z_7_anggota['z_7_anggota_{0}'.format(g)] = 1
                elif alpha_7_anggota['alpha_7_anggota_{0}'.format(g)] == 1:
                    z_7_anggota['z_7_anggota_{0}'.format(g)] = 100
                else:
                    z_7_anggota['z_7_anggota_{0}'.format(g)] = 1 + (
                                alpha_7_anggota['alpha_7_anggota_{0}'.format(g)] * (100 - 1))

                g += 1
            # Z8  naik
            z_8_anggota = {}
            h = 1
            for yyy in range(panjang_data):
                z_8_anggota['z_8_anggota_{0}'.format(h)] = ''
                if alpha_8_anggota['alpha_8_anggota_{0}'.format(h)] == 0:
                    z_8_anggota['z_8_anggota_{0}'.format(h)] = 1
                elif alpha_8_anggota['alpha_8_anggota_{0}'.format(h)] == 1:
                    z_8_anggota['z_8_anggota_{0}'.format(h)] = 100
                else:
                    z_8_anggota['z_8_anggota_{0}'.format(h)] = 1 + (
                                alpha_8_anggota['alpha_8_anggota_{0}'.format(h)] * (100 - 1))

                h += 1

            # alpha * z
            # AZ1
            az_1_anggota = {}
            a = 1
            for x in range(panjang_data):
                az_1_anggota['az_1_anggota_{0}'.format(a)] = alpha_1_anggota['alpha_1_anggota_{0}'.format(a)] * \
                                                             z_1_anggota['z_1_anggota_{0}'.format(a)]
                a += 1
            # AZ2
            az_2_anggota = {}
            b = 1
            for y in range(panjang_data):
                az_2_anggota['az_2_anggota_{0}'.format(b)] = alpha_2_anggota['alpha_2_anggota_{0}'.format(b)] * \
                                                             z_2_anggota['z_2_anggota_{0}'.format(b)]
                b += 1
            # AZ3
            az_3_anggota = {}
            c = 1
            for z in range(panjang_data):
                az_3_anggota['az_3_anggota_{0}'.format(c)] = alpha_3_anggota['alpha_3_anggota_{0}'.format(c)] * \
                                                             z_3_anggota['z_3_anggota_{0}'.format(c)]
                c += 1
            # AZ4
            az_4_anggota = {}
            d = 1
            for xx in range(panjang_data):
                az_4_anggota['az_4_anggota_{0}'.format(d)] = alpha_4_anggota['alpha_4_anggota_{0}'.format(d)] * \
                                                             z_4_anggota['z_4_anggota_{0}'.format(d)]
                d += 1

            # AZ5
            az_5_anggota = {}
            e = 1
            for yy in range(panjang_data):
                az_5_anggota['az_5_anggota_{0}'.format(e)] = alpha_5_anggota['alpha_5_anggota_{0}'.format(e)] * \
                                                             z_5_anggota['z_5_anggota_{0}'.format(e)]
                e += 1
            # AZ6
            az_6_anggota = {}
            f = 1
            for zz in range(panjang_data):
                az_6_anggota['az_6_anggota_{0}'.format(f)] = alpha_6_anggota['alpha_6_anggota_{0}'.format(f)] * \
                                                             z_6_anggota['z_6_anggota_{0}'.format(f)]
                f += 1
            # AZ7
            az_7_anggota = {}
            g = 1
            for xxx in range(panjang_data):
                az_7_anggota['az_7_anggota_{0}'.format(g)] = alpha_7_anggota['alpha_7_anggota_{0}'.format(g)] * \
                                                             z_7_anggota['z_7_anggota_{0}'.format(g)]
                g += 1
            # AZ8
            az_8_anggota = {}
            h = 1
            for yyy in range(panjang_data):
                az_8_anggota['az_8_anggota_{0}'.format(h)] = alpha_8_anggota['alpha_8_anggota_{0}'.format(h)] * \
                                                             z_8_anggota['z_8_anggota_{0}'.format(h)]
                h += 1

            # rata_rata(defuzzyfikasi)
            # rata-rata = sum(alpha*z)/sum(alpha)

            # sum(alpha*z)
            jumlah_az_anggota = {}
            a = 1
            for x in range(panjang_data):
                jumlah_az_anggota['jumlah_az_anggota_{0}'.format(a)] = az_1_anggota['az_1_anggota_{0}'.format(a)] + \
                                                                       az_2_anggota['az_2_anggota_{0}'.format(a)] + \
                                                                       az_3_anggota['az_3_anggota_{0}'.format(a)] + \
                                                                       az_4_anggota['az_4_anggota_{0}'.format(a)] + \
                                                                       az_5_anggota['az_5_anggota_{0}'.format(a)] + \
                                                                       az_6_anggota['az_6_anggota_{0}'.format(a)] + \
                                                                       az_7_anggota['az_7_anggota_{0}'.format(a)] + \
                                                                       az_8_anggota['az_8_anggota_{0}'.format(a)]
                a += 1
            # sum(alpha)
            jumlah_alpha_anggota = {}
            b = 1
            for y in range(panjang_data):
                jumlah_alpha_anggota['jumlah_alpha_anggota_{0}'.format(b)] = alpha_1_anggota[
                                                                                 'alpha_1_anggota_{0}'.format(b)] + \
                                                                             alpha_2_anggota[
                                                                                 'alpha_2_anggota_{0}'.format(b)] + \
                                                                             alpha_3_anggota[
                                                                                 'alpha_3_anggota_{0}'.format(b)] + \
                                                                             alpha_4_anggota[
                                                                                 'alpha_4_anggota_{0}'.format(b)] + \
                                                                             alpha_5_anggota[
                                                                                 'alpha_5_anggota_{0}'.format(b)] + \
                                                                             alpha_6_anggota[
                                                                                 'alpha_6_anggota_{0}'.format(b)] + \
                                                                             alpha_7_anggota[
                                                                                 'alpha_7_anggota_{0}'.format(b)] + \
                                                                             alpha_8_anggota[
                                                                                 'alpha_8_anggota_{0}'.format(b)]
                b += 1
            # rata-rata
            rata_rata_anggota = {}
            c = 1
            for z in range(panjang_data):
                rata_rata_anggota['rata_rata_anggota_{0}'.format(c)] = jumlah_az_anggota[
                                                                           'jumlah_az_anggota_{0}'.format(c)] / \
                                                                       jumlah_alpha_anggota[
                                                                           'jumlah_alpha_anggota_{0}'.format(c)]
                c += 1

            # insert score ke dataframe
            for x in range(panjang_data):
                data_hp.iloc[:, 9] = rata_rata_anggota.values()

            data_hp

            # ======================================================================== Fuzzy input ====================================================================================#

            input_antutu_score = entry_antutu_score.get()
            input_ram = entry_ram.get()
            input_internal_storage = entry_internal_storage.get()

            # fungsi keanggotaan input
            input_antutu_score_anggota = FungsiKeanggotaan(xantutu_score, lo_antutu_score, hi_antutu_score,
                                                           input_antutu_score)
            input_ram_anggota = FungsiKeanggotaan(xram, lo_ram, hi_ram, input_ram)
            input_internal_storage_anggota = FungsiKeanggotaan(xinternal_storage, lo_internal_storage,
                                                               hi_internal_storage,
                                                               input_internal_storage)

            # memisahkan low dan high
            low_antutu_score_input_anggota = input_antutu_score_anggota[0]
            high_antutu_score_input_anggota = input_antutu_score_anggota[1]

            low_ram_input_anggota = input_ram_anggota[0]
            high_ram_input_anggota = input_ram_anggota[1]

            low_internal_storage_input_anggota = input_internal_storage_anggota[0]
            high_internal_storage_input_anggota = input_internal_storage_anggota[1]

            # menghitung alpha dari tiap rules
            # Rule
            # R1 ANTUTU LOW RAM LOW INTERNAL LOW
            alpha_1_input_anggota = min(low_antutu_score_input_anggota, low_ram_input_anggota,
                                        low_internal_storage_input_anggota)

            # R2 ANTUTU LOW RAM LOW INTERNAL HIGH
            alpha_2_input_anggota = min(low_antutu_score_input_anggota, low_ram_input_anggota,
                                        high_internal_storage_input_anggota)

            # R3 ANTUTU LOW RAM HIGH INTERNAL LOW
            alpha_3_input_anggota = min(low_antutu_score_input_anggota, high_ram_input_anggota,
                                        low_internal_storage_input_anggota)

            # R4 ANTUTU LOW RAM HIGH INTERNAL HIGH
            alpha_4_input_anggota = min(low_antutu_score_input_anggota, high_ram_input_anggota,
                                        high_internal_storage_input_anggota)

            # R5 ANTUTU HIGH RAM LOW INTERNAL LOW
            alpha_5_input_anggota = min(high_antutu_score_input_anggota, low_ram_input_anggota,
                                        low_internal_storage_input_anggota)

            # R6 ANTUTU HIGH RAM LOW INTERNAL HIGH
            alpha_6_input_anggota = min(high_antutu_score_input_anggota, low_ram_input_anggota,
                                        high_internal_storage_input_anggota)

            # R7 ANTUTU HIGH RAM HIGH INTERNAL LOW
            alpha_7_input_anggota = min(high_antutu_score_input_anggota, high_ram_input_anggota,
                                        low_internal_storage_input_anggota)

            # R8 ANTUTU HIGH RAM HIGH INTERNAL HIGH
            alpha_8_input_anggota = min(high_antutu_score_input_anggota, high_ram_input_anggota,
                                        high_internal_storage_input_anggota)

            # menghitung Z dari tiap rules
            # z1 turun
            z_1_input_anggota = ''
            if alpha_1_input_anggota == 0:
                z_1_input_anggota = 100
            elif alpha_1_input_anggota == 1:
                z_1_input_anggota = 1
            else:
                z_1_input_anggota = 100 - (alpha_1_input_anggota * (100 - 1))

            # z2 turun
            z_2_input_anggota = ''
            if alpha_2_input_anggota == 0:
                z_2_input_anggota = 100
            elif alpha_2_input_anggota == 1:
                z_2_input_anggota = 1
            else:
                z_2_input_anggota = 100 - (alpha_2_input_anggota * (100 - 1))

            # z3 turun
            z_3_input_anggota = ''
            if alpha_3_input_anggota == 0:
                z_3_input_anggota = 100
            elif alpha_3_input_anggota == 1:
                z_3_input_anggota = 1
            else:
                z_3_input_anggota = 100 - (alpha_3_input_anggota * (100 - 1))

            # z4 turun
            z_4_input_anggota = ''
            if alpha_4_input_anggota == 0:
                z_4_input_anggota = 100
            elif alpha_4_input_anggota == 1:
                z_4_input_anggota = 1
            else:
                z_4_input_anggota = 100 - (alpha_4_input_anggota * (100 - 1))

            # z5 turun
            z_5_input_anggota = ''
            if alpha_5_input_anggota == 0:
                z_5_input_anggota = 100
            elif alpha_5_input_anggota == 1:
                z_5_input_anggota = 1
            else:
                z_5_input_anggota = 100 - (alpha_5_input_anggota * (100 - 1))

            # z6 turun
            z_6_input_anggota = ''
            if alpha_6_input_anggota == 0:
                z_6_input_anggota = 100
            elif alpha_6_input_anggota == 1:
                z_6_input_anggota = 1
            else:
                z_6_input_anggota = 100 - (alpha_6_input_anggota * (100 - 1))

            # z7 naik
            z_7_input_anggota = ''
            if alpha_7_input_anggota == 0:
                z_7_input_anggota = 1
            elif alpha_7_input_anggota == 1:
                z_7_input_anggota = 100
            else:
                z_7_input_anggota = 1 + (alpha_7_input_anggota * (100 - 1))

            # z8 naik
            z_8_input_anggota = ''
            if alpha_8_input_anggota == 0:
                z_8_input_anggota = 1
            elif alpha_8_input_anggota == 1:
                z_8_input_anggota = 100
            else:
                z_8_input_anggota = 1 + (alpha_8_input_anggota * (100 - 1))

            # menghitung az
            # az1
            az_1_input_anggota = alpha_1_input_anggota * z_1_input_anggota
            # az2
            az_2_input_anggota = alpha_2_input_anggota * z_2_input_anggota
            # az3
            az_3_input_anggota = alpha_3_input_anggota * z_3_input_anggota
            # az4
            az_4_input_anggota = alpha_4_input_anggota * z_4_input_anggota
            # az5
            az_5_input_anggota = alpha_5_input_anggota * z_5_input_anggota
            # az6
            az_6_input_anggota = alpha_6_input_anggota * z_6_input_anggota
            # az7
            az_7_input_anggota = alpha_7_input_anggota * z_7_input_anggota
            # az8
            az_8_input_anggota = alpha_8_input_anggota * z_8_input_anggota

            # defuzzyfikasi
            # jumlah az
            jumlah_az_input = az_1_input_anggota + az_2_input_anggota + az_3_input_anggota + az_4_input_anggota + \
                              az_5_input_anggota + az_6_input_anggota + az_7_input_anggota + az_8_input_anggota
            # jumlah alpha
            jumlah_alpha_input = alpha_1_input_anggota + alpha_2_input_anggota + alpha_3_input_anggota + alpha_4_input_anggota + \
                                 alpha_5_input_anggota + alpha_6_input_anggota + alpha_7_input_anggota + alpha_8_input_anggota
            # rata-rata
            rata_rata_input = jumlah_az_input / jumlah_alpha_input

            # mencari score terdekat
            # rata_rata_anggota_values = rata_rata_anggota.values()
            # rata_rata_list = list(rata_rata_anggota_values)

            rata_rata_list = []
            for x in rata_rata_anggota.values():
                rata_rata_list.append(x)

            data_tipe = np.array(data_hp)
            data_tipe = data_tipe[:, 1]
            data_chipset = np.array(data_hp)
            data_chipset = data_chipset[:, 3]

            # merangking

            comparing = []
            for x in rata_rata_anggota.values():
                comparing.append(np.abs(x - rata_rata_input))

            data_comparing = {
                'tipe': data_tipe,
                'chipset': data_chipset,
                'antutu_score': data_antutu_score,
                'ram': data_ram,
                'internal_storage': data_internal_storage,
                'skor': rata_rata_list,
                'compared': comparing
            }

            dataframe_data_komparasi = pd.DataFrame(data_comparing, columns=['tipe', 'chipset', 'antutu_score', 'ram',
                                                                             'internal_storage', 'skor', 'compared'])

            rekomendasi = dataframe_data_komparasi.sort_values(by=['compared']).head(5)
            array_rekomendasi = np.asarray(rekomendasi)

            spk_window.destroy()
            def hasil_spk_display():
                global hasil_spk_window
                hasil_spk_window = Tk()
                hasil_spk_window.title('Awong Cell')
                window_height = 550
                window_width = 905

                def center_screen():
                    """ gets the coordinates of the center of the screen """
                    global screen_height, screen_width, x_cordinate, y_cordinate

                    screen_width = hasil_spk_window.winfo_screenwidth()
                    screen_height = hasil_spk_window.winfo_screenheight()
                    # Coordinates of the upper left corner of the window to make the window appear in the center
                    x_cordinate = int((screen_width / 2) - (window_width / 2))
                    y_cordinate = int((screen_height / 2) - (window_height / 2))
                    hasil_spk_window.geometry(
                        "{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

                center_screen()

                # background
                j = 0
                r = 0
                for i in range(100):
                    c = str(222222 + r)
                    Frame(hasil_spk_window, width=1900, height=1000, bg="#" + c).place(x=j, y=0)
                    j = j + 80
                    r = r + 8

                Frame(hasil_spk_window, width=855, height=500, bg="white").place(x=25, y=30)
                second_frame = Frame(hasil_spk_window, width=825, height=440, bg="grey").place(x=40, y=80)

                # label header
                label_header_hasil_spk_display = Label(hasil_spk_window, text='AWONG CELL', bg='white')
                l = ('consolas', 20)
                label_header_hasil_spk_display.config(font=l)
                label_header_hasil_spk_display.place(x=385, y=40)

                # label sub header
                label_sub_header_hasil_spk_display = Label(hasil_spk_window, text='Riwayat SPK', bg='grey',
                                                              fg='white')
                l2 = ('consolas', 15)
                label_sub_header_hasil_spk_display.config(font=l2)
                label_sub_header_hasil_spk_display.place(x=400, y=85)

                # display table
                treeview_table = ttk.Treeview(hasil_spk_window, columns=(1, 2, 3, 4, 5, 6), show='headings', height=14)
                treeview_table.place(x=50, y=150)

                treeview_table.column(1, anchor=CENTER, stretch=NO, width=100)
                treeview_table.heading(1, text='Tipe')
                treeview_table.column(2, anchor=CENTER, stretch=NO, width=150)
                treeview_table.heading(2, text='Chipset')
                treeview_table.column(3, anchor=CENTER, stretch=NO, width=100)
                treeview_table.heading(3, text='Antutu Score')
                treeview_table.column(4, anchor=CENTER, stretch=NO, width=150)
                treeview_table.heading(4, text='RAM')
                treeview_table.column(5, anchor=CENTER, stretch=NO, width=150)
                treeview_table.heading(5, text='Internal')
                treeview_table.column(6, anchor=CENTER, stretch=NO, width=150)
                treeview_table.heading(6, text='Skor')

                for x1,x2,x3,x4,x5,x6,x7 in array_rekomendasi:
                    treeview_table.insert('', 'end', values=(x1,x2,x3,x4,x5,x6))

                def simpan_hasil_spk():
                    today = date.today()
                    today_s_date = today.strftime('%Y-%m-%d')
                    database = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        database='siac'
                    )
                    tipe_rekomendasi = np.asarray(rekomendasi['tipe'])
                    list_tipe_rekomendasi = list(tipe_rekomendasi)
                    cursordb = database.cursor()
                    for x in list_tipe_rekomendasi:
                        cursordb.execute(
                            'insert into hasil_spk(nama_pelanggan, rekomendasi, tanggal) values(%s, %s, %s)',
                            (data_nama_pelanggan, x, today_s_date))
                        database.commit()

                    database.close()
                    messagebox.showinfo('Success', 'Simpan Data Sukses')

                def back_button_hasil_spk():
                    hasil_spk_window.destroy()
                    spk_display()

                Button(hasil_spk_window, width=20, height=2, fg='white', bg='#994422', border=0, command=simpan_hasil_spk,
                       text='SIMPAN').place(x=390, y=355)
                Button(hasil_spk_window, width=20, height=2, fg='white', bg='#994422', border=0, command=back_button_hasil_spk,
                       text='BACK').place(x=390, y=400)

            hasil_spk_display()

    # def tombol back
    def back():
        spk_window.destroy()
        main_menu_display()

    def help():
        messagebox._show('Help', 'Klasifikasi \n\n| Low |\nRAM 2 GB - 4 GB | Antutu Score = 40000 - 170000 | Internal = 8 GB - 64 GB \n\n| High |\nRAM 6 GB - 8 GB | Antutu Score = 150000 - 300000 | Internal = 64 Gb - 256 GB')

    # button
    Button(spk_window, width=20, height=2, fg='white', bg='#994422', border=0, command=back, text='Back').place(x=95, y=475)
    Button(spk_window, width=20, height=2, fg='white', bg='#994422', border=0, command=calculate, text='Calculate').place(x=95, y=433)
    Button(spk_window, width=20, height=2, fg='white', bg='#994422', border=0, command=help, text='Help').place(x=95, y=517)

    spk_window.mainloop()


# ===============================================   Input Stok Display DONE   ===================================================================================================================#

def daftar_hp_display():
    global daftar_hp_window
    daftar_hp_window = Tk()
    daftar_hp_window.title('Awong Cell')
    window_height = 1000
    window_width = 1900

    def center_screen():
        """ gets the coordinates of the center of the screen """
        global screen_height, screen_width, x_cordinate, y_cordinate

        screen_width = daftar_hp_window.winfo_screenwidth()
        screen_height = daftar_hp_window.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        daftar_hp_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    center_screen()

    # background
    j = 0
    r = 0
    for i in range(100):
        c = str(222222 + r)
        Frame(daftar_hp_window, width=1900, height=1000, bg="#" + c).place(x=j, y=0)
        j = j + 8000
        r = r + 800

    Frame(daftar_hp_window, width=1810, height=940, bg="white").place(x=50, y=50)
    second_frame = Frame(daftar_hp_window, width=1810, height=730, bg="grey").place(x=50, y=260)

    # label header
    label_header_daftar_hp_display = Label(daftar_hp_window, text='AWONG CELL', bg='white')
    l = ('consolas', 35)
    label_header_daftar_hp_display.config(font=l)
    label_header_daftar_hp_display.place(x=810, y=50)

    # label sub header
    label_sub_header_cek_stok = Label(daftar_hp_window, text='Stok Tersedia', bg='grey', fg='white')
    l2 = ('consolas', 20)
    label_sub_header_cek_stok.config(font=l2)
    label_sub_header_cek_stok.place(x=840, y=280)

    # config label input
    l3 = ('consolas', 13)

    # label kode barang
    label_kode_barang = Label(daftar_hp_window, text='Kode Barang', bg='white')
    label_kode_barang.config(font=l3)
    label_kode_barang.place(x=70, y=130)

    # entry kode barang
    entry_kode_barang = Entry(daftar_hp_window, width=20, border=0)
    entry_kode_barang.config(font=l3)
    entry_kode_barang.place(x=180, y=133)

    # garis dibawah entry kode barang
    Frame(daftar_hp_window, width=180, height=2, bg="#141414").place(x=180, y=153)

    # label tipe
    label_tipe = Label(daftar_hp_window, text='Tipe', bg='white')
    label_tipe.config(font=l3)
    label_tipe.place(x=400, y=130)

    # entry tipe
    entry_tipe = Entry(daftar_hp_window, width=20, border=0)
    entry_tipe.config(font=l3)
    entry_tipe.place(x=450, y=133)

    # garis dibawah entry tipe
    Frame(daftar_hp_window, width=180, height=2, bg="#141414").place(x=450, y=153)

    # label merk
    label_merk = Label(daftar_hp_window, text='Merk', bg='white')
    label_merk.config(font=l3)
    label_merk.place(x=670, y=130)

    # entry merk
    entry_merk = Entry(daftar_hp_window, width=20, border=0)
    entry_merk.config(font=l3)
    entry_merk.place(x=720, y=133)

    # garis dibawah entry merk
    Frame(daftar_hp_window, width=180, height=2, bg="#141414").place(x=720, y=153)

    # label chipset
    label_chipset = Label(daftar_hp_window, text='Chipset', bg='white')
    label_chipset.config(font=l3)
    label_chipset.place(x=940, y=130)

    # entry chipset
    entry_chipset = Entry(daftar_hp_window, width=20, border=0)
    entry_chipset.config(font=l3)
    entry_chipset.place(x=1020, y=133)

    # garis dibawah entry chipset
    Frame(daftar_hp_window, width=180, height=2, bg="#141414").place(x=1020, y=153)

    # label antutu score
    label_antutu_score = Label(daftar_hp_window, text='Antutu Score', bg='white')
    label_antutu_score.config(font=l3)
    label_antutu_score.place(x=1230, y=130)

    # entry antutu score
    entry_antutu_score = Entry(daftar_hp_window, width=20, border=0)
    entry_antutu_score.config(font=l3)
    entry_antutu_score.place(x=1350, y=133)

    # garis dibawah entry antutu score
    Frame(daftar_hp_window, width=180, height=2, bg="#141414").place(x=1350, y=153)

    # label ram
    label_ram = Label(daftar_hp_window, text='RAM', bg='white')
    label_ram.config(font=l3)
    label_ram.place(x=290, y=200)

    # entry ram
    entry_ram = Entry(daftar_hp_window, width=20, border=0)
    entry_ram.config(font=l3)
    entry_ram.place(x=340, y=203)

    # garis dibawah entry ram
    Frame(daftar_hp_window, width=180, height=2, bg="#141414").place(x=340, y=223)

    # label internal storage
    label_internal_storage = Label(daftar_hp_window, text='Internal Storage', bg='white')
    label_internal_storage.config(font=l3)
    label_internal_storage.place(x=560, y=200)

    # entry internal storage
    entry_internal_storage = Entry(daftar_hp_window, width=20, border=0)
    entry_internal_storage.config(font=l3)
    entry_internal_storage.place(x=720, y=203)

    # garis dibawah entry internal storage
    Frame(daftar_hp_window, width=180, height=2, bg="#141414").place(x=720, y=223)

    # label harga
    label_harga = Label(daftar_hp_window, text='Harga', bg='white')
    label_harga.config(font=l3)
    label_harga.place(x=960, y=200)

    # entry harga
    entry_harga = Entry(daftar_hp_window, width=20, border=0)
    entry_harga.config(font=l3)
    entry_harga.place(x=1020, y=203)

    # garis dibawah entry harga
    Frame(daftar_hp_window, width=180, height=2, bg="#141414").place(x=1020, y=223)

    # label stok
    label_stok = Label(daftar_hp_window, text='Stok', bg='white')
    label_stok.config(font=l3)
    label_stok.place(x=1300, y=200)

    # entry stok
    entry_stok = Entry(daftar_hp_window, width=20, border=0)
    entry_stok.config(font=l3)
    entry_stok.place(x=1350, y=203)

    # garis dibawah entry stok
    Frame(daftar_hp_window, width=180, height=2, bg="#141414").place(x=1350, y=223)

    # query
    database = mysql.connector.connect(
            host='localhost',
            user='root',
            database='siac'
    )
    cursordb = database.cursor()
    cursordb.execute('select * from stok')
    data_stok = cursordb.fetchall()
    database.close()

    # display table
    treeview_table = ttk.Treeview(daftar_hp_window, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show='headings', height=30)
    treeview_table.place(x=53, y=330)

    treeview_table.heading(1, text='Kode Barang')
    treeview_table.heading(2, text='Tipe')
    treeview_table.heading(3, text='Merk')
    treeview_table.heading(4, text='Chipset')
    treeview_table.heading(5, text='Score Antutu V7')
    treeview_table.heading(6, text='RAM')
    treeview_table.heading(7, text='Internal Storage')
    treeview_table.heading(8, text='Harga')
    treeview_table.heading(9, text='Stok')

    for i in data_stok:
        treeview_table.insert('', 'end', values=i)

    #mengosongkan form
    def clear_entry():
        entry_tipe.delete(0, 'end')
        entry_merk.delete(0, 'end')
        entry_chipset.delete(0, 'end')
        entry_antutu_score.delete(0, 'end')
        entry_ram.delete(0, 'end')
        entry_internal_storage.delete(0, 'end')
        entry_harga.delete(0, 'end')
        entry_stok.delete(0, 'end')

    def reset_auto_increment_kode_barang_to_latest_number():
        database = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            database = 'siac'
        )
        cursor = database.cursor()
        cursor.execute('select max(kode_barang) from stok')
        last_number_of_kode_barang = cursor.fetchone()
        cursor.execute('ALTER TABLE stok AUTO_INCREMENT = %s', last_number_of_kode_barang)
        database.close()

    # def tombol
    def insert():
        data_entry_tipe = entry_tipe.get()
        data_entry_merk = entry_merk.get()
        data_entry_chipset = entry_chipset.get()
        data_entry_antutuscore = entry_antutu_score.get()
        data_entry_ram = entry_ram.get()
        data_entry_internal_storage = entry_internal_storage.get()
        data_entry_harga = entry_harga.get()
        data_entry_stok = entry_stok.get()

        if len(data_entry_tipe) == 0 or len(data_entry_merk) == 0 or len(data_entry_chipset) == 0 or len(
                data_entry_antutuscore) == 0 or len(data_entry_ram) == 0 or len(
                data_entry_internal_storage) == 0 or len(data_entry_harga) == 0 or len(data_entry_stok) == 0:
            messagebox.showerror("Error!", "Ada data yang belum diisi")
        else:
            try:
                database = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    database='siac'
                )
                cursordb = database.cursor()
                data_terinput = [data_entry_tipe, data_entry_merk, data_entry_chipset, data_entry_antutuscore,
                                 data_entry_ram, data_entry_internal_storage, data_entry_harga, data_entry_stok]
                cursordb.execute(
                    'insert into stok(tipe, merk, chipset, antutu_score, ram, internal_storage, harga, stok) values(%s, %s, %s, %s, %s, %s, %s, %s)',
                    data_terinput)
                messagebox.showinfo('Input Sukses', 'Data berhasil ditambahkan')
                clear_entry()
                database.commit()
                database.close()
                clear_entry()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def delete():
        data_entry_kode_barang = entry_kode_barang.get()
        if data_entry_kode_barang=='':
            messagebox.showerror("Error", 'Anda belum memasukkan kode barang yang ingin dihapus')
        else:
            try:
                data_input_kode_barang = [data_entry_kode_barang]
                database = mysql.connector.connect(
                    host = 'localhost',
                    user = 'root',
                    database = 'siac'
                )
                cursordb = database.cursor()
                cursordb.execute('delete from stok where kode_barang = %s', data_input_kode_barang)
                messagebox.showinfo('Delete Sukses', 'Data berhasil dihapus')
                database.commit()
                database.close()
                clear_entry()
                reset_auto_increment_kode_barang_to_latest_number()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def back():
        daftar_hp_window.destroy()
        main_menu_display()

    def reload():
        daftar_hp_window.destroy()
        daftar_hp_display()

    # button back
    Button(daftar_hp_window, width=20, height=2, fg='white', bg='#994422', border=0, command=insert, text='Insert').place(x=1650, y=120)
    Button(daftar_hp_window, width=20, height=2, fg='white', bg='#994422', border=0, command=delete, text='Delete').place(x=1650, y=165)
    Button(daftar_hp_window, width=20, height=2, fg='white', bg='#994422', border=0, command=back, text='Back').place(x=1650, y=210)
    Button(daftar_hp_window, width=20, height=2, fg='white', bg='#994422', border=0, command=reload, text='Reload').place(x=1650, y=270)

    #help
    label_help = Label(daftar_hp_window, text='*Help:   1. Untuk Insert data harus isi semua form kecuali kode barang;    2. Untuk Delete data hanya perlu isi kode barang', bg='grey', fg='white')
    l_help = ('consolas', 10)
    label_help.config(font=l_help)
    label_help.place(x=80,y=965)


# =================================================================   Cek Riwayat SPK DONE  =========================================================================================================#

def riwayat_spk():
    global riwayat_spk_window
    riwayat_spk_window = Tk()
    riwayat_spk_window.title('Awong Cell')
    window_height = 550
    window_width = 500

    def center_screen():
        """ gets the coordinates of the center of the screen """
        global screen_height, screen_width, x_cordinate, y_cordinate

        screen_width = riwayat_spk_window.winfo_screenwidth()
        screen_height = riwayat_spk_window.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        riwayat_spk_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    center_screen()

    # background
    j = 0
    r = 0
    for i in range(100):
        c = str(222222 + r)
        Frame(riwayat_spk_window, width=1900, height=1000, bg="#" + c).place(x=j, y=0)
        j = j + 80
        r = r + 8

    Frame(riwayat_spk_window, width=450, height=500, bg="white").place(x=25, y=30)
    second_frame = Frame(riwayat_spk_window, width=420, height=440, bg="grey").place(x=40, y=80)

    # label header
    label_header_riwayat_stok_display = Label(riwayat_spk_window, text='AWONG CELL', bg='white')
    l = ('consolas', 20)
    label_header_riwayat_stok_display.config(font=l)
    label_header_riwayat_stok_display.place(x=170, y=40)

    # label sub header
    label_sub_header_riwayat_stok_display = Label(riwayat_spk_window, text='Riwayat SPK', bg='grey', fg='white')
    l2 = ('consolas', 15)
    label_sub_header_riwayat_stok_display.config(font=l2)
    label_sub_header_riwayat_stok_display.place(x=185, y=85)

    # query
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        database='siac'
    )
    cursordb = database.cursor()
    cursordb.execute('select * from hasil_spk')
    data_hasil_spk = cursordb.fetchall()
    database.close()

    # display table
    treeview_table = ttk.Treeview(riwayat_spk_window, columns=(1, 2, 3, 4), show='headings', height=14)
    treeview_table.place(x=50, y=150)

    treeview_table.column(1, anchor=CENTER, stretch=NO, width=20)
    treeview_table.heading(1, text='ID')
    treeview_table.column(2, anchor=CENTER, stretch=NO, width=130)
    treeview_table.heading(2, text='Nama Pelanggan')
    treeview_table.column(3, anchor=CENTER, stretch=NO, width=150)
    treeview_table.heading(3, text='Rekomendasi')
    treeview_table.column(4, anchor=CENTER, stretch=NO, width=100)
    treeview_table.heading(4, text='Tanggal')

    for i in data_hasil_spk:
        treeview_table.insert('', 'end', values=i)

    def back():
        riwayat_spk_window.destroy()
        main_menu_display()

    Button(riwayat_spk_window, width=20, height=2, fg='white', bg='#994422', border=0, command=back, text='BACK').place(x=175, y=470)

    riwayat_spk_window.mainloop()

#=================================================================================================================================================================================================#

if __name__ == '__main__':
    login_display()


#=================================================================================================================================================================================================#
#=================================================================================================================================================================================================#