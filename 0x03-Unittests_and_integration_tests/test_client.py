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
        payload = {
            "repo_url": "https://api.github.com/users/abc/repos",
            "repo": [
                {
                    'id':	572997712,
                    'name':	"advent-of-code-2022",
                    'full_name':	"abc/advent-of-code-2022",
                    'html_url':	"https://github.com/abc/advent-of-code-2022",
                    'url':	"https://api.github.com/r…/abc/advent-of-code-2022",
                    'created_at':	"2022-12-01T13:36:46Z",
                    'updated_at':	"2023-10-09T14:13:16Z",
                    'pushed_at':	"2022-12-13T00:54:50Z",
                    'git_url':	"git://github.com/abc/advent-of-code-2022.git",
                    'ssh_url':	"git@github.com:abc/advent-of-code-2022.git",
                    'clone_url':	"https://github.com/abc/advent-of-code-2022.git",
                    'svn_url':	"https://github.com/abc/advent-of-code-2022",
                },
                {
                    'id': 440222033,
                    'name': "advent-of-code-2021",
                    'full_name':	"abc/advent-of-code-2021",
                    'html_url':"https://github.com/abc/advent-of-code-2021",
                    'url': "https://api.github.com/r…/abc/advent-of-code-2021",
                    'created_at':	"2021-12-20T15:41:38Z",
                    'updated_at':	"2023-10-09T13:58:58Z",
                    'pushed_at':	"2021-12-22T00:28:44Z",
                    'git_url':	"git://github.com/abc/advent-of-code-2021.git",
                    'ssh_url':	"git@github.com:abc/advent-of-code-2021.git",
                    'clone_url':	"https://github.com/abc/advent-of-code-2021.git",
                    'svn_url':	"https://github.com/abc/advent-of-code-2021"
                }
            ]
        }
        mock_get_json.return_value = payload["repo"]

        # mock GithubOrgClient._public_repos_url
        with unittest.mock.patch.object(
            GithubOrgClient, '_public_repos_url',
            new_callable=unittest.mock.PropertyMock
        ) as mock_org:
            # Give mock_org a return value
            mock_org.return_value = payload["repo_url"]

            client = GithubOrgClient("google")
            result = client.public_repos()

            # Assert mock_org was called once
            mock_org.assert_called_once()

            # Assert their value is same
            self.assertEqual(result, ['advent-of-code-2022', "advent-of-code-2021"])
        mock_get_json.assert_called_once()
