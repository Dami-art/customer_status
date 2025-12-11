
while True:
    ime_kupca = input("Unesite ime i prezime korisnika: ")
    if " " not in ime_kupca:
        print("Ime nije dobro unijeto, molimo unesite ime i prezime korisnika: ")
        continue
    else:
        ime_i_prezime_kupca = ime_kupca.split()
        ime = ime_i_prezime_kupca[0]
        prezime = ime_i_prezime_kupca[1]
        break
    
broj_kupovina = int(input("Unesite broj kupovina u toku posljednjih godinu dana: "))


if broj_kupovina > 0:
    ukupan_potroseni_iznos = 0
    broj_kupovina_iznad_10_hiljada = 0
    for x in range(1,broj_kupovina+1):
        vrijednost_kupovine = float(input(f"Unesite iznos za kupovinu {x} u dinarima: "))
        ukupan_potroseni_iznos  += vrijednost_kupovine 
        if vrijednost_kupovine > 10000:
            broj_kupovina_iznad_10_hiljada +=1
                
    print(f"Poštovani {ime}, ukupno ste potrošili {ukupan_potroseni_iznos}, od toga je bilo {broj_kupovina_iznad_10_hiljada} kupovina iznad 10.000 dinara.") 
 
def status(ukupan_potroseni_iznos, broj_kupovina):
    if  ukupan_potroseni_iznos > 100000 and broj_kupovina > 10:
        return "VIP" 
    else:
        return "STANDARD" 
    

status_kupca = status(ukupan_potroseni_iznos, broj_kupovina)
print(f"Korisnik {ime} {prezime} ima status {status_kupca} korisnika.")

cijena = float(input(f"Poštovani {ime}, unesite cijenu artikla koji želite da kupite: "))
iznos_popusta = 0

def racunanje_popusta(cijena,status_kupca):
      
    if status_kupca == "VIP":
        iznos_popusta = 10
    else:
        iznos_popusta = 5 
    cijena_sa_popustom = float(cijena - (cijena*iznos_popusta/100)) 
    return cijena_sa_popustom

nova_cijena = racunanje_popusta(cijena, status_kupca)

print(f"Cijena artikla sa popustom iznosi: {nova_cijena} dinara.")