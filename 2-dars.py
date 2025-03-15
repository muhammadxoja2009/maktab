# 1-vazifa. MarsStudent nomli klas yaratilsin. Unda id, password, ism, familiya, yosh kabi parametrlari bo'lsin va koin nomli stantart qiymati bo'lsin.

#  2-vazifa. full_data nomli funksiyaga murojaat qilinganda talabaning idsi va passwordi so'ralsin, agar kiritilgan id va password obyektdagi id va passwordga teng bo'lsa uning ismi, familiyasi, yoshi va koinlari soni chiqarilsin

#  3-vazifa. get_coin nomli funksiyada talabaning koinlari soni chiqsin

#  4-vazifa. set_coin nomli funksiya orqali talabaga koin qo'shish yoki koin ayirish imkoniyati bo'lsin
# class MarsStudent
#       def init(self, id, password, ism, familiya, yosh, koin_nomli_stantart_qiymati coin=0):
#         self.id = id
#         self.password = password
#         self.ism = ism 
#         self.familiya = familiya
#         self.yosh = yosh
#         self.koin_nomli_stantart_qiymati = koin_nomli_stantart_qiymati
    
#     def full_data(self):
#         user_id = input("ID kiriting: ")
#         user_password = input("Password kiriting: ")
#         if self.id == user_id and self.password == user_password :
# print(f"Ismi: {self.ism}")
# print(f"Familiyasi: {self.familiya}")
# print(f"Yoshi: {self.yosh}")
# print(f"Koinlari soni: {self.koin_nomli_stantart_q
                        
# class MarsStudent:
#     def __init__(self, id, password, ism, familiya, yosh, koin=0):
#         self.id = id  # Talabaning IDsi
#         self.password = password  # Talabaning paroli
#         self.ism = ism  # Talabaning ismi
#         self.familiya = familiya  # Talabaning familiyasi
#         self.yosh = yosh  # Talabaning yoshi
#         self.koin = koin  # Talabaning koini, standart qiymat 0

#     def full_data(self, input_id, input_password):
#         """Talaba ma'lumotlarini chiqarish"""
#         if self.id == input_id and self.password == input_password:
#             return f"Ism: {self.ism}\nFamiliya: {self.familiya}\nYosh: {self.yosh}\nKoin: {self.koin}"
#         else:
#             return "ID yoki parol noto'g'ri"

#     def get_coin(self):
#         """Talabaning koini sonini olish"""
#         return self.koin

#     def set_coin(self, amount):
#         """Talabaning koinini qo'shish yoki ayirish"""
#         self.koin += amount
#         return self.koin

student1 = MarsStudent(id="12345", password="mypassword", ism="Ali", familiya="Valiyev", yosh=20)
print(student1.full_data("12345", "mypassword"))
print(f"Talabaning koini: {student1.get_coin()}")
student1.set_coin(10) 
print(f"Yangilangan koin: {student1.get_coin()}")
student1.set_coin(-5)  h
print(f"Yangilangan koin: {student1.get_coin()}")
