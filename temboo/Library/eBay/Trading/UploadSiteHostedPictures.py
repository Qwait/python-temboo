# -*- coding: utf-8 -*-

###############################################################################
#
# UploadSiteHostedPictures
# Allows you to uploads a picture to eBay Picture Services by specifying a binary attachment or image URL.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UploadSiteHostedPictures(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UploadSiteHostedPictures Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/eBay/Trading/UploadSiteHostedPictures')


    def new_input_set(self):
        return UploadSiteHostedPicturesInputSet()

    def _make_result_set(self, result, path):
        return UploadSiteHostedPicturesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadSiteHostedPicturesChoreographyExecution(session, exec_id, path)

class UploadSiteHostedPicturesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UploadSiteHostedPictures
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ExtensionInDays(self, value):
        """
        Set the value of the ExtensionInDays input for this Choreo. ((optional, integer) The number of days to extend the expiration date for the specified image, after a listing has ended.)
        """
        InputSet._set_input(self, 'ExtensionInDays', value)
    def set_ExternalPictureURL(self, value):
        """
        Set the value of the ExternalPictureURL input for this Choreo. ((conditional, string) The URL of an image to upload. Required unless providing PictureData. Max image size is 7 MB. Max URL length is 1024. Formats supported are: JPG, GIF, PNG, BMP, and TIF.)
        """
        InputSet._set_input(self, 'ExternalPictureURL', value)
    def set_PictureData(self, value):
        """
        Set the value of the PictureData input for this Choreo. ((conditional, string) The Base64 encoded string for an the image data. Required unless providing the ExternalPictureURL. Max image size is 7 MB. Formats supported are: JPG, GIF, PNG, BMP, and TIF.)
        """
        InputSet._set_input(self, 'PictureData', value)
    def set_PictureName(self, value):
        """
        Set the value of the PictureName input for this Choreo. ((optional, string) The name of the picture.)
        """
        InputSet._set_input(self, 'PictureName', value)
    def set_PictureSet(self, value):
        """
        Set the value of the PictureSet input for this Choreo. ((optional, string) The image sizes that will be generated. Valid values are: Standard and Supersize.)
        """
        InputSet._set_input(self, 'PictureSet', value)
    def set_PictureUploadPolicy(self, value):
        """
        Set the value of the PictureUploadPolicy input for this Choreo. ((optional, string) Indicates that an uploaded picture is available to a seller on the eBay site. Valid values are: Add and ClearAndAdd.)
        """
        InputSet._set_input(self, 'PictureUploadPolicy', value)
    def set_PictureWatermark(self, value):
        """
        Set the value of the PictureWatermark input for this Choreo. ((optional, string) The type of watermark that should be applied to the pictures hosted by the eBay Picture Services. Valid values are: User and Icon.)
        """
        InputSet._set_input(self, 'PictureWatermark', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((optional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        InputSet._set_input(self, 'SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        InputSet._set_input(self, 'SiteID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        InputSet._set_input(self, 'UserToken', value)

class UploadSiteHostedPicturesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UploadSiteHostedPictures Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class UploadSiteHostedPicturesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadSiteHostedPicturesResultSet(response, path)
