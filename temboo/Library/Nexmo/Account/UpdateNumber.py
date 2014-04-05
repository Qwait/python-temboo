# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateNumber
# Updates the callback details for the specified number.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateNumber(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateNumber Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Nexmo/Account/UpdateNumber')


    def new_input_set(self):
        return UpdateNumberInputSet()

    def _make_result_set(self, result, path):
        return UpdateNumberResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateNumberChoreographyExecution(session, exec_id, path)

class UpdateNumberInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateNumber
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
    def set_CallbackURL(self, value):
        """
        Set the value of the CallbackURL input for this Choreo. ((optional, string) Mobile originated Callback URL.)
        """
        InputSet._set_input(self, 'CallbackURL', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((required, string) 2-digit country code. (e.g. CA))
        """
        InputSet._set_input(self, 'Country', value)
    def set_Number(self, value):
        """
        Set the value of the Number input for this Choreo. ((required, string) Your inbound (MSISDN) number (e.g. 34911067000).)
        """
        InputSet._set_input(self, 'Number', value)
    def set_SMPPSystemType(self, value):
        """
        Set the value of the SMPPSystemType input for this Choreo. ((optional, string) The Mobile Orignated associated system type for SMPP client only. (e.g.: inbound))
        """
        InputSet._set_input(self, 'SMPPSystemType', value)

class UpdateNumberResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateNumber Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. For a successful request, an empty response body is returned.)
        """
        return self._output.get('Response', None)
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Nexmo. A 200 is returned for a successful request.)
        """
        return self._output.get('ResponseStatusCode', None)

class UpdateNumberChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateNumberResultSet(response, path)
