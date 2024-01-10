# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NotificationSettingsFromEmailAddress(object):
    """
    From email address to be used in the notification emails

    **SCIM++ Properties:**
    - caseExact: false
    - multiValued: false
    - mutability: readWrite
    - required: true
    - returned: always
    - type: complex
    - uniqueness: none
    """

    #: A constant which can be used with the validation_status property of a NotificationSettingsFromEmailAddress.
    #: This constant has a value of "VERIFIED"
    VALIDATION_STATUS_VERIFIED = "VERIFIED"

    #: A constant which can be used with the validation_status property of a NotificationSettingsFromEmailAddress.
    #: This constant has a value of "PENDING"
    VALIDATION_STATUS_PENDING = "PENDING"

    #: A constant which can be used with the validate property of a NotificationSettingsFromEmailAddress.
    #: This constant has a value of "email"
    VALIDATE_EMAIL = "email"

    #: A constant which can be used with the validate property of a NotificationSettingsFromEmailAddress.
    #: This constant has a value of "domain"
    VALIDATE_DOMAIN = "domain"

    def __init__(self, **kwargs):
        """
        Initializes a new NotificationSettingsFromEmailAddress object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this NotificationSettingsFromEmailAddress.
        :type value: str

        :param validation_status:
            The value to assign to the validation_status property of this NotificationSettingsFromEmailAddress.
            Allowed values for this property are: "VERIFIED", "PENDING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type validation_status: str

        :param validate:
            The value to assign to the validate property of this NotificationSettingsFromEmailAddress.
            Allowed values for this property are: "email", "domain", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type validate: str

        :param display_name:
            The value to assign to the display_name property of this NotificationSettingsFromEmailAddress.
        :type display_name: str

        """
        self.swagger_types = {
            'value': 'str',
            'validation_status': 'str',
            'validate': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'validation_status': 'validationStatus',
            'validate': 'validate',
            'display_name': 'displayName'
        }

        self._value = None
        self._validation_status = None
        self._validate = None
        self._display_name = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this NotificationSettingsFromEmailAddress.
        Value of the From email address

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :return: The value of this NotificationSettingsFromEmailAddress.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this NotificationSettingsFromEmailAddress.
        Value of the From email address

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :param value: The value of this NotificationSettingsFromEmailAddress.
        :type: str
        """
        self._value = value

    @property
    def validation_status(self):
        """
        Gets the validation_status of this NotificationSettingsFromEmailAddress.
        Validation status for the From email address

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string

        Allowed values for this property are: "VERIFIED", "PENDING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The validation_status of this NotificationSettingsFromEmailAddress.
        :rtype: str
        """
        return self._validation_status

    @validation_status.setter
    def validation_status(self, validation_status):
        """
        Sets the validation_status of this NotificationSettingsFromEmailAddress.
        Validation status for the From email address

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string


        :param validation_status: The validation_status of this NotificationSettingsFromEmailAddress.
        :type: str
        """
        allowed_values = ["VERIFIED", "PENDING"]
        if not value_allowed_none_or_none_sentinel(validation_status, allowed_values):
            validation_status = 'UNKNOWN_ENUM_VALUE'
        self._validation_status = validation_status

    @property
    def validate(self):
        """
        **[Required]** Gets the validate of this NotificationSettingsFromEmailAddress.
        From address verification mode. If postmaster account is available then 'domain' mode is used or entire valid email can be verified using 'email' mode

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "email", "domain", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The validate of this NotificationSettingsFromEmailAddress.
        :rtype: str
        """
        return self._validate

    @validate.setter
    def validate(self, validate):
        """
        Sets the validate of this NotificationSettingsFromEmailAddress.
        From address verification mode. If postmaster account is available then 'domain' mode is used or entire valid email can be verified using 'email' mode

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param validate: The validate of this NotificationSettingsFromEmailAddress.
        :type: str
        """
        allowed_values = ["email", "domain"]
        if not value_allowed_none_or_none_sentinel(validate, allowed_values):
            validate = 'UNKNOWN_ENUM_VALUE'
        self._validate = validate

    @property
    def display_name(self):
        """
        Gets the display_name of this NotificationSettingsFromEmailAddress.
        Display name for the From email address

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :return: The display_name of this NotificationSettingsFromEmailAddress.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this NotificationSettingsFromEmailAddress.
        Display name for the From email address

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :param display_name: The display_name of this NotificationSettingsFromEmailAddress.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other