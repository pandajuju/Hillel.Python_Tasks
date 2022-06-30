# Завдання: перебудувати словник (не створюючи новий) таким чином що
#           його значення стануть ключами значенням котрих буде їхній
#           ключ з початкового словника.

data = {
 	'colors': ['red', 'green', 'blue', 'purple'],
 	'fruits': ['pineapple', 'orange', 'banana'],
 	'clothes': ['coat', 'tshirt']
}


data = {j:i for i in data for j in data.get(i)}
print(data)


