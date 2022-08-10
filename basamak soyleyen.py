sayilar = [["birler"],
				["onlar"],
				["yüzler"],
				["binler"],
				["onbinler"],
				["yuzbinler"],
				["milyonlar"],
				["onmilyonlar"],
				["yuzmilyonlar"],
				["milyarlar"],
				["onmilyarlar"],
				["yuzmilyarlar"],
				["trilyonlar"],
				["ontrilyonlar"],
				["yuztrilyonlar"],
				["katrilyonlar"],
				["onkatrilyonlar"],
				["yuzkatrilyonlar"],
				["kentilyonlar"],
				["onkentilyonlar"],
				["yuzkentilyonlar"]]
aralik = int(1)
basamak = input("Sayi kac basamakli(öğrenmek icin kucuk harflerle 'basamak' yazin)")

if basamak == "basamak":
	sayi = input("sayiyi yaz")
	print("sayiniz {} basamakli".format(len(str(sayi))))
	basamak = int(sayi)
if int(basamak) > 21:
	print("ben yuz kentilyonlara kadar yazdim gerisine usendim")
	quit()
while int(basamak) != aralik-1:
	if int(basamak) == aralik:
		print("sayinizin basamagi {}".format(*sayilar[int(aralik)-1]))
		input("cikmak icin herhangi birsey yaz")
		quit()
	else:
		aralik += 1