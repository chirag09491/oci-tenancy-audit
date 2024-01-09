# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190325


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LineageRelationship(object):
    """
    Declares how two elements of object lineage are related.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LineageRelationship object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param from_object_key:
            The value to assign to the from_object_key property of this LineageRelationship.
        :type from_object_key: str

        :param to_object_key:
            The value to assign to the to_object_key property of this LineageRelationship.
        :type to_object_key: str

        :param relationship_type:
            The value to assign to the relationship_type property of this LineageRelationship.
        :type relationship_type: str

        """
        self.swagger_types = {
            'from_object_key': 'str',
            'to_object_key': 'str',
            'relationship_type': 'str'
        }

        self.attribute_map = {
            'from_object_key': 'fromObjectKey',
            'to_object_key': 'toObjectKey',
            'relationship_type': 'relationshipType'
        }

        self._from_object_key = None
        self._to_object_key = None
        self._relationship_type = None

    @property
    def from_object_key(self):
        """
        Gets the from_object_key of this LineageRelationship.
        Object key of source lineage element.


        :return: The from_object_key of this LineageRelationship.
        :rtype: str
        """
        return self._from_object_key

    @from_object_key.setter
    def from_object_key(self, from_object_key):
        """
        Sets the from_object_key of this LineageRelationship.
        Object key of source lineage element.


        :param from_object_key: The from_object_key of this LineageRelationship.
        :type: str
        """
        self._from_object_key = from_object_key

    @property
    def to_object_key(self):
        """
        Gets the to_object_key of this LineageRelationship.
        Object key of target lineage element.


        :return: The to_object_key of this LineageRelationship.
        :rtype: str
        """
        return self._to_object_key

    @to_object_key.setter
    def to_object_key(self, to_object_key):
        """
        Sets the to_object_key of this LineageRelationship.
        Object key of target lineage element.


        :param to_object_key: The to_object_key of this LineageRelationship.
        :type: str
        """
        self._to_object_key = to_object_key

    @property
    def relationship_type(self):
        """
        Gets the relationship_type of this LineageRelationship.
        Type of the relationship.


        :return: The relationship_type of this LineageRelationship.
        :rtype: str
        """
        return self._relationship_type

    @relationship_type.setter
    def relationship_type(self, relationship_type):
        """
        Sets the relationship_type of this LineageRelationship.
        Type of the relationship.


        :param relationship_type: The relationship_type of this LineageRelationship.
        :type: str
        """
        self._relationship_type = relationship_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
