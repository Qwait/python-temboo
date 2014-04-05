# -*- coding: utf-8 -*-

###############################################################################
#
# GetSellerTransactions
# Retrieves order line item (transaction) information for the authenticated user only.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetSellerTransactions(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetSellerTransactions Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/eBay/Trading/GetSellerTransactions')


    def new_input_set(self):
        return GetSellerTransactionsInputSet()

    def _make_result_set(self, result, path):
        return GetSellerTransactionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSellerTransactionsChoreographyExecution(session, exec_id, path)

class GetSellerTransactionsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetSellerTransactions
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DetailLevel(self, value):
        """
        Set the value of the DetailLevel input for this Choreo. ((optional, string) The detail level of the response. Valid values are: ItemReturnDescription and ReturnAll.)
        """
        InputSet._set_input(self, 'DetailLevel', value)
    def set_EntriesPerPage(self, value):
        """
        Set the value of the EntriesPerPage input for this Choreo. ((optional, integer) The maximum number of records to return in the result.)
        """
        InputSet._set_input(self, 'EntriesPerPage', value)
    def set_IncludeCodiceFiscale(self, value):
        """
        Set the value of the IncludeCodiceFiscale input for this Choreo. ((optional, string) When set to 'true', the buyer's Codice Fiscale number is returned in the response.)
        """
        InputSet._set_input(self, 'IncludeCodiceFiscale', value)
    def set_IncludeContainingOrder(self, value):
        """
        Set the value of the IncludeContainingOrder input for this Choreo. ((optional, boolean) When set to true, the ContainingOrder container is returned in the response for each transaction node.)
        """
        InputSet._set_input(self, 'IncludeContainingOrder', value)
    def set_IncludeFinalValueFee(self, value):
        """
        Set the value of the IncludeFinalValueFee input for this Choreo. ((optional, boolean) When set to true, the Final Value Fee (FVF) for all order line items is returned in the response.)
        """
        InputSet._set_input(self, 'IncludeFinalValueFee', value)
    def set_InventoryTrackingMethod(self, value):
        """
        Set the value of the InventoryTrackingMethod input for this Choreo. ((optional, boolean) Filters the response to only include order line items for listings that match this InventoryTrackingMethod setting. Valid values are: ItemID and SKU.)
        """
        InputSet._set_input(self, 'InventoryTrackingMethod', value)
    def set_ModTimeFrom(self, value):
        """
        Set the value of the ModTimeFrom input for this Choreo. ((optional, date) Used to filter by date range (e.g., 2013-02-08T00:00:00.000Z).)
        """
        InputSet._set_input(self, 'ModTimeFrom', value)
    def set_ModTimeTo(self, value):
        """
        Set the value of the ModTimeTo input for this Choreo. ((optional, date) Used to filter by date range (e.g., 2013-02-08T00:00:00.000Z).)
        """
        InputSet._set_input(self, 'ModTimeTo', value)
    def set_NumberOfDays(self, value):
        """
        Set the value of the NumberOfDays input for this Choreo. ((optional, integer) The number of days in the past to search for order line items.)
        """
        InputSet._set_input(self, 'NumberOfDays', value)
    def set_PageNumber(self, value):
        """
        Set the value of the PageNumber input for this Choreo. ((optional, integer) Specifies the page number of the results to return.)
        """
        InputSet._set_input(self, 'PageNumber', value)
    def set_Platform(self, value):
        """
        Set the value of the Platform input for this Choreo. ((optional, string) The name of the eBay co-branded site upon which the order line item was created. Valid values are: eBay, Express, Half, Shopping, or WorldOfGood.)
        """
        InputSet._set_input(self, 'Platform', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SKU(self, value):
        """
        Set the value of the SKU input for this Choreo. ((optional, string) One or more seller SKUs to filter the result. Multiple SKUs can be provided in a comma-separated list.)
        """
        InputSet._set_input(self, 'SKU', value)
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

class GetSellerTransactionsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetSellerTransactions Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetSellerTransactionsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetSellerTransactionsResultSet(response, path)
