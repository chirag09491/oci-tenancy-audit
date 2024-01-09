# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210216


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Metrics(object):
    """
    Backup performance and storage utilization metrics for the protected database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Metrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backup_space_used_in_gbs:
            The value to assign to the backup_space_used_in_gbs property of this Metrics.
        :type backup_space_used_in_gbs: float

        :param backup_space_estimate_in_gbs:
            The value to assign to the backup_space_estimate_in_gbs property of this Metrics.
        :type backup_space_estimate_in_gbs: float

        :param unprotected_window_in_seconds:
            The value to assign to the unprotected_window_in_seconds property of this Metrics.
        :type unprotected_window_in_seconds: float

        :param db_size_in_gbs:
            The value to assign to the db_size_in_gbs property of this Metrics.
        :type db_size_in_gbs: float

        :param is_redo_logs_enabled:
            The value to assign to the is_redo_logs_enabled property of this Metrics.
        :type is_redo_logs_enabled: bool

        :param retention_period_in_days:
            The value to assign to the retention_period_in_days property of this Metrics.
        :type retention_period_in_days: float

        :param current_retention_period_in_seconds:
            The value to assign to the current_retention_period_in_seconds property of this Metrics.
        :type current_retention_period_in_seconds: float

        """
        self.swagger_types = {
            'backup_space_used_in_gbs': 'float',
            'backup_space_estimate_in_gbs': 'float',
            'unprotected_window_in_seconds': 'float',
            'db_size_in_gbs': 'float',
            'is_redo_logs_enabled': 'bool',
            'retention_period_in_days': 'float',
            'current_retention_period_in_seconds': 'float'
        }

        self.attribute_map = {
            'backup_space_used_in_gbs': 'backupSpaceUsedInGBs',
            'backup_space_estimate_in_gbs': 'backupSpaceEstimateInGBs',
            'unprotected_window_in_seconds': 'unprotectedWindowInSeconds',
            'db_size_in_gbs': 'dbSizeInGBs',
            'is_redo_logs_enabled': 'isRedoLogsEnabled',
            'retention_period_in_days': 'retentionPeriodInDays',
            'current_retention_period_in_seconds': 'currentRetentionPeriodInSeconds'
        }

        self._backup_space_used_in_gbs = None
        self._backup_space_estimate_in_gbs = None
        self._unprotected_window_in_seconds = None
        self._db_size_in_gbs = None
        self._is_redo_logs_enabled = None
        self._retention_period_in_days = None
        self._current_retention_period_in_seconds = None

    @property
    def backup_space_used_in_gbs(self):
        """
        Gets the backup_space_used_in_gbs of this Metrics.
        Backup storage space, in gigabytes, utilized by the protected database. Oracle charges for the total storage used.


        :return: The backup_space_used_in_gbs of this Metrics.
        :rtype: float
        """
        return self._backup_space_used_in_gbs

    @backup_space_used_in_gbs.setter
    def backup_space_used_in_gbs(self, backup_space_used_in_gbs):
        """
        Sets the backup_space_used_in_gbs of this Metrics.
        Backup storage space, in gigabytes, utilized by the protected database. Oracle charges for the total storage used.


        :param backup_space_used_in_gbs: The backup_space_used_in_gbs of this Metrics.
        :type: float
        """
        self._backup_space_used_in_gbs = backup_space_used_in_gbs

    @property
    def backup_space_estimate_in_gbs(self):
        """
        Gets the backup_space_estimate_in_gbs of this Metrics.
        The estimated backup storage space, in gigabytes, required to meet the recovery window goal, including foot print and backups for the protected database.


        :return: The backup_space_estimate_in_gbs of this Metrics.
        :rtype: float
        """
        return self._backup_space_estimate_in_gbs

    @backup_space_estimate_in_gbs.setter
    def backup_space_estimate_in_gbs(self, backup_space_estimate_in_gbs):
        """
        Sets the backup_space_estimate_in_gbs of this Metrics.
        The estimated backup storage space, in gigabytes, required to meet the recovery window goal, including foot print and backups for the protected database.


        :param backup_space_estimate_in_gbs: The backup_space_estimate_in_gbs of this Metrics.
        :type: float
        """
        self._backup_space_estimate_in_gbs = backup_space_estimate_in_gbs

    @property
    def unprotected_window_in_seconds(self):
        """
        Gets the unprotected_window_in_seconds of this Metrics.
        This is the time window when there is data loss exposure. The point after which recovery is impossible unless additional redo is available.
        This is the time we received the last backup or last redo-log shipped.


        :return: The unprotected_window_in_seconds of this Metrics.
        :rtype: float
        """
        return self._unprotected_window_in_seconds

    @unprotected_window_in_seconds.setter
    def unprotected_window_in_seconds(self, unprotected_window_in_seconds):
        """
        Sets the unprotected_window_in_seconds of this Metrics.
        This is the time window when there is data loss exposure. The point after which recovery is impossible unless additional redo is available.
        This is the time we received the last backup or last redo-log shipped.


        :param unprotected_window_in_seconds: The unprotected_window_in_seconds of this Metrics.
        :type: float
        """
        self._unprotected_window_in_seconds = unprotected_window_in_seconds

    @property
    def db_size_in_gbs(self):
        """
        Gets the db_size_in_gbs of this Metrics.
        The estimated space, in gigabytes, consumed by the protected database. The database size is based on the size of the data files in the catalog, and does not include archive logs.


        :return: The db_size_in_gbs of this Metrics.
        :rtype: float
        """
        return self._db_size_in_gbs

    @db_size_in_gbs.setter
    def db_size_in_gbs(self, db_size_in_gbs):
        """
        Sets the db_size_in_gbs of this Metrics.
        The estimated space, in gigabytes, consumed by the protected database. The database size is based on the size of the data files in the catalog, and does not include archive logs.


        :param db_size_in_gbs: The db_size_in_gbs of this Metrics.
        :type: float
        """
        self._db_size_in_gbs = db_size_in_gbs

    @property
    def is_redo_logs_enabled(self):
        """
        Gets the is_redo_logs_enabled of this Metrics.
        The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service.
        Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups.


        :return: The is_redo_logs_enabled of this Metrics.
        :rtype: bool
        """
        return self._is_redo_logs_enabled

    @is_redo_logs_enabled.setter
    def is_redo_logs_enabled(self, is_redo_logs_enabled):
        """
        Sets the is_redo_logs_enabled of this Metrics.
        The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service.
        Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups.


        :param is_redo_logs_enabled: The is_redo_logs_enabled of this Metrics.
        :type: bool
        """
        self._is_redo_logs_enabled = is_redo_logs_enabled

    @property
    def retention_period_in_days(self):
        """
        Gets the retention_period_in_days of this Metrics.
        The maximum number of days to retain backups for a protected database.


        :return: The retention_period_in_days of this Metrics.
        :rtype: float
        """
        return self._retention_period_in_days

    @retention_period_in_days.setter
    def retention_period_in_days(self, retention_period_in_days):
        """
        Sets the retention_period_in_days of this Metrics.
        The maximum number of days to retain backups for a protected database.


        :param retention_period_in_days: The retention_period_in_days of this Metrics.
        :type: float
        """
        self._retention_period_in_days = retention_period_in_days

    @property
    def current_retention_period_in_seconds(self):
        """
        Gets the current_retention_period_in_seconds of this Metrics.
        Number of seconds backups are currently retained for this database.


        :return: The current_retention_period_in_seconds of this Metrics.
        :rtype: float
        """
        return self._current_retention_period_in_seconds

    @current_retention_period_in_seconds.setter
    def current_retention_period_in_seconds(self, current_retention_period_in_seconds):
        """
        Sets the current_retention_period_in_seconds of this Metrics.
        Number of seconds backups are currently retained for this database.


        :param current_retention_period_in_seconds: The current_retention_period_in_seconds of this Metrics.
        :type: float
        """
        self._current_retention_period_in_seconds = current_retention_period_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
