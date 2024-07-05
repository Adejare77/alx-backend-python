#!/usr/bin/env python3
""" Test Client """

import unittest
from client import GithubOrgClient
import unittest.mock
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
# import requests
from requests.exceptions import HTTPError


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
                    'svn_url':	"https://github.com/abc/advent-of-code-2022",
                },
                {
                    'id': 440222033,
                    'name': "advent-of-code-2021",
                    'full_name': "abc/advent-of-code-2021",
                    'html_url': "https://github.com/abc/advent-of-code-2021",
                    'url': "https://api.github.com/r…/abc/advent-of-code-2021",
                    'created_at':	"2021-12-20T15:41:38Z",
                    'updated_at':	"2023-10-09T13:58:58Z",
                    'pushed_at':	"2021-12-22T00:28:44Z",
                    'git_url':	"git://github.com/abc/advent-of-code-2021.git",
                    'ssh_url':	"git@github.com:abc/advent-of-code-2021.git",
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
            self.assertEqual(result, ['advent-of-code-2022',
                                      "advent-of-code-2021"])

        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_value):
        """ Test has_license method """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected_value)

    @parameterized_class(
        ("org_payload", "repos_payload", "expected_repos",
            "apache2_repos"),
        [
            (TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1],
             TEST_PAYLOAD[0][2], TEST_PAYLOAD[0][3])
            ]
    )
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """ Integration test: fixtures """
        @classmethod
        def setUpClass(cls) -> None:
            """ Set up class method to start patching request.get """
            cls.get_patcher = unittest.mock.patch(
                'requests.get', side_effect=cls.mocked_requests_get)
            cls.mock_get = cls.get_patcher.start()

        @classmethod
        def tearDownClass(cls) -> None:
            cls.get_patcher.stop()

        @classmethod
        def mocked_requests_get(cls, url):
            """ Mock function for requests.get"""
            class MockResponse:
                def __init__(self, json_data, status_code):
                    self.json_data = json_data
                    self.status_code = status_code

                def json(self):
                    return self.json_data

            if 'repos' in url:
                return MockResponse(cls.repos_payload, 200)
            elif 'orgs' in url:
                return MockResponse(cls.org_payload, 200)

            return HTTPError(f'404 client not found for url: {url}')

        def test_public_repos(self):
            """ Test the public_repos method without license """
            client = GithubOrgClient("google")
            result = client.public_repos()
            self.assertEqual(result, self.expected_repos)

        def test_public_repos_with_license(self):
            """ Test the public_repos method with license """
            client = GithubOrgClient("google")
            result = client.public_repos(license="apache-2.0")
            self.assertEqual(result, self.apache2_repos)


"""
@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()
"""
