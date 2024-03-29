# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181231


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceCategories(object):
    """
    List of Service Categories of a Service for MOS Taxonomy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceCategories object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param service_category:
            The value to assign to the service_category property of this ServiceCategories.
        :type service_category: dict(str, str)

        :param schema:
            The value to assign to the schema property of this ServiceCategories.
        :type schema: str

        :param issue_type:
            The value to assign to the issue_type property of this ServiceCategories.
        :type issue_type: dict(str, str)

        """
        self.swagger_types = {
            'service_category': 'dict(str, str)',
            'schema': 'str',
            'issue_type': 'dict(str, str)'
        }

        self.attribute_map = {
            'service_category': 'serviceCategory',
            'schema': 'schema',
            'issue_type': 'issueType'
        }

        self._service_category = None
        self._schema = None
        self._issue_type = None

    @property
    def service_category(self):
        """
        Gets the service_category of this ServiceCategories.
        Service Category list.


        :return: The service_category of this ServiceCategories.
        :rtype: dict(str, str)
        """
        return self._service_category

    @service_category.setter
    def service_category(self, service_category):
        """
        Sets the service_category of this ServiceCategories.
        Service Category list.


        :param service_category: The service_category of this ServiceCategories.
        :type: dict(str, str)
        """
        self._service_category = service_category

    @property
    def schema(self):
        """
        Gets the schema of this ServiceCategories.
        Schema of a Service Category.


        :return: The schema of this ServiceCategories.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this ServiceCategories.
        Schema of a Service Category.


        :param schema: The schema of this ServiceCategories.
        :type: str
        """
        self._schema = schema

    @property
    def issue_type(self):
        """
        Gets the issue_type of this ServiceCategories.
        Issue type list.


        :return: The issue_type of this ServiceCategories.
        :rtype: dict(str, str)
        """
        return self._issue_type

    @issue_type.setter
    def issue_type(self, issue_type):
        """
        Sets the issue_type of this ServiceCategories.
        Issue type list.


        :param issue_type: The issue_type of this ServiceCategories.
        :type: dict(str, str)
        """
        self._issue_type = issue_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
