# -*- coding: utf-8 -*-

###############################################################################
#
# Vote
# Returns roll call votes in the U.S. Congress since 1789.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Vote(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Vote Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GovTrack/Vote')


    def new_input_set(self):
        return VoteInputSet()

    def _make_result_set(self, result, path):
        return VoteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VoteChoreographyExecution(session, exec_id, path)

class VoteInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Vote
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Chamber(self, value):
        """
        Set the value of the Chamber input for this Choreo. ((optional, string) The chamber in which the vote was held. Valid values are: house or senate. Filter operators allowed but only when filtering by Congress as well. Sortable.)
        """
        InputSet._set_input(self, 'Chamber', value)
    def set_Congress(self, value):
        """
        Set the value of the Congress input for this Choreo. ((optional, string) The number of the congress in which the vote took place. The current congress is 113. Filter operators allowed. Sortable.)
        """
        InputSet._set_input(self, 'Congress', value)
    def set_Created(self, value):
        """
        Set the value of the Created input for this Choreo. ((optional, string) The date (and in recent history also the time) on which the vote was held. Filter operators allowed. Sortable.)
        """
        InputSet._set_input(self, 'Created', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return in the response. Use double-underscores to span relationships (e.g. person__firstname).)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Results are paged 100 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Number(self, value):
        """
        Set the value of the Number input for this Choreo. ((optional, string) The number of the vote, unique to a Congress and session pair. Filter operators allowed. Sortable.)
        """
        InputSet._set_input(self, 'Number', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Offset the results by the number given, useful for paging through results.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_RelatedAmendment(self, value):
        """
        Set the value of the RelatedAmendment input for this Choreo. ((optional, string) The ID of a related amendment. Filter operators allowed. Sortable.)
        """
        InputSet._set_input(self, 'RelatedAmendment', value)
    def set_RelatedBill(self, value):
        """
        Set the value of the RelatedBill input for this Choreo. ((optional, string) A bill related to this vote. Filter operators allowed. Sortable.)
        """
        InputSet._set_input(self, 'RelatedBill', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Session(self, value):
        """
        Set the value of the Session input for this Choreo. ((optional, string) The session of congress. Filter operators allowed. Sortable.)
        """
        InputSet._set_input(self, 'Session', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) You can order the results using created (ascending) or -created (descending) for the dates that each vote was held.)
        """
        InputSet._set_input(self, 'Sort', value)
    def set_VoteID(self, value):
        """
        Set the value of the VoteID input for this Choreo. ((optional, integer) The ID of a vote object to retrieve. When using this input, all other filter parameters are ignored, and a single record is returned.)
        """
        InputSet._set_input(self, 'VoteID', value)

class VoteResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Vote Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from GovTrack.)
        """
        return self._output.get('Response', None)

class VoteChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return VoteResultSet(response, path)
