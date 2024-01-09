# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogListEndpoint(object):
    """
    An endpoint used to fetch a list of log URLs.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogListEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this LogListEndpoint.
        :type name: str

        :param description:
            The value to assign to the description property of this LogListEndpoint.
        :type description: str

        :param model:
            The value to assign to the model property of this LogListEndpoint.
        :type model: str

        :param endpoint_id:
            The value to assign to the endpoint_id property of this LogListEndpoint.
        :type endpoint_id: int

        :param request:
            The value to assign to the request property of this LogListEndpoint.
        :type request: oci.log_analytics.models.EndpointRequest

        :param response:
            The value to assign to the response property of this LogListEndpoint.
        :type response: oci.log_analytics.models.EndpointResponse

        :param credentials:
            The value to assign to the credentials property of this LogListEndpoint.
        :type credentials: oci.log_analytics.models.EndpointCredentials

        :param proxy:
            The value to assign to the proxy property of this LogListEndpoint.
        :type proxy: oci.log_analytics.models.EndpointProxy

        :param is_enabled:
            The value to assign to the is_enabled property of this LogListEndpoint.
        :type is_enabled: bool

        :param is_system:
            The value to assign to the is_system property of this LogListEndpoint.
        :type is_system: bool

        :param endpoint_properties:
            The value to assign to the endpoint_properties property of this LogListEndpoint.
        :type endpoint_properties: list[oci.log_analytics.models.LogAnalyticsProperty]

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'model': 'str',
            'endpoint_id': 'int',
            'request': 'EndpointRequest',
            'response': 'EndpointResponse',
            'credentials': 'EndpointCredentials',
            'proxy': 'EndpointProxy',
            'is_enabled': 'bool',
            'is_system': 'bool',
            'endpoint_properties': 'list[LogAnalyticsProperty]'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'model': 'model',
            'endpoint_id': 'endpointId',
            'request': 'request',
            'response': 'response',
            'credentials': 'credentials',
            'proxy': 'proxy',
            'is_enabled': 'isEnabled',
            'is_system': 'isSystem',
            'endpoint_properties': 'endpointProperties'
        }

        self._name = None
        self._description = None
        self._model = None
        self._endpoint_id = None
        self._request = None
        self._response = None
        self._credentials = None
        self._proxy = None
        self._is_enabled = None
        self._is_system = None
        self._endpoint_properties = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this LogListEndpoint.
        The endpoint name.


        :return: The name of this LogListEndpoint.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogListEndpoint.
        The endpoint name.


        :param name: The name of this LogListEndpoint.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this LogListEndpoint.
        The endpoint description.


        :return: The description of this LogListEndpoint.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogListEndpoint.
        The endpoint description.


        :param description: The description of this LogListEndpoint.
        :type: str
        """
        self._description = description

    @property
    def model(self):
        """
        Gets the model of this LogListEndpoint.
        The endpoint model.


        :return: The model of this LogListEndpoint.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this LogListEndpoint.
        The endpoint model.


        :param model: The model of this LogListEndpoint.
        :type: str
        """
        self._model = model

    @property
    def endpoint_id(self):
        """
        Gets the endpoint_id of this LogListEndpoint.
        The endpoint unique identifier.


        :return: The endpoint_id of this LogListEndpoint.
        :rtype: int
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """
        Sets the endpoint_id of this LogListEndpoint.
        The endpoint unique identifier.


        :param endpoint_id: The endpoint_id of this LogListEndpoint.
        :type: int
        """
        self._endpoint_id = endpoint_id

    @property
    def request(self):
        """
        **[Required]** Gets the request of this LogListEndpoint.

        :return: The request of this LogListEndpoint.
        :rtype: oci.log_analytics.models.EndpointRequest
        """
        return self._request

    @request.setter
    def request(self, request):
        """
        Sets the request of this LogListEndpoint.

        :param request: The request of this LogListEndpoint.
        :type: oci.log_analytics.models.EndpointRequest
        """
        self._request = request

    @property
    def response(self):
        """
        Gets the response of this LogListEndpoint.

        :return: The response of this LogListEndpoint.
        :rtype: oci.log_analytics.models.EndpointResponse
        """
        return self._response

    @response.setter
    def response(self, response):
        """
        Sets the response of this LogListEndpoint.

        :param response: The response of this LogListEndpoint.
        :type: oci.log_analytics.models.EndpointResponse
        """
        self._response = response

    @property
    def credentials(self):
        """
        Gets the credentials of this LogListEndpoint.

        :return: The credentials of this LogListEndpoint.
        :rtype: oci.log_analytics.models.EndpointCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this LogListEndpoint.

        :param credentials: The credentials of this LogListEndpoint.
        :type: oci.log_analytics.models.EndpointCredentials
        """
        self._credentials = credentials

    @property
    def proxy(self):
        """
        Gets the proxy of this LogListEndpoint.

        :return: The proxy of this LogListEndpoint.
        :rtype: oci.log_analytics.models.EndpointProxy
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """
        Sets the proxy of this LogListEndpoint.

        :param proxy: The proxy of this LogListEndpoint.
        :type: oci.log_analytics.models.EndpointProxy
        """
        self._proxy = proxy

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this LogListEndpoint.
        A flag indicating whether or not the endpoint is enabled for log collection.


        :return: The is_enabled of this LogListEndpoint.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this LogListEndpoint.
        A flag indicating whether or not the endpoint is enabled for log collection.


        :param is_enabled: The is_enabled of this LogListEndpoint.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def is_system(self):
        """
        Gets the is_system of this LogListEndpoint.
        The system flag. A value of false denotes a custom, or user
        defined endpoint. A value of true denotes an Oracle defined endpoint.


        :return: The is_system of this LogListEndpoint.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogListEndpoint.
        The system flag. A value of false denotes a custom, or user
        defined endpoint. A value of true denotes an Oracle defined endpoint.


        :param is_system: The is_system of this LogListEndpoint.
        :type: bool
        """
        self._is_system = is_system

    @property
    def endpoint_properties(self):
        """
        Gets the endpoint_properties of this LogListEndpoint.
        A list of endpoint properties.


        :return: The endpoint_properties of this LogListEndpoint.
        :rtype: list[oci.log_analytics.models.LogAnalyticsProperty]
        """
        return self._endpoint_properties

    @endpoint_properties.setter
    def endpoint_properties(self, endpoint_properties):
        """
        Sets the endpoint_properties of this LogListEndpoint.
        A list of endpoint properties.


        :param endpoint_properties: The endpoint_properties of this LogListEndpoint.
        :type: list[oci.log_analytics.models.LogAnalyticsProperty]
        """
        self._endpoint_properties = endpoint_properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
