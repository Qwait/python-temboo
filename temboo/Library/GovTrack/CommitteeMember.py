# -*- coding: utf-8 -*-

###############################################################################
#
# CommitteeMember
# Returns records indicating the current membership of a Member of Congress on a committee or subcommittee.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CommitteeMember(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CommitteeMember Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GovTrack/CommitteeMember')


    def new_input_set(self):
        return CommitteeMemberInputSet()

    def _make_result_set(self, result, path):
        return CommitteeMemberResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CommitteeMemberChoreographyExecution(session, exec_id, path)

class CommitteeMemberInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CommitteeMember
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CommitteeMemberID(self, value):
        """
        Set the value of the CommitteeMemberID input for this Choreo. ((optional, integer) The ID of the committee member resource. When using this input, all other filter parameters are ignored, and a single record is returned.)
        """
        InputSet._set_input(self, 'CommitteeMemberID', value)
    def set_Committee(self, value):
        """
        Set the value of the Committee input for this Choreo. ((optional, string) The committee or subcommittee being served on. To filter by this field, you can pass the ID of the committee. Filter operators allowed. Sortable.)
        """
        InputSet._set_input(self, 'Committee', value)
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
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Offset the results by the number given, useful for paging through results.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_Person(self, value):
        """
        Set the value of the Person input for this Choreo. ((optional, string) The ID of the Member of Congress serving on a committee. Filter operators allowed. Sortable.)
        """
        InputSet._set_input(self, 'Person', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) You can order the results using fieldname (ascending) or -fieldname (descending) where "fieldname" is one of the variables that is listed as 'Sortable' in the description. Ex: '-lastname')
        """
        InputSet._set_input(self, 'Sort', value)

class CommitteeMemberResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CommitteeMember Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from GovTrack.)
        """
        return self._output.get('Response', None)

class CommitteeMemberChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CommitteeMemberResultSet(response, path)
