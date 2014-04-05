# -*- coding: utf-8 -*-

###############################################################################
#
# InsertFirewall
# Creates a Firewall resource in the specified project.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class InsertFirewall(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the InsertFirewall Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/ComputeEngine/Firewalls/InsertFirewall')


    def new_input_set(self):
        return InsertFirewallInputSet()

    def _make_result_set(self, result, path):
        return InsertFirewallResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InsertFirewallChoreographyExecution(session, exec_id, path)

class InsertFirewallInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the InsertFirewall
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FirewallResource(self, value):
        """
        Set the value of the FirewallResource input for this Choreo. ((optional, json) A JSON string containing the firewall resource properties to set. This can be used as an alternative to individual inputs representing firewall properties.)
        """
        InputSet._set_input(self, 'FirewallResource', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_AllowedIPProtocol(self, value):
        """
        Set the value of the AllowedIPProtocol input for this Choreo. ((conditional, json) The IP protocol that is allowed for this rule. This is an array and can have the following properties: IPProtocol (valid values are: tcp, udp, or icmp) and ports[].)
        """
        InputSet._set_input(self, 'AllowedIPProtocol', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description of the firewall.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((conditional, string) The name of the firewall resource being created.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_Network(self, value):
        """
        Set the value of the Network input for this Choreo. ((conditional, string) The fully-qualified URL of the network to which this firewall is applied.)
        """
        InputSet._set_input(self, 'Network', value)
    def set_Project(self, value):
        """
        Set the value of the Project input for this Choreo. ((required, string) The ID of a Google Compute project.)
        """
        InputSet._set_input(self, 'Project', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_SourceRanges(self, value):
        """
        Set the value of the SourceRanges input for this Choreo. ((conditional, json) An array of address blocks that this rule applies to. This is required if the SourceTags input is not provided.)
        """
        InputSet._set_input(self, 'SourceRanges', value)
    def set_SourceTags(self, value):
        """
        Set the value of the SourceTags input for this Choreo. ((conditional, json) An array of instance tags which this rule applies to. This is required unless the SourceRanges input is provided.)
        """
        InputSet._set_input(self, 'SourceTags', value)

class InsertFirewallResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the InsertFirewall Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)

class InsertFirewallChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return InsertFirewallResultSet(response, path)
