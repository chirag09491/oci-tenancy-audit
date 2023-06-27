# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlPlanBaseline(object):
    """
    The details of a SQL plan baseline.
    """

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "ADDM_SQLTUNE"
    ORIGIN_ADDM_SQLTUNE = "ADDM_SQLTUNE"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "AUTO_CAPTURE"
    ORIGIN_AUTO_CAPTURE = "AUTO_CAPTURE"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "AUTO_SQLTUNE"
    ORIGIN_AUTO_SQLTUNE = "AUTO_SQLTUNE"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "EVOLVE_AUTO_INDEX_LOAD"
    ORIGIN_EVOLVE_AUTO_INDEX_LOAD = "EVOLVE_AUTO_INDEX_LOAD"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "EVOLVE_CREATE_FROM_ADAPTIVE"
    ORIGIN_EVOLVE_CREATE_FROM_ADAPTIVE = "EVOLVE_CREATE_FROM_ADAPTIVE"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "EVOLVE_LOAD_FROM_STS"
    ORIGIN_EVOLVE_LOAD_FROM_STS = "EVOLVE_LOAD_FROM_STS"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "EVOLVE_LOAD_FROM_AWR"
    ORIGIN_EVOLVE_LOAD_FROM_AWR = "EVOLVE_LOAD_FROM_AWR"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "EVOLVE_LOAD_FROM_CURSOR_CACHE"
    ORIGIN_EVOLVE_LOAD_FROM_CURSOR_CACHE = "EVOLVE_LOAD_FROM_CURSOR_CACHE"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "MANUAL_LOAD"
    ORIGIN_MANUAL_LOAD = "MANUAL_LOAD"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "MANUAL_LOAD_FROM_AWR"
    ORIGIN_MANUAL_LOAD_FROM_AWR = "MANUAL_LOAD_FROM_AWR"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "MANUAL_LOAD_FROM_CURSOR_CACHE"
    ORIGIN_MANUAL_LOAD_FROM_CURSOR_CACHE = "MANUAL_LOAD_FROM_CURSOR_CACHE"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "MANUAL_LOAD_FROM_STS"
    ORIGIN_MANUAL_LOAD_FROM_STS = "MANUAL_LOAD_FROM_STS"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "MANUAL_SQLTUNE"
    ORIGIN_MANUAL_SQLTUNE = "MANUAL_SQLTUNE"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "STORED_OUTLINE"
    ORIGIN_STORED_OUTLINE = "STORED_OUTLINE"

    #: A constant which can be used with the origin property of a SqlPlanBaseline.
    #: This constant has a value of "UNKNOWN"
    ORIGIN_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlPlanBaseline object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plan_name:
            The value to assign to the plan_name property of this SqlPlanBaseline.
        :type plan_name: str

        :param sql_handle:
            The value to assign to the sql_handle property of this SqlPlanBaseline.
        :type sql_handle: str

        :param sql_text:
            The value to assign to the sql_text property of this SqlPlanBaseline.
        :type sql_text: str

        :param origin:
            The value to assign to the origin property of this SqlPlanBaseline.
            Allowed values for this property are: "ADDM_SQLTUNE", "AUTO_CAPTURE", "AUTO_SQLTUNE", "EVOLVE_AUTO_INDEX_LOAD", "EVOLVE_CREATE_FROM_ADAPTIVE", "EVOLVE_LOAD_FROM_STS", "EVOLVE_LOAD_FROM_AWR", "EVOLVE_LOAD_FROM_CURSOR_CACHE", "MANUAL_LOAD", "MANUAL_LOAD_FROM_AWR", "MANUAL_LOAD_FROM_CURSOR_CACHE", "MANUAL_LOAD_FROM_STS", "MANUAL_SQLTUNE", "STORED_OUTLINE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type origin: str

        :param time_created:
            The value to assign to the time_created property of this SqlPlanBaseline.
        :type time_created: datetime

        :param time_last_modified:
            The value to assign to the time_last_modified property of this SqlPlanBaseline.
        :type time_last_modified: datetime

        :param time_last_executed:
            The value to assign to the time_last_executed property of this SqlPlanBaseline.
        :type time_last_executed: datetime

        :param enabled:
            The value to assign to the enabled property of this SqlPlanBaseline.
        :type enabled: str

        :param accepted:
            The value to assign to the accepted property of this SqlPlanBaseline.
        :type accepted: str

        :param fixed:
            The value to assign to the fixed property of this SqlPlanBaseline.
        :type fixed: str

        :param reproduced:
            The value to assign to the reproduced property of this SqlPlanBaseline.
        :type reproduced: str

        :param auto_purge:
            The value to assign to the auto_purge property of this SqlPlanBaseline.
        :type auto_purge: str

        :param adaptive:
            The value to assign to the adaptive property of this SqlPlanBaseline.
        :type adaptive: str

        :param module:
            The value to assign to the module property of this SqlPlanBaseline.
        :type module: str

        :param action:
            The value to assign to the action property of this SqlPlanBaseline.
        :type action: str

        :param execution_plan:
            The value to assign to the execution_plan property of this SqlPlanBaseline.
        :type execution_plan: str

        """
        self.swagger_types = {
            'plan_name': 'str',
            'sql_handle': 'str',
            'sql_text': 'str',
            'origin': 'str',
            'time_created': 'datetime',
            'time_last_modified': 'datetime',
            'time_last_executed': 'datetime',
            'enabled': 'str',
            'accepted': 'str',
            'fixed': 'str',
            'reproduced': 'str',
            'auto_purge': 'str',
            'adaptive': 'str',
            'module': 'str',
            'action': 'str',
            'execution_plan': 'str'
        }

        self.attribute_map = {
            'plan_name': 'planName',
            'sql_handle': 'sqlHandle',
            'sql_text': 'sqlText',
            'origin': 'origin',
            'time_created': 'timeCreated',
            'time_last_modified': 'timeLastModified',
            'time_last_executed': 'timeLastExecuted',
            'enabled': 'enabled',
            'accepted': 'accepted',
            'fixed': 'fixed',
            'reproduced': 'reproduced',
            'auto_purge': 'autoPurge',
            'adaptive': 'adaptive',
            'module': 'module',
            'action': 'action',
            'execution_plan': 'executionPlan'
        }

        self._plan_name = None
        self._sql_handle = None
        self._sql_text = None
        self._origin = None
        self._time_created = None
        self._time_last_modified = None
        self._time_last_executed = None
        self._enabled = None
        self._accepted = None
        self._fixed = None
        self._reproduced = None
        self._auto_purge = None
        self._adaptive = None
        self._module = None
        self._action = None
        self._execution_plan = None

    @property
    def plan_name(self):
        """
        **[Required]** Gets the plan_name of this SqlPlanBaseline.
        The unique plan identifier.


        :return: The plan_name of this SqlPlanBaseline.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """
        Sets the plan_name of this SqlPlanBaseline.
        The unique plan identifier.


        :param plan_name: The plan_name of this SqlPlanBaseline.
        :type: str
        """
        self._plan_name = plan_name

    @property
    def sql_handle(self):
        """
        **[Required]** Gets the sql_handle of this SqlPlanBaseline.
        The unique SQL identifier.


        :return: The sql_handle of this SqlPlanBaseline.
        :rtype: str
        """
        return self._sql_handle

    @sql_handle.setter
    def sql_handle(self, sql_handle):
        """
        Sets the sql_handle of this SqlPlanBaseline.
        The unique SQL identifier.


        :param sql_handle: The sql_handle of this SqlPlanBaseline.
        :type: str
        """
        self._sql_handle = sql_handle

    @property
    def sql_text(self):
        """
        **[Required]** Gets the sql_text of this SqlPlanBaseline.
        The SQL text.


        :return: The sql_text of this SqlPlanBaseline.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        """
        Sets the sql_text of this SqlPlanBaseline.
        The SQL text.


        :param sql_text: The sql_text of this SqlPlanBaseline.
        :type: str
        """
        self._sql_text = sql_text

    @property
    def origin(self):
        """
        Gets the origin of this SqlPlanBaseline.
        The origin of the SQL plan baseline.

        Allowed values for this property are: "ADDM_SQLTUNE", "AUTO_CAPTURE", "AUTO_SQLTUNE", "EVOLVE_AUTO_INDEX_LOAD", "EVOLVE_CREATE_FROM_ADAPTIVE", "EVOLVE_LOAD_FROM_STS", "EVOLVE_LOAD_FROM_AWR", "EVOLVE_LOAD_FROM_CURSOR_CACHE", "MANUAL_LOAD", "MANUAL_LOAD_FROM_AWR", "MANUAL_LOAD_FROM_CURSOR_CACHE", "MANUAL_LOAD_FROM_STS", "MANUAL_SQLTUNE", "STORED_OUTLINE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The origin of this SqlPlanBaseline.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """
        Sets the origin of this SqlPlanBaseline.
        The origin of the SQL plan baseline.


        :param origin: The origin of this SqlPlanBaseline.
        :type: str
        """
        allowed_values = ["ADDM_SQLTUNE", "AUTO_CAPTURE", "AUTO_SQLTUNE", "EVOLVE_AUTO_INDEX_LOAD", "EVOLVE_CREATE_FROM_ADAPTIVE", "EVOLVE_LOAD_FROM_STS", "EVOLVE_LOAD_FROM_AWR", "EVOLVE_LOAD_FROM_CURSOR_CACHE", "MANUAL_LOAD", "MANUAL_LOAD_FROM_AWR", "MANUAL_LOAD_FROM_CURSOR_CACHE", "MANUAL_LOAD_FROM_STS", "MANUAL_SQLTUNE", "STORED_OUTLINE", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(origin, allowed_values):
            origin = 'UNKNOWN_ENUM_VALUE'
        self._origin = origin

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SqlPlanBaseline.
        The date and time when the plan baseline was created.


        :return: The time_created of this SqlPlanBaseline.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SqlPlanBaseline.
        The date and time when the plan baseline was created.


        :param time_created: The time_created of this SqlPlanBaseline.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_last_modified(self):
        """
        Gets the time_last_modified of this SqlPlanBaseline.
        The date and time when the plan baseline was last modified.


        :return: The time_last_modified of this SqlPlanBaseline.
        :rtype: datetime
        """
        return self._time_last_modified

    @time_last_modified.setter
    def time_last_modified(self, time_last_modified):
        """
        Sets the time_last_modified of this SqlPlanBaseline.
        The date and time when the plan baseline was last modified.


        :param time_last_modified: The time_last_modified of this SqlPlanBaseline.
        :type: datetime
        """
        self._time_last_modified = time_last_modified

    @property
    def time_last_executed(self):
        """
        Gets the time_last_executed of this SqlPlanBaseline.
        The date and time when the plan baseline was last executed.

        **Note:** For performance reasons, database does not update this value
        immediately after each execution of the plan baseline. Therefore, the plan
        baseline may have been executed more recently than this value indicates.


        :return: The time_last_executed of this SqlPlanBaseline.
        :rtype: datetime
        """
        return self._time_last_executed

    @time_last_executed.setter
    def time_last_executed(self, time_last_executed):
        """
        Sets the time_last_executed of this SqlPlanBaseline.
        The date and time when the plan baseline was last executed.

        **Note:** For performance reasons, database does not update this value
        immediately after each execution of the plan baseline. Therefore, the plan
        baseline may have been executed more recently than this value indicates.


        :param time_last_executed: The time_last_executed of this SqlPlanBaseline.
        :type: datetime
        """
        self._time_last_executed = time_last_executed

    @property
    def enabled(self):
        """
        Gets the enabled of this SqlPlanBaseline.
        Indicates whether the plan baseline is enabled (`YES`) or disabled (`NO`).


        :return: The enabled of this SqlPlanBaseline.
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SqlPlanBaseline.
        Indicates whether the plan baseline is enabled (`YES`) or disabled (`NO`).


        :param enabled: The enabled of this SqlPlanBaseline.
        :type: str
        """
        self._enabled = enabled

    @property
    def accepted(self):
        """
        Gets the accepted of this SqlPlanBaseline.
        Indicates whether the plan baseline is accepted (`YES`) or not (`NO`).


        :return: The accepted of this SqlPlanBaseline.
        :rtype: str
        """
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        """
        Sets the accepted of this SqlPlanBaseline.
        Indicates whether the plan baseline is accepted (`YES`) or not (`NO`).


        :param accepted: The accepted of this SqlPlanBaseline.
        :type: str
        """
        self._accepted = accepted

    @property
    def fixed(self):
        """
        Gets the fixed of this SqlPlanBaseline.
        Indicates whether the plan baseline is fixed (`YES`) or not (`NO`).


        :return: The fixed of this SqlPlanBaseline.
        :rtype: str
        """
        return self._fixed

    @fixed.setter
    def fixed(self, fixed):
        """
        Sets the fixed of this SqlPlanBaseline.
        Indicates whether the plan baseline is fixed (`YES`) or not (`NO`).


        :param fixed: The fixed of this SqlPlanBaseline.
        :type: str
        """
        self._fixed = fixed

    @property
    def reproduced(self):
        """
        Gets the reproduced of this SqlPlanBaseline.
        Indicates whether the optimizer was able to reproduce the plan (`YES`) or not (`NO`).
        The value is set to `YES` when a plan is initially added to the plan baseline.


        :return: The reproduced of this SqlPlanBaseline.
        :rtype: str
        """
        return self._reproduced

    @reproduced.setter
    def reproduced(self, reproduced):
        """
        Sets the reproduced of this SqlPlanBaseline.
        Indicates whether the optimizer was able to reproduce the plan (`YES`) or not (`NO`).
        The value is set to `YES` when a plan is initially added to the plan baseline.


        :param reproduced: The reproduced of this SqlPlanBaseline.
        :type: str
        """
        self._reproduced = reproduced

    @property
    def auto_purge(self):
        """
        Gets the auto_purge of this SqlPlanBaseline.
        Indicates whether the plan baseline is auto-purged (`YES`) or not (`NO`).


        :return: The auto_purge of this SqlPlanBaseline.
        :rtype: str
        """
        return self._auto_purge

    @auto_purge.setter
    def auto_purge(self, auto_purge):
        """
        Sets the auto_purge of this SqlPlanBaseline.
        Indicates whether the plan baseline is auto-purged (`YES`) or not (`NO`).


        :param auto_purge: The auto_purge of this SqlPlanBaseline.
        :type: str
        """
        self._auto_purge = auto_purge

    @property
    def adaptive(self):
        """
        Gets the adaptive of this SqlPlanBaseline.
        Indicates whether a plan that is automatically captured by SQL plan management is marked adaptive or not.

        When a new adaptive plan is found for a SQL statement that has an existing SQL plan baseline, that new plan
        will be added to the SQL plan baseline as an unaccepted plan, and the `ADAPTIVE` property will be marked `YES`.
        When this new plan is verified (either manually or via the auto evolve task), the plan will be test executed
        and the final plan determined at execution will become an accepted plan if its performance is better than
        the existing plan baseline. At this point, the value of the `ADAPTIVE` property is set to `NO` since the plan
        is no longer adaptive, but resolved.


        :return: The adaptive of this SqlPlanBaseline.
        :rtype: str
        """
        return self._adaptive

    @adaptive.setter
    def adaptive(self, adaptive):
        """
        Sets the adaptive of this SqlPlanBaseline.
        Indicates whether a plan that is automatically captured by SQL plan management is marked adaptive or not.

        When a new adaptive plan is found for a SQL statement that has an existing SQL plan baseline, that new plan
        will be added to the SQL plan baseline as an unaccepted plan, and the `ADAPTIVE` property will be marked `YES`.
        When this new plan is verified (either manually or via the auto evolve task), the plan will be test executed
        and the final plan determined at execution will become an accepted plan if its performance is better than
        the existing plan baseline. At this point, the value of the `ADAPTIVE` property is set to `NO` since the plan
        is no longer adaptive, but resolved.


        :param adaptive: The adaptive of this SqlPlanBaseline.
        :type: str
        """
        self._adaptive = adaptive

    @property
    def module(self):
        """
        Gets the module of this SqlPlanBaseline.
        The application module name.


        :return: The module of this SqlPlanBaseline.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """
        Sets the module of this SqlPlanBaseline.
        The application module name.


        :param module: The module of this SqlPlanBaseline.
        :type: str
        """
        self._module = module

    @property
    def action(self):
        """
        Gets the action of this SqlPlanBaseline.
        The application action.


        :return: The action of this SqlPlanBaseline.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this SqlPlanBaseline.
        The application action.


        :param action: The action of this SqlPlanBaseline.
        :type: str
        """
        self._action = action

    @property
    def execution_plan(self):
        """
        **[Required]** Gets the execution_plan of this SqlPlanBaseline.
        The execution plan for the SQL statement.


        :return: The execution_plan of this SqlPlanBaseline.
        :rtype: str
        """
        return self._execution_plan

    @execution_plan.setter
    def execution_plan(self, execution_plan):
        """
        Sets the execution_plan of this SqlPlanBaseline.
        The execution plan for the SQL statement.


        :param execution_plan: The execution_plan of this SqlPlanBaseline.
        :type: str
        """
        self._execution_plan = execution_plan

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other