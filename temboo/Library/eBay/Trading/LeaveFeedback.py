# -*- coding: utf-8 -*-

###############################################################################
#
# LeaveFeedback
# Enables a buyer and seller to leave feedback for their order partner at the conclusion of a successful order.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class LeaveFeedback(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LeaveFeedback Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/eBay/Trading/LeaveFeedback')


    def new_input_set(self):
        return LeaveFeedbackInputSet()

    def _make_result_set(self, result, path):
        return LeaveFeedbackResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LeaveFeedbackChoreographyExecution(session, exec_id, path)

class LeaveFeedbackInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LeaveFeedback
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_LeaveFeedbackRequest(self, value):
        """
        Set the value of the LeaveFeedbackRequest input for this Choreo. ((optional, xml) The complete XML request body containing properties you wish to set. This can be used as an alternative to individual inputs that represent request properties.)
        """
        InputSet._set_input(self, 'LeaveFeedbackRequest', value)
    def set_CommentText(self, value):
        """
        Set the value of the CommentText input for this Choreo. ((conditional, string) The comment text to leave Feedback about the buyer.)
        """
        InputSet._set_input(self, 'CommentText', value)
    def set_CommentType(self, value):
        """
        Set the value of the CommentType input for this Choreo. ((conditional, string) The type of comment. Valid values are: Positive, Negative, and Neutral.)
        """
        InputSet._set_input(self, 'CommentType', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((conditional, string) The unique identifier for an eBay item listing that was sold. Required unless OrderLineItemID is specified.)
        """
        InputSet._set_input(self, 'ItemID', value)
    def set_OrderLineItemID(self, value):
        """
        Set the value of the OrderLineItemID input for this Choreo. ((optional, string) This is a unique identifier for an eBay order line item and is based upon the concatenation of ItemID and TransactionID, with a hyphen in between these two IDs.)
        """
        InputSet._set_input(self, 'OrderLineItemID', value)
    def set_RatingDetail(self, value):
        """
        Set the value of the RatingDetail input for this Choreo. ((conditional, string) The subject that is being rated. Valid values are: Communication, ItemAsDescribed, ShippingAndHandlingCharges, and ShippingTime.)
        """
        InputSet._set_input(self, 'RatingDetail', value)
    def set_Rating(self, value):
        """
        Set the value of the Rating input for this Choreo. ((conditional, integer) A detailed numeric rating (1 through 5) for an order line item. This rating is applied to the subject provided for RatingDetail.)
        """
        InputSet._set_input(self, 'Rating', value)
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
    def set_TargetUser(self, value):
        """
        Set the value of the TargetUser input for this Choreo. ((conditional, string) The user ID of the buyer who you want to leave feedback for.)
        """
        InputSet._set_input(self, 'TargetUser', value)
    def set_TransactionID(self, value):
        """
        Set the value of the TransactionID input for this Choreo. ((optional, string) The unique identifier for an eBay order line item (transaction). Required when there are multiple order ine items between the two order partners that require feedback.)
        """
        InputSet._set_input(self, 'TransactionID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        InputSet._set_input(self, 'UserToken', value)

class LeaveFeedbackResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LeaveFeedback Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class LeaveFeedbackChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LeaveFeedbackResultSet(response, path)
