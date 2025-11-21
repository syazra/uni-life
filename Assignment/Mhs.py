# ====================================================================================================================
# TYPE MAHASISWA
# ====================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# ==============================
# type Mhs: <NIM: string, Nama: string, Kelas: character, Nilai: list of integer>
# type Mhs terdiri atas NIM, nama, dan kelas mahasiswa, serta kumpulan nilai kuis yang pernah dikerjakan,
#   dengan maksimal jumlah mengerjakan adalah 10 kali nilai mahasiswa memiliki rentang antara 0-100

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# =====================================
# MakeMhs: <string, string, character, list of integer> -> Mhs
# MakeMhs(NIM, Nama, Kelas, Nilai) membentuk sebuah mahasiswa dengan nim, nama, kelas, dan nilai berbentuk list of integer
#   Contoh:
#   MakeMhs('234', 'Andi', 'C', []) membentuk mahasiswa dengan nim '234', nama 'Andi' dari kelas C,
#       dan belum pernah mengerjakan kuis (nilainya berupa list kosong)
#   MakeMhs('123', 'Caca', 'C', [90, 80, 100]) membentuk mahasiswa dengan nim '123', nama 'Caca' dari kelas C,
#       dan telah mengerjakan kuis sebanyak tiga kali dengan masing-masing nilai adalah 90, 80, dan 100
# REALISASI
def MakeMhs(NIM, Nama, Kelas, Nilai):
    return [NIM, Nama, Kelas, Nilai]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# ==================================
# GetNIM: Mhs -> string
# GetNIM(M) mengembalikan NIM dari mahasiswa M
# REALISASI
def GetNIM(M):
    return M[0]

# GetNama: Mhs -> string
# GetNama(M) mengembalikan nama dari mahasiswa M
# REALISASI
def GetNama(M):
    return M[1]

# GetKelas: Mhs -> character
# GetKelas(M) mengembalikan kelas dari mahasiswa M
# REALISASI
def GetKelas(M):
    return M[2]

# GetNilai: Mhs -> list of integer
# GetNilai(M) mengembalikan daftar nilai kuis dari mahasiswa M
# REALISASI
def GetNilai(M):
    return M[3]

# ====================================================================================================================
# TYPE LIST
# ====================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# ==============================
# Konstruktor menambahkan elemen di awal, notasi prefix
# type list: [] atau [e o list]
# Konstruktor menambahkan elemen di akhir, notasi prefix
# type list: [] atau [list o e]

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# =====================================
# Konso: elemen, list -> list
# Konso(e, L) menambahkan elemen di baris awal list
# REALISASI
def Konso(e, L):
    return [e] + L

# Konsi: list, elemen -> list
# Konsi(L, e) menambahkan elemen di baris akhir list
# REALISASI
def Konsi(L, e):
    return L + [e]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# ==================================
# FirstElmt: list tidak kosong -> elemen
# FirstElmt(L) mengembalikan elemen pertama list L
# REALISASI
def FirstElmt(L):
    return L[0]

# Tail: list -> list
# Tail(L) mengembalikan list tanpa elemen pertama list L, mungkin kosong
# REALISASI
def Tail(L):
    return L[1:] 

# LastElmt: list tidak kososng -> elemen
# LastElmt(L) mengembalikan elemen terakhir pada list L
# REALISASI
def LastElmt(L):
    return L[-1]

# Head: list -> list
# Head(L) mengembalikan list tanpa elemen terakhir list L, mungkin kosong
# REALISASI
def Head(L):
    return L[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# ==================================
# IsEmpty: list -> boolean
# IsEmpty(L) benar jika list kosong
# REALISASI
def IsEmpty(L):
    return L == []

# IsMember: elemen, list -> boolean
# IsMember(x, L) benar jika x adalah elemen list L
# REALISASI
def IsMember(x, L):
    if IsEmpty(L):
        return False
    else:
        return IsMember(x, Tail(L)) or FirstElmt(L) == x

# DEFINISI DAN SPESIFIKASI OPERATOR
# ==================================
# NbElmt: list -> integer
# NbElmt(L) menghitung jumlah elemen dari list, nol jika kosong
# REALISASI
def NbElmt(L):
    if L == []:
        return 0
    else: 
        return 1 + NbElmt(Tail(L))

# ====================================================================================================================
# NILAI RATA KUIS MAHASISWA
# ====================================================================================================================

# DEFINISI DAN SPESIFIKASI
# =========================
# NilaiTotal: Mhs -> integer
# NilaiTotal(M) menghitung nilai total dari kuis yang dikerjakan
# REALISASI
def NilaiTotal(M):
    if IsEmpty(M):
        return 0
    else:
        return FirstElmt(M) + NilaiTotal(Tail(M))

# NilaiRata: Mhs -> real
# NilaiRata(M) menghitung nilai rata-rata dari kuis yang dikerjakan
# REALISASI
def NilaiRata(M):
    if NilaiTotal(GetNilai(M)) == 0:
        return 0.0
    else:
        return NilaiTotal(GetNilai(M)) / NbElmt(GetNilai(M))

# APLIKASI
print(NilaiRata(MakeMhs('121', 'Raka', 'F', [])))
print(NilaiRata(MakeMhs('122', 'Ana', 'A', [92, 97])))
print(NilaiRata(MakeMhs('123', 'Rose', 'B', [95, 64, 77])))
# ====================================================================================================================

# ====================================================================================================================
# TYPE SET OF MAHASISWA (HIMPUNAN MAHASISWA)
# ====================================================================================================================

# DEFINISI DAN SPESIFIKASI PREDIKAT UNTUK MEMBUAT KONSTRUKTOR
# ============================================================
# IsMhs: Mhs, list of Mhs -> boolean
# IsMhs(M1, M2) benar jika nim mahasiswa M1 terdapat di dalam list mahasiswa M2
# REALISASI
def IsMhs(M1, M2):
    if IsEmpty(M2):
        return False
    else:
        return IsMhs(M1, Tail(M2)) or GetNIM(M1) == GetNIM(FirstElmt(M2))

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# =====================================
# MakeSetMhs: list of Mhs -> set of Mhs
# MakeSetMhs(M) membuat sebuah set mahasiswa, yaitu membuang semua mahasiswa yang memiliki nim sama
#   sehingga tidak ada duplikasi
# REALISASI
def MakeSetMhs(M):
    if IsEmpty(M):
        return []
    elif IsMhs(FirstElmt(M), Tail(M)):
        return MakeSetMhs(Tail(M))
    else:
        return Konso(FirstElmt(M), MakeSetMhs(Tail(M)))

# APLIKASI
print(MakeSetMhs([
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),  
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),  
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
# ====================================================================================================================

# ====================================================================================================================
# MAHASISWA LULUS
# ====================================================================================================================

# DEFINISI DAN SPESIFIKASI
# =========================
# MhsLulus: set of Mhs -> set
# MhsLulus(M) mengembalikan himpunan mahasiswa yang lulus, yaitu mahasiswa yang memiliki nilai rata-rata
#   lebih dari sama dengan 70
# REALISASI
def MhsLulus(M):
    if IsEmpty(M):
        return []
    elif NilaiRata(FirstElmt(M)) >= 70:
        return Konso(GetNama(FirstElmt(M)), MhsLulus(Tail(M)))
    else:
        return MhsLulus(Tail(M))

# APLIKASI
print(MhsLulus([
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
# ====================================================================================================================

# ====================================================================================================================
# MAHASISWA TIDAK KUIS DI KELAS 'K'
# ====================================================================================================================
# DEFINISI DAN SPESIFIKASI
# MhsTidakKuisKelas: character, set of Mhs -> set
# MhsTidakKuisKelas(K, M) mengembalikan himpunan mahasiswa yang tidak mengerjakan kuis sama sekali di kelas K
# REALISASI
def MhsTidakKuisKelas(K, M):
    if IsEmpty(M):
        return []
    elif K == GetKelas(FirstElmt(M)):
        if IsEmpty(GetNilai(FirstElmt(M))):
            return Konso(GetNama(FirstElmt(M)), MhsTidakKuisKelas(K, Tail(M)))
        else:
            return MhsTidakKuisKelas(K, Tail(M))
    else:
        return MhsTidakKuisKelas(K, Tail(M))  

# APLIKASI
print(MhsTidakKuisKelas('A', [
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
print(MhsTidakKuisKelas('B', [
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
print(MhsTidakKuisKelas('C', [
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
print(MhsTidakKuisKelas('D', [
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
print(MhsTidakKuisKelas('E', [
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
print(MhsTidakKuisKelas('F', [
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
# ====================================================================================================================

# ====================================================================================================================
# NILAI TERTINGGI MAHASISWA
# ====================================================================================================================

# DEFINISI DAN SPESIFIKASI
# =========================
# Max2: real, real --> real
# Max2(a, b) adalah fungsi antara yang mengembalikan nilai maksimum antara a dan b
# REALISASI
def Max2(a, b):
    if a >= b:
        return a
    else:
        return b

# NilaiTertinggiMhs: set of Mhs -> real
# NilaiTertinggiMhs(M) mengembalikan nilai rata-rata tertinggi dari semua kelas
# REALISASI
def NilaiTertinggiMhs(M):
    if IsEmpty(M):
        return 0
    else:
        return Max2(NilaiRata(FirstElmt(M)), NilaiTertinggiMhs(Tail(M)))

# APLIKASI
print(NilaiTertinggiMhs([
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
# ====================================================================================================================

# ====================================================================================================================
# MAHASISWA NILAI TERTINGGI DI KELAS 'K'
# ====================================================================================================================

# DEFINISI DAN SPESIFIKASI
# =========================
# MhsKelas: character, set of Mhs -> set of Mhs
# MhsKelas(K, M) mengembalikan himpunan mahasiswa yang merupakan mahasiswa kelas K
# REALISASI
def MhsKelas(K, M):
    if IsEmpty(M):
        return []
    elif K == GetKelas(FirstElmt(M)):
        return Konso(FirstElmt(M), MhsKelas(K, Tail(M)))
    else:
        return MhsKelas(K, Tail(M))

# MhsKuisKelas: character, set of Mhs -> set of Mhs 
# MhsKuisKelas(K, M) mengembalikan himpunan mahasiswa yang mengerjakan kuis dan membuang mahasiswa
#   yang tidak mengerjakan kuis di kelas K
# REALISASI
def MhsKuisKelas(K, M):
    if IsEmpty(MhsKelas(K, M)):
        return []
    elif IsMember(GetNama(FirstElmt(MhsKelas(K, M))), MhsTidakKuisKelas(K, M)):
        return MhsKuisKelas(K, Tail(MhsKelas(K, M)))
    else:
        return Konso(FirstElmt(MhsKelas(K, M)), MhsKuisKelas(K, Tail(MhsKelas(K, M))))

# MhsNilaiTertinggi: real, set of Mhs -> set
# MhsNilaiTertinggi(N, M) mengembalikan himpunan mahasiswa yang memiliki nilai rata-rata N
# REALISASI
def MhsNilaiTertinggi(N, M):
    if IsEmpty(M):
        return []
    elif N == NilaiRata(FirstElmt(M)):
        return Konso(GetNama(FirstElmt(M)), MhsNilaiTertinggi(N, Tail(M)))
    else:
        return MhsNilaiTertinggi(N, Tail(M))

# MhsNilaiTertinggiKelas: character, set of Mhs -> set
# MhsNilaiTertinggiKelas(K, M) mengembalikan himpunan mahasiswa yang mendapatkan nilai tertinggi di kelas K
# REALISASI
def MhsNilaiTertinggiKelas(K, M):
    return MhsNilaiTertinggi(NilaiTertinggiMhs(MhsKelas(K, M)), MhsKuisKelas(K, M))       

# APLIKASI
print(MhsNilaiTertinggiKelas('A', [
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
print(MhsNilaiTertinggiKelas('B', [
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
print(MhsNilaiTertinggiKelas('C', [
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
print(MhsNilaiTertinggiKelas('D', [
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
print(MhsNilaiTertinggiKelas('E', [
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
print(MhsNilaiTertinggiKelas('F', [
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
# ====================================================================================================================

# ====================================================================================================================
# BANYAK MAHASISWA TIDAK KUIS
# ====================================================================================================================

# DEFINISI DAN SPESIFIKASI
# =========================
# JumlahMhsTidakKuis: set of Mhs -> integer
# JumlahMhsTidakKuis(M) menghitung banyaknya mahasiswa yang tidak mengerjakan kuis dari semua kelas
# REALISASI
def JumlahMhsTidakKuis(M):
    if IsEmpty(M):
        return 0
    elif IsEmpty(GetNilai(FirstElmt(M))):
        return 1 + JumlahMhsTidakKuis(Tail(M))
    else:
        return JumlahMhsTidakKuis(Tail(M))   

# APLIKASI
print(JumlahMhsTidakKuis([
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
# ====================================================================================================================

# ====================================================================================================================
# BANYAK MAHASISWA LULUS
# ====================================================================================================================

# DEFINISI DAN SPESIFIKASI
# =========================
# JumlahMhsLulus: set of Mhs -> integer
# JumlahMhsLulus(M) menghitung banyaknya mahasiswa yang lulus dari semua kelas
# REALISASI
def JumlahMhsLulus(M):
    return NbElmt(MhsLulus(M))

# APLIKASI
print(JumlahMhsLulus([
    MakeMhs('111', 'Dino', 'C', []),
    MakeMhs('112', 'Nuca', 'A', [88, 84, 65]),
    MakeMhs('113', 'Yusuf', 'D', []),
    MakeMhs('114', 'Ninis', 'D', [93]),
    MakeMhs('115', 'Didit', 'E', [0]),
    MakeMhs('116', 'Tora', 'D', [66, 86]),
    MakeMhs('117', 'Seva', 'B', []),
    MakeMhs('118', 'Zaki', 'C', [98]),
    MakeMhs('119', 'Bona', 'D', [88, 87, 78, 64, 72, 91, 85, 73, 92, 77]),
    MakeMhs('120', 'Faras', 'B', [32, 49, 88, 67]),
    MakeMhs('121', 'Raka', 'F', []),
    MakeMhs('122', 'Ana', 'A', [92, 97]),
    MakeMhs('123', 'Rose', 'B', [95, 64, 77]),
    MakeMhs('124', 'Ciki', 'E', [61, 90]),
    MakeMhs('125', 'Ani', 'E', [0, 0, 91]),
    MakeMhs('126', 'Raju', 'D', [100, 90, 99]),
    MakeMhs('127', 'Qory', 'D', [100, 92, 96, 99, 100]),
    MakeMhs('128', 'Angel', 'F', []),
    MakeMhs('129', 'Teguh', 'D', [51, 74, 65, 89, 90]),
    MakeMhs('130', 'Tina', 'A', [93, 95, 75]),
    MakeMhs('131', 'Zara', 'C', [76, 81, 92, 98]),
    MakeMhs('132', 'Lala', 'E', [45, 67, 70, 91, 95]),
    MakeMhs('133', 'Denis', 'A', [88, 79, 62, 91, 85]),
    MakeMhs('134', 'Joko', 'D', [93, 93]),
    MakeMhs('135', 'Dina', 'E', []),
    MakeMhs('136', 'Tasya', 'E', [92, 100]),
    MakeMhs('137', 'Kiki', 'C', [0, 0, 0]),
    MakeMhs('138', 'Putri', 'D', [90, 100, 100]),
    MakeMhs('139', 'Rafi', 'A', [100, 96, 84, 62]),
    MakeMhs('140', 'Iqbal', 'E', []),
    MakeMhs('141', 'Fauzan', 'B', [44, 97, 67, 78]),
    MakeMhs('142', 'Tata', 'D', [96, 75, 92]),
    MakeMhs('143', 'Oki', 'C', [100, 79, 65, 98]),
    MakeMhs('144', 'Aldi', 'E', [46, 57, 79, 83, 77]),
    MakeMhs('145', 'Ais', 'B', [92, 92, 88, 100]),
    MakeMhs('146', 'Ila', 'C', [93, 92, 95, 90]),
    MakeMhs('147', 'Yoga', 'D', [70, 71, 69, 88, 93]),
    MakeMhs('148', 'Juan', 'F', []),
    MakeMhs('149', 'Doni', 'E', [100, 98, 98]),
    MakeMhs('150', 'Niki', 'B', [80]),
    MakeMhs('151', 'Alya', 'E', []),
    MakeMhs('152', 'Fatih', 'E', [71, 88, 76, 63, 57, 84, 92, 81, 66, 75]),
    MakeMhs('153', 'Cici', 'E', [94]),   
    MakeMhs('154', 'Rara', 'A', [89, 77, 92]),   
    MakeMhs('155', 'Putih', 'C', [75, 65]),  
    MakeMhs('156', 'Dian', 'B', [78, 100, 100, 94]),  
    MakeMhs('157', 'Jesi', 'D', [66, 95]),  
    MakeMhs('158', 'Bening', 'E', [68, 76, 79]),
    MakeMhs('159', 'Nofa', 'D', [90, 79, 88, 92, 64, 93]),
    MakeMhs('160', 'Linda', 'E', [99, 100, 97])
]))
# ====================================================================================================================