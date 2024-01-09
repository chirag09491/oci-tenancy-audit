# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppConnectorBundle(object):
    """
    ConnectorBundle

    **SCIM++ Properties:**
    - idcsSearchable: true
    - multiValued: false
    - mutability: readOnly
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    #: A constant which can be used with the type property of a AppConnectorBundle.
    #: This constant has a value of "ConnectorBundle"
    TYPE_CONNECTOR_BUNDLE = "ConnectorBundle"

    #: A constant which can be used with the type property of a AppConnectorBundle.
    #: This constant has a value of "LocalConnectorBundle"
    TYPE_LOCAL_CONNECTOR_BUNDLE = "LocalConnectorBundle"

    def __init__(self, **kwargs):
        """
        Initializes a new AppConnectorBundle object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this AppConnectorBundle.
        :type value: str

        :param type:
            The value to assign to the type property of this AppConnectorBundle.
            Allowed values for this property are: "ConnectorBundle", "LocalConnectorBundle", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param ref:
            The value to assign to the ref property of this AppConnectorBundle.
        :type ref: str

        :param display:
            The value to assign to the display property of this AppConnectorBundle.
        :type display: str

        :param well_known_id:
            The value to assign to the well_known_id property of this AppConnectorBundle.
        :type well_known_id: str

        """
        self.swagger_types = {
            'value': 'str',
            'type': 'str',
            'ref': 'str',
            'display': 'str',
            'well_known_id': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'type': 'type',
            'ref': '$ref',
            'display': 'display',
            'well_known_id': 'wellKnownId'
        }

        self._value = None
        self._type = None
        self._ref = None
        self._display = None
        self._well_known_id = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this AppConnectorBundle.
        ConnectorBundle identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this AppConnectorBundle.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AppConnectorBundle.
        ConnectorBundle identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this AppConnectorBundle.
        :type: str
        """
        self._value = value

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AppConnectorBundle.
        Connector Bundle type. Allowed values are ConnectorBundle, LocalConnectorBundle.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsDefaultValue: ConnectorBundle
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "ConnectorBundle", "LocalConnectorBundle", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AppConnectorBundle.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AppConnectorBundle.
        Connector Bundle type. Allowed values are ConnectorBundle, LocalConnectorBundle.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsDefaultValue: ConnectorBundle
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this AppConnectorBundle.
        :type: str
        """
        allowed_values = ["ConnectorBundle", "LocalConnectorBundle"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def ref(self):
        """
        Gets the ref of this AppConnectorBundle.
        ConnectorBundle URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this AppConnectorBundle.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this AppConnectorBundle.
        ConnectorBundle URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this AppConnectorBundle.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this AppConnectorBundle.
        ConnectorBundle display name

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this AppConnectorBundle.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this AppConnectorBundle.
        ConnectorBundle display name

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this AppConnectorBundle.
        :type: str
        """
        self._display = display

    @property
    def well_known_id(self):
        """
        Gets the well_known_id of this AppConnectorBundle.
        Unique Well-known identifier used to reference connector bundle.

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The well_known_id of this AppConnectorBundle.
        :rtype: str
        """
        return self._well_known_id

    @well_known_id.setter
    def well_known_id(self, well_known_id):
        """
        Sets the well_known_id of this AppConnectorBundle.
        Unique Well-known identifier used to reference connector bundle.

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param well_known_id: The well_known_id of this AppConnectorBundle.
        :type: str
        """
        self._well_known_id = well_known_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
