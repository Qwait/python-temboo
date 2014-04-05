# -*- coding: utf-8 -*-

###############################################################################
#
# GetEbayDetails
# Retrieves the available meta-data for the specified eBay site.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetEbayDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetEbayDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/eBay/Trading/GetEbayDetails')


    def new_input_set(self):
        return GetEbayDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetEbayDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEbayDetailsChoreographyExecution(session, exec_id, path)

class GetEbayDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetEbayDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DetailName(self, value):
        """
        Set the value of the DetailName input for this Choreo. ((optional, string) An enumeration value used to filter the result by Detail Name (e.g., PaymentOptionDetails, RegionDetail, ShippingLocationDetails, ShippingServiceDetails, SiteDetails, etc).)
        """
        InputSet._set_input(self, 'DetailName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((optional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        InputSet._set_input(self, 'SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        InputSet._set_input(self, 'SiteID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        InputSet._set_input(self, 'UserToken', value)

class GetEbayDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetEbayDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetEbayDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetEbayDetailsResultSet(response, path)
