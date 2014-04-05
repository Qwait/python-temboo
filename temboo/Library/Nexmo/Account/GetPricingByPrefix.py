# -*- coding: utf-8 -*-

###############################################################################
#
# GetPricingByPrefix
# Retrieve Nexmo's outbound pricing for the specified international prefix.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetPricingByPrefix(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPricingByPrefix Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Nexmo/Account/GetPricingByPrefix')


    def new_input_set(self):
        return GetPricingByPrefixInputSet()

    def _make_result_set(self, result, path):
        return GetPricingByPrefixResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPricingByPrefixChoreographyExecution(session, exec_id, path)

class GetPricingByPrefixInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPricingByPrefix
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your API Key provided to you by Nexmo.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your API Secret provided to you by Nexmo.)
        """
        InputSet._set_input(self, 'APISecret', value)
    def set_Prefix(self, value):
        """
        Set the value of the Prefix input for this Choreo. ((required, integer) International dialing code. (e.g. 44))
        """
        InputSet._set_input(self, 'Prefix', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetPricingByPrefixResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPricingByPrefix Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class GetPricingByPrefixChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPricingByPrefixResultSet(response, path)
