def apakahBilanganPrima(nilai):
    if nilai > 1:
        for i in range(2,nilai):
            if (nilai % i) == 0:
                return False
        else:
            return True
    else:
        return False

def palindrome(nilai):
    nilai = str(nilai)
    if nilai == nilai[::-1]:
        return True
    else:
        return False