# -*- coding: utf-8 -*-

###############################################################################
#
# ShowAudit
# Returns detailed information on the specified audit.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ShowAudit(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ShowAudit Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/TicketAudits/ShowAudit')


    def new_input_set(self):
        return ShowAuditInputSet()

    def _make_result_set(self, result, path):
        return ShowAuditResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShowAuditChoreographyExecution(session, exec_id, path)

class ShowAuditInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ShowAudit
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AuditID(self, value):
        """
        Set the value of the AuditID input for this Choreo. ((required, string) The ID of the audit to show.)
        """
        InputSet._set_input(self, 'AuditID', value)
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
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        InputSet._set_input(self, 'Server', value)
    def set_TicketID(self, value):
        """
        Set the value of the TicketID input for this Choreo. ((required, string) The ID of the ticket associated with the audit.)
        """
        InputSet._set_input(self, 'TicketID', value)

class ShowAuditResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ShowAudit Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class ShowAuditChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShowAuditResultSet(response, path)
