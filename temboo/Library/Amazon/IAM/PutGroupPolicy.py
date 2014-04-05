# -*- coding: utf-8 -*-

###############################################################################
#
# PutGroupPolicy
# Adds or updates a policy document associated with a specified group.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PutGroupPolicy(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutGroupPolicy Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/IAM/PutGroupPolicy')


    def new_input_set(self):
        return PutGroupPolicyInputSet()

    def _make_result_set(self, result, path):
        return PutGroupPolicyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutGroupPolicyChoreographyExecution(session, exec_id, path)

class PutGroupPolicyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutGroupPolicy
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_PolicyDocument(self, value):
        """
        Set the value of the PolicyDocument input for this Choreo. ((required, json) The policy document. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'PolicyDocument', value)
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_GroupName(self, value):
        """
        Set the value of the GroupName input for this Choreo. ((required, string) The name of the group to associate the policy with.)
        """
        InputSet._set_input(self, 'GroupName', value)
    def set_PolicyName(self, value):
        """
        Set the value of the PolicyName input for this Choreo. ((required, string) The name of the policy document.)
        """
        InputSet._set_input(self, 'PolicyName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class PutGroupPolicyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutGroupPolicy Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class PutGroupPolicyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutGroupPolicyResultSet(response, path)
