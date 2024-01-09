# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppRoleApp(object):
    """
    A unique identifier for the application that references this role.

    **SCIM++ Properties:**
    - idcsSearchable: true
    - idcsCsvAttributeNameMappings: [[columnHeaderName:App Name, mapsTo:app.display]]
    - multiValued: false
    - mutability: immutable
    - required: true
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppRoleApp object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this AppRoleApp.
        :type value: str

        :param ref:
            The value to assign to the ref property of this AppRoleApp.
        :type ref: str

        :param display:
            The value to assign to the display property of this AppRoleApp.
        :type display: str

        :param name:
            The value to assign to the name property of this AppRoleApp.
        :type name: str

        :param service_instance_identifier:
            The value to assign to the service_instance_identifier property of this AppRoleApp.
        :type service_instance_identifier: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'display': 'str',
            'name': 'str',
            'service_instance_identifier': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'display': 'display',
            'name': 'name',
            'service_instance_identifier': 'serviceInstanceIdentifier'
        }

        self._value = None
        self._ref = None
        self._display = None
        self._name = None
        self._service_instance_identifier = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this AppRoleApp.
        App identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this AppRoleApp.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AppRoleApp.
        App identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this AppRoleApp.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this AppRoleApp.
        App URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this AppRoleApp.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this AppRoleApp.
        App URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this AppRoleApp.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this AppRoleApp.
        App display name

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The display of this AppRoleApp.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this AppRoleApp.
        App display name

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param display: The display of this AppRoleApp.
        :type: str
        """
        self._display = display

    @property
    def name(self):
        """
        Gets the name of this AppRoleApp.
        Application name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The name of this AppRoleApp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AppRoleApp.
        Application name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param name: The name of this AppRoleApp.
        :type: str
        """
        self._name = name

    @property
    def service_instance_identifier(self):
        """
        Gets the service_instance_identifier of this AppRoleApp.
        The serviceInstanceIdentifier of the App that defines this AppRole. This value will match the opcServiceInstanceGUID of any service-instance that the App represents.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The service_instance_identifier of this AppRoleApp.
        :rtype: str
        """
        return self._service_instance_identifier

    @service_instance_identifier.setter
    def service_instance_identifier(self, service_instance_identifier):
        """
        Sets the service_instance_identifier of this AppRoleApp.
        The serviceInstanceIdentifier of the App that defines this AppRole. This value will match the opcServiceInstanceGUID of any service-instance that the App represents.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param service_instance_identifier: The service_instance_identifier of this AppRoleApp.
        :type: str
        """
        self._service_instance_identifier = service_instance_identifier

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
