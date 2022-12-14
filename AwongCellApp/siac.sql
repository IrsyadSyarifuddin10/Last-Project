CREATE DATABASE SIAC

CREATE TABLE stok(
kode_barang INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
tipe VARCHAR(30) NOT NULL,
merk VARCHAR(10) NOT NULL,
chipset VARCHAR(30) NOT NULL,
antutu_score VARCHAR(6) NOT NULL,
ram INT NOT NULL,
internal_storage INT NOT NULL,
harga INT NOT NULL,
stok INT NOT NULL
);


CREATE TABLE admin(
nama_admin VARCHAR(10) NOT NULL PRIMARY KEY,
passcode VARCHAR(8) NOT NULL
);

CREATE TABLE penjualan(
tanggal DATE NOT NULL,
kode_barang INT PRIMARY KEY,
jumlah INT NOT NULL,
total_harga INT,
FOREIGN KEY (kode_barang) REFERENCES stok(kode_barang)
);

CREATE TABLE (

);

SELECT * FROM stok;

INSERT INTO admin VALUE('sandman', 'adgjl135');

/*data samsung j2 prime ramnya jadi 1 dari 1.5*/
INSERT INTO stok (tipe, merk, chipset, antutu_score, ram, internal_storage, harga, stok) VALUES
('NOKIA C3', 'NOKIA', 'UNISOC SC9863A', '72796', '2', '16', 1599000, 2),
('OPPO A11K', 'OPPO', 'MEDIATEK HELIO P35', '99304', '2', '32', 1800000, 78),
('OPPO A15', 'OPPO', 'MEDIATEK HELIO P35', '99304', '3', '32', 1999000, 50),
('OPPO A15S', 'OPPO', 'MEDIATEK HELIO P35', '99304', '4', '64', 2299000, 50),
('OPPO A33', 'OPPO', 'SNAPDRAGON 460', '148976', '3', '32', 2299000, 2),
('OPPO A53', 'OPPO', 'SNAPDRAGON 460', '148976', '4', '64', 2499000, 2),
('OPPO RENO 3', 'OPPO', 'MEDIATEK HELIO P90', '211698', '8', '128', 5199000, 1),
('OPPO RENO 4', 'OPPO', 'SNAPDRAGON 720G', '211698', '8', '128', 4999000, 1),
('OPPO RENO 4F', 'OPPO', 'MEDIATEK HELIO P95', '211698', '8', '128', 4299000, 2),
('OPPO RENO 5', 'OPPO', 'SNAPDRAGON 720G', '281220', '8', '128', 5000000, 14),
('REALME 2', 'REALME', 'SNAPDRAGON 450', '88269', '4', '64', 2300000, 3),
('REALME 3', 'REALME', 'MEDIATEK HELIO P60', '171434', '3', '32', 1999000, 4),
('REALME 7', 'REALME', 'MEDIATEK HELIO G95', '301940', '8', '128', 3699000, 5),
('REALME 7 PRO', 'REALME', 'SNAPDRAGON 720G', '281220', '8', '128', 4599000, 8),
('REALME 7I', 'REALME', 'SNAPDRAGON 662', '177145', '8', '128', 3199000, 4),
('REALME C1', 'REALME', 'SNAPDRAGON 450', '88269', '2', '32', 1499000, 4),
('REALME C11', 'REALME', 'MEDIATEK HELIO G35', '110128', '2', '32', 1364000, 85),
('REALME C12', 'REALME', 'MEDIATEK HELIO G35', '110128', '3', '32', 1899000, 10),
('REALME C15 QE', 'REALME', 'MEDIATEK HELIO G35', '110128', '4', '64', 2199000, 40),
('REALME C17', 'REALME', 'SNAPDRAGON 460', '148976', '6', '256', 2799000, 3),
('SAMSUNG A01', 'SAMSUNG', 'SNAPDRAGON 439', '97952', '2', '16', 1249000, 22),
('SAMSUNG A01 CORE', 'SAMSUNG', 'MEDIATEK MT6739', '50015', '1', '16', 1099000, 82),
('SAMSUNG A01 CORE', 'SAMSUNG', 'MEDIATEK MT6739', '50015', '2', '32', 1299000, 12),
('SAMSUNG A02S', 'SAMSUNG', 'SNAPDRAGON 450', '88296', '4', '64', 1999000, 3),
('SAMSUNG A10', 'SAMSUNG', 'EXYNOS 7885', '109070', '2', '32', 1899000, 7),
('SAMSUNG A11', 'SAMSUNG', 'SNAPDRAGON 450', '88269', '3', '32', 1899000, 7),
('SAMSUNG A12', 'SAMSUNG', 'MEDIATEK HELIO P35', '99304', '4', '128', 2499000, 7),
('SAMSUNG A12', 'SAMSUNG', 'MEDIATEK HELIO P35', '99304', '6', '128', 2799000, 2),
('SAMSUNG A20', 'SAMSUNG', 'EXYNOS 7885', '109070', '3', '32', 2200000, 6),
('SAMSUNG A21S', 'SAMSUNG', 'EXYNOS 850', '125664', '3', '32', 2189000, 5),
('SAMSUNG A21S', 'SAMSUNG', 'EXYNOS 850', '125664', '6', '128', 3099000, 5),
('SAMSUNG A31', 'SAMSUNG', 'MEDIATEK HELIO P65', '187305', '6', '128', 3699000, 3),
('SAMSUNG A31', 'SAMSUNG', 'MEDIATEK HELIO P65', '187305', '8', '128', 3999000, 2),
('SAMSUNG A50', 'SAMSUNG', 'EXYNOS 9610', '176340', '4', '64', 3100000, 2),
('SAMSUNG A50', 'SAMSUNG', 'EXYNOS 9610', '176340', '6', '128', 3400000, 1),
('SAMSUNG A51', 'SAMSUNG', 'EXYNOS 9611', '178067', '6', '128', 4299000, 3),
('SAMSUNG A51', 'SAMSUNG', 'EXYNOS 9611', '178067', '8', '128', 4599000, 1),
('SAMSUNG A71', 'SAMSUNG', 'SNAPDRAGON 720G', '281220', '8', '128', 5999000, 3),
('SAMSUNG G532G J2 PRIME', 'SAMSUNG', 'MEDIATEK MT6737T', '41675', '1.5', '8', 1200000, 22),
('SAMSUNG J4 PLUS', 'SAMSUNG', 'SNAPDRAGON 425', '43584', '2', '32', 1775000, 3),
('SAMSUNG M20', 'SAMSUNG', 'EXYNOS 7904', '119180', '3', '32', 2500000, 7),
('VIVO V11', 'VIVO', 'MEDIATEK HELIO P60', '156869', '4', '64', 3499000, 3),
('VIVO V15', 'VIVO', 'MEDIATEK HELIO P70', '183710', '6', '64', 3499000, 5),
('VIVO V15 PRO', 'VIVO', 'SNAPDRAGON 675', '205931', '6', '128',4999000 , 2),
('VIVO V20', 'VIVO', 'SNAPDRAGON 720G', '281220', '8', '128', 4999000, 9),
('VIVO V20 SE', 'VIVO', 'SNAPDRAGON 665', '177530', '8', '128', 3999000, 14),
('VIVO Y1S', 'VIVO', 'MEDIATEK HELIO P35', '99304', '2', '32', 1699000, 5),
('VIVO Y12S', 'VIVO', 'MEDIATEK HELIO P35', '99304', '3', '32', 1899000, 53),
('VIVO Y20', 'VIVO', 'SNAPDRAGON 460', '148976', '3', '64', 2199000, 15),
('VIVO Y20S', 'VIVO', 'SNAPDRAGON 460', '148976', '8', '128', 3099000, 5),
('VIVO Y30', 'VIVO', 'MEDIATEK HELIO P35', '99304', '4', '128', 2699000, 11),
('VIVO Y30I', 'VIVO', 'MEDIATEK HELIO P35', '99304', '4', '64', 2499000, 31),
('VIVO Y51', 'VIVO', 'SNAPDRAGON 665', '177630', '8', '128', 3399000, 12),
('VIVO Y81', 'VIVO', 'MEDIATEK HELIO P22', '99333', '2', '16', 1799000, 4),
('VIVO Y91', 'VIVO', 'SNAPDRAGON 439', '97952', '2', '32', 1599000, 27),
('VIVO Y91C', 'VIVO', 'MEDIATEK HELIO P22', '99333', '2', '32', 1699000, 6),
('VIVO Y93', 'VIVO', 'SNAPDRAGON 439', '97952', '3', '32', 1699000, 9),
('VIVO Y95', 'VIVO', 'SNAPDRAGON 439', '97952', '4', '64', 2049000, 6),
('XIAOMI REDMI 9A', 'XIAOMI', 'MEDIATEK HELIO G25', '91014', '2', '32', 1199000, 3),
('XIAOMI REDMI 9A', 'XIAOMI', 'MEDIATEK HELIO G25', '91014', '3', '32', 1299000, 6),
('XIAOMI REDMI 9C', 'XIAOMI', 'MEDIATEK HELIO G35', '110128', '3', '32', 1399000, 17),
('XIAOMI REDMI 9C', 'XIAOMI', 'MEDIATEK HELIO G35', '110128', '4', '64', 1599000, 9),
('XIAOMI REDMI NOTE 9', 'XIAOMI', 'MEDIATEK HELIO G85', '197288', '6', '128', 2900000, 8),
('XIAOMI REDMI NOTE 9 PRO', 'XIAOMI', 'SNAPDRAGON 720G', '281220', '6', '64', 3500000, 15),
('XIAOMI REDMI NOTE 9 PRO', 'XIAOMI', 'SNAPDRAGON 720G', '281220', '8', '128', 3900000, 14);