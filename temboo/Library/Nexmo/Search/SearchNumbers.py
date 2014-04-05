# -*- coding: utf-8 -*-

###############################################################################
#
# SearchNumbers
# Get available inbound numbers for a given country.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchNumbers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchNumbers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Nexmo/Search/SearchNumbers')


    def new_input_set(self):
        return SearchNumbersInputSet()

    def _make_result_set(self, result, path):
        return SearchNumbersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchNumbersChoreographyExecution(session, exec_id, path)

class SearchNumbersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchNumbers
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
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((required, string) 2-digit country code. (e.g. CA))
        """
        InputSet._set_input(self, 'Country', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) Page index)
        """
        InputSet._set_input(self, 'Index', value)
    def set_Pattern(self, value):
        """
        Set the value of the Pattern input for this Choreo. ((optional, string) Pattern to match.)
        """
        InputSet._set_input(self, 'Pattern', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Size(self, value):
        """
        Set the value of the Size input for this Choreo. ((optional, integer) Page size.)
        """
        InputSet._set_input(self, 'Size', value)

class SearchNumbersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchNumbers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class SearchNumbersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchNumbersResultSet(response, path)
