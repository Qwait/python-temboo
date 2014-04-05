# -*- coding: utf-8 -*-

###############################################################################
#
# CreateMember
# Adds one or more members to a list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateMember(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateMember Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Lists/CreateMember')


    def new_input_set(self):
        return CreateMemberInputSet()

    def _make_result_set(self, result, path):
        return CreateMemberResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateMemberChoreographyExecution(session, exec_id, path)

class CreateMemberInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateMember
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
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((conditional, string) The numerical ID of the list. Required unless Slug is provided.)
        """
        InputSet._set_input(self, 'ListId', value)
    def set_OwnerId(self, value):
        """
        Set the value of the OwnerId input for this Choreo. ((optional, string) The user ID of the user who owns the list being requested by a slug.)
        """
        InputSet._set_input(self, 'OwnerId', value)
    def set_OwnerScreenName(self, value):
        """
        Set the value of the OwnerScreenName input for this Choreo. ((optional, string) The screen name of the user who owns the list being requested by a slug.)
        """
        InputSet._set_input(self, 'OwnerScreenName', value)
    def set_ScreenName(self, value):
        """
        Set the value of the ScreenName input for this Choreo. ((conditional, string) The screen name of the user to add to the list. Required unless providing the UserId. Multiple screen names can be provided in a comma-separated list.)
        """
        InputSet._set_input(self, 'ScreenName', value)
    def set_Slug(self, value):
        """
        Set the value of the Slug input for this Choreo. ((optional, string) When identifying a list by a slug, either OwnerScreenName or OwnerId must be provided.)
        """
        InputSet._set_input(self, 'Slug', value)
    def set_UserId(self, value):
        """
        Set the value of the UserId input for this Choreo. ((conditional, string) The ID of the user to add to the list. Required unless providing the ScreenName. Multiple user IDs can be provided in a comma-separated list.)
        """
        InputSet._set_input(self, 'UserId', value)

class CreateMemberResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateMember Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class CreateMemberChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateMemberResultSet(response, path)
