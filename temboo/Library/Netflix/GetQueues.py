# -*- coding: utf-8 -*-

###############################################################################
#
# GetQueues
# Retrieves a list of a subscriber's queues.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetQueues(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetQueues Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetQueues, self).__init__(temboo_session, '/Library/Netflix/GetQueues')


    def new_input_set(self):
        return GetQueuesInputSet()

    def _make_result_set(self, result, path):
        return GetQueuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetQueuesChoreographyExecution(session, exec_id, path)

class GetQueuesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetQueues
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Netflix (AKA the OAuth Consumer Key).)
        """
        super(GetQueuesInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetQueuesInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetQueuesInputSet, self)._set_input('AccessToken', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) Set this to the maximum number of results to return. This number cannot be greater than 500. If you do not specify max_results, the default value is 25)
        """
        super(GetQueuesInputSet, self)._set_input('MaxResults', value)
    def set_SharedSecret(self, value):
        """
        Set the value of the SharedSecret input for this Choreo. ((required, string) The Shared Secret provided by Netflix (AKA the OAuth Consumer Secret).)
        """
        super(GetQueuesInputSet, self)._set_input('SharedSecret', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Use this to specify the sort order for the queue entries. Sort order may be by queue_sequence, date_added, or alphabetical. The default sort order, if you do not specify one, is queue_sequence.)
        """
        super(GetQueuesInputSet, self)._set_input('Sort', value)
    def set_StartIndex(self, value):
        """
        Set the value of the StartIndex input for this Choreo. ((optional, integer) The offset number of the results from the query.)
        """
        super(GetQueuesInputSet, self)._set_input('StartIndex', value)
    def set_UpdatedMin(self, value):
        """
        Set the value of the UpdatedMin input for this Choreo. ((optional, date) If set, the response will include only those items with updated timestamps greater than or equal to the timestamp provided. Specify this value either in Unix time format (seconds since epoch).)
        """
        super(GetQueuesInputSet, self)._set_input('UpdatedMin', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID associated with the user whose queue information you want to retrieve.)
        """
        super(GetQueuesInputSet, self)._set_input('UserID', value)

class GetQueuesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetQueues Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Netflix.)
        """
        return self._output.get('Response', None)

class GetQueuesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetQueuesResultSet(response, path)
