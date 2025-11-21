# Nama File : set.py
# Pembuat   : Syafira Azka Ramadhani
# Tanggal   : 5 November 2024
# Deskripsi : Membuat type dan operasi set yang menggunakan list

from list_operators import *

# DEFINISI DAN SPESIFIKASI TYPE
# Set adalah sebuah list dengan syarat bahwa elemen harus unik
# Semua konstruktor, selektor, dan operasi yang telah didefinisikan
#   untuk list juga berlaku pada set

# DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK SET
# Rember_V1: elemen, list -> list
# Rember_V1(X, L) menghapus sebuah elemen X yang ditemui pertama kali pada list L
#   Jika X ada di dalam list L, maka elemen L berkurang satu
#   Jika X tidak ada di dalam list L maka L tetap
#   List kosong tetap menjadi list kosong
# REALISASI
def Rember_V1(X, L):
    if IsEmpty(L): # Basis
        return []
    else: # Rekurens
        if FirstElmt(L) == X:
            return Tail(L)
        else:
            return Konso(FirstElmt(L), Rember_V1(X, Tail(L)))
# APLIKASI
print(Rember_V1(1, [1, 2, 3, 4, 1]))
print(Rember_V1(2, [1]))
print(Rember_V1(3, []))
print(Rember_V1(1, [1, 2, 3, 4, 3, 2, 1]))

# Rember2: elemen, list --> list
# Rember2(x, L) menghapus sebuah elemen x yang ditemui terakhir kali pada list L
#   List yang baru berkurang SATU elemennya yaitu yang bernilai x
#   List kosong tetap menjadi list kosong
# REALISASI
def Rember2(x, L):
    if IsEmpty(L):
        return []
    else:
        if LastElmt(L) == x:
            return Head(L)
        else:
            return Konsi(Rember2(x, Head(L)), LastElmt(L))
# MultiRember: elemen, list --> list
# MultiRember(x, L) menghapus semua kemunculan elemen x pada list L
#   List baru yang dihasilkan tidak lagi memiliki elemen x
#   List kosong tetap menjadi list kosong
# REALISASI
def MultiRember(x, L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return MultiRember(x, Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(x, Tail(L)))
#====================================================================================================================================================================
# APLIKASI
print(Rember_V1(1, [1, 2, 3, 4, 5, 1]))               # --> [2, 3, 4, 5, 1]
print(Rember2(1, [1, 2, 3, 4, 5, 1]))               # --> [1, 2, 3, 4, 5]
print(MultiRember(1, [1, 2, 3, 4, 5, 1]))           # --> [2, 3, 4, 5]
#====================================================================================================================================================================




#====================================================================================================================================================================
# TYPE SET (HIMPUNAN)
#====================================================================================================================================================================
# DEFINISI DAN SPESIFIKASI TYPE
# Set adalah list dengan tambahan syarat bahwa tidak ada elemen yang sama
#   Semua konstruktor, selektor, dan fungsi pada list berlaku untuk set
#====================================================================================================================================================================
# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeSet1: list --> set
# MakeSet1(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali dengan memanfaatkan fungsi IsMember(x, L) pada list
#   untuk mengecek duplikasi elemen, list kosong tetap menjadi set kosong
# REALISASI
def MakeSet1(L):
    if IsEmpty(L):
        return []
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSet1(Tail(L))
        else:
            return Konso(FirstElmt(L), MakeSet1(Tail(L)))
# MakeSet2 : list --> set
# MakeSet2(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali dengan memanfaatkan fungsi MultiRember(x, L) pada list
#   untuk menghapus duplikasi elemen, list kosong tetap menjadi set kosong
# REALISASI
def MakeSet2(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), MultiRember(FirstElmt(L), MakeSet2(Tail(L))))
#====================================================================================================================================================================
# DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
# MaxElmt: set tidak kosong --> elemen
# MaxElmt(H) mengembalikan elemen maksimum dari set H
# REALISASI
def MaxElmt(H):
    if IsOneElmt(H):
        return FirstElmt(H)
    else:
        if FirstElmt(H) > LastElmt(H):
            return MaxElmt(Head(H))
        else:
            return MaxElmt(Tail(H))
# MaxH: set --> set
# MaxH(H) mengurutkan set H dari elemen maksimum menuju minimum
# REALISASI
def MaxH(H):
    if IsEmpty(H):
        return []
    else:
        return Konso(MaxElmt(H), MaxH(Rember_V1(MaxElmt(H), H)))
#====================================================================================================================================================================
# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSet: list --> boolean
# IsSet(L) benar jika L adalah sebuah set
# REALISASI
def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        return not IsMember(FirstElmt(L), Tail(L)) and IsSet(Tail(L))
# IsSubset: 2 set --> boolean
# IsSubset(H1, H2) benar jika H1 merupakan subset dari H2
# REALISASI
def IsSubset(H1, H2):
    if IsEmpty(H1):
        return True
    else:
        if not IsMember(FirstElmt(H1), H2):
            return False
        else:
            return IsSubset(Tail(H1), H2)
# IsEqualSet1: 2 set --> boolean
# IsEqualSet1(H1, H2) benar jika H1 adalah set yang sama dengan H2 dengan memanfaatkan fungsi IsSubset(H1, H2)
#   fungsi tidak memperhatikan urutan
# REALISASI
def IsEqualSet1(H1, H2):
    return IsSubset(H1, H2) and IsSubset(H2, H1)
# IsEqualSet2: 2 set --> boolean
# IsEqualSet2(H1, H2) benar jika H1 adalah set yang sama dengan H2 dengan mengecek satu-persatu elemen pada H1 dan H2
#   fungsi tidak memperhatikan urutan
# REALISASI
def IsEqualSet2(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return True
    elif IsEmpty(H1) and not IsEmpty(H2):
        return False
    elif not IsEmpty(H1) and IsEmpty(H2):
        return False
    elif not IsEmpty(H1) and not IsEmpty(H2):
        if FirstElmt(MaxH(H1)) == FirstElmt(MaxH(H2)):
            return IsEqualSet2(Tail(MaxH(H1)), Tail(MaxH(H2)))
        else:
            return False
# IsIntersect: 2 set --> set
# IsIntersect(H1, H2) benar jika H1 beririsan dengan H2
# REALISASI
def IsIntersect(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return False
    elif IsEmpty(H1) and not IsEmpty(H2):
        return False
    elif not IsEmpty(H1) and IsEmpty(H2):
        return False
    elif not IsEmpty(H1) and not IsEmpty(H2):
        return IsMember(FirstElmt(H1), H2) or IsIntersect(Tail(H1), H2)
#====================================================================================================================================================================
# DEFINISI DAN SPESIFIKASI OPERATOR
# KonsoSet: elemen, set --> set
# KonsoSet(e, H) menambahkan sebuah elemen e sebagai elemen pertama set H dengan syarat e belum ada di dalam set H
# REALISASI
def KonsoSet(e,H):
    if IsMember(e, H):
        return H
    else:
        return Konso(e, H)
# MakeIntersect1: 2 set --> set
# MakeIntersect1(H1, H2) menghasilkan set baru yang merupakan hasil irisan antara H1 dan H2 menggunakan rekursif terhadap H1
# REALISASI
def MakeIntersect1(H1,H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif IsEmpty(H1) and not IsEmpty(H2):
        return []
    elif not IsEmpty(H1) and IsEmpty(H2):
        return []
    elif not IsEmpty(H1) and not IsEmpty(H2):
        if IsMember(FirstElmt(H1), H2):
            return Konso(FirstElmt(H1), MakeIntersect1(Tail(H1), H2))
        else:
            return MakeIntersect1(Tail(H1), H2)
# MakeIntersect2
# MakeIntersect2(H1, H2) menghasilkan set baru yang merupakan hasil irisan antara H1 dan H2 menggunakan rekursif terhadap H2
# REALISASI
def MakeIntersect2(H1,H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif IsEmpty(H1) and not IsEmpty(H2):
        return []
    elif not IsEmpty(H1) and IsEmpty(H2):
        return []
    elif not IsEmpty(H1) and not IsEmpty(H2):
        if IsMember(FirstElmt(H2), H1):
            return Konso(FirstElmt(H2), MakeIntersect2(H1, Tail(H2)))
        else:
            return MakeIntersect2(H1, MakeIntersect2(H1, Tail(H2)))
# MakeUnion1: 2 set --> set
# MakeUnion1(H1,H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2 menggunakan rekursif terhadap H1
# REALISASI
def MakeUnion1(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif IsEmpty(H1) and not IsEmpty(H2):
        return H2
    elif not IsEmpty(H1) and IsEmpty(H2):
        return H1
    elif not IsEmpty(H1) and not IsEmpty(H2):
        if IsMember(FirstElmt(H1), H2):
            return MakeUnion1(Tail(H1), H2)
        else:
            return Konso(FirstElmt(H1), MakeUnion1(Tail(H1), H2))
# MakeUnion2: 2 set --> set
# MakeUnion2(H1,H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2 menggunakan rekursif terhadap H2
# REALISASI
def MakeUnion2(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif IsEmpty(H1) and not IsEmpty(H2):
        return H2
    elif not IsEmpty(H1) and IsEmpty(H2):
        return H1
    elif not IsEmpty(H1) and not IsEmpty(H2):
        if IsMember(LastElmt(H2), H1):
            return MakeUnion2(H1, Head(H2))
        else:
            return Konsi(MakeUnion2(H1, Head(H2)), LastElmt(H2))
# NBIntersect: 2 set --> integer
# NBIntersect(H1, H2) menghitung jumlah elemen yang beririsan pada H1 dan H2 tanpa memanfaatkan fungsi MakeIntersect(H1, H2)
# REALISASI
def NBIntersect(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return 0
    elif IsEmpty(H1) and not IsEmpty(H2):
        return 0
    elif not IsEmpty(H1) and IsEmpty(H2):
        return 0
    elif not IsEmpty(H1) and not IsEmpty(H2):
        if IsMember(FirstElmt(H1), H2):
            return 1 + NBIntersect(Tail(H1), H2)
        else:
            return NBIntersect(Tail(H1), H2)       
# NBUnion: 2 set --> integer
# NBUnion(H1,H2) menghitung jumlah elemen hasil gabungan antara H1 dan H2 tanpa memanfaatkan fungsi MakeUnion(H1, H2)
# REALISASI
def NBUnion(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return 0
    elif IsEmpty(H1) and not IsEmpty(H2):
        return NbElmt(H2)
    elif not IsEmpty(H1) and IsEmpty(H2):
        return NbElmt(H1)
    elif not IsEmpty(H1) and not IsEmpty(H2):
        if IsMember(FirstElmt(H1), H2):
            return NBUnion(Tail(H1), H2)
        else:
            return 1 + NBUnion(Tail(H1), H2)
#====================================================================================================================================================================
# # APLIKASI
# print(MakeSet1([3, 5, 1, 4, 3, 3, 2, 1, 1]))          # --> [5, 4, 3, 2, 1]
# print(MakeSet2([3, 5, 1, 4, 3, 3, 2, 1, 1]))          # --> [3, 5, 1, 4, 2]
# print(KonsoSet(4, [2, 3, 4, 5]))                      # --> [2, 3, 4, 5]
# print(KonsoSet(1, [2, 3, 4, 5]))                      # --> [1, 2, 3, 4, 5]
# print(IsSet([]))                                      # --> True
# print(IsSet([1, 2, 3, 4, 5]))                         # --> True
# print(IsSet([1, 2, 3, 2, 1]))                         # --> False
# print(IsSubset([1, 2], [3, 2, 1]))                    # --> True
# print(IsSubset([1, 2, 3], [3, 2, 1]))                 # --> True
# print(IsSubset([1, 2, 3, 4], [3, 2, 1]))              # --> False
# print(IsEqualSet1([1, 2, 3], [1, 2, 3]))              # --> True
# print(IsEqualSet1([1, 2, 3], [1, 2, 3, 4]))           # --> False
# print(IsEqualSet1([1, 2, 3], [3, 2, 1]))              # --> True
# print(IsEqualSet2([1, 2, 3], [1, 2, 3]))              # --> True
# print(IsEqualSet2([1, 2, 3], [1, 2, 3, 4]))           # --> False
# print(IsEqualSet2([1, 2, 3], [3, 2]))                 # --> False
# print(IsIntersect([], []))                            # --> False
# print(IsIntersect([1, 2], [3, 4, 5]))                 # --> False
# print(IsIntersect([1, 2, 3, 4], [3, 4, 5]))           # --> True
# print(MakeIntersect1([1, 2, 3, 4], [5, 4, 3]))        # --> [3, 4]
# print(MakeIntersect2([1, 2, 3, 4], [5, 4, 3]))        # --> [4, 3]
# print(MakeUnion1([1, 2, 3, 4], [5, 4, 3]))            # --> [1, 2, 5, 4, 3]
# print(MakeUnion2([1, 2, 3, 4], [5, 4, 3]))            # --> [1, 2, 3, 4, 5]
# print(NBIntersect([1, 4], [3, 2, 1]))                 # --> 1
# print(NBUnion([1, 2, 3, 4, 5], [5, 6, 7]))            # --> 7
#====================================================================================================================================================================
def RemberV2(x, L):
    if IsEmpty(L):
        return []
    else:
        if LastElmt(L) == x:
            return Head(L)
        else:
            return Konso(LastElmt(L), RemberV2(x, Head(L)))
        
print(RemberV2(1, [1,2, 3, 1, 2]))