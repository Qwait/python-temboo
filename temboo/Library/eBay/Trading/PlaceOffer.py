# -*- coding: utf-8 -*-

###############################################################################
#
# PlaceOffer
# Allows an authenticated user to to make a bid, a best offer, or a purchase on the item specified by the ItemID input field.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PlaceOffer(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PlaceOffer Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/eBay/Trading/PlaceOffer')


    def new_input_set(self):
        return PlaceOfferInputSet()

    def _make_result_set(self, result, path):
        return PlaceOfferResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PlaceOfferChoreographyExecution(session, exec_id, path)

class PlaceOfferInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PlaceOffer
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_PlaceOfferRequest(self, value):
        """
        Set the value of the PlaceOfferRequest input for this Choreo. ((optional, xml) The complete XML request body containing properties you wish to set. This can be used as an alternative to individual inputs that represent request properties.)
        """
        InputSet._set_input(self, 'PlaceOfferRequest', value)
    def set_Action(self, value):
        """
        Set the value of the Action input for this Choreo. ((conditional, string) Indicates the type of offer being made on the specified listing. Valid values are: Bid, Purchase, Accept, Counter, Decline, or Offer.)
        """
        InputSet._set_input(self, 'Action', value)
    def set_BestOfferID(self, value):
        """
        Set the value of the BestOfferID input for this Choreo. ((conditional, string) The ID of a Best Offer on an item. Required if Action is set to Accept or Decline.)
        """
        InputSet._set_input(self, 'BestOfferID', value)
    def set_DetailLevel(self, value):
        """
        Set the value of the DetailLevel input for this Choreo. ((optional, string) The response detail level. Valid values are: ItemReturnAttributes, ItemReturnDescription, and ReturnAll.)
        """
        InputSet._set_input(self, 'DetailLevel', value)
    def set_EndUserIP(self, value):
        """
        Set the value of the EndUserIP input for this Choreo. ((conditional, string) The public IP address of the machine from which the request is sent.)
        """
        InputSet._set_input(self, 'EndUserIP', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((conditional, string) The ItemID that uniquely identifies the item listing to bid on.)
        """
        InputSet._set_input(self, 'ItemID', value)
    def set_MaxBid(self, value):
        """
        Set the value of the MaxBid input for this Choreo. ((conditional, decimal) The amount of the offer placed on the listing.)
        """
        InputSet._set_input(self, 'MaxBid', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((conditional, string) A message from the buyer to the seller.)
        """
        InputSet._set_input(self, 'Message', value)
    def set_Quantity(self, value):
        """
        Set the value of the Quantity input for this Choreo. ((conditional, integer) Specifies the number of items from the specified listing that the user intends to purchase. For auctions, this must be set to 1.)
        """
        InputSet._set_input(self, 'Quantity', value)
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
    def set_UserConsent(self, value):
        """
        Set the value of the UserConsent input for this Choreo. ((conditional, boolean) When set to true, confirms that the bidder read and agrees to eBay's privacy policy.)
        """
        InputSet._set_input(self, 'UserConsent', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        InputSet._set_input(self, 'UserToken', value)

class PlaceOfferResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PlaceOffer Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class PlaceOfferChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PlaceOfferResultSet(response, path)
