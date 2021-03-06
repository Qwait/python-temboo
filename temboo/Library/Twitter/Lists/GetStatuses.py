# -*- coding: utf-8 -*-

###############################################################################
#
# GetStatuses
# Retrieves a timeline of tweets posted by members of the specified list.
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

class GetStatuses(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetStatuses Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetStatuses, self).__init__(temboo_session, '/Library/Twitter/Lists/GetStatuses')


    def new_input_set(self):
        return GetStatusesInputSet()

    def _make_result_set(self, result, path):
        return GetStatusesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetStatusesChoreographyExecution(session, exec_id, path)

class GetStatusesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetStatuses
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetStatusesInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetStatusesInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The API Key (or Consumer Key) provided by Twitter.)
        """
        super(GetStatusesInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The API Secret (or Consumer Secret) provided by Twitter.)
        """
        super(GetStatusesInputSet, self)._set_input('ConsumerSecret', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Specifies the number of records to retrieve. Must be less than or equal to 200. Defaults to 20.)
        """
        super(GetStatusesInputSet, self)._set_input('Count', value)
    def set_IncludeEntitities(self, value):
        """
        Set the value of the IncludeEntitities input for this Choreo. ((optional, boolean) The "entities" node containing extra metadata will not be included when set to false.)
        """
        super(GetStatusesInputSet, self)._set_input('IncludeEntitities', value)
    def set_IncludeRetweets(self, value):
        """
        Set the value of the IncludeRetweets input for this Choreo. ((optional, boolean) When set to true, the response will include retweets if they exist.)
        """
        super(GetStatusesInputSet, self)._set_input('IncludeRetweets', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((conditional, string) The numerical ID of the list. Required unless Slug is provided.)
        """
        super(GetStatusesInputSet, self)._set_input('ListId', value)
    def set_MaxId(self, value):
        """
        Set the value of the MaxId input for this Choreo. ((optional, string) Returns results with an ID less than (older than) or equal to the specified ID.)
        """
        super(GetStatusesInputSet, self)._set_input('MaxId', value)
    def set_OwnerId(self, value):
        """
        Set the value of the OwnerId input for this Choreo. ((optional, string) The user ID of the user who owns the list being requested by a slug.)
        """
        super(GetStatusesInputSet, self)._set_input('OwnerId', value)
    def set_OwnerScreenName(self, value):
        """
        Set the value of the OwnerScreenName input for this Choreo. ((optional, string) The screen name of the user who owns the list being requested by a slug.)
        """
        super(GetStatusesInputSet, self)._set_input('OwnerScreenName', value)
    def set_SinceId(self, value):
        """
        Set the value of the SinceId input for this Choreo. ((optional, string) Returns results with an ID greater than (more recent than) the specified ID.)
        """
        super(GetStatusesInputSet, self)._set_input('SinceId', value)
    def set_Slug(self, value):
        """
        Set the value of the Slug input for this Choreo. ((optional, string) When identifying a list by a slug, either OwnerScreenName or OwnerId must be provided.)
        """
        super(GetStatusesInputSet, self)._set_input('Slug', value)

class GetStatusesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetStatuses Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The rate limit ceiling for this particular request.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The number of requests left for the 15 minute window.)
        """
        return self._output.get('Remaining', None)
    def get_Reset(self):
        """
        Retrieve the value for the "Reset" output from this Choreo execution. ((date) The remaining window before the rate limit resets in UTC epoch seconds.)
        """
        return self._output.get('Reset', None)

class GetStatusesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetStatusesResultSet(response, path)
