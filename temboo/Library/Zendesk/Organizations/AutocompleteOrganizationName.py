# -*- coding: utf-8 -*-

###############################################################################
#
# AutocompleteOrganizationName
# Returns an array of organizations whose name starts with the value specified in the name parameter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AutocompleteOrganizationName(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AutocompleteOrganizationName Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Organizations/AutocompleteOrganizationName')


    def new_input_set(self):
        return AutocompleteOrganizationNameInputSet()

    def _make_result_set(self, result, path):
        return AutocompleteOrganizationNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AutocompleteOrganizationNameChoreographyExecution(session, exec_id, path)

class AutocompleteOrganizationNameInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AutocompleteOrganizationName
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) Prefix used to generate a list of Organization names. Must be at least 2 characters long.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        InputSet._set_input(self, 'Server', value)

class AutocompleteOrganizationNameResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AutocompleteOrganizationName Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class AutocompleteOrganizationNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AutocompleteOrganizationNameResultSet(response, path)
