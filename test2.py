import os
def print_menu():
	print ("-----------------------MENU MAKANAN INDONESIA---------------------")
	print ("MAKANAN")
	print ("1.SOTO")
	print ("2.SATE")
	print ("3.KETOPRAK")
	print ("MINUMAN")
	print ("4.ES TEH")
	print ("5.ES JERUK")
	print ("6.LEMON TEA")
	print ("------------------------MENU MAKANAN JEPANG-----------------------")
	print ("MAKANAN")
	print ("7.SUSHI")
	print ("8.SASHIMI")
	print ("9.RAMEN")
	print ("MINUMAN")
	print ("10.OCHA")
	print ("11.MATCHA")
	print ("12.SOBACHA")
	print ("-----------------------MENU MAKANAN KOREA-------------------------")
	print ("MAKANAN")
	print ("13.BULGOGI")
	print ("14.BIMBIMBAP")
	print ("15.KIMCHI")
	print ("MINUMAN")
	print ("16.BANANA MILK")
	print ("17.TEH OMIJA")
	print ("18.YUJA CHA")	
	print ("19.exit")
	print (68 * "-")

while True:
	print_menu()
	choice = int(input("Masukkan pesanan (1-19) : "))
	
	
	if choice==1:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 17000
		x = (jumlah*harga)
		os.system('cls')
		print("ANDA MEMESAN SOTO DENGAN HARGA RP. " + str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==2:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 15000
		x = (jumlah*harga)
		print("ANDA MEMESAN SATE DENGAN HARGA RP. " + str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==3:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 12000
		x = (jumlah*harga)
		print("ANDA MEMESAN KETOPRAK DENGAN HARGA RP. " + str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==4:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 10000
		x = (jumlah*harga)
		print("ANDA MEMESAN ES TEH DENGAN HARGA RP. " + str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==5:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 10000
		x = (jumlah*harga)
		print("ANDA MEMESAN ES JERUK DENGAN HARGA RP. " + str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==6:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 10000
		x = (jumlah*harga)
		print("ANDA MEMESAN LEMON TEA DENGAN HARGA RP. " + str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==7:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 30000
		x = (jumlah*harga)
		print("ANDA MEMESAN SUSHI DENGAN HARGA RP. " + str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==8:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 40000
		x = (jumlah*harga)
		print("ANDA MEMESAN SASHIMI DENGAN HARGA RP. "+ str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==9:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 20000
		x = (jumlah*harga)
		print("ANDA MEMESAN RAMEN DENGAN HARGA RP. " + str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==10:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 15000
		x = (jumlah*harga)
		print("ANDA MEMESAN OCHA DENGAN HARGA RP. " + str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==11:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 15000
		x = (jumlah*harga)
		print("ANDA MEMESAN MATCHA DENGAN HARGA RP. "+ str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==12:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 15000
		x = (jumlah*harga)
		print("ANDA MEMESAN SOBACHA DENGAN HARGA RP. " + str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==13:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 50000
		x = (jumlah*harga)
		print("ANDA MEMESAN BULGOGI DENGAN HARGA RP. " + str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==14:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 45000
		x = (jumlah*harga)
		print("ANDA MEMESAN BIMBIMBAP DENGAN HARGA RP. " + str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==15:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 10000
		x = (jumlah*harga)
		print("ANDA MEMESAN KIMCHI DENGAN HARGA RP. "+ str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==16:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 12000
		x = (jumlah*harga)
		print("ANDA MEMESAN BANANA MILK DENGAN HARGA RP. "+ str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==17:
		jumlah = int(input("Masukkan jumlah pesanan : "))
		harga = 12000
		x = (jumlah*harga)
		print("ANDA MEMESAN TEH OMIJA DENGAN HARGA RP. "+ str (x))
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==18:
		
		harga = 12000
		x = (jumlah*harga)
		print("ANDA MEMESAN YUJA CHA DENGAN HARGA RP. "+ str (x))	
		jawab = str(input("Apakah anda masih ingin memesan lagi? (y/t) : " ))
		if jawab == "y":
				continue
		else:
			break
	elif choice==19:
		input("Program Selesai")
		break
	else:
		input("Pilihan anda salah")
		print_menu()
print (" ")
print ("Terima kasih atas pesanannya. Harap menunggu pesanan anda diantarkan.")
