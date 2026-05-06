# I-TASK

# Shunday function tuzing, unga string argument pass bolsin.
# Function ushbu agrumentdagi
# digitlarni yangi stringda return qilsin

def get_digits(string):
    result = ""

    for char in string:
        if char.isdigit():
            result += char

    return result


print(get_digits("m14i1t"))


# G-TASK

# ❓ Shunday function tuzingki unga integerlardan iborat array pass bolsin
# va function bizga osha arrayning eng katta qiymatiga tegishli
# birinchi indexni qaytarsin.

# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.


# ✅ Masalaning yechimi:
# def sonlar(list):
#     eng_kata = 0

#     for s in range(0, len(list)):
#         if list[s] > list[eng_kata]:
#             eng_kata = s

#     return eng_kata


# print(sonlar([12, 6, 13, 34, 16]))

# ❓ Shunday funksiya yozingki, unga integerlardan iborat array
# berilsin va funksiya arraydagi
# eng kichik sonning birinchi indeksini qaytarsin.


# def eng_kichik(son):
#     kichik = 0

#     for x in range(0, len(son)):
#         if son[x] < son[kichik]:
#             kichik = x

#     return kichik


# print(eng_kichik([15, 9, 1, 12, 7]))


# ❓ Shunday funksiya yozingki, unga integerlardan iborat
# array berilsin va funksiya arraydagi barcha
# sonlarning yig'indisini qaytarsin.
# def sum_ofall(sonlar):
#     boshla = 0

#     for x in range(0, len(sonlar)):
#         boshla = boshla + sonlar[x]

#     return boshla


# print(sum_ofall([1, 5, 7, 9, 3]))
