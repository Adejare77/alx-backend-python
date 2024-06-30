#!/usr/bin/env python3
""" Test Client """

import unittest
from client import GithubOrgClient
import unittest.mock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ unittest GithubOrgClient.org """

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @unittest.mock.patch('client.get_json')
    def test_org(self, org_name, mock_obj):
        """ Test GithubOrgClient.org """

        # return value of get_json
        mock_obj.return_value = {"mocked": "response"}

        # Create a GithubOrgClient instance
        client = GithubOrgClient(org_name)
        result = client.org

        # # Assert get_json was called only once
        mock_obj.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(result, {"mocked": "response"})
