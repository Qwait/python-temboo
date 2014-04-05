# -*- coding: utf-8 -*-

###############################################################################
#
# GetSubscription
# Allows your application to check whether the notification service was previously subscribed on a specific user and to retrieve the subscription expiration date.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetSubscription(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetSubscription Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Withings/Notification/GetSubscription')


    def new_input_set(self):
        return GetSubscriptionInputSet()

    def _make_result_set(self, result, path):
        return GetSubscriptionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSubscriptionChoreographyExecution(session, exec_id, path)

class GetSubscriptionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetSubscription
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_CallbackURL(self, value):
        """
        Set the value of the CallbackURL input for this Choreo. ((required, string) The URL used when subscribing to the notification service.)
        """
        InputSet._set_input(self, 'CallbackURL', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Withings.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Withings.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID of the user to verify a subscription for.)
        """
        InputSet._set_input(self, 'UserID', value)

class GetSubscriptionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetSubscription Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Withings.)
        """
        return self._output.get('Response', None)

class GetSubscriptionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetSubscriptionResultSet(response, path)
