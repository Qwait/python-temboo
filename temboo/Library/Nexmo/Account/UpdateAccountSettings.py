# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateAccountSettings
# Update your account settings.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateAccountSettings(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateAccountSettings Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Nexmo/Account/UpdateAccountSettings')


    def new_input_set(self):
        return UpdateAccountSettingsInputSet()

    def _make_result_set(self, result, path):
        return UpdateAccountSettingsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateAccountSettingsChoreographyExecution(session, exec_id, path)

class UpdateAccountSettingsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateAccountSettings
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your API Key provided to you by Nexmo.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your API Secret provided to you by Nexmo.)
        """
        InputSet._set_input(self, 'APISecret', value)
    def set_DeliveryReceiptCallbackURL(self, value):
        """
        Set the value of the DeliveryReceiptCallbackURL input for this Choreo. ((conditional, string) Your new Delivery Receipt Callback URL.)
        """
        InputSet._set_input(self, 'DeliveryReceiptCallbackURL', value)
    def set_InboundCallbackURL(self, value):
        """
        Set the value of the InboundCallbackURL input for this Choreo. ((conditional, string) Your new Inbound Callback URL.)
        """
        InputSet._set_input(self, 'InboundCallbackURL', value)
    def set_NewSecret(self, value):
        """
        Set the value of the NewSecret input for this Choreo. ((optional, string) Your new API secret. (8 characters max))
        """
        InputSet._set_input(self, 'NewSecret', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class UpdateAccountSettingsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateAccountSettings Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Nexmo.)
        """
        return self._output.get('ResponseStatusCode', None)

class UpdateAccountSettingsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateAccountSettingsResultSet(response, path)
