# -*- coding: utf-8 -*-

###############################################################################
#
# GetMachineType
# Retrieves information about the specified Machine Type.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetMachineType(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetMachineType Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/ComputeEngine/MachineTypes/GetMachineType')


    def new_input_set(self):
        return GetMachineTypeInputSet()

    def _make_result_set(self, result, path):
        return GetMachineTypeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMachineTypeChoreographyExecution(session, exec_id, path)

class GetMachineTypeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetMachineType
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Comma-seperated list of fields you want to include in the response.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_MachineType(self, value):
        """
        Set the value of the MachineType input for this Choreo. ((required, string) The name of the machine type to retrieve.)
        """
        InputSet._set_input(self, 'MachineType', value)
    def set_Project(self, value):
        """
        Set the value of the Project input for this Choreo. ((required, string) The ID of a Google Compute project.)
        """
        InputSet._set_input(self, 'Project', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_Zone(self, value):
        """
        Set the value of the Zone input for this Choreo. ((required, string) The name of the zone that contains the machine type to retrieve.)
        """
        InputSet._set_input(self, 'Zone', value)

class GetMachineTypeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetMachineType Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class GetMachineTypeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetMachineTypeResultSet(response, path)
