# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PasswordPolicy(object):
    """
    Password policy, currently set for the given compartment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PasswordPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param minimum_password_length:
            The value to assign to the minimum_password_length property of this PasswordPolicy.
        :type minimum_password_length: int

        :param is_uppercase_characters_required:
            The value to assign to the is_uppercase_characters_required property of this PasswordPolicy.
        :type is_uppercase_characters_required: bool

        :param is_lowercase_characters_required:
            The value to assign to the is_lowercase_characters_required property of this PasswordPolicy.
        :type is_lowercase_characters_required: bool

        :param is_numeric_characters_required:
            The value to assign to the is_numeric_characters_required property of this PasswordPolicy.
        :type is_numeric_characters_required: bool

        :param is_special_characters_required:
            The value to assign to the is_special_characters_required property of this PasswordPolicy.
        :type is_special_characters_required: bool

        :param is_username_containment_allowed:
            The value to assign to the is_username_containment_allowed property of this PasswordPolicy.
        :type is_username_containment_allowed: bool

        """
        self.swagger_types = {
            'minimum_password_length': 'int',
            'is_uppercase_characters_required': 'bool',
            'is_lowercase_characters_required': 'bool',
            'is_numeric_characters_required': 'bool',
            'is_special_characters_required': 'bool',
            'is_username_containment_allowed': 'bool'
        }

        self.attribute_map = {
            'minimum_password_length': 'minimumPasswordLength',
            'is_uppercase_characters_required': 'isUppercaseCharactersRequired',
            'is_lowercase_characters_required': 'isLowercaseCharactersRequired',
            'is_numeric_characters_required': 'isNumericCharactersRequired',
            'is_special_characters_required': 'isSpecialCharactersRequired',
            'is_username_containment_allowed': 'isUsernameContainmentAllowed'
        }

        self._minimum_password_length = None
        self._is_uppercase_characters_required = None
        self._is_lowercase_characters_required = None
        self._is_numeric_characters_required = None
        self._is_special_characters_required = None
        self._is_username_containment_allowed = None

    @property
    def minimum_password_length(self):
        """
        Gets the minimum_password_length of this PasswordPolicy.
        Minimum password length required.


        :return: The minimum_password_length of this PasswordPolicy.
        :rtype: int
        """
        return self._minimum_password_length

    @minimum_password_length.setter
    def minimum_password_length(self, minimum_password_length):
        """
        Sets the minimum_password_length of this PasswordPolicy.
        Minimum password length required.


        :param minimum_password_length: The minimum_password_length of this PasswordPolicy.
        :type: int
        """
        self._minimum_password_length = minimum_password_length

    @property
    def is_uppercase_characters_required(self):
        """
        Gets the is_uppercase_characters_required of this PasswordPolicy.
        At least one uppercase character required.


        :return: The is_uppercase_characters_required of this PasswordPolicy.
        :rtype: bool
        """
        return self._is_uppercase_characters_required

    @is_uppercase_characters_required.setter
    def is_uppercase_characters_required(self, is_uppercase_characters_required):
        """
        Sets the is_uppercase_characters_required of this PasswordPolicy.
        At least one uppercase character required.


        :param is_uppercase_characters_required: The is_uppercase_characters_required of this PasswordPolicy.
        :type: bool
        """
        self._is_uppercase_characters_required = is_uppercase_characters_required

    @property
    def is_lowercase_characters_required(self):
        """
        Gets the is_lowercase_characters_required of this PasswordPolicy.
        At least one lower case character required.


        :return: The is_lowercase_characters_required of this PasswordPolicy.
        :rtype: bool
        """
        return self._is_lowercase_characters_required

    @is_lowercase_characters_required.setter
    def is_lowercase_characters_required(self, is_lowercase_characters_required):
        """
        Sets the is_lowercase_characters_required of this PasswordPolicy.
        At least one lower case character required.


        :param is_lowercase_characters_required: The is_lowercase_characters_required of this PasswordPolicy.
        :type: bool
        """
        self._is_lowercase_characters_required = is_lowercase_characters_required

    @property
    def is_numeric_characters_required(self):
        """
        Gets the is_numeric_characters_required of this PasswordPolicy.
        At least one numeric character required.


        :return: The is_numeric_characters_required of this PasswordPolicy.
        :rtype: bool
        """
        return self._is_numeric_characters_required

    @is_numeric_characters_required.setter
    def is_numeric_characters_required(self, is_numeric_characters_required):
        """
        Sets the is_numeric_characters_required of this PasswordPolicy.
        At least one numeric character required.


        :param is_numeric_characters_required: The is_numeric_characters_required of this PasswordPolicy.
        :type: bool
        """
        self._is_numeric_characters_required = is_numeric_characters_required

    @property
    def is_special_characters_required(self):
        """
        Gets the is_special_characters_required of this PasswordPolicy.
        At least one special character required.


        :return: The is_special_characters_required of this PasswordPolicy.
        :rtype: bool
        """
        return self._is_special_characters_required

    @is_special_characters_required.setter
    def is_special_characters_required(self, is_special_characters_required):
        """
        Sets the is_special_characters_required of this PasswordPolicy.
        At least one special character required.


        :param is_special_characters_required: The is_special_characters_required of this PasswordPolicy.
        :type: bool
        """
        self._is_special_characters_required = is_special_characters_required

    @property
    def is_username_containment_allowed(self):
        """
        Gets the is_username_containment_allowed of this PasswordPolicy.
        User name is allowed to be part of the password.


        :return: The is_username_containment_allowed of this PasswordPolicy.
        :rtype: bool
        """
        return self._is_username_containment_allowed

    @is_username_containment_allowed.setter
    def is_username_containment_allowed(self, is_username_containment_allowed):
        """
        Sets the is_username_containment_allowed of this PasswordPolicy.
        User name is allowed to be part of the password.


        :param is_username_containment_allowed: The is_username_containment_allowed of this PasswordPolicy.
        :type: bool
        """
        self._is_username_containment_allowed = is_username_containment_allowed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
