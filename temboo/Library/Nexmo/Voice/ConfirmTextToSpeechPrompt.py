# -*- coding: utf-8 -*-

###############################################################################
#
# ConfirmTextToSpeechPrompt
# Sends a Text-to-Speech message to the specifed Number and confirms the specifed pin-code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ConfirmTextToSpeechPrompt(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ConfirmTextToSpeechPrompt Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Nexmo/Voice/ConfirmTextToSpeechPrompt')


    def new_input_set(self):
        return ConfirmTextToSpeechPromptInputSet()

    def _make_result_set(self, result, path):
        return ConfirmTextToSpeechPromptResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ConfirmTextToSpeechPromptChoreographyExecution(session, exec_id, path)

class ConfirmTextToSpeechPromptInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ConfirmTextToSpeechPrompt
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
    def set_ByeText(self, value):
        """
        Set the value of the ByeText input for this Choreo. ((required, string) Body of the text message played after digits are entered. (with a maximum length of 500 characters),)
        """
        InputSet._set_input(self, 'ByeText', value)
    def set_CallbackURL(self, value):
        """
        Set the value of the CallbackURL input for this Choreo. ((required, string) A URL that Nexmo will request when the call ends to notify your application.)
        """
        InputSet._set_input(self, 'CallbackURL', value)
    def set_DropIfMachine(self, value):
        """
        Set the value of the DropIfMachine input for this Choreo. ((optional, integer) Set to 1 to drop the call if a machine is detected.)
        """
        InputSet._set_input(self, 'DropIfMachine', value)
    def set_FailedText(self, value):
        """
        Set the value of the FailedText input for this Choreo. ((required, string) Body of the text message played after 3 failed attempts. (with a maximum length of 500 characters),)
        """
        InputSet._set_input(self, 'FailedText', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) The language used to play back your message.  The default is "en-us" which corresponds to United States english.)
        """
        InputSet._set_input(self, 'Language', value)
    def set_MaxDigits(self, value):
        """
        Set the value of the MaxDigits input for this Choreo. ((required, integer) Number of digits entered by the end user.)
        """
        InputSet._set_input(self, 'MaxDigits', value)
    def set_PinCode(self, value):
        """
        Set the value of the PinCode input for this Choreo. ((required, string) Pin-code to be entered by end user (Pin-code length should be equals to MaxDigits).)
        """
        InputSet._set_input(self, 'PinCode', value)
    def set_Repeat(self, value):
        """
        Set the value of the Repeat input for this Choreo. ((optional, integer) Define how many times you want to repeat the text message (default is 1 , maximum is 10).)
        """
        InputSet._set_input(self, 'Repeat', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((conditional, string) Body of the text message (with a maximum length of 1000 characters).)
        """
        InputSet._set_input(self, 'Text', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) Phone number in international format and one recipient per request. (e.g. 447525856424 when sending to UK))
        """
        InputSet._set_input(self, 'To', value)
    def set_Voice(self, value):
        """
        Set the value of the Voice input for this Choreo. ((optional, string) The voice to be used female (default) or male.)
        """
        InputSet._set_input(self, 'Voice', value)

class ConfirmTextToSpeechPromptResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ConfirmTextToSpeechPrompt Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class ConfirmTextToSpeechPromptChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ConfirmTextToSpeechPromptResultSet(response, path)
