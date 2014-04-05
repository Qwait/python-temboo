# -*- coding: utf-8 -*-

###############################################################################
#
# SendMessage
# Send a text message to any global number.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SendMessage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SendMessage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Nexmo/SMS/SendMessage')


    def new_input_set(self):
        return SendMessageInputSet()

    def _make_result_set(self, result, path):
        return SendMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendMessageChoreographyExecution(session, exec_id, path)

class SendMessageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SendMessage
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
    def set_Body(self, value):
        """
        Set the value of the Body input for this Choreo. ((optional, string) Hex encoded binary data. (e.g. 0011223344556677).  Required when Type is binary.)
        """
        InputSet._set_input(self, 'Body', value)
    def set_CallbackID(self, value):
        """
        Set the value of the CallbackID input for this Choreo. ((conditional, string) A unique identifier that is part of your Temboo callback URL registered at Nexmo. Required in order to listen for a reply. See Choreo description for details.)
        """
        InputSet._set_input(self, 'CallbackID', value)
    def set_ClientReference(self, value):
        """
        Set the value of the ClientReference input for this Choreo. ((optional, string) Include a note for your reference. (40 characters max).)
        """
        InputSet._set_input(self, 'ClientReference', value)
    def set_DeliveryReceipt(self, value):
        """
        Set the value of the DeliveryReceipt input for this Choreo. ((optional, integer) Set to 1 to receive a Delivery Receipt for this message. Make sure to configure your "Callback URL" in your "API Settings".)
        """
        InputSet._set_input(self, 'DeliveryReceipt', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((required, string) Sender address may be alphanumeric (e.g. MyCompany20). Restrictions may apply, depending on the destination.)
        """
        InputSet._set_input(self, 'From', value)
    def set_MessageClass(self, value):
        """
        Set the value of the MessageClass input for this Choreo. ((optional, integer) Set to 0 for Flash SMS.)
        """
        InputSet._set_input(self, 'MessageClass', value)
    def set_NetworkCode(self, value):
        """
        Set the value of the NetworkCode input for this Choreo. ((optional, string) Sends this message to the specifed network operator (MCCMNC).)
        """
        InputSet._set_input(self, 'NetworkCode', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_TTL(self, value):
        """
        Set the value of the TTL input for this Choreo. ((optional, integer) Message life span (Time to  live) in milliseconds.)
        """
        InputSet._set_input(self, 'TTL', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((conditional, string) Required when Type is "text".  Body of the text message (with a maximum length of 3200 characters).)
        """
        InputSet._set_input(self, 'Text', value)
    def set_Timeout(self, value):
        """
        Set the value of the Timeout input for this Choreo. ((conditional, integer) The amount of time (in minutes) to wait for a reply when a CallbackID is provided. Defaults to 10. See Choreo description for details.)
        """
        InputSet._set_input(self, 'Timeout', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) Mobile number in international format, and one recipient per request. (e.g. 447525856424 or 00447525856424 when sending to UK).)
        """
        InputSet._set_input(self, 'To', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) This can be omitted for text (default), but is required when sending a Binary (binary), WAP Push (wappush), Unicode message (unicode), VCal (vcal) or VCard (vcard).)
        """
        InputSet._set_input(self, 'Type', value)
    def set_UDH(self, value):
        """
        Set the value of the UDH input for this Choreo. ((optional, string) Hex encoded User data header. (e.g. 06050415811581) (Required when Type is binary).)
        """
        InputSet._set_input(self, 'UDH', value)
    def set_VCal(self, value):
        """
        Set the value of the VCal input for this Choreo. ((optional, string) Correctly formatted VCal text body.)
        """
        InputSet._set_input(self, 'VCal', value)
    def set_VCard(self, value):
        """
        Set the value of the VCard input for this Choreo. ((optional, string) Correctly formatted VCard text body.)
        """
        InputSet._set_input(self, 'VCard', value)

class SendMessageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SendMessage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_CallbackData(self):
        """
        Retrieve the value for the "CallbackData" output from this Choreo execution. (The Nexmo callback data retrieved after a user has replied to the SMS message. This is only returned if you've setup your Temboo callback URL at Nexmo, and  have provided the CallbackID input.)
        """
        return self._output.get('CallbackData', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class SendMessageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SendMessageResultSet(response, path)
