# CalorieTracker - Databáze jídel a sledování kalorií
CalorieTracker je webová aplikace vytvořená v Django, která slouží ke sledování denního příjmu kalorií a živin. Uživatelé si budou moci vytvářet vlastní účet a zaznamenávat jednotlivá jídla během dne podle data a času. Každé jídlo bude obsahovat název, množství, kalorickou hodnotu a základní makroživiny (bílkoviny, sacharidy, tuky), které budou převzaty z nutriční tabulky produktů. Aplikace umožní zobrazování denních a týdenních přehledů, výpočet celkového příjmu kalorií a porovnání s individuálně nastaveným cílem. Součástí projektu bude také databáze potravin, možnost vyhledávání a filtrování jídel a jednoduché statistiky pro sledování dlouhodobého stravovacího pokroku a zlepšování životního stylu.

## Instalace a spuštění

### 1. Vytvoření venv

**Windows:**

```bash
py -3 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

**MacOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Spuštění aplikace

**Windows:**

```bash
py -3 ./prj/manage.py runserver
```

**MacOS / Linux:**

```bash
python3 ./prj/manage.py runserver
```
