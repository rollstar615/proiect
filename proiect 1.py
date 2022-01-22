
def create_vanzare(id_vanzare, name, gen, price, reducere):

    return {
        'id': id_vanzare,
        'name': name,
        'gen': gen,
        'price': price,
        'reducere': reducere,
    }


def get_id(vanzare):
    return vanzare['id']


def get_titlu_carte(vanzare):
    return vanzare['name']


def get_gen_carte(vanzare):
    return vanzare['gen']


def get_price(vanzare):
    return vanzare['price']


def get_tip_reducere(vanzare):
    return vanzare['reducere']

def set_reducere(vanzare, reducere):
    vanzare['reducere']='reducere'

def to_string(vanzare):
    return '{}. {}: {} - price: {}, calories: {}, year: {}'.format(
        get_id(vanzare),
        get_name(vanzare),
        get_gen_carte(vanzare),
        get_price(vanzare),
        get_tip_reducere(vanzare)
    )

def get_cake_by_id(list_of_vanzari, id_vanzare):
    for vanzare in list_of_vanzari:
        if get_id(vanzare) == id_vanzare:
            return vanzare
    return None


def add_vanzare(list_of_cakes, id_cake, name, description, price, calories, year):
    new_vanzare = create_vanzare(id_vanzare, name, gen, price, reducere)
    return list_of_vanzari + [new_vanzare]


def remove_vanzare(list_of_vanzari, id_cake):

    return [vanzare for vanzare in list_of_vanzari if get_id(cake) != id_cake]



def update_vanzare(list_of_cakes, id_cake, name, description, price, calories, year):
    new_vanzari = []
    for vanzare in list_of_vanzari:
        if get_id(vanzare) != id_vanzare:
            new_vanzari.append(vanzare)
        else:
            new_vanzare = create_vanzare(
                get_id(vanzare),
                name if name != '' else get_titlu_carte(vanzare),
                gen if gen != '' else get_titlu_carte(vanzare),
                int(price) if price != '' else get_price(vanzare),
                reducere if reducere !='' else get_tip_reducere(vanzare)
            )
            new_vanzari.append(new_vanzare)
    return new_vanzari

def reducere(list_of_vanzari, search_str, reduce_percentage):
    updated_vanzari = deepcopy(list_of_vanzari)
    for vanzare in updated_vanzari:
        if search_str in get_tip_reducere(vanzare):
            changed_price = (100 - reduce_percentage)* get_price(vanzare) / 100
            set_price(cake, changed_price)
    for vanzare in updated_vanzari:
        if search_str in get_tip_reducere(vanzare):
            changed_price=(100-reduce_percentage)*get_price(vanzare/100)
    return updated_vanzari

def main():
    list_of_vanzari = []
    list_of_vanzari = add_vanzare(list_of_vanzari, 1, 'abc', 'sdfa', 100,'Gold')
    list_of_vanzari = add_vanzare(list_of_vanzari, 2, 'cvxvx', '24322', 150, 'Gold' )
    list_of_vanzari = add_vanzare(list_of_vanzari, 3, '534', 'gfdgdf', 170, 'Silver')

    list_of_vanzari = run_ui(list_of_cakes)


if __name__ == '__main__':
    main()

Corectare de aici

def show_menu():
    print('1. Adauga prajitura')
    print('2. Sterge prajitura')
    print('3. Modifica prajitura')
    print('4. Reducerea caloriilor pe baza de nume')
    print('a. Show all cakes')
    print('x. Exit')


def ui_add_cake(list_of_cakes):
    id_cake = int(input('Dati id-ul: '))
    name = input('Dati numele: ')
    description = input('Dati descrierea: ')
    price = int(input('Dati pretul: '))
    calories = int(input('Dati caloriile: '))
    year = int(input('Dati anul introducerii: '))

    new_cakes = add_cake(list_of_cakes, id_cake, name, description, price, calories, year)
    print('Cake added!')
    return new_cakes


def ui_show_all(list_of_cakes):
    for cake in list_of_cakes:
        print(to_string(cake))


def ui_remove_cake(list_of_cakes):
    id_cake = int(input('Dati id-ul de sters: '))
    return remove_cake(list_of_cakes, id_cake)


def ui_update_cake(list_of_cakes):
    id_cake = int(input('Dati id-ul prajiturii de actualizat: '))
    name = input('Dati noul nume, gol pentru a nu schimba: ')
    description = input('Dati noua desc, gol pentru a nu schimba: ')
    price = input('Dati noul pret, gol pentru a nu schimba: ')
    calories = input('Dati noile calorii, gol pentru a nu schimba: ')
    year = input('Dati noul an al introducerii, gol pentru a nu schimba: ')

    list_of_cakes = update_cake(
        list_of_cakes,
        id_cake,
        name,
        description,
        price,
        calories,
        year)
    print('Prajituri a fost actualizata!')
    return list_of_cakes


def ui_reduce_calories(list_of_cakes):
    search_str = input('Dati stringul de cautare: ')
    reduce_percentage = float(input('Dati procentajul de reducere (0 - 100): '))

    list_of_cakes = reduce_calories(list_of_cakes, search_str, reduce_percentage)
    print('Reducere efectuata cu succes!')
    return list_of_cakes


def run_ui(list_of_cakes):
    while True:
        show_menu()
        op = input('Alegeti optiunea: ')
        if op == '1':
            #list_of_cakes[:] = ...
            list_of_cakes = ui_add_cake(list_of_cakes)
        elif op == '2':
            list_of_cakes = ui_remove_cake(list_of_cakes)
        elif op == '3':
            list_of_cakes = ui_update_cake(list_of_cakes)
        elif op == '4':
            list_of_cakes = ui_reduce_calories(list_of_cakes)
        elif op == 'a':
            ui_show_all(list_of_cakes)
        elif op == 'x':
            break

    return list_of_cakes




