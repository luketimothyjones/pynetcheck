import sys
import unittest

sys.path.append('..')
from netcheck import PyNetCheck


class TestPingParsing(unittest.TestCase):
    """
    These tests read from the ping output samples in this directory to ensure that the
    program correctly parses ping ouput across all target platforms regardless of the
    current development platform.
    """

    def check_platform(self, platform, filename):
        pnc = PyNetCheck(ping_count=4,
                         ping_host='www.google.com',
                         test_delay=10,
                         db_filename='testdb.sqlite',
                         timezone='US/Pacific',
                         timestamp_format='YY/MM/DD HH:mm:ss',
                         _test_platform=platform)

        with open(filename, encoding='utf-8') as pingfile:
            return pnc.execute_ping(_test_data=pingfile.read())

    # ----
    def test_windows_10(self):
        percent_lost, min_ms, average_ms, max_ms = self.check_platform('win32', 'windows10.txt')

    # ----
    def test_windows_10_german(self):
        percent_lost, min_ms, average_ms, max_ms = self.check_platform('win32', 'windows10_german.txt')

    # ----
    def test_ubuntu(self):
        percent_lost, min_ms, average_ms, max_ms = self.check_platform('linux', 'ubuntu.txt')

    # ----
    def test_macos(self):
        percent_lost, min_ms, average_ms, max_ms = self.check_platform('darwin', 'macos_sierra.txt')


# ----
if __name__ == '__main__':
    unittest.main()
