# -*- coding: utf-8 -*-

###############################################################################
#
# CreateList
# Creates a new list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Lists/CreateList')


    def new_input_set(self):
        return CreateListInputSet()

    def _make_result_set(self, result, path):
        return CreateListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateListChoreographyExecution(session, exec_id, path)

class CreateListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateList
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
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description of the list.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Mode(self, value):
        """
        Set the value of the Mode input for this Choreo. ((optional, string) Indicates if this list is "public" (the default) or "private".)
        """
        InputSet._set_input(self, 'Mode', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the new list.)
        """
        InputSet._set_input(self, 'Name', value)

class CreateListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class CreateListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateListResultSet(response, path)
