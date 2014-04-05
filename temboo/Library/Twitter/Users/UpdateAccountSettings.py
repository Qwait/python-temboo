# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateAccountSettings
# Updates the authenticating user's settings such as trend location and sleep time settings.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateAccountSettings(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateAccountSettings Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Users/UpdateAccountSettings')


    def new_input_set(self):
        return UpdateAccountSettingsInputSet()

    def _make_result_set(self, result, path):
        return UpdateAccountSettingsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateAccountSettingsChoreographyExecution(session, exec_id, path)

class UpdateAccountSettingsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateAccountSettings
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_EndSleepTime(self, value):
        """
        Set the value of the EndSleepTime input for this Choreo. ((optional, string) The hour that sleep time should end if it is enabled. The value should be provided in ISO8601 format (e.g., 00-23).)
        """
        InputSet._set_input(self, 'EndSleepTime', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) The language which Twitter should render in for this user. The language must be specified by the appropriate two letter ISO 639-1 representation.)
        """
        InputSet._set_input(self, 'Language', value)
    def set_SleepTimeEnabled(self, value):
        """
        Set the value of the SleepTimeEnabled input for this Choreo. ((optional, boolean) When set to true, enables sleep time for the user. Sleep time is when push or SMS notifications should not be sent to the user.)
        """
        InputSet._set_input(self, 'SleepTimeEnabled', value)
    def set_StartSleepTime(self, value):
        """
        Set the value of the StartSleepTime input for this Choreo. ((optional, string) The hour that sleep time should begin if it is enabled. The value should be provided in ISO8601 format (e.g., 00-23).)
        """
        InputSet._set_input(self, 'StartSleepTime', value)
    def set_Timezone(self, value):
        """
        Set the value of the Timezone input for this Choreo. ((optional, string) The timezone dates and times that should be displayed for the user (e.g., Europe/Copenhagen, Pacific/Tongatapu))
        """
        InputSet._set_input(self, 'Timezone', value)
    def set_TrendLocationWOEID(self, value):
        """
        Set the value of the TrendLocationWOEID input for this Choreo. ((optional, string) The Yahoo! Where On Earth ID to use as the user's default trend location.)
        """
        InputSet._set_input(self, 'TrendLocationWOEID', value)

class UpdateAccountSettingsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateAccountSettings Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The number of requests left for the 15 minute window.)
        """
        return self._output.get('Remaining', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The rate limit ceiling for this particular request.)
        """
        return self._output.get('Limit', None)
    def get_Reset(self):
        """
        Retrieve the value for the "Reset" output from this Choreo execution. ((date) The remaining window before the rate limit resets in UTC epoch seconds.)
        """
        return self._output.get('Reset', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class UpdateAccountSettingsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateAccountSettingsResultSet(response, path)
