# -*- coding: utf-8 -*-

###############################################################################
#
# Insert
# Adds a new media item to an album. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Insert(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Insert Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Plus/Domains/Media/Insert')


    def new_input_set(self):
        return InsertInputSet()

    def _make_result_set(self, result, path):
        return InsertResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InsertChoreographyExecution(session, exec_id, path)

class InsertInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Insert
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
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
    def set_Collection(self, value):
        """
        Set the value of the Collection input for this Choreo. ((optional, string) Currently the acceptable values are "cloud".  (Upload the media to share on Google+).)
        """
        InputSet._set_input(self, 'Collection', value)
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((conditional, string) The Content-Type of the file that is being uploaded (i.e. image/jpg). Required when specifying the FileContent input.)
        """
        InputSet._set_input(self, 'ContentType', value)
    def set_DisplayName(self, value):
        """
        Set the value of the DisplayName input for this Choreo. ((optional, string) The display name for the media. If this parameter is not provided, Google assigns a GUID to the media resource.)
        """
        InputSet._set_input(self, 'DisplayName', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Selector specifying a subset of fields to include in the response.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_FileContent(self, value):
        """
        Set the value of the FileContent input for this Choreo. ((conditional, string) The Base64 encoded contents of the file to upload.)
        """
        InputSet._set_input(self, 'FileContent', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The ID of the user to create the activity on behalf of.  The value "me" is set as the default to indicate the authenticated user.)
        """
        InputSet._set_input(self, 'UserID', value)


class InsertResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Insert Choreo.
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

class InsertChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return InsertResultSet(response, path)
