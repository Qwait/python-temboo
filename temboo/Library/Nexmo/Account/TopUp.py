# -*- coding: utf-8 -*-

###############################################################################
#
# TopUp
# Allows you to top-up your account provided that you've set up "auto-reload" in your Account Settings.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class TopUp(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TopUp Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Nexmo/Account/TopUp')


    def new_input_set(self):
        return TopUpInputSet()

    def _make_result_set(self, result, path):
        return TopUpResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopUpChoreographyExecution(session, exec_id, path)

class TopUpInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TopUp
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
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_TransactionID(self, value):
        """
        Set the value of the TransactionID input for this Choreo. ((required, string) The transaction id associated with your **first** 'auto reload' top-up.)
        """
        InputSet._set_input(self, 'TransactionID', value)

class TopUpResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TopUp Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Nexmo. A 200 is returned for a successful request.)
        """
        return self._output.get('ResponseStatusCode', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. For a successful request, an empty response body is returned.)
        """
        return self._output.get('Response', None)

class TopUpChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TopUpResultSet(response, path)
