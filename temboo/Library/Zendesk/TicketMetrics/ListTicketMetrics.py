# -*- coding: utf-8 -*-

###############################################################################
#
# ListTicketMetrics
# Retrieves a list of metrics for all available tickets.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListTicketMetrics(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListTicketMetrics Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/TicketMetrics/ListTicketMetrics')


    def new_input_set(self):
        return ListTicketMetricsInputSet()

    def _make_result_set(self, result, path):
        return ListTicketMetricsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListTicketMetricsChoreographyExecution(session, exec_id, path)

class ListTicketMetricsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListTicketMetrics
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page number of the results to be returned. Used together with the PerPage parameter to paginate a large set of results.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) The number of results to return per page. Maximum is 100 and default is 100.)
        """
        InputSet._set_input(self, 'PerPage', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        InputSet._set_input(self, 'Server', value)

class ListTicketMetricsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListTicketMetrics Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_NextPage(self):
        """
        Retrieve the value for the "NextPage" output from this Choreo execution. ((integer) The index for the next page of results.)
        """
        return self._output.get('NextPage', None)
    def get_PreviousPage(self):
        """
        Retrieve the value for the "PreviousPage" output from this Choreo execution. ((integer) The index for the previous page of results.)
        """
        return self._output.get('PreviousPage', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class ListTicketMetricsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListTicketMetricsResultSet(response, path)
