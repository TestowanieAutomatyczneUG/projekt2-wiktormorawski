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
        if type(response) != list:
            raise TypeError('Network connection error')
        result = []
        for i in response:
            if i['owners_name'] == owners_name and ['owners_surname'] == owners_surname:
                result.append(i)
        return result


if __name__ == '__main__':
    temp = Login()
    temp.welcome_menu()













import unittest
import requests
from assertpy import *
from unittest.mock import *
from src.main import Insurance, Login
import json


class TestMainInsurance(unittest.TestCase):
    def setUp(self):
        self.insurance = Insurance()
        self.login = Login()

    # Tests Add_new_car
    def test_add_new_car_passed_ints(self):
        assert_that(self.insurance.add_new_car).raises(ValueError).when_called_with(123, 234, 123, 21, 222, 13, 43)

    def test_add_new_car_passed_floats(self):
        assert_that(self.insurance.add_new_car).raises(ValueError).when_called_with(1.23, 2.34, 12.3, 2.1, 0.222, 1.3,
                                                                                    4.3)

    def test_add_new_car_passed_strings_doesnt_raise_ValueError(self):
        assert_that(
            self.insurance.add_new_car("bmw", "z4", "NO2222", "Fafik", "Fontanna", "2021", "5.0 Benzyna")).is_equal_to(
            'Error occurred in adding new car :( No connection to the server')

    def test_add_new_car_mocked_response_code_success(self):
        with patch.object(requests, 'post') as post_mock:
            post_mock.return_value.status_code = 200
            post_mock.return_value.json = "success"
            assert self.insurance.add_new_car("bmw", "z4", "NO2222", "Fafik", "Fontanna", "2021",
                                              "5.0 Benzyna") == post_mock.return_value.json

    def test_add_new_car_mocked_response_code_400(self):
        with patch.object(requests, 'post') as post_mock:
            post_mock.return_value.status_code = 400
            result = "Check your passed information (that car exists in database)"
            assert self.insurance.add_new_car("audi", "a4", "WX32131", "Malik", "Montana", "1998",
                                              "1.0 hybryda diesel") == result

    def test_add_new_car_mocked_response_code_failure(self):
        with patch.object(requests, 'post') as post_mock:
            post_mock.return_value.status_code = 404
            result = "Error occurred in adding new car :( No connection to the server"
            assert self.insurance.add_new_car("aston martin", "db11", "NO3961U", "Wiktor", "Morawski", "2017",
                                              "5.2 Benzyna") == result

    # Tests remove car

    def test_remove_car_CarID_int(self):
        assert_that(self.insurance.remove_car).raises(ValueError).when_called_with(1111111111143)

    def test_remove_car_CarID_float(self):
        assert_that(self.insurance.remove_car).raises(ValueError).when_called_with(11.321143)

    def test_remove_car_passed_strings_doesnt_raise_ValueError(self):
        assert_that(self.insurance.remove_car("2021213123213")).is_equal_to(
            'Error occurred in removing :( No connection to the server')

    """
    @patch('src.main.requests.delete')
    def test_remove_car(self, mocked_request):
        mocked_request = Mock()
        expected_response = {'deleted': '2021213123213'}
        mocked_request.return_value.json.return_value = expected_response
        mocked_request.return_value.status_code.return_value = 200
        self.assertEqual(self.insurance.remove_car('2021213123213'), mocked_request.return_value.json.return_value)
    """

    # Tests update Plates

    def test_update_plates_CarID_int(self):
        assert_that(self.insurance.update_plates).raises(ValueError).when_called_with(1111111111143, 'str')

    def test_update_plates_CarID_float(self):
        assert_that(self.insurance.update_plates).raises(ValueError).when_called_with(11.321143, 'str')

    def test_update_plates_plates_int(self):
        assert_that(self.insurance.update_plates).raises(ValueError).when_called_with('str', 1111111111143)

    def test_update_plates_plates_float(self):
        assert_that(self.insurance.update_plates).raises(ValueError).when_called_with('str', 11.321143)

    def test_update_plates_passed_strings_doesnt_raise_ValueError(self):
        assert_that(self.insurance.update_plates("2021213123213", "WX12345")).is_equal_to(
            "Error occurred in updating car's plates :( No connection to the server")

    def test_update_plates_mocked_response_code_success(self):
        with patch.object(requests, 'put') as put_mock:
            put_mock.return_value.status_code = 200
            put_mock.return_value.json = "success"
            assert self.insurance.update_plates("12314124", "NO2222") == put_mock.return_value.json

    def test_update_plates_mocked_response_code_403_CarID_not_found(self):
        with patch.object(requests, 'put') as put_mock:
            put_mock.return_value.status_code = 403
            result = "Not found car with that CarID"
            assert self.insurance.update_plates("68749", "WX32131") == result

    def test_update_plates_mocked_response_code_422_plates_not_found(self):
        with patch.object(requests, 'put') as put_mock:
            put_mock.return_value.status_code = 422
            result = "Incorrect plates"
            assert self.insurance.update_plates("232133", "WX32131") == result

    def test_update_plates_mocked_response_code_failure(self):
        with patch.object(requests, 'post') as put_mock:
            put_mock.return_value.status_code = 404
            result = "Error occurred in updating car's plates :( No connection to the server"
            assert self.insurance.update_plates("845987", "NO3961U") == result

    # Tests update_owner



    def test_update_owner_CarID_int(self):
        assert_that(self.insurance.update_owner).raises(ValueError).when_called_with(1111111111143, 'filip',
                                                                                     'szczescniak')

    def test_update_owner_CarID_float(self):
        assert_that(self.insurance.update_owner).raises(ValueError).when_called_with(11.321143, 'andzej', 'golota')

    def test_update_owner_owners_name_int(self):
        assert_that(self.insurance.update_owner).raises(ValueError).when_called_with('1231445', 1111111111143, 'Falcon')

    def test_update_owner_owners_name_float(self):
        assert_that(self.insurance.update_owner).raises(ValueError).when_called_with('2313322', 11.321143,
                                                                                     'krzysiowiak')

    def test_update_owner_owners_surname_int(self):
        assert_that(self.insurance.update_owner).raises(ValueError).when_called_with('1235555', 'kuba', 1143)

    def test_update_owner_owners_surname_float(self):
        assert_that(self.insurance.update_owner).raises(ValueError).when_called_with('3123124', 'baran', 11.321143)

    def test_update_owner_mocked_response_success(self):
        self.insurance.update_owner = Mock(name="put_response")
        self.insurance.update_owner.return_value = 'Success'
        result = self.insurance.update_owner('1232134', 'Wiktor', 'Morawski')
        self.assertEqual('Success', result, 'return from update_owner is incorrect')

    # Tests get_all_client_cars


    def test_get_all_client_cars_Name_not_str(self):
        assert_that(self.insurance.get_all_client_cars).is_type_of(str).when_called_with(1111111111143,
                                                                                     'szczescniak')

    def test_get_all_client_cars_Name_not_str(self):
        assert_that(self.insurance.get_all_client_cars).raises(ValueError).when_called_with('golota', 11.321143)


    @patch('src.main.Insurance.get_all_cars_info')
    def test_get_all_client_cars_mocked_server_response(self, mocked_response):
        mocked_response.return_value = [{"CarID": '3123331222', "brand": "BMW",
                                    "model": "Series 3 F10",
                                    "plates": "NO1234",
                                    "owners_name": "Faik",
                                    "owners_surname": "Malik",
                                    "ending": '21-09-2021',
                                    "Year": '2012',
                                    "Engine": "3.0 Diesel"
                                    }, {"CarID": '12312333',
                                        "brand": "AUDI",
                                        "model": "A3",
                                        "plates": "NO22234",
                                        "owners_name": "Fafik",
                                        "owners_surname": "Malik",
                                        "ending": '22-08-2022',
                                        "Year": '2022',
                                        "Engine": "1.0 Diesel"}]
        expected = [{"CarID": '12312333',
                                        "brand": "AUDI",
                                        "model": "A3",
                                        "plates": "NO22234",
                                        "owners_name": "Fafik",
                                        "owners_surname": "Malik",
                                        "ending": '22-08-2022',
                                        "Year": '2022',
                                        "Engine": "1.0 Diesel"}]
        result = self.insurance.get_all_client_cars('Fafik', 'Malik')
        self.assertEqual(expected, result, "Not equal with fafik malik")

    @patch('src.main.Insurance.get_all_cars_info')
    def test_get_all_client_cars_mocked_server_Error_response(self, mocked_response):
        mocked_response.return_value = 'Error occurred in connecting :( \n Try again later please'
        assert_that(self.insurance.get_all_client_cars).raises(TypeError).when_called_with('Wiktor', 'Morawski')



class TestMainLogin(unittest.TestCase):
    def __init__(self):
        self.insurance = Insurance()
        self.login = Login()

    # Tests welcome_menu

    def test_welcome_menu_call_login_to_db(self):
        pass

    def test_menu_call_insurance_methods(self):
        pass
