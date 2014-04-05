# -*- coding: utf-8 -*-

###############################################################################
#
# CompleteSale
# Allows the seller to perform the final steps for completing an order.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CompleteSale(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CompleteSale Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/eBay/Trading/CompleteSale')


    def new_input_set(self):
        return CompleteSaleInputSet()

    def _make_result_set(self, result, path):
        return CompleteSaleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompleteSaleChoreographyExecution(session, exec_id, path)

class CompleteSaleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CompleteSale
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CompleteSaleRequest(self, value):
        """
        Set the value of the CompleteSaleRequest input for this Choreo. ((optional, xml) The complete XML request body containing properties you wish to set. This can be used as an alternative to individual inputs that represent request properties.)
        """
        InputSet._set_input(self, 'CompleteSaleRequest', value)
    def set_CommentText(self, value):
        """
        Set the value of the CommentText input for this Choreo. ((optional, string) The comment text to leave Feedback about the buyer.)
        """
        InputSet._set_input(self, 'CommentText', value)
    def set_CommentType(self, value):
        """
        Set the value of the CommentType input for this Choreo. ((optional, string) The type of comment. Valid values are: Positive.)
        """
        InputSet._set_input(self, 'CommentType', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((conditional, string) The unique identifier for an eBay item listing that was sold. Either ItemID or TransactionID should be provided.)
        """
        InputSet._set_input(self, 'ItemID', value)
    def set_Notes(self, value):
        """
        Set the value of the Notes input for this Choreo. ((optional, string) A text field for shipping related notes.)
        """
        InputSet._set_input(self, 'Notes', value)
    def set_OrderID(self, value):
        """
        Set the value of the OrderID input for this Choreo. ((optional, string) A unique identifier that identifies a single line item or multiple line item order.)
        """
        InputSet._set_input(self, 'OrderID', value)
    def set_OrderLineItemID(self, value):
        """
        Set the value of the OrderLineItemID input for this Choreo. ((optional, string) This is a unique identifier for an eBay order line item and is based upon the concatenation of ItemID and TransactionID, with a hyphen in between these two IDs.)
        """
        InputSet._set_input(self, 'OrderLineItemID', value)
    def set_Paid(self, value):
        """
        Set the value of the Paid input for this Choreo. ((conditional, boolean) Set to true to indicate that the item has been paid for. One of Feedback info, Shipped status or Paid status is required.)
        """
        InputSet._set_input(self, 'Paid', value)
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
    def set_ShipmentTrackingNumber(self, value):
        """
        Set the value of the ShipmentTrackingNumber input for this Choreo. ((optional, string) The tracking number for the package.)
        """
        InputSet._set_input(self, 'ShipmentTrackingNumber', value)
    def set_ShippedTime(self, value):
        """
        Set the value of the ShippedTime input for this Choreo. ((optional, date) The date and time that the item was shipped.)
        """
        InputSet._set_input(self, 'ShippedTime', value)
    def set_Shipped(self, value):
        """
        Set the value of the Shipped input for this Choreo. ((conditional, boolean) Set to true to indicate that the item has been shipped. One of Feedback info, Shipped status or Paid status is required.)
        """
        InputSet._set_input(self, 'Shipped', value)
    def set_ShippingCarrierUsed(self, value):
        """
        Set the value of the ShippingCarrierUsed input for this Choreo. ((optional, string) The carrier used to ship the item.)
        """
        InputSet._set_input(self, 'ShippingCarrierUsed', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        InputSet._set_input(self, 'SiteID', value)
    def set_TargetUser(self, value):
        """
        Set the value of the TargetUser input for this Choreo. ((optional, string) The user ID of the buyer who you want to leave feedback for.)
        """
        InputSet._set_input(self, 'TargetUser', value)
    def set_TransactionID(self, value):
        """
        Set the value of the TransactionID input for this Choreo. ((conditional, string) The unique identifier for an eBay order line item (transaction). Either ItemID or TransactionID should be provided.)
        """
        InputSet._set_input(self, 'TransactionID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        InputSet._set_input(self, 'UserToken', value)

class CompleteSaleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CompleteSale Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class CompleteSaleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CompleteSaleResultSet(response, path)
