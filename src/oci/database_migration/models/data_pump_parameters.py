# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataPumpParameters(object):
    """
    Optional parameters for Datapump Export and Import. Refer to https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/ODMS_DATAPUMP.html#GUID-62324358-2F26-4A94-B69F-1075D53FA96D__BABDECJE
    """

    #: A constant which can be used with the estimate property of a DataPumpParameters.
    #: This constant has a value of "BLOCKS"
    ESTIMATE_BLOCKS = "BLOCKS"

    #: A constant which can be used with the estimate property of a DataPumpParameters.
    #: This constant has a value of "STATISTICS"
    ESTIMATE_STATISTICS = "STATISTICS"

    #: A constant which can be used with the table_exists_action property of a DataPumpParameters.
    #: This constant has a value of "TRUNCATE"
    TABLE_EXISTS_ACTION_TRUNCATE = "TRUNCATE"

    #: A constant which can be used with the table_exists_action property of a DataPumpParameters.
    #: This constant has a value of "REPLACE"
    TABLE_EXISTS_ACTION_REPLACE = "REPLACE"

    #: A constant which can be used with the table_exists_action property of a DataPumpParameters.
    #: This constant has a value of "APPEND"
    TABLE_EXISTS_ACTION_APPEND = "APPEND"

    #: A constant which can be used with the table_exists_action property of a DataPumpParameters.
    #: This constant has a value of "SKIP"
    TABLE_EXISTS_ACTION_SKIP = "SKIP"

    def __init__(self, **kwargs):
        """
        Initializes a new DataPumpParameters object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_cluster:
            The value to assign to the is_cluster property of this DataPumpParameters.
        :type is_cluster: bool

        :param estimate:
            The value to assign to the estimate property of this DataPumpParameters.
            Allowed values for this property are: "BLOCKS", "STATISTICS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type estimate: str

        :param table_exists_action:
            The value to assign to the table_exists_action property of this DataPumpParameters.
            Allowed values for this property are: "TRUNCATE", "REPLACE", "APPEND", "SKIP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type table_exists_action: str

        :param exclude_parameters:
            The value to assign to the exclude_parameters property of this DataPumpParameters.
        :type exclude_parameters: list[oci.database_migration.models.DataPumpExcludeParameters]

        :param import_parallelism_degree:
            The value to assign to the import_parallelism_degree property of this DataPumpParameters.
        :type import_parallelism_degree: int

        :param export_parallelism_degree:
            The value to assign to the export_parallelism_degree property of this DataPumpParameters.
        :type export_parallelism_degree: int

        """
        self.swagger_types = {
            'is_cluster': 'bool',
            'estimate': 'str',
            'table_exists_action': 'str',
            'exclude_parameters': 'list[DataPumpExcludeParameters]',
            'import_parallelism_degree': 'int',
            'export_parallelism_degree': 'int'
        }

        self.attribute_map = {
            'is_cluster': 'isCluster',
            'estimate': 'estimate',
            'table_exists_action': 'tableExistsAction',
            'exclude_parameters': 'excludeParameters',
            'import_parallelism_degree': 'importParallelismDegree',
            'export_parallelism_degree': 'exportParallelismDegree'
        }

        self._is_cluster = None
        self._estimate = None
        self._table_exists_action = None
        self._exclude_parameters = None
        self._import_parallelism_degree = None
        self._export_parallelism_degree = None

    @property
    def is_cluster(self):
        """
        Gets the is_cluster of this DataPumpParameters.
        False to force datapump worker process to run on one instance.


        :return: The is_cluster of this DataPumpParameters.
        :rtype: bool
        """
        return self._is_cluster

    @is_cluster.setter
    def is_cluster(self, is_cluster):
        """
        Sets the is_cluster of this DataPumpParameters.
        False to force datapump worker process to run on one instance.


        :param is_cluster: The is_cluster of this DataPumpParameters.
        :type: bool
        """
        self._is_cluster = is_cluster

    @property
    def estimate(self):
        """
        Gets the estimate of this DataPumpParameters.
        Estimate size of dumps that will be generated.

        Allowed values for this property are: "BLOCKS", "STATISTICS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The estimate of this DataPumpParameters.
        :rtype: str
        """
        return self._estimate

    @estimate.setter
    def estimate(self, estimate):
        """
        Sets the estimate of this DataPumpParameters.
        Estimate size of dumps that will be generated.


        :param estimate: The estimate of this DataPumpParameters.
        :type: str
        """
        allowed_values = ["BLOCKS", "STATISTICS"]
        if not value_allowed_none_or_none_sentinel(estimate, allowed_values):
            estimate = 'UNKNOWN_ENUM_VALUE'
        self._estimate = estimate

    @property
    def table_exists_action(self):
        """
        Gets the table_exists_action of this DataPumpParameters.
        IMPORT: Specifies the action to be performed when data is loaded into a preexisting table.

        Allowed values for this property are: "TRUNCATE", "REPLACE", "APPEND", "SKIP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The table_exists_action of this DataPumpParameters.
        :rtype: str
        """
        return self._table_exists_action

    @table_exists_action.setter
    def table_exists_action(self, table_exists_action):
        """
        Sets the table_exists_action of this DataPumpParameters.
        IMPORT: Specifies the action to be performed when data is loaded into a preexisting table.


        :param table_exists_action: The table_exists_action of this DataPumpParameters.
        :type: str
        """
        allowed_values = ["TRUNCATE", "REPLACE", "APPEND", "SKIP"]
        if not value_allowed_none_or_none_sentinel(table_exists_action, allowed_values):
            table_exists_action = 'UNKNOWN_ENUM_VALUE'
        self._table_exists_action = table_exists_action

    @property
    def exclude_parameters(self):
        """
        Gets the exclude_parameters of this DataPumpParameters.
        Exclude paratemers for export and import.


        :return: The exclude_parameters of this DataPumpParameters.
        :rtype: list[oci.database_migration.models.DataPumpExcludeParameters]
        """
        return self._exclude_parameters

    @exclude_parameters.setter
    def exclude_parameters(self, exclude_parameters):
        """
        Sets the exclude_parameters of this DataPumpParameters.
        Exclude paratemers for export and import.


        :param exclude_parameters: The exclude_parameters of this DataPumpParameters.
        :type: list[oci.database_migration.models.DataPumpExcludeParameters]
        """
        self._exclude_parameters = exclude_parameters

    @property
    def import_parallelism_degree(self):
        """
        Gets the import_parallelism_degree of this DataPumpParameters.
        Maximum number of worker processes that can be used for a Datapump Import job.
        For an Autonomous Database, ODMS will automatically query its CPU core count and set this property.


        :return: The import_parallelism_degree of this DataPumpParameters.
        :rtype: int
        """
        return self._import_parallelism_degree

    @import_parallelism_degree.setter
    def import_parallelism_degree(self, import_parallelism_degree):
        """
        Sets the import_parallelism_degree of this DataPumpParameters.
        Maximum number of worker processes that can be used for a Datapump Import job.
        For an Autonomous Database, ODMS will automatically query its CPU core count and set this property.


        :param import_parallelism_degree: The import_parallelism_degree of this DataPumpParameters.
        :type: int
        """
        self._import_parallelism_degree = import_parallelism_degree

    @property
    def export_parallelism_degree(self):
        """
        Gets the export_parallelism_degree of this DataPumpParameters.
        Maximum number of worker processes that can be used for a Datapump Export job.


        :return: The export_parallelism_degree of this DataPumpParameters.
        :rtype: int
        """
        return self._export_parallelism_degree

    @export_parallelism_degree.setter
    def export_parallelism_degree(self, export_parallelism_degree):
        """
        Sets the export_parallelism_degree of this DataPumpParameters.
        Maximum number of worker processes that can be used for a Datapump Export job.


        :param export_parallelism_degree: The export_parallelism_degree of this DataPumpParameters.
        :type: int
        """
        self._export_parallelism_degree = export_parallelism_degree

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
