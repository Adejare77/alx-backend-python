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

    def test_public_repos_url(self):
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

    @unittest.mock.patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test public_repos method """

        # Give mock_get_json a return values:
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
                ]
            }

        mock_get_json.return_value = test_payload["repos"]

        # mock GithubOrgClient._public_repos_url
        with unittest.mock.patch.object(
            GithubOrgClient, '_public_repos_url',
            new_callable=unittest.mock.PropertyMock
        ) as mock_org:
            # Give mock_org a return value
            mock_org.return_value = "https://rashisky.tech"

            client = GithubOrgClient("RashiskyAdejare")
            result = client.public_repos()

            # Assert mock_org was called once
            mock_org.assert_called_once()

            # Assert their value is same
            self.assertEqual(result, ['episodes.dart', 'kratu'])
