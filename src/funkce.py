"""
konstanty
funkce na nacitani, funkce pro praci s evidenci
"""

max_delka_jmena = 15
pokracujte = 'Pokračujte stisknutím klávesy Enter...'
hlavicka_evidence = "".join(slovo.ljust(max_delka_jmena) for slovo in ['Jméno', 'Příjmení', 'Věk', 'Telefonní číslo'])


def nacti_jmeno(prijmeni = False):
    jmeno_ok = False
    while not jmeno_ok:
        jmeno = input(f'Zadejte {"příjmení" if prijmeni else "jméno pojištěného"}: ').strip()
        if jmeno.isalpha() and len(jmeno) > 1 and len(jmeno) < max_delka_jmena:
            jmeno = jmeno.title()
            jmeno_ok = True
        else:
            print(f'Nesprávný formát. Použijte minimálně 2, maximálně {max_delka_jmena} znaků [a - ž].')
    return jmeno


def nacti_vek():
    vek_ok = False
    while not vek_ok:
        vek = input('Zadejte věk: ')
        try:
            vek = int(vek)
            if 0 <= vek <= 130:
                vek_ok = True
            else:
                print(f'Zadal(a) jste {vek}. Prosím zadejte věk v rozmezí 0 - 130.')
        except ValueError:
            print(f'Zadal(a) jste "{vek}". Prosím zadejte číslo [0 - 130].')
    return vek


def nacti_telefon():
    telefon_ok = False
    while not telefon_ok:
        telefon = input('Zadejte telefonní číslo: ')
        try:
            telefon = int(telefon.replace(' ', ''))
            if len(str(telefon)) == 9:
                telefon_ok = True
            else:
                print(f'Nesprávná délka telefonního čísla. Prosím zadejte 9-místné telefonní číslo (bez předvolby).')
        except ValueError:
            print(f'Zadal(a) jste "{telefon}". Prosím zadejte pouze číslice [0 - 9].')
    return telefon


def nacti_udaje(vek_nacist=False, telefon_nacist=False):
    udaje = [nacti_jmeno(), nacti_jmeno(prijmeni=True)]
    if vek_nacist:
        udaje.append(nacti_vek())
    if telefon_nacist:
        udaje.append(nacti_telefon())
    return udaje


def je_v_evidenci(evidence, jmeno, prijmeni, vek=None):
    je_v_evidenci = False
    for pojisteny in evidence:
        if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
            if vek:
                if pojisteny.vek == vek:
                    je_v_evidenci = True
            else:
                je_v_evidenci = True
    return je_v_evidenci


def vypis_evidenci(evidence, jmeno=None, prijmeni=None):
    print(hlavicka_evidence)
    for pojisteny in evidence:
        if jmeno and prijmeni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                print(pojisteny)
        else:
            print(pojisteny)
    print()
