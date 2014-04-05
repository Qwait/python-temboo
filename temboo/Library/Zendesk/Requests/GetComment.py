# -*- coding: utf-8 -*-

###############################################################################
#
# GetComment
# Retrieves the specified comment from a request.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetComment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetComment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Requests/GetComment')


    def new_input_set(self):
        return GetCommentInputSet()

    def _make_result_set(self, result, path):
        return GetCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCommentChoreographyExecution(session, exec_id, path)

class GetCommentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetComment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CommentID(self, value):
        """
        Set the value of the CommentID input for this Choreo. ((required, string) The ID of the comment to retrieve.)
        """
        InputSet._set_input(self, 'CommentID', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_RequestID(self, value):
        """
        Set the value of the RequestID input for this Choreo. ((required, string) The ID of the request that has been commented on.)
        """
        InputSet._set_input(self, 'RequestID', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        InputSet._set_input(self, 'Server', value)

class GetCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetComment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class GetCommentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCommentResultSet(response, path)
