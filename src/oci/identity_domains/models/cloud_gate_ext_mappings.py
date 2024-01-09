# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudGateExtMappings(object):
    """
    A list of Cloud Gate Mappings that map Apps to this Cloud Gate
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CloudGateExtMappings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mapping_id:
            The value to assign to the mapping_id property of this CloudGateExtMappings.
        :type mapping_id: str

        :param resource_prefix:
            The value to assign to the resource_prefix property of this CloudGateExtMappings.
        :type resource_prefix: str

        :param proxy_pass:
            The value to assign to the proxy_pass property of this CloudGateExtMappings.
        :type proxy_pass: str

        :param server_id:
            The value to assign to the server_id property of this CloudGateExtMappings.
        :type server_id: str

        :param nginx_settings:
            The value to assign to the nginx_settings property of this CloudGateExtMappings.
        :type nginx_settings: str

        :param app_id:
            The value to assign to the app_id property of this CloudGateExtMappings.
        :type app_id: str

        :param value:
            The value to assign to the value property of this CloudGateExtMappings.
        :type value: str

        :param name:
            The value to assign to the name property of this CloudGateExtMappings.
        :type name: str

        :param ref:
            The value to assign to the ref property of this CloudGateExtMappings.
        :type ref: str

        :param policy_name:
            The value to assign to the policy_name property of this CloudGateExtMappings.
        :type policy_name: str

        :param upstream_server_group_id:
            The value to assign to the upstream_server_group_id property of this CloudGateExtMappings.
        :type upstream_server_group_id: str

        """
        self.swagger_types = {
            'mapping_id': 'str',
            'resource_prefix': 'str',
            'proxy_pass': 'str',
            'server_id': 'str',
            'nginx_settings': 'str',
            'app_id': 'str',
            'value': 'str',
            'name': 'str',
            'ref': 'str',
            'policy_name': 'str',
            'upstream_server_group_id': 'str'
        }

        self.attribute_map = {
            'mapping_id': 'mappingId',
            'resource_prefix': 'resourcePrefix',
            'proxy_pass': 'proxyPass',
            'server_id': 'serverId',
            'nginx_settings': 'nginxSettings',
            'app_id': 'appId',
            'value': 'value',
            'name': 'name',
            'ref': '$ref',
            'policy_name': 'policyName',
            'upstream_server_group_id': 'upstreamServerGroupId'
        }

        self._mapping_id = None
        self._resource_prefix = None
        self._proxy_pass = None
        self._server_id = None
        self._nginx_settings = None
        self._app_id = None
        self._value = None
        self._name = None
        self._ref = None
        self._policy_name = None
        self._upstream_server_group_id = None

    @property
    def mapping_id(self):
        """
        Gets the mapping_id of this CloudGateExtMappings.
        The id of the Cloud Gate Mapping

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The mapping_id of this CloudGateExtMappings.
        :rtype: str
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        """
        Sets the mapping_id of this CloudGateExtMappings.
        The id of the Cloud Gate Mapping

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param mapping_id: The mapping_id of this CloudGateExtMappings.
        :type: str
        """
        self._mapping_id = mapping_id

    @property
    def resource_prefix(self):
        """
        **[Required]** Gets the resource_prefix of this CloudGateExtMappings.
        Resource prefix for this mapping.  This will be used to define the location block

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The resource_prefix of this CloudGateExtMappings.
        :rtype: str
        """
        return self._resource_prefix

    @resource_prefix.setter
    def resource_prefix(self, resource_prefix):
        """
        Sets the resource_prefix of this CloudGateExtMappings.
        Resource prefix for this mapping.  This will be used to define the location block

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param resource_prefix: The resource_prefix of this CloudGateExtMappings.
        :type: str
        """
        self._resource_prefix = resource_prefix

    @property
    def proxy_pass(self):
        """
        Gets the proxy_pass of this CloudGateExtMappings.
        NGINX ProxyPass entry for this Mapping

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The proxy_pass of this CloudGateExtMappings.
        :rtype: str
        """
        return self._proxy_pass

    @proxy_pass.setter
    def proxy_pass(self, proxy_pass):
        """
        Sets the proxy_pass of this CloudGateExtMappings.
        NGINX ProxyPass entry for this Mapping

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param proxy_pass: The proxy_pass of this CloudGateExtMappings.
        :type: str
        """
        self._proxy_pass = proxy_pass

    @property
    def server_id(self):
        """
        **[Required]** Gets the server_id of this CloudGateExtMappings.
        Server Instance for the Mapping. This is one of the server IDs(server blocks) from the associated Cloud Gate list

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The server_id of this CloudGateExtMappings.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """
        Sets the server_id of this CloudGateExtMappings.
        Server Instance for the Mapping. This is one of the server IDs(server blocks) from the associated Cloud Gate list

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param server_id: The server_id of this CloudGateExtMappings.
        :type: str
        """
        self._server_id = server_id

    @property
    def nginx_settings(self):
        """
        Gets the nginx_settings of this CloudGateExtMappings.
        More NGINX Settings. JSON encoded key value pairs similar to WTP encoding

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The nginx_settings of this CloudGateExtMappings.
        :rtype: str
        """
        return self._nginx_settings

    @nginx_settings.setter
    def nginx_settings(self, nginx_settings):
        """
        Sets the nginx_settings of this CloudGateExtMappings.
        More NGINX Settings. JSON encoded key value pairs similar to WTP encoding

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param nginx_settings: The nginx_settings of this CloudGateExtMappings.
        :type: str
        """
        self._nginx_settings = nginx_settings

    @property
    def app_id(self):
        """
        Gets the app_id of this CloudGateExtMappings.
        The ID of the App being mapped to

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The app_id of this CloudGateExtMappings.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """
        Sets the app_id of this CloudGateExtMappings.
        The ID of the App being mapped to

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param app_id: The app_id of this CloudGateExtMappings.
        :type: str
        """
        self._app_id = app_id

    @property
    def value(self):
        """
        Gets the value of this CloudGateExtMappings.
        The id of the App being mapped to

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this CloudGateExtMappings.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CloudGateExtMappings.
        The id of the App being mapped to

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this CloudGateExtMappings.
        :type: str
        """
        self._value = value

    @property
    def name(self):
        """
        Gets the name of this CloudGateExtMappings.
        The name (Client ID) of the App being mapped to

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The name of this CloudGateExtMappings.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CloudGateExtMappings.
        The name (Client ID) of the App being mapped to

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param name: The name of this CloudGateExtMappings.
        :type: str
        """
        self._name = name

    @property
    def ref(self):
        """
        Gets the ref of this CloudGateExtMappings.
        URI of the App being mapped to

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this CloudGateExtMappings.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this CloudGateExtMappings.
        URI of the App being mapped to

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this CloudGateExtMappings.
        :type: str
        """
        self._ref = ref

    @property
    def policy_name(self):
        """
        Gets the policy_name of this CloudGateExtMappings.
        The Web Tier policy name used for the App that is mapped to this Cloud Gate

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The policy_name of this CloudGateExtMappings.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """
        Sets the policy_name of this CloudGateExtMappings.
        The Web Tier policy name used for the App that is mapped to this Cloud Gate

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param policy_name: The policy_name of this CloudGateExtMappings.
        :type: str
        """
        self._policy_name = policy_name

    @property
    def upstream_server_group_id(self):
        """
        Gets the upstream_server_group_id of this CloudGateExtMappings.
        Upstream server group instance for the Mapping. This is one of the upstream server group IDs(upstream blocks) from the associated Cloud Gate list

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The upstream_server_group_id of this CloudGateExtMappings.
        :rtype: str
        """
        return self._upstream_server_group_id

    @upstream_server_group_id.setter
    def upstream_server_group_id(self, upstream_server_group_id):
        """
        Sets the upstream_server_group_id of this CloudGateExtMappings.
        Upstream server group instance for the Mapping. This is one of the upstream server group IDs(upstream blocks) from the associated Cloud Gate list

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param upstream_server_group_id: The upstream_server_group_id of this CloudGateExtMappings.
        :type: str
        """
        self._upstream_server_group_id = upstream_server_group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
