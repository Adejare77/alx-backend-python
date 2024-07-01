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

    # @unittest.mock.patch.object(GithubOrgClient, 'org',
    #                         new_callable=unittest.mock.PropertyMock)
    # def test_public_repos_url(self, mock_obj):
    #     """ Test public_repos_url method """

    #     mock_obj.return_value = {"repos_url": "payload"}

    #     client = GithubOrgClient("sample")
    #     result = client._public_repos_url

    #     mock_obj.assert_called_once_with()

    #     self.assertEqual(result, "payload")

    @unittest.mock.patch.object(
        GithubOrgClient, 'org', new_callable=unittest.mock.PropertyMock)
    def test_public_repos_url(self, mock_obj):
        """ Test public_repos_url method """

        # define a patch using either patch or patch.object
        with unittest.mock.patch(
            'client.GithubOrgClient.org',
             new_callable=unittest.mock.PropertyMock) as mock_obj:

            # Give the mock_obj a return value
            mock_obj.return_value = {"repos_url": "payload"}

            client = GithubOrgClient("sample")
            result = client._public_repos_url

            mock_obj.assert_called_once_with()

            self.assertEqual(result, "payload")
