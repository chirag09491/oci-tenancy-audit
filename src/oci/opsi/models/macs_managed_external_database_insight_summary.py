# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_insight_summary import DatabaseInsightSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MacsManagedExternalDatabaseInsightSummary(DatabaseInsightSummary):
    """
    Summary of a database insight resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MacsManagedExternalDatabaseInsightSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.MacsManagedExternalDatabaseInsightSummary.entity_source` attribute
        of this class is ``MACS_MANAGED_EXTERNAL_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MacsManagedExternalDatabaseInsightSummary.
        :type id: str

        :param database_id:
            The value to assign to the database_id property of this MacsManagedExternalDatabaseInsightSummary.
        :type database_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MacsManagedExternalDatabaseInsightSummary.
        :type compartment_id: str

        :param database_name:
            The value to assign to the database_name property of this MacsManagedExternalDatabaseInsightSummary.
        :type database_name: str

        :param database_display_name:
            The value to assign to the database_display_name property of this MacsManagedExternalDatabaseInsightSummary.
        :type database_display_name: str

        :param database_type:
            The value to assign to the database_type property of this MacsManagedExternalDatabaseInsightSummary.
        :type database_type: str

        :param database_version:
            The value to assign to the database_version property of this MacsManagedExternalDatabaseInsightSummary.
        :type database_version: str

        :param database_host_names:
            The value to assign to the database_host_names property of this MacsManagedExternalDatabaseInsightSummary.
        :type database_host_names: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MacsManagedExternalDatabaseInsightSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MacsManagedExternalDatabaseInsightSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MacsManagedExternalDatabaseInsightSummary.
        :type system_tags: dict(str, dict(str, object))

        :param entity_source:
            The value to assign to the entity_source property of this MacsManagedExternalDatabaseInsightSummary.
            Allowed values for this property are: "AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE"
        :type entity_source: str

        :param processor_count:
            The value to assign to the processor_count property of this MacsManagedExternalDatabaseInsightSummary.
        :type processor_count: int

        :param status:
            The value to assign to the status property of this MacsManagedExternalDatabaseInsightSummary.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED"
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this MacsManagedExternalDatabaseInsightSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MacsManagedExternalDatabaseInsightSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MacsManagedExternalDatabaseInsightSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MacsManagedExternalDatabaseInsightSummary.
        :type lifecycle_details: str

        :param database_resource_type:
            The value to assign to the database_resource_type property of this MacsManagedExternalDatabaseInsightSummary.
        :type database_resource_type: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this MacsManagedExternalDatabaseInsightSummary.
        :type management_agent_id: str

        :param connector_id:
            The value to assign to the connector_id property of this MacsManagedExternalDatabaseInsightSummary.
        :type connector_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'database_id': 'str',
            'compartment_id': 'str',
            'database_name': 'str',
            'database_display_name': 'str',
            'database_type': 'str',
            'database_version': 'str',
            'database_host_names': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'entity_source': 'str',
            'processor_count': 'int',
            'status': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'database_resource_type': 'str',
            'management_agent_id': 'str',
            'connector_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'database_id': 'databaseId',
            'compartment_id': 'compartmentId',
            'database_name': 'databaseName',
            'database_display_name': 'databaseDisplayName',
            'database_type': 'databaseType',
            'database_version': 'databaseVersion',
            'database_host_names': 'databaseHostNames',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'entity_source': 'entitySource',
            'processor_count': 'processorCount',
            'status': 'status',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'database_resource_type': 'databaseResourceType',
            'management_agent_id': 'managementAgentId',
            'connector_id': 'connectorId'
        }

        self._id = None
        self._database_id = None
        self._compartment_id = None
        self._database_name = None
        self._database_display_name = None
        self._database_type = None
        self._database_version = None
        self._database_host_names = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._entity_source = None
        self._processor_count = None
        self._status = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._database_resource_type = None
        self._management_agent_id = None
        self._connector_id = None
        self._entity_source = 'MACS_MANAGED_EXTERNAL_DATABASE'

    @property
    def database_resource_type(self):
        """
        Gets the database_resource_type of this MacsManagedExternalDatabaseInsightSummary.
        OCI database resource type


        :return: The database_resource_type of this MacsManagedExternalDatabaseInsightSummary.
        :rtype: str
        """
        return self._database_resource_type

    @database_resource_type.setter
    def database_resource_type(self, database_resource_type):
        """
        Sets the database_resource_type of this MacsManagedExternalDatabaseInsightSummary.
        OCI database resource type


        :param database_resource_type: The database_resource_type of this MacsManagedExternalDatabaseInsightSummary.
        :type: str
        """
        self._database_resource_type = database_resource_type

    @property
    def management_agent_id(self):
        """
        Gets the management_agent_id of this MacsManagedExternalDatabaseInsightSummary.
        The `OCID`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this MacsManagedExternalDatabaseInsightSummary.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this MacsManagedExternalDatabaseInsightSummary.
        The `OCID`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this MacsManagedExternalDatabaseInsightSummary.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def connector_id(self):
        """
        Gets the connector_id of this MacsManagedExternalDatabaseInsightSummary.
        The `OCID`__ of External Database Connector

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The connector_id of this MacsManagedExternalDatabaseInsightSummary.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """
        Sets the connector_id of this MacsManagedExternalDatabaseInsightSummary.
        The `OCID`__ of External Database Connector

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param connector_id: The connector_id of this MacsManagedExternalDatabaseInsightSummary.
        :type: str
        """
        self._connector_id = connector_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
