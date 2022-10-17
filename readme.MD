# DC NITRO PICKER

Tai skriptas, kuris automatizuotai ieško tarp discord žinučių nitro kodo, ir jeigu randa - bando aktyvuoti.

## Prieš naudojant

Prieš naudojant rekomenduojama iš anksto prisijungti prie daug skirtingų serverių, geriausia ten kur tarkim yra kažkoks žmogus kuris kartais pamėto kodus, ne visuose serveriuose juos mėto.


## Instaliacija/Konfiguracija

Naudokite paketų tvarkyklę [pip](https://pip.pypa.io/en/stable/) instaliuojant.

pirma reikia instaliuoti reikiamas python bibliotekas
```bash
git clone https://github.com/dariuxas/nitrosnaiperis
pip install -r requirements.txt
```

## Prieš pradedant naudojant

Prieš pradedant naudoti - redaguokite nustatymų failą config.json
```json
{
    "bot_token": "", // Tai jūsų boto autorizacijos kodas 
    "nitro_user_token": "", // autorizacijos kodas vartotojo kuriam norite aktyvuoti nitro
    "log_kanalas": "" // kanalas kuris logins nitro kodus
}
```

## Naudojimas

```bash
python3 bot.py
```
