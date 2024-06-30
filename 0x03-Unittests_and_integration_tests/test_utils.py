#!/usr/bin/env python3
""" Parameterize a unit test """

import unittest.mock
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json, memoize
import requests


class TestAccessNestedMap(unittest.TestCase):
    """ Create a unittest for nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ unittest access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a", )),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ unittest access_nested_map exceptions """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ unittest for utils.get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @unittest.mock.patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock):
        """ unittest get_json response """
        mock.return_value = unittest.mock.Mock(status_code=200)
        mock.return_value.json.return_value = test_payload

        result = get_json(test_url)

        mock.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ unittest for memoize decorator """
    def test_memoize(self):
        """ memoize decorator testing """
        class TestClass:
            """ testing """
            def a_method(self):
                """ testing a_method for memoize """
                return 42

            @memoize  # makes a_property  behaves like attribute
            def a_property(self):
                """create a property"""
                return self.a_method()

        with unittest.mock.patch.object(
                                        TestClass, 'a_method', return_value=42
                                        ) as mock_method:

            obj_inst = TestClass()

            # Call a_property twice
            result1 = obj_inst.a_property
            result2 = obj_inst.a_property

            # Assert a_method was called only once
            mock_method.assert_called_once()

            # Assert correct results
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
