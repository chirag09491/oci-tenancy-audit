# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200129


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PoolConfig(object):
    """
    An object containing the details about the compute shapes and number of compute instances to provison.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PoolConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shape:
            The value to assign to the shape property of this PoolConfig.
        :type shape: str

        :param shape_config:
            The value to assign to the shape_config property of this PoolConfig.
        :type shape_config: oci.data_flow.models.ShapeConfig

        :param min:
            The value to assign to the min property of this PoolConfig.
        :type min: int

        :param max:
            The value to assign to the max property of this PoolConfig.
        :type max: int

        """
        self.swagger_types = {
            'shape': 'str',
            'shape_config': 'ShapeConfig',
            'min': 'int',
            'max': 'int'
        }

        self.attribute_map = {
            'shape': 'shape',
            'shape_config': 'shapeConfig',
            'min': 'min',
            'max': 'max'
        }

        self._shape = None
        self._shape_config = None
        self._min = None
        self._max = None

    @property
    def shape(self):
        """
        Gets the shape of this PoolConfig.
        The compute shape of the resources you would like to provision.


        :return: The shape of this PoolConfig.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this PoolConfig.
        The compute shape of the resources you would like to provision.


        :param shape: The shape of this PoolConfig.
        :type: str
        """
        self._shape = shape

    @property
    def shape_config(self):
        """
        Gets the shape_config of this PoolConfig.

        :return: The shape_config of this PoolConfig.
        :rtype: oci.data_flow.models.ShapeConfig
        """
        return self._shape_config

    @shape_config.setter
    def shape_config(self, shape_config):
        """
        Sets the shape_config of this PoolConfig.

        :param shape_config: The shape_config of this PoolConfig.
        :type: oci.data_flow.models.ShapeConfig
        """
        self._shape_config = shape_config

    @property
    def min(self):
        """
        Gets the min of this PoolConfig.
        Minimum number of compute instances in the pool for a given compute shape.


        :return: The min of this PoolConfig.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this PoolConfig.
        Minimum number of compute instances in the pool for a given compute shape.


        :param min: The min of this PoolConfig.
        :type: int
        """
        self._min = min

    @property
    def max(self):
        """
        Gets the max of this PoolConfig.
        Maximum number of compute instances in the pool for a given compute shape.


        :return: The max of this PoolConfig.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this PoolConfig.
        Maximum number of compute instances in the pool for a given compute shape.


        :param max: The max of this PoolConfig.
        :type: int
        """
        self._max = max

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
