import os.path
import time
import tkinter
import pandas as pd
from JST import *
from matplotlib import pyplot as plt
import matplotlib
from os import path
from tkinter import ttk
from tkinter import *
matplotlib.use('TkAgg')
import tkinter.filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import datetime

jst = JST()

def Display():
    global gui
    gui = Tk()
    gui.title("PREDIKSI BITCOIN - USD")
    gui.resizable(0, 0)
    window_height = 700
    window_width = 1800

    # centering window
    def center_screen():
        """ gets the coordinates of the center of the screen """
        global screen_height, screen_width, x_cordinate, y_cordinate

        screen_width = gui.winfo_screenwidth()
        screen_height = gui.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        gui.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    center_screen()

    notebook = ttk.Notebook(gui)

    tab1 = Frame(notebook)
    tab2 = Frame(notebook)
    tab3 = Frame(notebook)

    notebook.add(tab1, text='   Latih    ')
    notebook.add(tab2, text='    Uji     ')
    notebook.add(tab3, text='  Prediksi  ')

    # config label
    l = ('consolas', 18)
    le = ('consolas', 13)

    ###========= Widget for tab 1 =========###

    # label header pelatihan
    label_header_pelatihan = Label(tab1, text='PELATIHAN')
    label_header_pelatihan.config(font=l)
    label_header_pelatihan.place(x=20, y=10)

    # input data latih
    label_data_latih = Label(tab1, text='Data Latih')
    label_data_latih.config(font=le)
    label_data_latih.place(x=20, y=60)

    def BacaDataLatih():
        global data_latih, n_datalatih, nilai_tukar_norm, nilai_tukar, nilai_usd, tanggal, data
        try:
            data_path = tkinter.filedialog.askopenfile(mode='r', filetypes=[('Excel Files', '*.xlsx')])

            file_path = os.path.abspath(data_path.name)
            data = pd.read_excel(file_path, sheet_name='Data Latih')

            data = data.to_numpy()
            tanggal = data[:, 0]
            nilai_usd = data[:, 1]
            nilai_tukar = data[:, 2]

            nilai_tukar_norm = jst.Normalisasi(nilai_tukar)
            data_latih = nilai_tukar_norm
            n_datalatih = len(data_latih)

            data_latih = data_latih
        except:
            print('Terjadi kesalahan pada pembacaan data latih', sys.exc_info()[0])

    Button(tab1, width=10, height=1, border=4, command=BacaDataLatih, text='Open').place(x=150, y=60)

    # input n_input
    label_n_input = Label(tab1, text='Neuron Input')
    label_n_input.config(font=le)
    label_n_input.place(x=20, y=120)

    entry_n_input = Entry(tab1, width=9, border=1, justify='center')
    entry_n_input.insert(0, 3)
    entry_n_input.config(font=le)
    entry_n_input.place(x=150, y=121)

    # inpun n_hidden
    label_n_hidden = Label(tab1, text='Neuron Hidden')
    label_n_hidden.config(font=le)
    label_n_hidden.place(x=20, y=160)

    entry_n_hidden = Entry(tab1, width=9, border=1, justify='center')
    entry_n_hidden.insert(0, 3)
    entry_n_hidden.config(font=le)
    entry_n_hidden.place(x=150, y=161)

    # input n_output
    label_n_output = Label(tab1, text='Neuron Output')
    label_n_output.config(font=le)
    label_n_output.place(x=20, y=200)

    entry_n_output = Entry(tab1, width=9, border=1, justify='center')
    entry_n_output.insert(0, 1)
    entry_n_output.config(font=le)
    entry_n_output.place(x=150, y=201)

    # input alpha
    label_alpha = Label(tab1, text='Alpha')
    label_alpha.config(font=le)
    label_alpha.place(x=250, y=120)

    entry_alpha = Entry(tab1, width=9, border=1, justify='center')
    entry_alpha.insert(0, 0.1)
    entry_alpha.config(font=le)
    entry_alpha.place(x=400, y=121)

    # input toleransi eror
    label_toleransi_eror = Label(tab1, text='Toleransi Eror')
    label_toleransi_eror.config(font=le)
    label_toleransi_eror.place(x=250, y=160)

    entry_toleransi_eror = Entry(tab1, width=9, border=1, justify='center')
    entry_toleransi_eror.insert(0, 0.001)
    entry_toleransi_eror.config(font=le)
    entry_toleransi_eror.place(x=400, y=161)

    # input iterasi
    label_iterasi = Label(tab1, text='Iterasi')
    label_iterasi.config(font=le)
    label_iterasi.place(x=250, y=200)

    entry_iterasi = Entry(tab1, width=9, border=1, justify='center')
    entry_iterasi.insert(0, 150)
    entry_iterasi.config(font=le)
    entry_iterasi.place(x=400, y=201)

    # munculin jumlah data latih
    label_n_datalatih = Label(tab1, text='Data Latih')
    label_n_datalatih.config(font=le)
    label_n_datalatih.place(x=20, y=260)

    # munculin waktu komputasi
    label_waktu_komputasi_latih = Label(tab1, text='Waktu Komputasi')
    label_waktu_komputasi_latih.config(font=le)
    label_waktu_komputasi_latih.place(x=20, y=280)

    # munculin MSE
    label_mse = Label(tab1, text='MSE')
    label_mse.config(font=le)
    label_mse.place(x=20, y=300)

    # munculin tabel data latih
    label_tabel_latih = Label(tab1, text='Data Latih')
    label_tabel_latih.config(font=le)
    label_tabel_latih.place(x=20, y=355)

    # munculin foot note
    le3 = ('consolas', 10)
    Label(tab1, text='*Neuron = Banyak Node Neural Network', font=le3).place(x=20, y=520)
    Label(tab1, text='*Alpha = Laju Pembelajaran', font=le3).place(x=20, y=540)
    Label(tab1, text='*Toleransi Eror = Ambang Batas Eror yang ditoleransi', font=le3).place(x=20, y=560)
    Label(tab1, text='*Iterasi = Jumlah Pengulangan', font=le3).place(x=20, y=580)
    Label(tab1, text='*MSE = Rata-Rata Eror Seluruh Data pada Iterasi Terakhir', font=le3).place(x=20, y=600)

    # button next
    def latih_btn_gui():
        def InisialisasiBobot():
            global V, W, n_input, n_hidden, n_output
            try:
                # mendapatkan inputan pada kotak teks
                n_input = int(entry_n_input.get())
                n_hidden = int(entry_n_hidden.get())
                n_output = int(entry_n_output.get())

                V = 0
                W = 0
                flag = False

                # mengecek apakah file bobot awal csv sudah ada atau belum,
                # apabila sudah ada maka bobot V dan W tidak akan dibangkitkan secara acak lagi
                # melainkan menggunakan bobot yang awal yang sudah ada
                if (path.exists('bobotawal_V.csv') == True and path.exists('bobotawal_W.csv') == True):
                    # membaca bobot awal yang tersimpan pada file csv
                    V = np.genfromtxt('bobotawal_V.csv', delimiter=',')
                    W = np.genfromtxt('bobotawal_W.csv', delimiter=',')
                    baris, kolom = V.shape

                    if (n_input == (baris - 1) and n_hidden == kolom):
                        W_tmp = np.zeros((n_hidden + 1, n_output))
                        W_tmp[:, 0] = W
                        W = W_tmp
                        flag = True
# membangkitkan bobot V dan W jika ukuran bobot awal yang terdapat dalam file csv tidak sesuai ukuran neuron
                if flag == False:
                    [V, W] = jst.InisialisasiBobot(n_input, n_hidden, n_output)

                V = V
                W = W

                # menyimpan bobot V dan bobot W awal pada file csv
                # print('BOBOT V AWAL:')
                np.savetxt('bobotawal_V.csv', V, delimiter=',')
                # print('BOBOT W AWAL :')
                np.savetxt('bobotawal_W.csv', W, delimiter=',')

            except:
                print('Terjadi kesalahan pada proses pembangkitan bobot awal', sys.exc_info()[0])

        def ProsesPelatihan():
            global n_input, n_hidden, n_output, alpha, toleransi_eror, iterasi, n_datalatih, b
            global m, x, error, errorsquare, mse, jumlah_iterasi, target_jst, keluaran_jst, x, y
            global datalatih, data_tmp, out_target, target_jst, Z, V, W, time_stop, time_start
            try:
                time_start = time.perf_counter()

                n_input = int(entry_n_input.get())
                n_hidden = int(entry_n_hidden.get())
                n_output = int(entry_n_output.get())
                alpha = float(entry_alpha.get())
                toleransi_eror = float(entry_toleransi_eror.get())
                iterasi = int(entry_iterasi.get())

                n_datalatih = len(data_latih)
                error = np.zeros((n_datalatih - n_input, 1))
                errorsquare = np.zeros((n_datalatih - n_input, 1))
                mse = np.zeros((iterasi, 1))
                jumlah_iterasi = 0

                target_jst = np.zeros((n_datalatih - n_input, 1))
                keluaran_jst = np.zeros((n_datalatih - n_input, 1))

                for i in range(iterasi):
                    print('Iterasi ke-', (i + 1))
                    for j in range(n_datalatih - n_input):
                        datalatih = np.zeros((1, n_input))
                        out_target = np.zeros((1, 1))

                        data_tmp = data_latih[j:j + n_input, :]
                        datalatih = np.transpose(data_tmp)
                        out_target[0, 0] = data_latih[j + n_input, 0]

                        target_jst[j, 0] = out_target[0, 0]

                        [Z, Y] = jst.PerambatanMaju(datalatih[0, :], V, W, n_hidden, n_output)
                        [W, V] = jst.PerambatanMundur(out_target[0, :], Y, datalatih[0, :], alpha, Z, W, V)
                        error[j, 0] = round(abs(out_target[0, 0] - Y[0, 0]), 8)
                        errorsquare[j, 0] = round(error[j, 0] ** 2, 8)
                        keluaran_jst[j, 0] = Y[0, 0]

                    mse[i, 0] = round(sum(errorsquare[:, 0]) / (n_datalatih - n_input), 8)  ### MSE
                    print('MSE :', mse[i, 0])

                    if mse[i, 0] <= toleransi_eror:
                        jumlah_iterasi = i + 1
                        break

                    jumlah_iterasi = i + 1

                # menyimpan bobot terlatih pada file csv
                np.savetxt('bobotterlatih_V.csv', V, delimiter=',')
                np.savetxt('bobotterlatih_W.csv', W, delimiter=',')

                # menampilkan grafik regresi proses pelatihan
                x = target_jst[:, 0]
                y = keluaran_jst[:, 0]
                m, b = np.polyfit(x, y, 1)

                # menampilkan waktu komputasi dan MSE pelatihan
                time_stop = (time.perf_counter() - time_start)

                label_hasil_n_datalatih = Label(tab1, text=n_datalatih)
                label_hasil_n_datalatih.config(font=le)
                label_hasil_n_datalatih.place(x=200, y=260)

                label_hasil_waktu_komputasi_latih = Label(tab1, text=str(round(time_stop, 3)) + ' sec')
                label_hasil_waktu_komputasi_latih.config(font=le)
                label_hasil_waktu_komputasi_latih.place(x=200, y=280)

                label_hasil_mse = Label(tab1, text=str(mse[jumlah_iterasi - 1, 0]))
                label_hasil_mse.config(font=le)
                label_hasil_mse.place(x=200, y=300)

                # treeview data latih
                treeview_table_datalatih = ttk.Treeview(tab1, columns=(1, 2, 3, 4), show='headings', height=5)
                treeview_table_datalatih.place(x=20, y=385)
                treeview_table_datalatih.column(1, anchor=CENTER, stretch=YES, width=150)
                treeview_table_datalatih.heading(1, text='Tanggal')
                treeview_table_datalatih.column(2, anchor=CENTER, stretch=YES, width=100)
                treeview_table_datalatih.heading(2, text='BTC')
                treeview_table_datalatih.column(3, anchor=CENTER, stretch=YES, width=100)
                treeview_table_datalatih.heading(3, text='BTC-USD')
                treeview_table_datalatih.column(4, anchor=CENTER, stretch=YES, width=120)
                treeview_table_datalatih.heading(4, text='BTC-USD Normalisasi')

                nilai_tukar_norm_ = []
                for xyz in range(len(nilai_tukar_norm)):
                    for xxyyzz in nilai_tukar_norm[xyz]:
                        nilai_tukar_norm_.append(xxyyzz)

                array_datalatih = np.array((tanggal, nilai_usd, nilai_tukar, nilai_tukar_norm_))
                for x1, x2, x3, x4 in array_datalatih.T:
                    treeview_table_datalatih.insert('', 'end', values=(x1, x2, x3, x4))

            except:
                print('An error occurred during the training process', sys.exc_info()[0])

        InisialisasiBobot()
        ProsesPelatihan()

        # menampilkan grafik di gui
        fig1 = Figure(figsize=(6,6), dpi=100)
        plot1 = fig1.add_subplot(111)
        plot1.plot(mse[0:jumlah_iterasi, 0])
        plot1.set_title('Grafik Konvergensi Proses Pelatihan')
        plot1.set_ylabel('MSE')
        plot1.set_xlabel('Iterasi')
        canvas1 = FigureCanvasTkAgg(fig1, master=tab1)
        canvas1.draw()
        canvas1.get_tk_widget().place(x=520, y=40)

        fig2 = Figure(figsize=(6,6), dpi=100)
        plot2 = fig2.add_subplot(111)
        plot2.plot(x, y, '*', color='blue')
        plot2.plot(x, m * x + b, color='red')
        plot2.set_title('Grafik Regresi Proses Pelatihan')
        plot2.set_ylabel('Keluaran JSt')
        plot2.set_xlabel('Target Keluaran')
        canvas2 = FigureCanvasTkAgg(fig2, master=tab1)
        canvas2.draw()
        canvas2.get_tk_widget().place(x=1150, y=40)

        toolbar = NavigationToolbar2Tk(canvas2, tab1)
        toolbar.update()

    Button(tab1, width=10, height=1, border=4, command=latih_btn_gui, text='Latih').place(x=260, y=60)

    # ======================================================== #

    label_pembatas1 = Label(tab1, text='|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n,'
                                       '|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|', background='White')
    label_pembatas1.config(font=le)
    label_pembatas1.place(x=500, y=-5)

    ###========= Widget for tab 2 =========###

    # label header pengujian
    label_header_pengujian = Label(tab2, text='PENGUJIAN')
    label_header_pengujian.config(font=l)
    label_header_pengujian.place(x=20, y=10)

    # input data uji
    label_data_uji = Label(tab2, text='Data Uji')
    label_data_uji.config(font=le)
    label_data_uji.place(x=20, y=60)

    # jumlah data uji
    label_jumlah_data_uji = Label(tab2, text='Jumlah Data Uji')
    label_jumlah_data_uji.config(font=le)
    label_jumlah_data_uji.place(x=150, y=80)

    # Waktu komputasi
    label_waktu_komputasi_uji = Label(tab2, text='Waktu Komputasi')
    label_waktu_komputasi_uji.config(font=le)
    label_waktu_komputasi_uji.place(x=150, y=110)

    # Rata rata eror
    label_rata_rata_eror = Label(tab2, text='Rata-Rata Eror')
    label_rata_rata_eror.config(font=le)
    label_rata_rata_eror.place(x=150, y=140)

    # rata rata akurasi
    label_rata_rata_akurasi = Label(tab2, text='Rata-Rata Akurasi')
    label_rata_rata_akurasi.config(font=le)
    label_rata_rata_akurasi.place(x=150, y=170)

    # munculin tabel data uji
    label_tabel_uji = Label(tab2, text='Data Uji')
    label_tabel_uji.config(font=le)
    label_tabel_uji.place(x=20, y=210)

    # munculin hasil prediksi pengujian
    label_hasil_uji_pengujian = Label(tab2, text='Prediksi Pengujian')
    label_hasil_uji_pengujian.config(font=le)
    label_hasil_uji_pengujian.place(x=20, y=405)

    def BacaDataUji():
        global data, tanggal, nilai_usd, nilai_tukar, data_uji, n_datauji, data_uji_full
        try:
            data_path = tkinter.filedialog.askopenfile(mode='r', filetypes=[('Excel Files', '*.xlsx')])
            file_path = os.path.abspath(data_path.name)
            data = pd.read_excel(file_path, sheet_name='Data Uji')

            writer = pd.ExcelWriter('datauji.xlsx')
            data.to_excel(writer, index=False)
            writer.save()

            data = data.to_numpy()

            tanggal = data[:, 0]
            nilai_usd = data[:, 1]
            nilai_tukar = data[:, 2]

            data_uji = nilai_tukar
            data_uji_full = data

            n_datauji = len(data_uji)

        except:
            print('Terjadi kesalahan pada pembacaan data uji', sys.exc_info()[0])

    Button(tab2, width=10, height=1, border=4, command=BacaDataUji, text='Open').place(x=20, y=91)

    # tombol uji
    def uji_btn_gui():

        def ProsesPengujian():
            global n_input, n_hidden, n_output, n_datauji, data_uji_norm, hasil_prediksi
            global datauji, data_tmp, Z, Y, hasil_prediksi, kurs_min, kurs_max, hasilprediksi_denorm
            global outputsebenarnya, eror_, a, akurasi, time_start, time_stop
            try:
                time_start = time.perf_counter()

                n_input = int(entry_n_input.get())
                n_hidden = int(entry_n_hidden.get())
                n_output = int(entry_n_output.get())

                n_datauji = len(data_uji)
                data_uji_norm = jst.Normalisasi(data_uji)
                hasil_prediksi = np.zeros((n_datauji - n_input, 1))
                for j in range(n_datauji - n_input):
                    datauji = np.zeros((1, n_input))
                    data_tmp = data_uji_norm[j:j + n_input, :]
                    datauji = np.transpose(data_tmp)

                    [Z, Y] = jst.PerambatanMaju(datauji[0, :], V, W, n_hidden, n_output)
                    hasil_prediksi[j, 0] = Y[0, 0]

                # melakukan denormalisasi hasil prediksi dan keluaran sebenarnya
                kurs_min = min(data_uji)
                kurs_max = max(data_uji)

                hasilprediksi_denorm = np.zeros((n_datauji - n_input, 1))
                outputsebenarnya = np.zeros((n_datauji - n_input, 1))

                for i in range(n_datauji - n_input):
                    hasilprediksi_denorm[i, 0] = jst.Denormalisasi(hasil_prediksi[i, 0], kurs_min, kurs_max)
                    outputsebenarnya[i, 0] = data_uji[i + n_input]

                # menampilkan hasil prediksi pada tabel
                rata2akurasi = 0
                rata2eror = 0

                # treeview hasil prediksi
                treeview_table_hasil_prediksi = ttk.Treeview(tab2, columns=(1, 2, 3, 4), show='headings', height=7)
                treeview_table_hasil_prediksi.place(x=20, y=435)
                treeview_table_hasil_prediksi.column(1, anchor=CENTER, stretch=YES, width=111)
                treeview_table_hasil_prediksi.heading(1, text='Prediksi')
                treeview_table_hasil_prediksi.column(2, anchor=CENTER, stretch=YES, width=111)
                treeview_table_hasil_prediksi.heading(2, text='BTC-USD')
                treeview_table_hasil_prediksi.column(3, anchor=CENTER, stretch=YES, width=111)
                treeview_table_hasil_prediksi.heading(3, text='Eror')
                treeview_table_hasil_prediksi.column(4, anchor=CENTER, stretch=YES, width=111)
                treeview_table_hasil_prediksi.heading(4, text='Akurasi(%)')

                array_hasilPengujian = []

                # === MAPE === #
                for i in range(n_datauji - n_input):
                    eror_ = round(abs(hasilprediksi_denorm[i, 0] - outputsebenarnya[i, 0]), 2)

                    a = 0

                    if (hasilprediksi_denorm[i, 0] > outputsebenarnya[i, 0]):
                        a = hasilprediksi_denorm[i, 0]
                    else:
                        a = outputsebenarnya[i, 0]

                    if (a == 0):
                        a = 1


                    rata2eror += round((eror_ / a * 100), 2)                # MAPE
                    akurasi = round(100 - (eror_ / a * 100), 2)
                    rata2akurasi += akurasi
                # === === #
                    arr_hasilPengujian = np.array((hasilprediksi_denorm[i, 0], outputsebenarnya[i, 0], eror_, akurasi))
                    array_hasilPengujian.append(arr_hasilPengujian)


                rata2eror = round(rata2eror / (n_datauji - n_input), 3)
                rata2akurasi = round(rata2akurasi / (n_datauji - n_input), 3)
                time_stop = (time.perf_counter() - time_start)

                label_n_datauji = Label(tab2, text=n_datauji)
                label_n_datauji.config(font=le)
                label_n_datauji.place(x=330, y=80)

                label_hasil_waktu_komputasi_uji = Label(tab2, text=str(round(time_stop, 3)) + ' sec')
                label_hasil_waktu_komputasi_uji.config(font=le)
                label_hasil_waktu_komputasi_uji.place(x=330, y=110)

                label_hasil_rata_rata_eror = Label(tab2, text=rata2eror)
                label_hasil_rata_rata_eror.config(font=le)
                label_hasil_rata_rata_eror.place(x=330, y=140)

                label_hasil_rata_rata_akurasi = Label(tab2, text=str(rata2akurasi) + ' %')
                label_hasil_rata_rata_akurasi.config(font=le)
                label_hasil_rata_rata_akurasi.place(x=330, y=170)

                list_hasilPengujian = np.array(array_hasilPengujian)
                # Perulangan masukin ke tabel hasil prediksi
                for x1, x2, x3, x4 in list_hasilPengujian:
                    treeview_table_hasil_prediksi.insert('', 'end', values=(x1, x2, x3, x4))

            except:
                print('Terjadi kesalahan pada proses pengujian', sys.exc_info()[0])

        def GrafikHasilPengujian():
            global y1, y2, n_datauji, x_tmp, x, x_, y_, m, b
            try:
                y1 = hasilprediksi_denorm
                y2 = outputsebenarnya
                n_datauji = len(y1)
                x_tmp = list(range(1, n_datauji + 1))
                x = np.array([x_tmp]).transpose()

                x_ = outputsebenarnya[:, 0]
                y_ = hasilprediksi_denorm[:, 0]
                m, b = np.polyfit(x_, y_, 1)

                # menampilkan grafik di gui
                fig1 = Figure(figsize=(6, 6), dpi=100)
                plot1 = fig1.add_subplot(111)
                plot1.plot(x, y1, color='blue')
                plot1.plot(x, y2, color='red')
                plot1.set_title('Grafik Perbandingan Antara Hasil Prediksi dan Data Sebenarnya')
                plot1.set_ylabel('Kurs Jual (USD)')
                plot1.set_xlabel('Data Uji')
                plot1.legend(('Hasil Prediksi', 'Data Sebenarnya'), loc='upper right')
                canvas1 = FigureCanvasTkAgg(fig1, master=tab2)
                canvas1.draw()
                canvas1.get_tk_widget().place(x=520, y=40)

                fig2 = Figure(figsize=(6, 6), dpi=100)
                plot2 = fig2.add_subplot(111)
                plot2.plot(x_, y_, '*', color='blue')
                plot2.plot(x_, m * x_ + b, color='red')
                plot2.set_title('Grafik Regresi Proses Pengujian')
                plot2.set_ylabel('Keluaran JSt')
                plot2.set_xlabel('Keluaran Sebenarnya')
                canvas2 = FigureCanvasTkAgg(fig2, master=tab2)
                canvas2.draw()
                canvas2.get_tk_widget().place(x=1150, y=40)

                toolbar = NavigationToolbar2Tk(canvas2, tab2)
                toolbar.update()

            except:
                print('Terjadi kesalahan pada saat menampilkan grafik hasil pengujian', sys.exc_info()[0])

        ProsesPengujian()

        # treeview data uji
        treeview_table_datauji = ttk.Treeview(tab2, columns=(1, 2, 3), show='headings', height=7)
        treeview_table_datauji.place(x=20, y=235)
        treeview_table_datauji.column(1, anchor=CENTER, stretch=YES, width=150)
        treeview_table_datauji.heading(1, text='Tanggal')
        treeview_table_datauji.column(2, anchor=CENTER, stretch=YES, width=150)
        treeview_table_datauji.heading(2, text='BTC')
        treeview_table_datauji.column(3, anchor=CENTER, stretch=YES, width=150)
        treeview_table_datauji.heading(3, text='BTC-USD')

        array_datauji = np.array((tanggal, nilai_usd, nilai_tukar))
        for x1, x2, x3 in array_datauji.T:
            treeview_table_datauji.insert('', 'end', values=(x1, x2, x3))

        GrafikHasilPengujian()

    Button(tab2, width=10, height=1, border=4, command=uji_btn_gui, text='Uji').place(x=20, y=131)

    # ======================================================== #

    label_pembatas1 = Label(tab2, text='|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|,'
                                       '\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|', background='White')
    label_pembatas1.config(font=le)
    label_pembatas1.place(x=500, y=-5)


    ###========= Widget for tab 3 =========###

    # label header Prediksi
    label_header_prediksi = Label(tab3, text='PREDIKSI')
    label_header_prediksi.config(font=l)
    label_header_prediksi.place(x=20, y=10)

    # input n_prediksi
    label_n_prediksi = Label(tab3, text='Jumlah Prediksi')
    label_n_prediksi.config(font=le)
    label_n_prediksi.place(x=20, y=60)

    entry_n_prediksi = Entry(tab3, width=9, border=1, justify='center')
    entry_n_prediksi.insert(0, 5)
    entry_n_prediksi.config(font=le)
    entry_n_prediksi.place(x=170, y=60)

    Label(tab3, text='Hari', font=le).place(x=260, y=60)

    # data sebelumnya
    label_data_sebelumnya = Label(tab3, text='Data Sebelumnya')
    label_data_sebelumnya.config(font=le)
    label_data_sebelumnya.place(x=20, y=210)

    # tabel hasil prediksi
    label_tabel_hasil_prediksi = Label(tab3, text='Hasil Prediksi')
    label_tabel_hasil_prediksi.config(font=le)
    label_tabel_hasil_prediksi.place(x=20, y=445)

    # label penghias space kosong
    label_penghias = Label(tab3, text='Sistem   Prediksi   Harga   Bitcoin\nBerdasarkan Historical Price Data,'
                                      '\nMenggunakan Metode Backpropagation')
    l0=('consolas', 18)
    label_penghias.config(font=l0)
    label_penghias.place(x=1280, y=270)

    # tombol prediksi
    def prediksi():

        treeview_table_datasebelumnya = ttk.Treeview(tab3, columns=(1, 2, 3), show='headings', height=9)
        treeview_table_datasebelumnya.place(x=20, y=235)
        treeview_table_datasebelumnya.column(1, anchor=CENTER, stretch=YES, width=150)
        treeview_table_datasebelumnya.heading(1, text='Tanggal')
        treeview_table_datasebelumnya.column(2, anchor=CENTER, stretch=YES, width=150)
        treeview_table_datasebelumnya.heading(2, text='BTC')
        treeview_table_datasebelumnya.column(3, anchor=CENTER, stretch=YES, width=150)
        treeview_table_datasebelumnya.heading(3, text='BTC-USD')

        # tree hasil prediksi
        treeview_table_hasil_prediksi = ttk.Treeview(tab3, columns=(1, 2), show='headings', height=5)
        treeview_table_hasil_prediksi.place(x=20, y=470)
        treeview_table_hasil_prediksi.column(1, anchor=CENTER, stretch=YES, width=225)
        treeview_table_hasil_prediksi.heading(1, text='Kurs BTC')
        treeview_table_hasil_prediksi.column(2, anchor=CENTER, stretch=YES, width=225)
        treeview_table_hasil_prediksi.heading(2, text='Kurs BTC-USD')

        def LoadDataSebelumnya():
            global data_uji_full, tanggal, nilai_usd, nilai_tukar, n_datasebelumnya
            try:
                data = {
                    'Tanggal': tanggal,
                    'Nilai USD': nilai_usd,
                    'IDR - USD': nilai_tukar
                }
                data = pd.DataFrame(data)
                data = data.to_numpy()

                tanggal = data[:, 0]
                nilai_usd = data[:, 1]
                nilai_tukar = data[:, 2]

                array_datalatih = np.array((tanggal, nilai_usd, nilai_tukar))
                for x1, x2, x3 in array_datalatih.T:
                    treeview_table_datasebelumnya.insert('', 'end', values=(x1, x2, x3))

            except:
                print('Terjadi kelasalahan pada saat menampilkan data sebelumnya', sys.exc_info()[0])
                # treeview data sebelumnya

        def ProsesPrediksi():
            global n_input, n_hidden, n_output, n_dataprediksi, V, W, data_uji, data_uji_norm, n_datauji
            global data_uji_terakhir, data_prediksi, hasil_prediksi, data_tmp, datauji, Z, Y, kurs_min
            global kurs_max, hasilprediksi_denorm, x, y, y1, y2, x_tmp, x1
            try:
                n_input = int(entry_n_input.get())
                n_hidden = int(entry_n_hidden.get())
                n_output = int(entry_n_output.get())
                n_dataprediksi = int(entry_n_prediksi.get())

                V = V
                W = W

                data_uji = data_uji
                data_uji_norm = jst.Normalisasi(data_uji)
                n_datauji = len(data_uji_norm)

                data_uji_terakhir = data_uji_norm[n_datauji - n_input:n_datauji]
                data_prediksi = np.zeros((n_input + n_dataprediksi, 1))
                data_prediksi[0:n_input] = data_uji_terakhir
                hasil_prediksi = np.zeros((n_dataprediksi, 1))

                # melakukakan proses prediksi sebanyak data yang diinginkan
                for j in range(n_dataprediksi):
                    datauji = np.zeros((1, n_input))

                    data_tmp = data_prediksi[j:j + n_input, :]
                    datauji = np.transpose(data_tmp)

                    [Z, Y] = jst.PerambatanMaju(datauji[0, :], V, W, n_hidden, n_output)

                    hasil_prediksi[j, 0] = Y[0, 0]
                    data_prediksi[j + n_input, 0] = Y[0, 0]

                # Melakukan denormalisasi hasil prediksi dan menampilaknnya pada tabel
                kurs_min = min(data_uji)
                kurs_max = max(data_uji)

                hasilprediksi_denorm = np.zeros((n_dataprediksi, 1))
                for i in range(n_dataprediksi):
                    hasilprediksi_denorm[i, 0] = jst.Denormalisasi(hasil_prediksi[i, 0], kurs_min, kurs_max)

                # menampilkan grafk perbandingan hasil prediksi dan data sebenarnya pada form
                x = list(range(n_datauji + 1, n_datauji + 1 + len(hasil_prediksi)))
                y = hasilprediksi_denorm[:, 0]

                # menampilkan grafik pada figure
                y1 = data_uji
                y2 = y
                n_datauji = len(y1)
                x_tmp = list(range(1, n_datauji + 1))
                x1 = np.array([x_tmp]).transpose()

                data_hasil_prediksi_ = []
                for xxxx in range(len(hasil_prediksi)):
                    for yyyy in hasil_prediksi[xxxx]:
                        data_hasil_prediksi_.append(yyyy)

                data_hasilprediksi_denorm_ = []
                for qqqq in range(len(hasilprediksi_denorm)):
                    for wwww in hasilprediksi_denorm[qqqq]:
                        data_hasilprediksi_denorm_.append(wwww)

                array_hasil_prediksi = np.array((data_hasil_prediksi_, data_hasilprediksi_denorm_))

                for xx1, xx2 in array_hasil_prediksi.T:
                    treeview_table_hasil_prediksi.insert('', 'end', values=(xx1, xx2))

                fig1 = Figure(figsize=(7, 6), dpi=100)
                plot1 = fig1.add_subplot(111)
                plot1.plot(x1, y1, 'b', x, y2, 'r')
                plot1.set_title('Grafik Hasil Prediksi')
                plot1.set_ylabel('Kurs Jual (USD)')
                plot1.set_xlabel('Data Ke -')
                plot1.legend(('Data Uji/Data Sebelumnnya', 'Data Hasil Prediksi'), loc='upper right')
                canvas1 = FigureCanvasTkAgg(fig1, master=tab3)
                canvas1.draw()
                canvas1.get_tk_widget().place(x=520, y=40)

                toolbar = NavigationToolbar2Tk(canvas1, tab3)
                toolbar.update()

            except:
                print('Terjadi Kesalahan pada proses prediksi ', sys.exc_info()[0])

        LoadDataSebelumnya()
        ProsesPrediksi()

    Button(tab3, width=10, height=1, border=4, command=prediksi, text='Prediksi').place(x=20, y=100)

    # ======================================================== #

    label_pembatas1 = Label(tab3,
                            text='|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n,'
                                 '|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|', background='White')
    label_pembatas1.config(font=le)
    label_pembatas1.place(x=500, y=-5)

    ###------- Reload ---------###

    def reload():
        gui.destroy()
        Display()

    Button(tab1, width=10, height=1, border=4, command=reload, text='Reload').place(x=1700, y=5)
    Button(tab2, width=10, height=1, border=4, command=reload, text='Reload').place(x=1700, y=5)
    Button(tab3, width=10, height=1, border=4, command=reload, text='Reload').place(x=1700, y=5)

    ###------- Save PDF ---------###

    def save_pdf():
        tanggal2pdf = tanggal.tolist()
        tanggalterakhir = tanggal2pdf[-1]
        usd2pdf = nilai_usd.tolist()
        tukar2pdf = nilai_tukar.tolist()
        import datetime

        date_generator = pd.date_range(start=tanggalterakhir, periods=n_dataprediksi + 1)
        date_prediksi = date_generator[1:]

        for q in date_prediksi:
            tanggal2pdf.append(q)

        for qq in range(n_dataprediksi):
            usd2pdf.append(1)

        for qqq in y2:
            tukar2pdf.append(qqq)

        data2pdf = {
            'Tanggal': tanggal2pdf,
            'Nilai BTC': usd2pdf,
            'BTC - USD': tukar2pdf
        }
        data2pdf = pd.DataFrame(data2pdf)
        data2pdf.to_excel('reportPrediksi.xlsx', sheet_name='Hasil Prediksi')
        from tkinter import messagebox
        messagebox.showinfo('Save PDF', 'Tabel Berhasil Disimpan')

    Button(tab3, width=10, height=1, border=4, command=save_pdf, text='Save PDF').place(x=1700, y=45)

    ###------- -------- ---------###

    notebook.pack(expand=1, fill="both")


    gui.mainloop()
Display()