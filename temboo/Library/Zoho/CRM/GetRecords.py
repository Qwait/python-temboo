# -*- coding: utf-8 -*-

###############################################################################
#
# GetRecords
# Retrieves all users data specified in the API request.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetRecords(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRecords Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zoho/CRM/GetRecords')


    def new_input_set(self):
        return GetRecordsInputSet()

    def _make_result_set(self, result, path):
        return GetRecordsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecordsChoreographyExecution(session, exec_id, path)

class GetRecordsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRecords
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AuthenticationToken(self, value):
        """
        Set the value of the AuthenticationToken input for this Choreo. ((required, string) A valid authentication token. Permanent authentication tokens can be generated by the GenerateAuthToken Choreo.)
        """
        InputSet._set_input(self, 'AuthenticationToken', value)
    def set_FromIndex(self, value):
        """
        Set the value of the FromIndex input for this Choreo. ((optional, integer) The beginning index of the result set to return. Defaults to 1.)
        """
        InputSet._set_input(self, 'FromIndex', value)
    def set_LastModifiedTime(self, value):
        """
        Set the value of the LastModifiedTime input for this Choreo. ((optional, date) Used to return records with a created or modified date that is after the specified time.  (i.e. 2010-04-21 11:09:23))
        """
        InputSet._set_input(self, 'LastModifiedTime', value)
    def set_Module(self, value):
        """
        Set the value of the Module input for this Choreo. ((optional, string) The Zoho module you want to access. Defaults to 'Leads'.)
        """
        InputSet._set_input(self, 'Module', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid formats are: json and xml (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SelectColumns(self, value):
        """
        Set the value of the SelectColumns input for this Choreo. ((optional, string) The columns to return separated by commas (i.e. First Name,Last Name,Email). When left empty, only IDs are returned.)
        """
        InputSet._set_input(self, 'SelectColumns', value)
    def set_SortColumnString(self, value):
        """
        Set the value of the SortColumnString input for this Choreo. ((optional, string) Used to specify a column to sort by (in ascending order))
        """
        InputSet._set_input(self, 'SortColumnString', value)
    def set_SortOrderString(self, value):
        """
        Set the value of the SortOrderString input for this Choreo. ((optional, string) Sorting order: asc or desc. Default sort order is set to ascending.)
        """
        InputSet._set_input(self, 'SortOrderString', value)
    def set_ToIndex(self, value):
        """
        Set the value of the ToIndex input for this Choreo. ((optional, integer) The ending index of the result set to return. Defaults to 20. Max is 200.)
        """
        InputSet._set_input(self, 'ToIndex', value)

class GetRecordsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRecords Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Zoho. Format corresponds to the ResponseFormat input. Defaults to xml.)
        """
        return self._output.get('Response', None)

class GetRecordsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecordsResultSet(response, path)