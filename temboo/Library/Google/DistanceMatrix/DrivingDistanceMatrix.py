# -*- coding: utf-8 -*-

###############################################################################
#
# DrivingDistanceMatrix
# Obtain travel distances and times for a matrix of addresses and/or latitude/longitude coordinates.
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

class DrivingDistanceMatrix(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DrivingDistanceMatrix Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DrivingDistanceMatrix, self).__init__(temboo_session, '/Library/Google/DistanceMatrix/DrivingDistanceMatrix')


    def new_input_set(self):
        return DrivingDistanceMatrixInputSet()

    def _make_result_set(self, result, path):
        return DrivingDistanceMatrixResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DrivingDistanceMatrixChoreographyExecution(session, exec_id, path)

class DrivingDistanceMatrixInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DrivingDistanceMatrix
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Alternatives(self, value):
        """
        Set the value of the Alternatives input for this Choreo. ((optional, string) If set to true, additional routes will be returned.)
        """
        super(DrivingDistanceMatrixInputSet, self)._set_input('Alternatives', value)
    def set_Avoid(self, value):
        """
        Set the value of the Avoid input for this Choreo. ((optional, string) Specify whether the calculated directions should avoid the following features: tolls, or highways.)
        """
        super(DrivingDistanceMatrixInputSet, self)._set_input('Avoid', value)
    def set_Destinations(self, value):
        """
        Set the value of the Destinations input for this Choreo. ((required, string) Enter the address or latitude/longitude coordinates to which directions will be generated. Multiple destinations can be separated by pipes (|).  For example: Boston, MA|New Haven|40.7160,-74.0037.)
        """
        super(DrivingDistanceMatrixInputSet, self)._set_input('Destinations', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) Set the language in which to return restults.  A list of supported languages is available here: https://spreadsheets.google.com/pub?key=p9pdwsai2hDMsLkXsoM05KQ&gid=1)
        """
        super(DrivingDistanceMatrixInputSet, self)._set_input('Language', value)
    def set_Origins(self, value):
        """
        Set the value of the Origins input for this Choreo. ((required, string) Enter the address(es) or geo-coordinates from which distance and time will be computed. Multiple destinations can be separated by pipes (|).  For example: Boston, MA|New Haven|40.7160,-74.0037.)
        """
        super(DrivingDistanceMatrixInputSet, self)._set_input('Origins', value)
    def set_Region(self, value):
        """
        Set the value of the Region input for this Choreo. ((optional, string) Enter the region code for the directions, specified as a ccTLD two-character value.)
        """
        super(DrivingDistanceMatrixInputSet, self)._set_input('Region', value)
    def set_Sensor(self, value):
        """
        Set the value of the Sensor input for this Choreo. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        super(DrivingDistanceMatrixInputSet, self)._set_input('Sensor', value)
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) Specify the units to be used when displaying results.  Options include, metric, or imperial.)
        """
        super(DrivingDistanceMatrixInputSet, self)._set_input('Units', value)

class DrivingDistanceMatrixResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DrivingDistanceMatrix Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)

class DrivingDistanceMatrixChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DrivingDistanceMatrixResultSet(response, path)
