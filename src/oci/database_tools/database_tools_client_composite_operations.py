# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201005

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class DatabaseToolsClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.database_tools.DatabaseToolsClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new DatabaseToolsClientCompositeOperations object

        :param DatabaseToolsClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def add_database_tools_connection_lock_and_wait_for_state(self, database_tools_connection_id, add_resource_lock_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_tools.DatabaseToolsClient.add_database_tools_connection_lock` and waits for the :py:class:`~oci.database_tools.models.DatabaseToolsConnection` acted upon
        to enter the given state(s).

        :param str database_tools_connection_id: (required)
            The `OCID`__ of a Database Tools connection.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_tools.models.AddResourceLockDetails add_resource_lock_details: (required)
            AddResourceLockDetails body parameter

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_tools.models.DatabaseToolsConnection.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_tools.DatabaseToolsClient.add_database_tools_connection_lock`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.add_database_tools_connection_lock(database_tools_connection_id, add_resource_lock_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        database_tools_connection_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_database_tools_connection(database_tools_connection_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def add_database_tools_private_endpoint_lock_and_wait_for_state(self, database_tools_private_endpoint_id, add_resource_lock_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_tools.DatabaseToolsClient.add_database_tools_private_endpoint_lock` and waits for the :py:class:`~oci.database_tools.models.DatabaseToolsPrivateEndpoint` acted upon
        to enter the given state(s).

        :param str database_tools_private_endpoint_id: (required)
            The `OCID`__ of a Database Tools private endpoint.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_tools.models.AddResourceLockDetails add_resource_lock_details: (required)
            AddResourceLockDetails body parameter

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_tools.models.DatabaseToolsPrivateEndpoint.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_tools.DatabaseToolsClient.add_database_tools_private_endpoint_lock`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.add_database_tools_private_endpoint_lock(database_tools_private_endpoint_id, add_resource_lock_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        database_tools_private_endpoint_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_database_tools_private_endpoint(database_tools_private_endpoint_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def change_database_tools_connection_compartment_and_wait_for_state(self, database_tools_connection_id, change_database_tools_connection_compartment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_tools.DatabaseToolsClient.change_database_tools_connection_compartment` and waits for the :py:class:`~oci.database_tools.models.WorkRequest`
        to enter the given state(s).

        :param str database_tools_connection_id: (required)
            The `OCID`__ of a Database Tools connection.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_tools.models.ChangeDatabaseToolsConnectionCompartmentDetails change_database_tools_connection_compartment_details: (required)
            Request to change the compartment of the DatabaseToolsConnection.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_tools.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_tools.DatabaseToolsClient.change_database_tools_connection_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_database_tools_connection_compartment(database_tools_connection_id, change_database_tools_connection_compartment_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def change_database_tools_private_endpoint_compartment_and_wait_for_state(self, database_tools_private_endpoint_id, change_database_tools_private_endpoint_compartment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_tools.DatabaseToolsClient.change_database_tools_private_endpoint_compartment` and waits for the :py:class:`~oci.database_tools.models.WorkRequest`
        to enter the given state(s).

        :param str database_tools_private_endpoint_id: (required)
            The `OCID`__ of a Database Tools private endpoint.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_tools.models.ChangeDatabaseToolsPrivateEndpointCompartmentDetails change_database_tools_private_endpoint_compartment_details: (required)
            Request to change the compartment of the DatabaseToolsPrivateEndpoint.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_tools.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_tools.DatabaseToolsClient.change_database_tools_private_endpoint_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_database_tools_private_endpoint_compartment(database_tools_private_endpoint_id, change_database_tools_private_endpoint_compartment_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_database_tools_connection_and_wait_for_state(self, create_database_tools_connection_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_tools.DatabaseToolsClient.create_database_tools_connection` and waits for the :py:class:`~oci.database_tools.models.WorkRequest`
        to enter the given state(s).

        :param oci.database_tools.models.CreateDatabaseToolsConnectionDetails create_database_tools_connection_details: (required)
            Details for the new `DatabaseToolsConnection`.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_tools.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_tools.DatabaseToolsClient.create_database_tools_connection`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_database_tools_connection(create_database_tools_connection_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_database_tools_private_endpoint_and_wait_for_state(self, create_database_tools_private_endpoint_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_tools.DatabaseToolsClient.create_database_tools_private_endpoint` and waits for the :py:class:`~oci.database_tools.models.WorkRequest`
        to enter the given state(s).

        :param oci.database_tools.models.CreateDatabaseToolsPrivateEndpointDetails create_database_tools_private_endpoint_details: (required)
            Details for the new DatabaseToolsPrivateEndpoint.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_tools.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_tools.DatabaseToolsClient.create_database_tools_private_endpoint`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_database_tools_private_endpoint(create_database_tools_private_endpoint_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_database_tools_connection_and_wait_for_state(self, database_tools_connection_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_tools.DatabaseToolsClient.delete_database_tools_connection` and waits for the :py:class:`~oci.database_tools.models.WorkRequest`
        to enter the given state(s).

        :param str database_tools_connection_id: (required)
            The `OCID`__ of a Database Tools connection.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_tools.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_tools.DatabaseToolsClient.delete_database_tools_connection`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_database_tools_connection(database_tools_connection_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_database_tools_private_endpoint_and_wait_for_state(self, database_tools_private_endpoint_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_tools.DatabaseToolsClient.delete_database_tools_private_endpoint` and waits for the :py:class:`~oci.database_tools.models.WorkRequest`
        to enter the given state(s).

        :param str database_tools_private_endpoint_id: (required)
            The `OCID`__ of a Database Tools private endpoint.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_tools.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_tools.DatabaseToolsClient.delete_database_tools_private_endpoint`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_database_tools_private_endpoint(database_tools_private_endpoint_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def remove_database_tools_connection_lock_and_wait_for_state(self, database_tools_connection_id, remove_resource_lock_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_tools.DatabaseToolsClient.remove_database_tools_connection_lock` and waits for the :py:class:`~oci.database_tools.models.DatabaseToolsConnection` acted upon
        to enter the given state(s).

        :param str database_tools_connection_id: (required)
            The `OCID`__ of a Database Tools connection.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_tools.models.RemoveResourceLockDetails remove_resource_lock_details: (required)
            RemoveResourceLockDetails body parameter

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_tools.models.DatabaseToolsConnection.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_tools.DatabaseToolsClient.remove_database_tools_connection_lock`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.remove_database_tools_connection_lock(database_tools_connection_id, remove_resource_lock_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        database_tools_connection_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_database_tools_connection(database_tools_connection_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def remove_database_tools_private_endpoint_lock_and_wait_for_state(self, database_tools_private_endpoint_id, remove_resource_lock_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_tools.DatabaseToolsClient.remove_database_tools_private_endpoint_lock` and waits for the :py:class:`~oci.database_tools.models.DatabaseToolsPrivateEndpoint` acted upon
        to enter the given state(s).

        :param str database_tools_private_endpoint_id: (required)
            The `OCID`__ of a Database Tools private endpoint.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_tools.models.RemoveResourceLockDetails remove_resource_lock_details: (required)
            RemoveResourceLockDetails body parameter

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_tools.models.DatabaseToolsPrivateEndpoint.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_tools.DatabaseToolsClient.remove_database_tools_private_endpoint_lock`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.remove_database_tools_private_endpoint_lock(database_tools_private_endpoint_id, remove_resource_lock_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        database_tools_private_endpoint_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_database_tools_private_endpoint(database_tools_private_endpoint_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_database_tools_connection_and_wait_for_state(self, database_tools_connection_id, update_database_tools_connection_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_tools.DatabaseToolsClient.update_database_tools_connection` and waits for the :py:class:`~oci.database_tools.models.WorkRequest`
        to enter the given state(s).

        :param str database_tools_connection_id: (required)
            The `OCID`__ of a Database Tools connection.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_tools.models.UpdateDatabaseToolsConnectionDetails update_database_tools_connection_details: (required)
            The information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_tools.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_tools.DatabaseToolsClient.update_database_tools_connection`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_database_tools_connection(database_tools_connection_id, update_database_tools_connection_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_database_tools_private_endpoint_and_wait_for_state(self, database_tools_private_endpoint_id, update_database_tools_private_endpoint_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.database_tools.DatabaseToolsClient.update_database_tools_private_endpoint` and waits for the :py:class:`~oci.database_tools.models.WorkRequest`
        to enter the given state(s).

        :param str database_tools_private_endpoint_id: (required)
            The `OCID`__ of a Database Tools private endpoint.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_tools.models.UpdateDatabaseToolsPrivateEndpointDetails update_database_tools_private_endpoint_details: (required)
            The information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.database_tools.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.database_tools.DatabaseToolsClient.update_database_tools_private_endpoint`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_database_tools_private_endpoint(database_tools_private_endpoint_id, update_database_tools_private_endpoint_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
