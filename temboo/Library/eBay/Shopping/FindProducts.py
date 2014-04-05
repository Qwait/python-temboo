# -*- coding: utf-8 -*-

###############################################################################
#
# FindProducts
# Retrieves the listings for products that match the specified keywords.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FindProducts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindProducts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/eBay/Shopping/FindProducts')


    def new_input_set(self):
        return FindProductsInputSet()

    def _make_result_set(self, result, path):
        return FindProductsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindProductsChoreographyExecution(session, exec_id, path)

class FindProductsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindProducts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The unique identifier for the application.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_AvailableItemsOnly(self, value):
        """
        Set the value of the AvailableItemsOnly input for this Choreo. ((optional, boolean) If set to true, only retrieve data for products that have been used to pre-fill active listings. If false, retrieve all products that match the query. Defaults to false.)
        """
        InputSet._set_input(self, 'AvailableItemsOnly', value)
    def set_CategoryID(self, value):
        """
        Set the value of the CategoryID input for this Choreo. ((conditional, string) Restricts your query to a specific category. The request requires one of the following filter parameters: QueryKeywords, ProductID, or CategoryID. Only one of the filters should be provided.)
        """
        InputSet._set_input(self, 'CategoryID', value)
    def set_DomainName(self, value):
        """
        Set the value of the DomainName input for this Choreo. ((optional, string) A domain to search in (e.g. Textbooks).)
        """
        InputSet._set_input(self, 'DomainName', value)
    def set_HideDuplicateItems(self, value):
        """
        Set the value of the HideDuplicateItems input for this Choreo. ((optional, string) Specifies whether or not to remove duplicate items from search results.)
        """
        InputSet._set_input(self, 'HideDuplicateItems', value)
    def set_IncludeSelector(self, value):
        """
        Set the value of the IncludeSelector input for this Choreo. ((optional, string) Defines standard subsets of fields to return within the response. Valid values are: Details, DomainHistogram, and Items.)
        """
        InputSet._set_input(self, 'IncludeSelector', value)
    def set_MaxEntries(self, value):
        """
        Set the value of the MaxEntries input for this Choreo. ((optional, integer) The maximum number of entries to return in the response.)
        """
        InputSet._set_input(self, 'MaxEntries', value)
    def set_PageNumber(self, value):
        """
        Set the value of the PageNumber input for this Choreo. ((optional, string) The page number to retrieve.)
        """
        InputSet._set_input(self, 'PageNumber', value)
    def set_ProductID(self, value):
        """
        Set the value of the ProductID input for this Choreo. ((conditional, string) Used to retrieve product details. The request requires one of the following filter parameters: QueryKeywords, ProductID, or CategoryID. Only one of the filters should be provided.)
        """
        InputSet._set_input(self, 'ProductID', value)
    def set_ProductSort(self, value):
        """
        Set the value of the ProductSort input for this Choreo. ((optional, string) Sorts the list of products returned. Valid values are: ItemCount, Popularity, Rating, ReviewCount, and Title.)
        """
        InputSet._set_input(self, 'ProductSort', value)
    def set_QueryKeywords(self, value):
        """
        Set the value of the QueryKeywords input for this Choreo. ((conditional, string) The query keywords to use for the product search. The request requires one of the following filter parameters: QueryKeywords, ProductID, or CategoryID. Only one of the filters should be provided.)
        """
        InputSet._set_input(self, 'QueryKeywords', value)
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
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Sorts search results in ascending or descending order. Valid values are: Ascending and Descending.)
        """
        InputSet._set_input(self, 'SortOrder', value)

class FindProductsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindProducts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class FindProductsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindProductsResultSet(response, path)
