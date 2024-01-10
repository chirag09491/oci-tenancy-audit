# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlInParamDetails(object):
    """
    Position and value for an IN parameter of PL/SQL statement
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlInParamDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param in_param_position:
            The value to assign to the in_param_position property of this SqlInParamDetails.
        :type in_param_position: int

        :param in_param_value:
            The value to assign to the in_param_value property of this SqlInParamDetails.
        :type in_param_value: str

        """
        self.swagger_types = {
            'in_param_position': 'int',
            'in_param_value': 'str'
        }

        self.attribute_map = {
            'in_param_position': 'inParamPosition',
            'in_param_value': 'inParamValue'
        }

        self._in_param_position = None
        self._in_param_value = None

    @property
    def in_param_position(self):
        """
        **[Required]** Gets the in_param_position of this SqlInParamDetails.
        Position of IN parameter


        :return: The in_param_position of this SqlInParamDetails.
        :rtype: int
        """
        return self._in_param_position

    @in_param_position.setter
    def in_param_position(self, in_param_position):
        """
        Sets the in_param_position of this SqlInParamDetails.
        Position of IN parameter


        :param in_param_position: The in_param_position of this SqlInParamDetails.
        :type: int
        """
        self._in_param_position = in_param_position

    @property
    def in_param_value(self):
        """
        **[Required]** Gets the in_param_value of this SqlInParamDetails.
        Value of IN parameter


        :return: The in_param_value of this SqlInParamDetails.
        :rtype: str
        """
        return self._in_param_value

    @in_param_value.setter
    def in_param_value(self, in_param_value):
        """
        Sets the in_param_value of this SqlInParamDetails.
        Value of IN parameter


        :param in_param_value: The in_param_value of this SqlInParamDetails.
        :type: str
        """
        self._in_param_value = in_param_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other