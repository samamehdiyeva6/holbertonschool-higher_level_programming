#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at  # Funksiyanı idxal edirik

if __name__ == "__main__":  # Bura düzəldilmiş yazılışdır
    my_list = [1, 2, 3, 4, 5]  # Siyahı
    idx = 3  # Silinəcək elementin indexi
    new_list = delete_at(my_list, idx)  # delete_at funksiyasını çağırırıq

    # Nəticəni bir dəfə çap edirik
    print(new_list, end="")  # Yeni sətir əlavə etməmək üçün end="" istifadə edirik
    print(my_list, end="")   # Eyni şəkildə ikinci siyahını çap edirik