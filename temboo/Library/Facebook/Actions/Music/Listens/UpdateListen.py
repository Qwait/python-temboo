# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateListen
# Updates and existing listen action.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateListen(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateListen Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Actions/Music/Listens/UpdateListen')


    def new_input_set(self):
        return UpdateListenInputSet()

    def _make_result_set(self, result, path):
        return UpdateListenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateListenChoreographyExecution(session, exec_id, path)

class UpdateListenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateListen
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ActionID(self, value):
        """
        Set the value of the ActionID input for this Choreo. ((required, string) The id of the action to update.)
        """
        InputSet._set_input(self, 'ActionID', value)
    def set_Album(self, value):
        """
        Set the value of the Album input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing  representing an album.)
        """
        InputSet._set_input(self, 'Album', value)
    def set_EndTime(self, value):
        """
        Set the value of the EndTime input for this Choreo. ((optional, date) The time that the user ended the action (e.g. 2013-06-24T18:53:35+0000).)
        """
        InputSet._set_input(self, 'EndTime', value)
    def set_ExpiresIn(self, value):
        """
        Set the value of the ExpiresIn input for this Choreo. ((optional, integer) The amount of time (in milliseconds) from the publish_time that the action will expire.)
        """
        InputSet._set_input(self, 'ExpiresIn', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message attached to this fitness action. Setting this parameter requires enabling of message capabilities.)
        """
        InputSet._set_input(self, 'Message', value)
    def set_Musician(self, value):
        """
        Set the value of the Musician input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing representing a musician.)
        """
        InputSet._set_input(self, 'Musician', value)
    def set_Paused(self, value):
        """
        Set the value of the Paused input for this Choreo. ((optional, boolean) Whether the audio is paused or not)
        """
        InputSet._set_input(self, 'Paused', value)
    def set_Place(self, value):
        """
        Set the value of the Place input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing the location associated with this action.)
        """
        InputSet._set_input(self, 'Place', value)
    def set_Playlist(self, value):
        """
        Set the value of the Playlist input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing representing a playlist.)
        """
        InputSet._set_input(self, 'Playlist', value)
    def set_RadioStation(self, value):
        """
        Set the value of the RadioStation input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing  representing a radio station.)
        """
        InputSet._set_input(self, 'RadioStation', value)
    def set_Song(self, value):
        """
        Set the value of the Song input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing  representing a song.)
        """
        InputSet._set_input(self, 'Song', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) A comma separated list of other profile IDs that also performed this action.)
        """
        InputSet._set_input(self, 'Tags', value)
    def set_ViaUser(self, value):
        """
        Set the value of the ViaUser input for this Choreo. ((optional, integer) The ID of anyone whom the user discovered this audio from)
        """
        InputSet._set_input(self, 'ViaUser', value)

class UpdateListenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateListen Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class UpdateListenChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateListenResultSet(response, path)
