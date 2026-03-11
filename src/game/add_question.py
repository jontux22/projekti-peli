from src.database.models import Question, Answer


def run_add_question(session):
    kysymys_teksti = input('Anna kysymys: ')

    while True:
        try:
            vaikeus = int(input('Anna vaikeustaso (1-3): '))
            if 1 <= vaikeus <= 3:
                break
            print('Valitse numero väliltä 1-3.')
        except ValueError:
            print('Virhe! Syötäthän numeron.')

    kategoria = str(input('Anna kategoria: '))
    vastaukset = []

    while True:
        vastaus = input('Anna vastaus (vähintään kolme), tyhjä lopettaa: ')

        if vastaus == '' and len(vastaukset) >= 3:
            break

        elif vastaus == '' and len(vastaukset) < 3:
            print('Syötä seuraava vastaus.')

        else:
            vastaukset.append(vastaus)

    print(f'\nKysymys: {kysymys_teksti}')
    for i, v in enumerate(vastaukset, 1):
        print(f'{i}. {v}')

    while True:
        try:
            valinta = int(input(f'Anna oikean vastauksen numero (1-{len(vastaukset)}): '))
            if 1 <= valinta <= len(vastaukset):
                oikea_vastaus_indeksi = valinta - 1
                break
            print(f'Valitse luku väliltä 1-{len(vastaukset)}.')
        except ValueError:
            print(f'Syötä numero 1-{len(vastaukset)}: ')

    vastaus_oliot = []
    for indeksi, teksti in enumerate(vastaukset):
        vastaus_oliot.append(Answer(answer=teksti, correct=(indeksi == oikea_vastaus_indeksi)))

    uusi_kysymys = Question(
        question=kysymys_teksti,
        difficulty=vaikeus,
        category=kategoria,
        answers=vastaus_oliot
    )
    session.add(uusi_kysymys)
    session.commit()
    print('\nKysymys tallennettu onnistuneesti! 🎉\n')

    pass
