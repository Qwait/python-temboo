# -*- coding: utf-8 -*-

###############################################################################
#
# Inbox
# Retrieves a list of messages in a specified user's inbox.
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

class Inbox(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Inbox Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Inbox, self).__init__(temboo_session, '/Library/Facebook/Reading/Inbox')


    def new_input_set(self):
        return InboxInputSet()

    def _make_result_set(self, result, path):
        return InboxResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InboxChoreographyExecution(session, exec_id, path)

class InboxInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Inbox
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(InboxInputSet, self)._set_input('AccessToken', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return (i.e. id,name).)
        """
        super(InboxInputSet, self)._set_input('Fields', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the profile to retrieve messages for. Defaults to "me" indicating the authenticated user.)
        """
        super(InboxInputSet, self)._set_input('ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(InboxInputSet, self)._set_input('ResponseFormat', value)

class InboxResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Inbox Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class InboxChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return InboxResultSet(response, path)
