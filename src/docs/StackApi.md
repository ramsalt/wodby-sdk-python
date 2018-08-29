# wodby_sdk.StackApi

All URIs are relative to *https://api.wodby.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stack**](StackApi.md#get_stack) | **GET** /stacks/{id} | 
[**get_stacks**](StackApi.md#get_stacks) | **GET** /stacks | 


# **get_stack**
> Stack get_stack(id)



Retrieve stack

### Example
```python
from __future__ import print_function
import time
import wodby_sdk
from wodby_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = wodby_sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = wodby_sdk.StackApi(wodby_sdk.ApiClient(configuration))
id = 'id_example' # str | Stack ID

try:
    api_response = api_instance.get_stack(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackApi->get_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Stack ID | 

### Return type

[**Stack**](Stack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stacks**
> list[Stack] get_stacks(id=id)



Retrieve stacks

### Example
```python
from __future__ import print_function
import time
import wodby_sdk
from wodby_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = wodby_sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = wodby_sdk.StackApi(wodby_sdk.ApiClient(configuration))
id = 'id_example' # str | Organization ID (optional)

try:
    api_response = api_instance.get_stacks(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackApi->get_stacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization ID | [optional] 

### Return type

[**list[Stack]**](Stack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
