# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Grant(object):
    """
    Schema for Grant Resource
    """

    #: A constant which can be used with the idcs_prevented_operations property of a Grant.
    #: This constant has a value of "replace"
    IDCS_PREVENTED_OPERATIONS_REPLACE = "replace"

    #: A constant which can be used with the idcs_prevented_operations property of a Grant.
    #: This constant has a value of "update"
    IDCS_PREVENTED_OPERATIONS_UPDATE = "update"

    #: A constant which can be used with the idcs_prevented_operations property of a Grant.
    #: This constant has a value of "delete"
    IDCS_PREVENTED_OPERATIONS_DELETE = "delete"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "IMPORT_APPROLE_MEMBERS"
    GRANT_MECHANISM_IMPORT_APPROLE_MEMBERS = "IMPORT_APPROLE_MEMBERS"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "ADMINISTRATOR_TO_USER"
    GRANT_MECHANISM_ADMINISTRATOR_TO_USER = "ADMINISTRATOR_TO_USER"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "ADMINISTRATOR_TO_DELEGATED_USER"
    GRANT_MECHANISM_ADMINISTRATOR_TO_DELEGATED_USER = "ADMINISTRATOR_TO_DELEGATED_USER"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "ADMINISTRATOR_TO_GROUP"
    GRANT_MECHANISM_ADMINISTRATOR_TO_GROUP = "ADMINISTRATOR_TO_GROUP"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "SERVICE_MANAGER_TO_USER"
    GRANT_MECHANISM_SERVICE_MANAGER_TO_USER = "SERVICE_MANAGER_TO_USER"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "ADMINISTRATOR_TO_APP"
    GRANT_MECHANISM_ADMINISTRATOR_TO_APP = "ADMINISTRATOR_TO_APP"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "SERVICE_MANAGER_TO_APP"
    GRANT_MECHANISM_SERVICE_MANAGER_TO_APP = "SERVICE_MANAGER_TO_APP"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "OPC_INFRA_TO_APP"
    GRANT_MECHANISM_OPC_INFRA_TO_APP = "OPC_INFRA_TO_APP"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "GROUP_MEMBERSHIP"
    GRANT_MECHANISM_GROUP_MEMBERSHIP = "GROUP_MEMBERSHIP"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "IMPORT_GRANTS"
    GRANT_MECHANISM_IMPORT_GRANTS = "IMPORT_GRANTS"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "SYNC_TO_USER"
    GRANT_MECHANISM_SYNC_TO_USER = "SYNC_TO_USER"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "ACCESS_REQUEST"
    GRANT_MECHANISM_ACCESS_REQUEST = "ACCESS_REQUEST"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "APP_ENTITLEMENT_COLLECTION"
    GRANT_MECHANISM_APP_ENTITLEMENT_COLLECTION = "APP_ENTITLEMENT_COLLECTION"

    #: A constant which can be used with the grant_mechanism property of a Grant.
    #: This constant has a value of "ADMINISTRATOR_TO_DYNAMIC_RESOURCE_GROUP"
    GRANT_MECHANISM_ADMINISTRATOR_TO_DYNAMIC_RESOURCE_GROUP = "ADMINISTRATOR_TO_DYNAMIC_RESOURCE_GROUP"

    def __init__(self, **kwargs):
        """
        Initializes a new Grant object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Grant.
        :type id: str

        :param ocid:
            The value to assign to the ocid property of this Grant.
        :type ocid: str

        :param schemas:
            The value to assign to the schemas property of this Grant.
        :type schemas: list[str]

        :param meta:
            The value to assign to the meta property of this Grant.
        :type meta: oci.identity_domains.models.Meta

        :param idcs_created_by:
            The value to assign to the idcs_created_by property of this Grant.
        :type idcs_created_by: oci.identity_domains.models.IdcsCreatedBy

        :param idcs_last_modified_by:
            The value to assign to the idcs_last_modified_by property of this Grant.
        :type idcs_last_modified_by: oci.identity_domains.models.IdcsLastModifiedBy

        :param idcs_prevented_operations:
            The value to assign to the idcs_prevented_operations property of this Grant.
            Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type idcs_prevented_operations: list[str]

        :param tags:
            The value to assign to the tags property of this Grant.
        :type tags: list[oci.identity_domains.models.Tags]

        :param delete_in_progress:
            The value to assign to the delete_in_progress property of this Grant.
        :type delete_in_progress: bool

        :param idcs_last_upgraded_in_release:
            The value to assign to the idcs_last_upgraded_in_release property of this Grant.
        :type idcs_last_upgraded_in_release: str

        :param domain_ocid:
            The value to assign to the domain_ocid property of this Grant.
        :type domain_ocid: str

        :param compartment_ocid:
            The value to assign to the compartment_ocid property of this Grant.
        :type compartment_ocid: str

        :param tenancy_ocid:
            The value to assign to the tenancy_ocid property of this Grant.
        :type tenancy_ocid: str

        :param grant_mechanism:
            The value to assign to the grant_mechanism property of this Grant.
            Allowed values for this property are: "IMPORT_APPROLE_MEMBERS", "ADMINISTRATOR_TO_USER", "ADMINISTRATOR_TO_DELEGATED_USER", "ADMINISTRATOR_TO_GROUP", "SERVICE_MANAGER_TO_USER", "ADMINISTRATOR_TO_APP", "SERVICE_MANAGER_TO_APP", "OPC_INFRA_TO_APP", "GROUP_MEMBERSHIP", "IMPORT_GRANTS", "SYNC_TO_USER", "ACCESS_REQUEST", "APP_ENTITLEMENT_COLLECTION", "ADMINISTRATOR_TO_DYNAMIC_RESOURCE_GROUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type grant_mechanism: str

        :param composite_key:
            The value to assign to the composite_key property of this Grant.
        :type composite_key: str

        :param is_fulfilled:
            The value to assign to the is_fulfilled property of this Grant.
        :type is_fulfilled: bool

        :param granted_attribute_values_json:
            The value to assign to the granted_attribute_values_json property of this Grant.
        :type granted_attribute_values_json: str

        :param app_entitlement_collection:
            The value to assign to the app_entitlement_collection property of this Grant.
        :type app_entitlement_collection: oci.identity_domains.models.GrantAppEntitlementCollection

        :param grantor:
            The value to assign to the grantor property of this Grant.
        :type grantor: oci.identity_domains.models.GrantGrantor

        :param grantee:
            The value to assign to the grantee property of this Grant.
        :type grantee: oci.identity_domains.models.GrantGrantee

        :param app:
            The value to assign to the app property of this Grant.
        :type app: oci.identity_domains.models.GrantApp

        :param entitlement:
            The value to assign to the entitlement property of this Grant.
        :type entitlement: oci.identity_domains.models.GrantEntitlement

        """
        self.swagger_types = {
            'id': 'str',
            'ocid': 'str',
            'schemas': 'list[str]',
            'meta': 'Meta',
            'idcs_created_by': 'IdcsCreatedBy',
            'idcs_last_modified_by': 'IdcsLastModifiedBy',
            'idcs_prevented_operations': 'list[str]',
            'tags': 'list[Tags]',
            'delete_in_progress': 'bool',
            'idcs_last_upgraded_in_release': 'str',
            'domain_ocid': 'str',
            'compartment_ocid': 'str',
            'tenancy_ocid': 'str',
            'grant_mechanism': 'str',
            'composite_key': 'str',
            'is_fulfilled': 'bool',
            'granted_attribute_values_json': 'str',
            'app_entitlement_collection': 'GrantAppEntitlementCollection',
            'grantor': 'GrantGrantor',
            'grantee': 'GrantGrantee',
            'app': 'GrantApp',
            'entitlement': 'GrantEntitlement'
        }

        self.attribute_map = {
            'id': 'id',
            'ocid': 'ocid',
            'schemas': 'schemas',
            'meta': 'meta',
            'idcs_created_by': 'idcsCreatedBy',
            'idcs_last_modified_by': 'idcsLastModifiedBy',
            'idcs_prevented_operations': 'idcsPreventedOperations',
            'tags': 'tags',
            'delete_in_progress': 'deleteInProgress',
            'idcs_last_upgraded_in_release': 'idcsLastUpgradedInRelease',
            'domain_ocid': 'domainOcid',
            'compartment_ocid': 'compartmentOcid',
            'tenancy_ocid': 'tenancyOcid',
            'grant_mechanism': 'grantMechanism',
            'composite_key': 'compositeKey',
            'is_fulfilled': 'isFulfilled',
            'granted_attribute_values_json': 'grantedAttributeValuesJson',
            'app_entitlement_collection': 'appEntitlementCollection',
            'grantor': 'grantor',
            'grantee': 'grantee',
            'app': 'app',
            'entitlement': 'entitlement'
        }

        self._id = None
        self._ocid = None
        self._schemas = None
        self._meta = None
        self._idcs_created_by = None
        self._idcs_last_modified_by = None
        self._idcs_prevented_operations = None
        self._tags = None
        self._delete_in_progress = None
        self._idcs_last_upgraded_in_release = None
        self._domain_ocid = None
        self._compartment_ocid = None
        self._tenancy_ocid = None
        self._grant_mechanism = None
        self._composite_key = None
        self._is_fulfilled = None
        self._granted_attribute_values_json = None
        self._app_entitlement_collection = None
        self._grantor = None
        self._grantee = None
        self._app = None
        self._entitlement = None

    @property
    def id(self):
        """
        Gets the id of this Grant.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :return: The id of this Grant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Grant.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :param id: The id of this Grant.
        :type: str
        """
        self._id = id

    @property
    def ocid(self):
        """
        Gets the ocid of this Grant.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :return: The ocid of this Grant.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this Grant.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :param ocid: The ocid of this Grant.
        :type: str
        """
        self._ocid = ocid

    @property
    def schemas(self):
        """
        **[Required]** Gets the schemas of this Grant.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The schemas of this Grant.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this Grant.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param schemas: The schemas of this Grant.
        :type: list[str]
        """
        self._schemas = schemas

    @property
    def meta(self):
        """
        Gets the meta of this Grant.

        :return: The meta of this Grant.
        :rtype: oci.identity_domains.models.Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this Grant.

        :param meta: The meta of this Grant.
        :type: oci.identity_domains.models.Meta
        """
        self._meta = meta

    @property
    def idcs_created_by(self):
        """
        Gets the idcs_created_by of this Grant.

        :return: The idcs_created_by of this Grant.
        :rtype: oci.identity_domains.models.IdcsCreatedBy
        """
        return self._idcs_created_by

    @idcs_created_by.setter
    def idcs_created_by(self, idcs_created_by):
        """
        Sets the idcs_created_by of this Grant.

        :param idcs_created_by: The idcs_created_by of this Grant.
        :type: oci.identity_domains.models.IdcsCreatedBy
        """
        self._idcs_created_by = idcs_created_by

    @property
    def idcs_last_modified_by(self):
        """
        Gets the idcs_last_modified_by of this Grant.

        :return: The idcs_last_modified_by of this Grant.
        :rtype: oci.identity_domains.models.IdcsLastModifiedBy
        """
        return self._idcs_last_modified_by

    @idcs_last_modified_by.setter
    def idcs_last_modified_by(self, idcs_last_modified_by):
        """
        Sets the idcs_last_modified_by of this Grant.

        :param idcs_last_modified_by: The idcs_last_modified_by of this Grant.
        :type: oci.identity_domains.models.IdcsLastModifiedBy
        """
        self._idcs_last_modified_by = idcs_last_modified_by

    @property
    def idcs_prevented_operations(self):
        """
        Gets the idcs_prevented_operations of this Grant.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none

        Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The idcs_prevented_operations of this Grant.
        :rtype: list[str]
        """
        return self._idcs_prevented_operations

    @idcs_prevented_operations.setter
    def idcs_prevented_operations(self, idcs_prevented_operations):
        """
        Sets the idcs_prevented_operations of this Grant.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_prevented_operations: The idcs_prevented_operations of this Grant.
        :type: list[str]
        """
        allowed_values = ["replace", "update", "delete"]
        if idcs_prevented_operations:
            idcs_prevented_operations[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in idcs_prevented_operations]
        self._idcs_prevented_operations = idcs_prevented_operations

    @property
    def tags(self):
        """
        Gets the tags of this Grant.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :return: The tags of this Grant.
        :rtype: list[oci.identity_domains.models.Tags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Grant.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :param tags: The tags of this Grant.
        :type: list[oci.identity_domains.models.Tags]
        """
        self._tags = tags

    @property
    def delete_in_progress(self):
        """
        Gets the delete_in_progress of this Grant.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The delete_in_progress of this Grant.
        :rtype: bool
        """
        return self._delete_in_progress

    @delete_in_progress.setter
    def delete_in_progress(self, delete_in_progress):
        """
        Sets the delete_in_progress of this Grant.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param delete_in_progress: The delete_in_progress of this Grant.
        :type: bool
        """
        self._delete_in_progress = delete_in_progress

    @property
    def idcs_last_upgraded_in_release(self):
        """
        Gets the idcs_last_upgraded_in_release of this Grant.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The idcs_last_upgraded_in_release of this Grant.
        :rtype: str
        """
        return self._idcs_last_upgraded_in_release

    @idcs_last_upgraded_in_release.setter
    def idcs_last_upgraded_in_release(self, idcs_last_upgraded_in_release):
        """
        Sets the idcs_last_upgraded_in_release of this Grant.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_last_upgraded_in_release: The idcs_last_upgraded_in_release of this Grant.
        :type: str
        """
        self._idcs_last_upgraded_in_release = idcs_last_upgraded_in_release

    @property
    def domain_ocid(self):
        """
        Gets the domain_ocid of this Grant.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The domain_ocid of this Grant.
        :rtype: str
        """
        return self._domain_ocid

    @domain_ocid.setter
    def domain_ocid(self, domain_ocid):
        """
        Sets the domain_ocid of this Grant.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param domain_ocid: The domain_ocid of this Grant.
        :type: str
        """
        self._domain_ocid = domain_ocid

    @property
    def compartment_ocid(self):
        """
        Gets the compartment_ocid of this Grant.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The compartment_ocid of this Grant.
        :rtype: str
        """
        return self._compartment_ocid

    @compartment_ocid.setter
    def compartment_ocid(self, compartment_ocid):
        """
        Sets the compartment_ocid of this Grant.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param compartment_ocid: The compartment_ocid of this Grant.
        :type: str
        """
        self._compartment_ocid = compartment_ocid

    @property
    def tenancy_ocid(self):
        """
        Gets the tenancy_ocid of this Grant.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The tenancy_ocid of this Grant.
        :rtype: str
        """
        return self._tenancy_ocid

    @tenancy_ocid.setter
    def tenancy_ocid(self, tenancy_ocid):
        """
        Sets the tenancy_ocid of this Grant.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param tenancy_ocid: The tenancy_ocid of this Grant.
        :type: str
        """
        self._tenancy_ocid = tenancy_ocid

    @property
    def grant_mechanism(self):
        """
        **[Required]** Gets the grant_mechanism of this Grant.
        Each value of grantMechanism indicates how (or by what component) some App (or App-Entitlement) was granted.
        A customer or the UI should use only grantMechanism values that start with 'ADMINISTRATOR':
          - 'ADMINISTRATOR_TO_USER' is for a direct grant to a specific User.
          - 'ADMINISTRATOR_TO_GROUP' is for a grant to a specific Group, which results in indirect grants to Users who are members of that Group.
          - 'ADMINISTRATOR_TO_APP' is for a grant to a specific App.  The grantee (client) App gains access to the granted (server) App.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsCsvAttributeNameMappings: [[defaultValue:IMPORT_GRANTS]]
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "IMPORT_APPROLE_MEMBERS", "ADMINISTRATOR_TO_USER", "ADMINISTRATOR_TO_DELEGATED_USER", "ADMINISTRATOR_TO_GROUP", "SERVICE_MANAGER_TO_USER", "ADMINISTRATOR_TO_APP", "SERVICE_MANAGER_TO_APP", "OPC_INFRA_TO_APP", "GROUP_MEMBERSHIP", "IMPORT_GRANTS", "SYNC_TO_USER", "ACCESS_REQUEST", "APP_ENTITLEMENT_COLLECTION", "ADMINISTRATOR_TO_DYNAMIC_RESOURCE_GROUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The grant_mechanism of this Grant.
        :rtype: str
        """
        return self._grant_mechanism

    @grant_mechanism.setter
    def grant_mechanism(self, grant_mechanism):
        """
        Sets the grant_mechanism of this Grant.
        Each value of grantMechanism indicates how (or by what component) some App (or App-Entitlement) was granted.
        A customer or the UI should use only grantMechanism values that start with 'ADMINISTRATOR':
          - 'ADMINISTRATOR_TO_USER' is for a direct grant to a specific User.
          - 'ADMINISTRATOR_TO_GROUP' is for a grant to a specific Group, which results in indirect grants to Users who are members of that Group.
          - 'ADMINISTRATOR_TO_APP' is for a grant to a specific App.  The grantee (client) App gains access to the granted (server) App.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsCsvAttributeNameMappings: [[defaultValue:IMPORT_GRANTS]]
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param grant_mechanism: The grant_mechanism of this Grant.
        :type: str
        """
        allowed_values = ["IMPORT_APPROLE_MEMBERS", "ADMINISTRATOR_TO_USER", "ADMINISTRATOR_TO_DELEGATED_USER", "ADMINISTRATOR_TO_GROUP", "SERVICE_MANAGER_TO_USER", "ADMINISTRATOR_TO_APP", "SERVICE_MANAGER_TO_APP", "OPC_INFRA_TO_APP", "GROUP_MEMBERSHIP", "IMPORT_GRANTS", "SYNC_TO_USER", "ACCESS_REQUEST", "APP_ENTITLEMENT_COLLECTION", "ADMINISTRATOR_TO_DYNAMIC_RESOURCE_GROUP"]
        if not value_allowed_none_or_none_sentinel(grant_mechanism, allowed_values):
            grant_mechanism = 'UNKNOWN_ENUM_VALUE'
        self._grant_mechanism = grant_mechanism

    @property
    def composite_key(self):
        """
        Gets the composite_key of this Grant.
        Unique key of grant, composed by combining a subset of app, entitlement, grantee, grantor and grantMechanism.  Used to prevent duplicate Grants.

        **Added In:** 18.1.2

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: server


        :return: The composite_key of this Grant.
        :rtype: str
        """
        return self._composite_key

    @composite_key.setter
    def composite_key(self, composite_key):
        """
        Sets the composite_key of this Grant.
        Unique key of grant, composed by combining a subset of app, entitlement, grantee, grantor and grantMechanism.  Used to prevent duplicate Grants.

        **Added In:** 18.1.2

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: server


        :param composite_key: The composite_key of this Grant.
        :type: str
        """
        self._composite_key = composite_key

    @property
    def is_fulfilled(self):
        """
        Gets the is_fulfilled of this Grant.
        If true, this Grant has been fulfilled successfully.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The is_fulfilled of this Grant.
        :rtype: bool
        """
        return self._is_fulfilled

    @is_fulfilled.setter
    def is_fulfilled(self, is_fulfilled):
        """
        Sets the is_fulfilled of this Grant.
        If true, this Grant has been fulfilled successfully.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param is_fulfilled: The is_fulfilled of this Grant.
        :type: bool
        """
        self._is_fulfilled = is_fulfilled

    @property
    def granted_attribute_values_json(self):
        """
        Gets the granted_attribute_values_json of this Grant.
        Store granted attribute-values as a string in Javascript Object Notation (JSON) format.

        **Added In:** 18.3.4

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The granted_attribute_values_json of this Grant.
        :rtype: str
        """
        return self._granted_attribute_values_json

    @granted_attribute_values_json.setter
    def granted_attribute_values_json(self, granted_attribute_values_json):
        """
        Sets the granted_attribute_values_json of this Grant.
        Store granted attribute-values as a string in Javascript Object Notation (JSON) format.

        **Added In:** 18.3.4

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param granted_attribute_values_json: The granted_attribute_values_json of this Grant.
        :type: str
        """
        self._granted_attribute_values_json = granted_attribute_values_json

    @property
    def app_entitlement_collection(self):
        """
        Gets the app_entitlement_collection of this Grant.

        :return: The app_entitlement_collection of this Grant.
        :rtype: oci.identity_domains.models.GrantAppEntitlementCollection
        """
        return self._app_entitlement_collection

    @app_entitlement_collection.setter
    def app_entitlement_collection(self, app_entitlement_collection):
        """
        Sets the app_entitlement_collection of this Grant.

        :param app_entitlement_collection: The app_entitlement_collection of this Grant.
        :type: oci.identity_domains.models.GrantAppEntitlementCollection
        """
        self._app_entitlement_collection = app_entitlement_collection

    @property
    def grantor(self):
        """
        Gets the grantor of this Grant.

        :return: The grantor of this Grant.
        :rtype: oci.identity_domains.models.GrantGrantor
        """
        return self._grantor

    @grantor.setter
    def grantor(self, grantor):
        """
        Sets the grantor of this Grant.

        :param grantor: The grantor of this Grant.
        :type: oci.identity_domains.models.GrantGrantor
        """
        self._grantor = grantor

    @property
    def grantee(self):
        """
        **[Required]** Gets the grantee of this Grant.

        :return: The grantee of this Grant.
        :rtype: oci.identity_domains.models.GrantGrantee
        """
        return self._grantee

    @grantee.setter
    def grantee(self, grantee):
        """
        Sets the grantee of this Grant.

        :param grantee: The grantee of this Grant.
        :type: oci.identity_domains.models.GrantGrantee
        """
        self._grantee = grantee

    @property
    def app(self):
        """
        Gets the app of this Grant.

        :return: The app of this Grant.
        :rtype: oci.identity_domains.models.GrantApp
        """
        return self._app

    @app.setter
    def app(self, app):
        """
        Sets the app of this Grant.

        :param app: The app of this Grant.
        :type: oci.identity_domains.models.GrantApp
        """
        self._app = app

    @property
    def entitlement(self):
        """
        Gets the entitlement of this Grant.

        :return: The entitlement of this Grant.
        :rtype: oci.identity_domains.models.GrantEntitlement
        """
        return self._entitlement

    @entitlement.setter
    def entitlement(self, entitlement):
        """
        Sets the entitlement of this Grant.

        :param entitlement: The entitlement of this Grant.
        :type: oci.identity_domains.models.GrantEntitlement
        """
        self._entitlement = entitlement

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
