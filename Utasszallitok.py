import copy

import pandas


class Utasszallito():
    def __init__(self,tipus, ev, utas, szemelyzet, utazosebesseg, felszallotomeg, fesztav,seb_kategoria):
        self.tipus = tipus
        self.ev = ev
        self.utas = utas
        self.szemelyzet = szemelyzet
        self.utazosebesseg = utazosebesseg
        self.felszallotomeg = felszallotomeg
        self.fesztav = fesztav
        self.seb_kategoria = seb_kategoria

    def __str__(self):
        return f'{self.tipus};{self.ev};{self.utas};{self.szemelyzet};{self.utazosebesseg};' \
        f'{self.felszallotomeg};{self.fesztav};{self.seb_kategoria}'


my_datas = []
my_datas_write = []
my_file_name = 'utasszallitok.txt'
seb_kateg_lista =  []
with open(my_file_name,'r',encoding='utf8') as file:
    header = file.readline().strip().split(';')
    for i in file:
        row = i.strip().split(';')
        if int(row[4]) < 500:
            seb_kateg = 'Alacsony sebességű'
        elif int(row[4]) < 1000:
            seb_kateg = 'Szubszonikus'
        elif int(row[4]) < 1200:
            seb_kateg = 'Transzszonikus'
        else:
            seb_kateg = 'Szuperszonikus'
        seb_kateg_lista.append(seb_kateg)
        if '-' in row[2]:
            row[2] = row[2].split('-')
            row[2] = int(row[2][1])
        else:
            row[2] = int(row[2])
        my_datas.append(Utasszallito(row[0],
                                     int(row[1]),
                                     row[2],
                                     row[3],
                                     int(row[4]),
                                     int(row[5]),
                                     float(row[6].replace(',','.')),
                                     seb_kateg))

my_datas_write = copy.copy(my_datas)
for row in my_datas_write:
    row.felszallotomeg = f'{row.felszallotomeg / 1000:.0f}'
    row.fesztav = f'{row.fesztav * 3.2808:.0f}'



seb_kateg = []
if 'Alacsony sebességű' not in seb_kateg_lista:
    seb_kateg.append('Alacsony sebességű')
elif 'Szubszonikus' not in seb_kateg_lista:
    seb_kateg.append('Szubszonikus')
elif 'Transzszonikus' not in seb_kateg_lista:
    seb_kateg.append('Transzszonikus')
elif 'Szuperszonikus' not in seb_kateg_lista:
    seb_kateg.append('Szuperszonikus')
else:
    seb_kateg.append('Minden sebességkategóriából van repülőgéptípus')

#print(my_datas)
boeing_count = 0
for i in my_datas:
    #print(i)
    if 'Boeing' in i.tipus:
        boeing_count += 1

print(f'4. feladat: Adatsorok száma: {len(my_datas)}')
print(f'5. feladat: Boeing típusok száma: {boeing_count}')
max_utas = 0
for index,data in enumerate(my_datas):
    legtobb_utas = (max(my_datas, key=lambda x: x.utas))

print(f'6. feladat: A legtöbb utast szállító repülőgéptípus'
      f'\n\t Típus: {legtobb_utas.tipus}'
      f'\n\t Első felszállás: {legtobb_utas.ev}'
      f'\n\t Utasok száma: {legtobb_utas.utas}'
      f'\n\t Személyzet: {legtobb_utas.szemelyzet}'
      f'\n\t Utazósebesség: {legtobb_utas.utazosebesseg}')
print(f'7. feladat:'
      f'\n\t', ';'.join(seb_kateg))

#8. feladat:

with open('utasszallitok_new.txt', 'w', encoding='utf8') as write:
    print(*header,sep=';',file=write)
    print(*my_datas_write,sep='\n',file=write)
