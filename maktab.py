import sqlite3 as sq

con = sq.connect("baza.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    last_name TEXT, 
    first_name TEXT,
    age INTEGER,
    sinifi INTEGER,
    father_name TEXT,
    address TEXT,
    phone TEXT,
    birth_date TEXT,
    email TEXT,
    car TEXT,
    phone_model TEXT
)
""")

students = [
    (1,"Ahmed", "Aliyev", 16, 9,"Davron", "Oxunboboyev", "+998901234567", "2008-01-10", "ahmed12@gmail.com", "Nexia 3", "iPhone 11"),
    (2,"Asliddin", "Valiyev",16, 9,"Shavkat", "Sayapir", "+998902345678", "2008-02-11"," asliddin45@gmail.com", "Cobalt", "Samsung A12"),
    (3,"Toxtaboy", "Karimov",16, 9, "Azamat","Pastom","+998903456789","2008-03-12","toxtaboy77@gmail.com","Malibu","iPhone 12"),
    (4,"Jasur", "Qodirov", 16, 9,"Rustam","SHEX","+998904567890","2008-04-13","jasur33@gmail.com","Spark","Redmi Note 10"),
    (5,"Bunyod", "Toshmatov", 16, 9,"Sardor","Oxunboboyev","+998905678901","2008-05-14","bunyod88@gmail.com","Lacetti","iPhone 13"),
    (6,"Solih", "Umarov",16,9,"Umar","Sayapir","+998906789012","2008-06-15","solih91@gmail.com","Nexia 2","Samsung A20"),
    (7,"Anvar", "Nazarov",16,9,"Nazar","Pastom","+998907890123","2008-07-16","anvar56@gmail.com","Cobalt","iPhone X"),
    (8,"Komil", "Yuldoshev",16,9,"Yuldosh","SHEX","+998908901234","2008-08-17","komil24@gmail.com","Malibu","Samsung S10"),
    (9,"Otabek", "Mirzaev",16,9,"Mirza","Oxunboboyev","+998909012345","2008-09-18","otabek11@gmail.com","Spark","iPhone 11"),
    (10,"Diyor", "Ahmedov",16,9,"Ahmed","Sayapir","+998900123456","2008-10-19","diyor99@gmail.com","Cobalt","Samsung A10"),
    (11,"Islom", "Qurbanov",16,9,"Qurban","Pastom","+998901112233","2008-11-20","islom22@gmail.com","Nexia 3","iPhone 12"),
    (12,"Shohjahon","Ergashev",16,9,"Ergash","SHEX","+998902223344","2008-12-21","shohjahon66@gmail.com","Malibu","Samsung A32"),
    (13,"Azamat", "Rasulov",16,9,"Rasul","Oxunboboyev","+998903334455","2008-01-22","azamat77@gmail.com","Cobalt","iPhone 13"),
    (14,"Bekhruz", "Tursunov",16,9,"Tursun","Sayapir","+998904445566","2008-02-23","bekhruz44@gmail.com","Spark","Redmi 9"),
    (15,"Shoxrux", "Karimov",16,9,"Karim","Pastom","+998905556677","2008-03-24","shoxrux88@gmail.com","Lacetti","iPhone X"),
    (16,"Suhrob", "Toirov",16,9,"Toir","SHEX","+998906667788","2008-04-25","suhrob55@gmail.com","Cobalt","Samsung S21"),
    (17,"Javohir", "Saidov",16,9,"Said","Oxunboboyev","+998907778899","2008-05-26","javohir33@gmail.com","Nexia 2","iPhone 11"),
    (18,"Ulugbek", "Hamidov",16,9,"Hamid","Sayapir","+998908889900","2008-06-27","ulugbek12@gmail.com","Malibu","Samsung A12"),
    (19,"Murod", "Xolmatov",16,9,"Xolmat","Pastom","+998909990011","2008-07-28","murod45@gmail.com","Spark","iPhone 12"),
    (20,"Akmal","Abdullayev",16,9,"Abdulla","SHEX","+998900001122","2008-08-29","akmal78@gmail.com","Cobalt","Redmi Note 11"),
    (21,"Sirojiddin", "Yoqubov",16,9,"Yoqub","Oxunboboyev","+998901122334","2008-09-30","sirojiddin66@gmail.com","Nexia 3","iPhone 13"),
    (22,"Doniyor", "Raxmonov",16,9,"Raxmon","Sayapir","+998902233445","2008-10-01","doniyor44@gmail.com","Malibu","Samsung A10"),
    (23,"Farrux", "Aliyev",16,9,"Ali","Pastom","+998903344556","2008-11-02","farrux99@gmail.com","Cobalt","iPhone X"),
    (24,"Shoxruh", "Qayumov",16,9,"Qayum","SHEX","+998904455667","2008-12-03","shoxruh11@gmail.com","Spark","Samsung A12"),
    (25,"Maqsadbek","Xudoyberdiyev",16,9,"Xudoyberdi","Oxunboboyev","+998905566778","2008-01-04","maqsad77@gmail.com","Nexia 2","iPhone 11"),
    (26,"Bobur", "Shomurodov",16,9,"Shomurod","Sayapir","+998906677889","2008-02-05","bobur33@gmail.com","Cobalt","Samsung S10"),
    (27,"Sevara", "Khudashkurova",16,9,"Ermat","Pastom","+998907788990","2008-03-06","sevara55@gmail.com","Spark","iPhone 12"),
    (28,"Ali", "Murodov",16,9,"Murod","SHEX","+998908899001","2008-04-07","ali88@gmail.com","Malibu","Samsung A20"),
    (29,"Amirxon", "Yusupov",16,9,"Yusup","Oxunboboyev","+998909900112","2008-05-08","amirxon12@gmail.com","Cobalt","iPhone 13"),
    (30,"Asadbek", "Kadirov",16,9,"Kadir","Sayapir","+998900011223","2008-06-09","asadbek99@gmail.com","Nexia 3","Redmi Note 10"),
]

con.commit()
con.close()