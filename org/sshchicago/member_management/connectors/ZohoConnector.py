__author__ = 'chris'

import json
import urllib2

class ZohoConnector(object):
    """
    Utility class for building a list of users stored in Zoho.
    Upstream documentation is at https://www.zoho.com/crm/help/api/
    """

    def __init__(self, zohoAuthToken):
        """
        Instantiates an instance of the ZohoConnector class.
        :param zohoAuthToken: Authentication token from the Developer Space control panel.
        :return: Instance of this class.
        """
        users = list()
        return

    def __downloadUserList(self):
        """
        Populates the user list variable.
        """
        # This downloads the user list from Zoho, creates objects for each User, and shoves them in
        # self.users.

        # Zoho's goofy - you can only request 200 records at a time, and there's no way to look up how many records
        # you might have. Therefore, you end up requesting indexes 1-200, 201-400, ad infinitum, until you get an error.
        # Note that the error isn't an HTTP error - the API continues to return a HTTP 200 OK when it fails.
        records_to_fetch = 200
        startIndex = 1
        endIndex = 0
        zohoCallFailed = False
        while zohoCallFailed is False:
            # Do stuff
            endIndex += records_to_fetch
            url_to_call = "https://crm.zoho.com/crm/private/json/Contacts/getRecords?newFormat=1&authtoken=%s&scope=crmapi&fromIndex=%s&toIndex=%s" % (
                self.zohoAuthToken,
                startIndex,
                endIndex
            )
            result = urllib2.urlopen(url_to_call)
            resultBody = result.read()
            jBody = json.loads(resultBody)
            if self.__checkZohoApiResponseCode(jBody):
                # Do stuff
                pass
            else:
                zohoCallFailed = True

    def __checkZohoApiResponseCode(self, response):
        """
        Takes the raw JSON, checks if it failed or not.
        :param response: JSON object from a Zoho API call
        :return: True if the response is successful, false otherwise.
        """
        if 'nodata' in response['response'].keys():
            return False
        else:
            return True







