import numpy as np
import sys
from math import *


class JST:

    # mendefinisikan fungsi untuk membangkitkan/menginisialisasi bobot awal
    def InisialisasiBobot(self, n_input, n_hidden, n_output):  # fungsi untuk menginisiasi bobot awal secara random
        try:
            V = np.zeros((n_input + 1, n_hidden))  # bobot dari input ke hidden
            W = np.zeros((n_hidden + 1, n_output))  # bobot dari hidden ke output

            np.random.seed(10)
            tmp_v = np.random.rand(n_input, n_hidden)
            tmp_w = np.random.rand(n_hidden, n_output)

            V[0, :] = 0.1           # bias
            V[1: n_input + 1, :] = tmp_v

            W[0, :] = 0.1
            W[1: n_hidden + 1, :] = tmp_w

            return [V, W]
        except:
            print('Terjadi kesalahan dalam fungsi inisiasi bobot', sys.exc_info()[0])

    def Normalisasi(self, data):  # fungsi untuk normalisasi/scaling data (minmaxscaler)
        try:
            n_data = data.shape[0]
            x = np.zeros((n_data, 1))
            datamax = max(data)
            datamin = min(data)

            for i in range(n_data):
                x[i, 0] = round((data[i] - datamin) / (datamax - datamin), 3) # round = fungsi untuk membatasi banyak desimal dibelakang koma

            return x  # dataset ternormalisasi
        except:
            print('Terjadi kesalahan dalam fungsi normalisasi', sys.exc_info()[0])

    def Denormalisasi(self, data, mindata, maxdata):  # fungsi denormalisasi
        try:
            x = round((data * maxdata - data * mindata) + mindata, 3)

            return x
        except:
            print('Terjadi kesalahan dalam fungsi denormalisasi', sys.exc_info()[0])

    def Input2Hidden(self, data, n_hidden, V):  # fungsi untuk perhitungan di hidden layer
        try:
            n_data = data.shape[0]
            Z = np.zeros((1, n_hidden))

            for j in range(n_hidden):
                tmp = 0
                for i in range(n_data):
                    tmp = tmp + V[i + 1, j] * data[i]

                tmp = V[0, j] + tmp
                Z[0, j] = round(1 / (1 + exp(-tmp)), 3)

            return Z
        except:
            print('Terjadi kesalahan dalam fungsi hitung nilai neuron hidden layer/nilai Z', sys.exc_info()[0])

    def Hidden2Output(self, Z, n_output, W):  # fungsi untuk perhitungan di output layer
        try:
            [row, col] = Z.shape
            Y = np.zeros((1, n_output))

            for k in range(n_output):
                tmp = 0
                for j in range(col):
                    tmp = tmp + W[j + 1, k] * Z[0, j]

                tmp = W[0, k] + tmp
                Y[0, k] = round(1 / (1 + exp(-tmp)), 3)

            return Y
        except:
            print('Terjadi kesalahan dalam fungsi hitung nilai neuron output layer/nilai Y', sys.exc_info()[0])

    def PerambatanMaju(self, data, V, W, n_hidden, n_output):
        try:
            Z = self.Input2Hidden(data, n_hidden, V)
            Y = self.Hidden2Output(Z, n_output, W)

            return (Z, Y)
        except:
            print('Terjadi kesalahan dalam fungsi perambatan maju', sys.exc_info()[0])

    def Output2Hidden(self, target_output, Y, Z, alpha, W):
        try:
            row, col = Y.shape
            tao = np.zeros((row, col))

            for i in range(row):
                for j in range(col):
                    tao[i, j] = (target_output[j] - Y[i, j]) * Y[i, j] * (1 - Y[i, j])

            row, col = tao.shape
            row1, col1 = Z.shape
            deltaW = np.zeros((col1 + 1, col))

            for i in range(col):
                for j in range(col1):
                    deltaW[j + 1, i] = round(alpha * tao[0, i] * Z[0, j], 4)

                deltaW[0, i] = round(alpha * tao[0, i], 4)

            W_baru = W + deltaW

            return W_baru
        except:
            print('Terjadi kesalahan dalam fungsi propagasi mundur dari layer output ke layer hidden',
                  sys.exc_info()[0])

    def Hidden2Input(self, target_output, Y, data, alpha, Z, W, V):
        try:
            row, col = Y.shape
            tao = np.zeros((row, col))

            for i in range(row):
                for j in range(col):
                    tao[i, j] = (target_output[j] - Y[i, j]) * Y[i, j] * (1 - Y[i, j])

            row1, col1 = W.shape
            row2, col2 = Z.shape
            taow = np.zeros((row2, col2))

            for i in range(col2):
                tmp = 0
                for j in range(col):
                    tmp = round(tmp + tao[0, j] * W[i + 1, j], 4)

                taow[0, i] = round(tmp * Z[0, i] * (1 - Z[0, i]), 4)

            row, col = taow.shape
            n_data = data.shape[0]
            m, n = V.shape
            deltaV = np.zeros((m, n))
            for j in range(col):
                tmp = 0
                for i in range(n_data):
                    deltaV[i + 1, j] = round(alpha * taow[0, j] * data[i], 4)

                deltaV[0, j] = round(alpha * taow[0, j], 4)

            V_baru = V + deltaV
            return V_baru

        except:
            print('Terjadi kesalahan dalam fungsi propagasi mundur dari layer hidden ke layer input', sys.exc_info()[0])

    def PerambatanMundur(self, target_output, Y, data, alpha, Z, W, V):
        try:
            W_baru = self.Output2Hidden(target_output, Y, Z, alpha, W)
            V_baru = self.Hidden2Input(target_output, Y, data, alpha, Z, W, V)

            return [W_baru, V_baru]
        except:
            print('Terjadi kesalahan dalam fungsi propagasi mundur', sys.exc_info()[0])