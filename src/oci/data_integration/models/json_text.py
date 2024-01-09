# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JsonText(object):
    """
    The JSON type of the formatted text.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JsonText object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this JsonText.
        :type model_type: str

        :param config_values:
            The value to assign to the config_values property of this JsonText.
        :type config_values: oci.data_integration.models.ConfigValues

        """
        self.swagger_types = {
            'model_type': 'str',
            'config_values': 'ConfigValues'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'config_values': 'configValues'
        }

        self._model_type = None
        self._config_values = None

    @property
    def model_type(self):
        """
        Gets the model_type of this JsonText.
        The object type.


        :return: The model_type of this JsonText.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this JsonText.
        The object type.


        :param model_type: The model_type of this JsonText.
        :type: str
        """
        self._model_type = model_type

    @property
    def config_values(self):
        """
        Gets the config_values of this JsonText.

        :return: The config_values of this JsonText.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this JsonText.

        :param config_values: The config_values of this JsonText.
        :type: oci.data_integration.models.ConfigValues
        """
        self._config_values = config_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
