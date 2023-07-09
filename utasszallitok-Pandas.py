import copy

import numpy
import pandas

my_file_name = 'utasszallitok.txt'

# típus  év  utas  személyzet  utazósebesség  felszállótömeg  fesztáv

#with open(my_file_name, 'r', encoding='utf8') as file:
my_panda = pandas.read_csv(my_file_name, sep=';').replace(',','.',regex=True) # adatok beolvasása, és a fesztáv ',' átalakitom '.'-ra
my_panda['fesztáv'] = pandas.to_numeric(my_panda['fesztáv'])        # az oszlop típusát floatra változtatom

pandas.options.display.max_rows=(100)
my_panda_2 = copy.copy(my_panda)
my_panda_2['utas'] = my_panda['utas'].str.split('-')
print(my_panda_2['utas'])
#my_panda_2['utas'] = my_panda_2['utas'].str.replace('[^0-9]','',regex=True, ).astype('int32')

for i,j in enumerate(my_panda_2['utas']):
    if len(j) == 2:
        my_panda_2.loc[i,'utas'] = int(j[1])
    else:
        my_panda_2.loc[i,'utas'] = int(j[0])

my_panda_2['felszállótömeg'] = (my_panda["felszállótömeg"] / 1000).round(decimals=0)
my_panda_2['fesztáv'] = (my_panda["fesztáv"] * 3.2808).round(decimals=0)
utas_max = my_panda_2['utas'] == my_panda_2['utas'].max()


#print(my_panda_2['utas'])
boeing = my_panda['típus'].str.contains('Boeing')

seb_kateg = []
low_speed = my_panda[my_panda['utazósebesség'] < 500]
subsonic_speed = my_panda[(my_panda['utazósebesség'] < 1000) & (my_panda['utazósebesség'] > 500)]
transsonic_speed = my_panda[(my_panda['utazósebesség'] < 1200) & (my_panda['utazósebesség'] > 1000)]
supersonic_speed = my_panda[my_panda['utazósebesség'] > 1200]

if len(low_speed) == 0:
    seb_kateg.append('Alacsony sebességű')
elif len(subsonic_speed) == 0:
    seb_kateg.append('Szubszonikus')
elif len(transsonic_speed) == 0:
    seb_kateg.append('Transzszonikus')
elif len(supersonic_speed) == 0:
    seb_kateg.append('Szuperszonikus')
else:
    seb_kateg.append('Minden sebességkategóriából van repülőgéptípus')
#print(my_panda['felszállótömeg'])

print(f'4. feladat: Adatsorok száma: {len(my_panda)}')

print(f'5. feladat: Boeing típusok száma: {len(my_panda[boeing])}')

print('6. feladat: A legtöbb utast szállító repülőgéptípus')
print('\t Típus: ',*my_panda_2[utas_max]["típus"].values)
print('\t Első felszállás: ',*my_panda_2[utas_max]["év"].values)
print('\t Utasok száma: ',*my_panda[utas_max]["utas"])
print('\t Személyzet: ',*my_panda_2[utas_max]["személyzet"].values)
print('\t Utazósebesség: ',*my_panda_2[utas_max]["utazósebesség"].values)

print(f'7. feladat:'
     f'\n\t', ';'.join(seb_kateg))
# 8 feladat
my_panda_2.to_csv('utasszallitok_new_panda.txt', index=False)
