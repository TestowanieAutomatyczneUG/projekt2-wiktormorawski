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
