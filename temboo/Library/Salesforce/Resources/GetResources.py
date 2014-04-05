# -*- coding: utf-8 -*-

###############################################################################
#
# GetResources
# List available resources for a specified API version.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetResources(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetResources Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Salesforce/Resources/GetResources')


    def new_input_set(self):
        return GetResourcesInputSet()

    def _make_result_set(self, result, path):
        return GetResourcesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetResourcesChoreographyExecution(session, exec_id, path)

class GetResourcesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetResources
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Salesforce. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Salesforce. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_InstanceName(self, value):
        """
        Set the value of the InstanceName input for this Choreo. ((required, string) The server url prefix that indicates which instance your Salesforce account is on (e.g. na1, na2, na3, etc).)
        """
        InputSet._set_input(self, 'InstanceName', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Version(self, value):
        """
        Set the value of the Version input for this Choreo. ((optional, string) The API version number to retrieve resources for. Defaults to "v28.0".)
        """
        InputSet._set_input(self, 'Version', value)

class GetResourcesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetResources Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Salesforce.)
        """
        return self._output.get('Response', None)

class GetResourcesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetResourcesResultSet(response, path)
