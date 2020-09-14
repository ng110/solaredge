import requests
import datetime as dt
from functools import wraps
import pytz
import numbers

__title__ = "solaredge"
__version__ = "0.0.1"
__author__ = "Bert Outtier"
__license__ = "MIT"

BASEURL = 'https://monitoringapi.solaredge.com'

def urljoin(*parts):
    part_list = []
    for part in parts:
        p = str(part)
        if p.endswith('//'):
            p = p[0:-1]
        else:
            p = p.strip('/')
        part_list.append(p)
    # join everything together
    url = '/'.join(part_list)
    return url

class Solaredge(object):
    """
    Object containing SolarEdge's site API-methods.
    See https://www.solaredge.com/sites/default/files/se_monitoring_api.pdf
    """
    def __init__(self, site_token):
        """
        To communicate, you need to set a site token.
        Get it from your account.
        """
        self.token = site_token
        self.details = self.get_details()['details']
        self.siteid = self.details['id']

    def get_details(self):
        """
        Request service location info
        """
        url = urljoin(BASEURL, "site", self.site_id, "details")
        params = {
            'api_key': self.token
        }
        r = requests.get(url, params)
        r.raise_for_status()
        return r.json()

    def get_dataPeriod(self):
        """
        Request start and end date of installation data 
        """
        url = urljoin(BASEURL, "site", self.site_id, "dataPeriod")
        params = {
            'api_key': self.token
        }
        r = requests.get(url, params)
        r.raise_for_status()
        return r.json()

    def get_energy(self, startDate, endDate, timeUnit='DAY'):
        url = urljoin(BASEURL, "site", self.site_id, "energy")
        params = {
            'api_key': self.token,
            'startDate': startDate,
            'endDate': endDate,
            'timeUnit': timeUnit
        }
        r = requests.get(url, params)
        r.raise_for_status()
        return r.json()

    # def get_timeFrameEnergy(self, startDate, endDate, timeUnit='DAY'):
    #     url = urljoin(BASEURL, "site", self.site_id, "timeFrameEnergy")
    #     params = {
    #         'api_key': self.token,
    #         'startDate': startDate,
    #         'endDate': endDate,
    #         'timeUnit': timeUnit
    #     }
    #     r = requests.get(url, params)
    #     r.raise_for_status()
    #     return r.json()

    # def get_power(self, startTime, endTime):
    #     url = urljoin(BASEURL, "site", self.site_id, "power")
    #     params = {
    #         'api_key': self.token,
    #         'startTime': startTime,
    #         'endTime': endTime
    #     }
    #     r = requests.get(url, params)
    #     r.raise_for_status()
    #     return r.json()

    def get_overview(self):
        url = urljoin(BASEURL, "site", self.site_id, "overview")
        params = {
            'api_key': self.token
        }
        r = requests.get(url, params)
        r.raise_for_status()
        return r.json()

    def get_powerDetails(self, startTime, endTime, meters=None):
        url = urljoin(BASEURL, "site", self.site_id, "powerDetails")
        params = {
            'api_key': self.token,
            'startTime': startTime,
            'endTime': endTime
        }

        if meters:
            params['meters'] = meters

        r = requests.get(url, params)
        r.raise_for_status()
        return r.json()

    def get_energyDetails(self, startTime, endTime, meters=None, timeUnit="DAY"):
        url = urljoin(BASEURL, "site", self.site_id, "energyDetails")
        params = {
            'api_key': self.token,
            'startTime': startTime,
            'endTime': endTime,
            'timeUnit': timeUnit
        }

        if meters:
            params['meters'] = meters

        r = requests.get(url, params)
        r.raise_for_status()
        return r.json()

    # def get_currentPowerFlow(self):
    #     url = urljoin(BASEURL, "site", self.site_id, "currentPowerFlow")
    #     params = {
    #         'api_key': self.token
    #     }

    #     r = requests.get(url, params)
    #     r.raise_for_status()
    #     return r.json()

    # def get_storageData(self, startTime, endTime, serials=None):
    #     url = urljoin(BASEURL, "site", self.site_id, "storageData")
    #     params = {
    #         'api_key': self.token,
    #         'startTime': startTime,
    #         'endTime': endTime
    #     }

    #     if serials:
    #         params['serials'] = serials.join(',')

    #     r = requests.get(url, params)
    #     r.raise_for_status()
    #     return r.json()


