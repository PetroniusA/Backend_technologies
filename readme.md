# Django

# Instalace
Django nainstalujeme prikazem (verze 4.1.1)
python -m pip install django==4.1.1

DŮLEŽITÉ: VŠICHNI V TÝMU MUSÍ MÍT STEJNOU VERZI

Vytvoříme nový projekt příkazem:
djangodjango-admin startproject hollymovies .

V settings.py máme nastavení našeho projektu.

v path.py mame nastavene cesty

## Spuštění

python manage.py runserver

pokud potrebujeme spustit vice serveru najednou, muzeme zmenit port 

python manage.py runserver 8001 - server poběží na portu 8001, tedy na více portech najednou

##Vytvoreni aplikace 

python manage.py startapp viewer

-migrations -- složka, která obsahuje migrace
- admin.py - administrační část
- apps.py - nastavení aplikace( necháme beze změn)
- models.py - zde jsou definované modely ( tabulky databáze)
- tests.py - zde řešíme testování (ukážeme si později)
- views.py - zde bude logika( propojení databáze a template)

### Registrace aplikace 
Aplikaci můžeme zaregistrovat v souboru C:\Users\Dell\Desktop\python\Backend_technologies\hollymovies\settings.py

# ORM

Modely vytváříme v aplikaci 'models.py' v dané aplikaci.

DŮLEŽITÉ: Po každé změně v modelech(tj. v souboru 'models.py' ) musime 

vytvoření migračního skriptu: 'python manage.py makemigrations'
-aplikujeme migraci: 'python manage.py migrate'








