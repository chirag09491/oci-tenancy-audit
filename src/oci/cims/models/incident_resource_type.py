# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181231


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IncidentResourceType(object):
    """
    Details about the resource associated with the support request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IncidentResourceType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_type_key:
            The value to assign to the resource_type_key property of this IncidentResourceType.
        :type resource_type_key: str

        :param name:
            The value to assign to the name property of this IncidentResourceType.
        :type name: str

        :param label:
            The value to assign to the label property of this IncidentResourceType.
        :type label: str

        :param description:
            The value to assign to the description property of this IncidentResourceType.
        :type description: str

        :param service_category_list:
            The value to assign to the service_category_list property of this IncidentResourceType.
        :type service_category_list: list[oci.cims.models.ServiceCategory]

        :param service:
            The value to assign to the service property of this IncidentResourceType.
        :type service: dict(str, str)

        :param service_categories:
            The value to assign to the service_categories property of this IncidentResourceType.
        :type service_categories: list[oci.cims.models.ServiceCategories]

        """
        self.swagger_types = {
            'resource_type_key': 'str',
            'name': 'str',
            'label': 'str',
            'description': 'str',
            'service_category_list': 'list[ServiceCategory]',
            'service': 'dict(str, str)',
            'service_categories': 'list[ServiceCategories]'
        }

        self.attribute_map = {
            'resource_type_key': 'resourceTypeKey',
            'name': 'name',
            'label': 'label',
            'description': 'description',
            'service_category_list': 'serviceCategoryList',
            'service': 'service',
            'service_categories': 'serviceCategories'
        }

        self._resource_type_key = None
        self._name = None
        self._label = None
        self._description = None
        self._service_category_list = None
        self._service = None
        self._service_categories = None

    @property
    def resource_type_key(self):
        """
        Gets the resource_type_key of this IncidentResourceType.
        A unique identifier for the resource.


        :return: The resource_type_key of this IncidentResourceType.
        :rtype: str
        """
        return self._resource_type_key

    @resource_type_key.setter
    def resource_type_key(self, resource_type_key):
        """
        Sets the resource_type_key of this IncidentResourceType.
        A unique identifier for the resource.


        :param resource_type_key: The resource_type_key of this IncidentResourceType.
        :type: str
        """
        self._resource_type_key = resource_type_key

    @property
    def name(self):
        """
        Gets the name of this IncidentResourceType.
        The display name of the resource.


        :return: The name of this IncidentResourceType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IncidentResourceType.
        The display name of the resource.


        :param name: The name of this IncidentResourceType.
        :type: str
        """
        self._name = name

    @property
    def label(self):
        """
        **[Required]** Gets the label of this IncidentResourceType.
        The label associated with the resource.


        :return: The label of this IncidentResourceType.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this IncidentResourceType.
        The label associated with the resource.


        :param label: The label of this IncidentResourceType.
        :type: str
        """
        self._label = label

    @property
    def description(self):
        """
        Gets the description of this IncidentResourceType.
        The description of the resource.


        :return: The description of this IncidentResourceType.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this IncidentResourceType.
        The description of the resource.


        :param description: The description of this IncidentResourceType.
        :type: str
        """
        self._description = description

    @property
    def service_category_list(self):
        """
        Gets the service_category_list of this IncidentResourceType.
        The service category list.


        :return: The service_category_list of this IncidentResourceType.
        :rtype: list[oci.cims.models.ServiceCategory]
        """
        return self._service_category_list

    @service_category_list.setter
    def service_category_list(self, service_category_list):
        """
        Sets the service_category_list of this IncidentResourceType.
        The service category list.


        :param service_category_list: The service_category_list of this IncidentResourceType.
        :type: list[oci.cims.models.ServiceCategory]
        """
        self._service_category_list = service_category_list

    @property
    def service(self):
        """
        Gets the service of this IncidentResourceType.
        The map of services for MOS Taxonomy.


        :return: The service of this IncidentResourceType.
        :rtype: dict(str, str)
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this IncidentResourceType.
        The map of services for MOS Taxonomy.


        :param service: The service of this IncidentResourceType.
        :type: dict(str, str)
        """
        self._service = service

    @property
    def service_categories(self):
        """
        Gets the service_categories of this IncidentResourceType.
        The service categories list for MOS Taxonomy.


        :return: The service_categories of this IncidentResourceType.
        :rtype: list[oci.cims.models.ServiceCategories]
        """
        return self._service_categories

    @service_categories.setter
    def service_categories(self, service_categories):
        """
        Sets the service_categories of this IncidentResourceType.
        The service categories list for MOS Taxonomy.


        :param service_categories: The service_categories of this IncidentResourceType.
        :type: list[oci.cims.models.ServiceCategories]
        """
        self._service_categories = service_categories

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
