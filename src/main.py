import requests

"""
[
  {
    "CarID": 3123331222,
    "brand": "BMW",
    "model": "Series 3 F10",
    "plates": "NO1234",
    "owners_name": "Fafik",
    "owners_surname": "Malik",
    "ending":21-09-2021,
    "Year":2012,
    "Engine": "3.0 Diesel"
  },
  ...
]
"""


class Login:
    def __init__(self):
        self.url = "https://axa.pl/worker_logon"

    def welcome_menu(self):
        print("Welcome to Axa Worker Service")
        print("Please insert your login : ")
        login = input()
        print("Please insert your password : ")
        password = input()
        self.login_to_database(login, password)

    def menu(self):
        temp = Insurance()
        print('\n')
        print(
            '////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('\n' +
              '$$$$$$\  $$\   $$\  $$$$$$\        $$$$$$\ $$\   $$\  $$$$$$\  $$\   $$\ $$$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ ' + '\n' +
              '$$  __$$\ $$ |  $$ |$$  __$$\       \_$$  _|$$$\  $$ |$$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|\n' +
              '$$ /  $$ |\$$\ $$  |$$ /  $$ |        $$ |  $$$$\ $$ |$$ /  \__|$$ |  $$ |$$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |\n' +
              '$$$$$$$$ | \$$$$  / $$$$$$$$ |        $$ |  $$ $$\$$ |\$$$$$$\  $$ |  $$ |$$$$$$$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\ ' + '\n' +
              '$$  __$$ | $$  $$<  $$  __$$ |        $$ |  $$ \$$$$ | \____$$\ $$ |  $$ |$$  __$$< $$  __$$ |$$ \$$$$ |$$ |      $$  __| \n' +
              '$$ |  $$ |$$  /\$$\ $$ |  $$ |        $$ |  $$ |\$$$ |$$\   $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ | \n' +
              '$$ |  $$ |$$ /  $$ |$$ |  $$ |      $$$$$$\ $$ | \$$ |\$$$$$$  |\$$$$$$  |$$ |  $$ |$$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ ' + '\n' +
              '\__|  \__|\__|  \__|\__|  \__|      \______|\__|  \__| \______/  \______/ \__|  \__|\__|  \__|\__|  \__| \______/ \________|')
        print('\n')
        print("Type in number of choice")
        print("Adding new Car ->  1")
        print("Removing Car -> 2")
        print("Updating Car plates -> 3")
        print("Updating owners information -> 4")
        print("Get Car info -> 5")
        print("Get All cars -> 6")
        print("Get all cars of 1 owner -> 7")
        choice = input()

        if (choice == "1"):
            print("Type in brand of the car : ")
            brand = input()
            print("Type in model of the car : ")
            model = input()
            print("Type in car's plates : ")
            plates = input()
            print("Type in owner's Name : ")
            owners_name = input()
            print("Type in owner's Surname : ")
            owners_surname = input()
            print("Type in engine (liters and type) : ")
            engine = input()
            print("Type in production year of the car : ")
            year = input()
            result = temp.add_new_car(brand, model, plates, owners_name, owners_surname, engine, year)
            print(result)
            self.menu()

        if (choice == "2"):
            print("Type in CarID : ")
            CarID = input()
            result = temp.remove_car(CarID)
            print(result)
            self.menu()

        if (choice == "3"):
            print("Type in CarID : ")
            CarID = input()
            print("Type in new plates : ")
            plates = input()
            result = temp.update_plates(CarID, plates)
            print(result)
            self.menu()

        if (choice == "4"):
            print("Type in CarID : ")
            CarID = input()
            print("Type in new owner's Name : ")
            owners_name = input()
            print("Type in new owner's Surname : ")
            owners_surname = input()
            result = temp.update_owner(CarID, owners_name, owners_surname)
            print(result)
            self.menu()

        if (choice == "5"):
            print("Type in CarID : ")
            CarID = input()
            print("Type in plates : ")
            plates = input()
            result = temp.get_car_info(CarID, plates)
            print(result)
            self.menu()

        if (choice == "6"):
            result = temp.get_all_cars_info()
            print(result)
            self.menu()

        if (choice == "7"):
            print("Type in owner's name : ")
            owners_name = input()
            print("Type in owner's surname : ")
            owners_surname = input()
            result = temp.get_all_client_cars(owners_name, owners_surname)
            print(result)
            self.menu()
        else:
            self.menu()

    def login_to_database(self, worker_login, worker_password):
        response = requests.post(self.url, data={'login': worker_login, 'password': worker_password})
        response.status_code = 200
        if (200 <= response.status_code <= 299):
            print("Logging into axa finished successfully")
            self.menu()
        if (response.status_code == 401):
            print("Bad login or password")
            print("Try Again !")
            self.welcome_menu()
        else:
            print("Error occurred in connecting :( \n Try again later please")
            self.welcome_menu()


class Insurance:
    def __init__(self):
        self.add_url = "https://axa.pl/add"
        self.remove_url = "https://axa.pl/remove"
        self.all_cars = "https://axa.pl/all"
        self.update = "https://axa.pl/update"

    def add_new_car(self, brand, model, plates, owners_name, owners_surname, engine, year):
        if not isinstance(brand, str):
            raise ValueError("brand type Error ; Must be string !")
        if not isinstance(model, str):
            raise ValueError("model type Error ; Must be string !")
        if not isinstance(plates, str):
            raise ValueError("plates type Error ; Must be string !")
        if not isinstance(owners_name, str):
            raise ValueError("owner's name type Error ; Must be string !")
        if not isinstance(owners_surname, str):
            raise ValueError("owner's surname type Error ; Must be string !")
        if not isinstance(engine, str):
            raise ValueError("engine type Error ; Must be string !")
        if not isinstance(year, str):
            raise ValueError("year type Error ; Must be string !")

        response = requests.post(self.add_url,
                                 data={'brand': brand, 'model': model, 'plates': plates, 'owners_name': owners_name,
                                       'owners_surname': owners_surname, 'engine': engine, 'year': year})

        if 200 <= response.status_code <= 299:
            return response.json
        if response.status_code == 400:
            return 'Check your passed information (that car exists in database)'
        else:
            return 'Error occurred in adding new car :( No connection to the server'

    def remove_car(self, CarID):
        if not isinstance(CarID, str):
            raise ValueError("CarID type Error ; Must be string !")
        response = requests.delete(self.remove_url, data={'CarID': CarID})
        if 200 <= response.status_code <= 299:
            return response.json
        if response.status_code == 403:
            return 'Not found car with that CarID'
        else:
            return 'Error occurred in removing :( No connection to the server'

    def update_plates(self, CarID, plates):
        if not isinstance(CarID, str):
            raise ValueError("CarID type Error ; Must be string !")
        if not isinstance(plates, str):
            raise ValueError("plates type Error ; Must be string !")

        response = requests.put(self.update + '/' + CarID, data={'plates': plates})
        if 200 <= response.status_code <= 299:
            return response.json
        if response.status_code == 403:
            return 'Not found car with that CarID'
        if response.status_code == 422:
            return 'Incorrect plates'
        else:
            return "Error occurred in updating car's plates :( No connection to the server"

    def update_owner(self, CarID, owners_name, owners_surname):
        if not isinstance(CarID, str):
            raise ValueError("CarID type Error ; Must be string !")
        if not isinstance(owners_name, str):
            raise ValueError("owner's name type Error ; Must be string !")
        if not isinstance(owners_surname, str):
            raise ValueError("owner's surname type Error ; Must be string !")
        response = requests.put(self.update + '/' + CarID,
                                data={'owners_name': owners_name, 'owners_surname': owners_surname})
        if 200 <= response.status_code <= 299:
            return response.json
        if response.status_code == 403:
            return 'Check passed CarID (probably incorrect)'
        if response.status_code == 400:
            return 'That owner is already connected with that CarID'
        else:
            return 'Error occurred in adding new car :( No connection to the server'

    def get_car_info(self, CarID, plates):
        if not isinstance(CarID, str):
            raise ValueError("CarID type Error ; Must be string !")
        if not isinstance(plates, str):
            raise ValueError("plates type Error ; Must be string !")
        response = requests.get(self.all_cars + '/' + CarID, data={'plates': plates})
        if 200 <= response.status_code <= 299:
            return response.json
        if response.status_code == 403:
            return 'Check passed CarID (probably incorrect) and plates'
        else:
            return 'Error occurred in adding new car :( No connection to the server'


    def get_all_cars_info(self):
        response = requests.get(self.all_cars)
        if (response.status_code >= 300):
            return "Error occurred in connecting :( \n Try again later please"
        return response.json

    def get_all_client_cars(self, owners_name, owners_surname):
        if not isinstance(owners_name, str) or not isinstance(owners_surname, str):
            raise ValueError("You passed incorrect owner's name or surname")
        response = self.get_all_cars_info()
        if (response == str):
            raise TypeError('Error in getting all cars')
        result = []
        for i in response:
            if i['owners_name'] == owners_name and i['owners_surname'] == owners_surname:
                result.append(i)
        return result


if __name__ == '__main__':
    temp = Login()
    temp.welcome_menu()
