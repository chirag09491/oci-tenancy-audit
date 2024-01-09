# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableExternalPluggableDatabaseDatabaseManagementDetails(object):
    """
    Details to enable Database Management on an external pluggable database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnableExternalPluggableDatabaseDatabaseManagementDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param external_database_connector_id:
            The value to assign to the external_database_connector_id property of this EnableExternalPluggableDatabaseDatabaseManagementDetails.
        :type external_database_connector_id: str

        """
        self.swagger_types = {
            'external_database_connector_id': 'str'
        }

        self.attribute_map = {
            'external_database_connector_id': 'externalDatabaseConnectorId'
        }

        self._external_database_connector_id = None

    @property
    def external_database_connector_id(self):
        """
        **[Required]** Gets the external_database_connector_id of this EnableExternalPluggableDatabaseDatabaseManagementDetails.
        The `OCID`__ of the
        :func:`create_external_database_connector_details`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_database_connector_id of this EnableExternalPluggableDatabaseDatabaseManagementDetails.
        :rtype: str
        """
        return self._external_database_connector_id

    @external_database_connector_id.setter
    def external_database_connector_id(self, external_database_connector_id):
        """
        Sets the external_database_connector_id of this EnableExternalPluggableDatabaseDatabaseManagementDetails.
        The `OCID`__ of the
        :func:`create_external_database_connector_details`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_database_connector_id: The external_database_connector_id of this EnableExternalPluggableDatabaseDatabaseManagementDetails.
        :type: str
        """
        self._external_database_connector_id = external_database_connector_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
