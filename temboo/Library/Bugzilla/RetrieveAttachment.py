# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveAttachment
# Retrieves a bug attachment by ID.
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

class RetrieveAttachment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveAttachment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveAttachment, self).__init__(temboo_session, '/Library/Bugzilla/RetrieveAttachment')


    def new_input_set(self):
        return RetrieveAttachmentInputSet()

    def _make_result_set(self, result, path):
        return RetrieveAttachmentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveAttachmentChoreographyExecution(session, exec_id, path)

class RetrieveAttachmentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveAttachment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AttachmentID(self, value):
        """
        Set the value of the AttachmentID input for this Choreo. ((required, integer) The ID of the attachment to retrieve.)
        """
        super(RetrieveAttachmentInputSet, self)._set_input('AttachmentID', value)
    def set_AttachmentsWithData(self, value):
        """
        Set the value of the AttachmentsWithData input for this Choreo. ((optional, integer) Enter 1 to obtain full bug attachments data.  If null, only attachments fields will be returned with no associated data.)
        """
        super(RetrieveAttachmentInputSet, self)._set_input('AttachmentsWithData', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) Your Bugzilla password.)
        """
        super(RetrieveAttachmentInputSet, self)._set_input('Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((optional, string) The base URL for the Bugzilla server to access. Defaults to https://api-dev.bugzilla.mozilla.org/latest. To access the test server, set to https://api-dev.bugzilla.mozilla.org/test/latest.)
        """
        super(RetrieveAttachmentInputSet, self)._set_input('Server', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((optional, string) Your Bugzilla username.)
        """
        super(RetrieveAttachmentInputSet, self)._set_input('Username', value)

class RetrieveAttachmentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveAttachment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Bugzilla.)
        """
        return self._output.get('Response', None)

class RetrieveAttachmentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveAttachmentResultSet(response, path)
