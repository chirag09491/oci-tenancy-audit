# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OAuthPartnerCertificate(object):
    """
    OAuth Partner Certificate schema
    """

    #: A constant which can be used with the idcs_prevented_operations property of a OAuthPartnerCertificate.
    #: This constant has a value of "replace"
    IDCS_PREVENTED_OPERATIONS_REPLACE = "replace"

    #: A constant which can be used with the idcs_prevented_operations property of a OAuthPartnerCertificate.
    #: This constant has a value of "update"
    IDCS_PREVENTED_OPERATIONS_UPDATE = "update"

    #: A constant which can be used with the idcs_prevented_operations property of a OAuthPartnerCertificate.
    #: This constant has a value of "delete"
    IDCS_PREVENTED_OPERATIONS_DELETE = "delete"

    def __init__(self, **kwargs):
        """
        Initializes a new OAuthPartnerCertificate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OAuthPartnerCertificate.
        :type id: str

        :param ocid:
            The value to assign to the ocid property of this OAuthPartnerCertificate.
        :type ocid: str

        :param schemas:
            The value to assign to the schemas property of this OAuthPartnerCertificate.
        :type schemas: list[str]

        :param meta:
            The value to assign to the meta property of this OAuthPartnerCertificate.
        :type meta: oci.identity_domains.models.Meta

        :param idcs_created_by:
            The value to assign to the idcs_created_by property of this OAuthPartnerCertificate.
        :type idcs_created_by: oci.identity_domains.models.IdcsCreatedBy

        :param idcs_last_modified_by:
            The value to assign to the idcs_last_modified_by property of this OAuthPartnerCertificate.
        :type idcs_last_modified_by: oci.identity_domains.models.IdcsLastModifiedBy

        :param idcs_prevented_operations:
            The value to assign to the idcs_prevented_operations property of this OAuthPartnerCertificate.
            Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type idcs_prevented_operations: list[str]

        :param tags:
            The value to assign to the tags property of this OAuthPartnerCertificate.
        :type tags: list[oci.identity_domains.models.Tags]

        :param delete_in_progress:
            The value to assign to the delete_in_progress property of this OAuthPartnerCertificate.
        :type delete_in_progress: bool

        :param idcs_last_upgraded_in_release:
            The value to assign to the idcs_last_upgraded_in_release property of this OAuthPartnerCertificate.
        :type idcs_last_upgraded_in_release: str

        :param domain_ocid:
            The value to assign to the domain_ocid property of this OAuthPartnerCertificate.
        :type domain_ocid: str

        :param compartment_ocid:
            The value to assign to the compartment_ocid property of this OAuthPartnerCertificate.
        :type compartment_ocid: str

        :param tenancy_ocid:
            The value to assign to the tenancy_ocid property of this OAuthPartnerCertificate.
        :type tenancy_ocid: str

        :param external_id:
            The value to assign to the external_id property of this OAuthPartnerCertificate.
        :type external_id: str

        :param key_store_name:
            The value to assign to the key_store_name property of this OAuthPartnerCertificate.
        :type key_store_name: str

        :param map:
            The value to assign to the map property of this OAuthPartnerCertificate.
        :type map: str

        :param key_store_password:
            The value to assign to the key_store_password property of this OAuthPartnerCertificate.
        :type key_store_password: str

        :param key_store_id:
            The value to assign to the key_store_id property of this OAuthPartnerCertificate.
        :type key_store_id: str

        :param certificate_alias:
            The value to assign to the certificate_alias property of this OAuthPartnerCertificate.
        :type certificate_alias: str

        :param sha1_thumbprint:
            The value to assign to the sha1_thumbprint property of this OAuthPartnerCertificate.
        :type sha1_thumbprint: str

        :param sha256_thumbprint:
            The value to assign to the sha256_thumbprint property of this OAuthPartnerCertificate.
        :type sha256_thumbprint: str

        :param cert_start_date:
            The value to assign to the cert_start_date property of this OAuthPartnerCertificate.
        :type cert_start_date: str

        :param x509_base64_certificate:
            The value to assign to the x509_base64_certificate property of this OAuthPartnerCertificate.
        :type x509_base64_certificate: str

        :param cert_end_date:
            The value to assign to the cert_end_date property of this OAuthPartnerCertificate.
        :type cert_end_date: str

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
            'external_id': 'str',
            'key_store_name': 'str',
            'map': 'str',
            'key_store_password': 'str',
            'key_store_id': 'str',
            'certificate_alias': 'str',
            'sha1_thumbprint': 'str',
            'sha256_thumbprint': 'str',
            'cert_start_date': 'str',
            'x509_base64_certificate': 'str',
            'cert_end_date': 'str'
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
            'external_id': 'externalId',
            'key_store_name': 'keyStoreName',
            'map': 'map',
            'key_store_password': 'keyStorePassword',
            'key_store_id': 'keyStoreId',
            'certificate_alias': 'certificateAlias',
            'sha1_thumbprint': 'sha1Thumbprint',
            'sha256_thumbprint': 'sha256Thumbprint',
            'cert_start_date': 'certStartDate',
            'x509_base64_certificate': 'x509Base64Certificate',
            'cert_end_date': 'certEndDate'
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
        self._external_id = None
        self._key_store_name = None
        self._map = None
        self._key_store_password = None
        self._key_store_id = None
        self._certificate_alias = None
        self._sha1_thumbprint = None
        self._sha256_thumbprint = None
        self._cert_start_date = None
        self._x509_base64_certificate = None
        self._cert_end_date = None

    @property
    def id(self):
        """
        Gets the id of this OAuthPartnerCertificate.
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


        :return: The id of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OAuthPartnerCertificate.
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


        :param id: The id of this OAuthPartnerCertificate.
        :type: str
        """
        self._id = id

    @property
    def ocid(self):
        """
        Gets the ocid of this OAuthPartnerCertificate.
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


        :return: The ocid of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this OAuthPartnerCertificate.
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


        :param ocid: The ocid of this OAuthPartnerCertificate.
        :type: str
        """
        self._ocid = ocid

    @property
    def schemas(self):
        """
        **[Required]** Gets the schemas of this OAuthPartnerCertificate.
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


        :return: The schemas of this OAuthPartnerCertificate.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this OAuthPartnerCertificate.
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


        :param schemas: The schemas of this OAuthPartnerCertificate.
        :type: list[str]
        """
        self._schemas = schemas

    @property
    def meta(self):
        """
        Gets the meta of this OAuthPartnerCertificate.

        :return: The meta of this OAuthPartnerCertificate.
        :rtype: oci.identity_domains.models.Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this OAuthPartnerCertificate.

        :param meta: The meta of this OAuthPartnerCertificate.
        :type: oci.identity_domains.models.Meta
        """
        self._meta = meta

    @property
    def idcs_created_by(self):
        """
        Gets the idcs_created_by of this OAuthPartnerCertificate.

        :return: The idcs_created_by of this OAuthPartnerCertificate.
        :rtype: oci.identity_domains.models.IdcsCreatedBy
        """
        return self._idcs_created_by

    @idcs_created_by.setter
    def idcs_created_by(self, idcs_created_by):
        """
        Sets the idcs_created_by of this OAuthPartnerCertificate.

        :param idcs_created_by: The idcs_created_by of this OAuthPartnerCertificate.
        :type: oci.identity_domains.models.IdcsCreatedBy
        """
        self._idcs_created_by = idcs_created_by

    @property
    def idcs_last_modified_by(self):
        """
        Gets the idcs_last_modified_by of this OAuthPartnerCertificate.

        :return: The idcs_last_modified_by of this OAuthPartnerCertificate.
        :rtype: oci.identity_domains.models.IdcsLastModifiedBy
        """
        return self._idcs_last_modified_by

    @idcs_last_modified_by.setter
    def idcs_last_modified_by(self, idcs_last_modified_by):
        """
        Sets the idcs_last_modified_by of this OAuthPartnerCertificate.

        :param idcs_last_modified_by: The idcs_last_modified_by of this OAuthPartnerCertificate.
        :type: oci.identity_domains.models.IdcsLastModifiedBy
        """
        self._idcs_last_modified_by = idcs_last_modified_by

    @property
    def idcs_prevented_operations(self):
        """
        Gets the idcs_prevented_operations of this OAuthPartnerCertificate.
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


        :return: The idcs_prevented_operations of this OAuthPartnerCertificate.
        :rtype: list[str]
        """
        return self._idcs_prevented_operations

    @idcs_prevented_operations.setter
    def idcs_prevented_operations(self, idcs_prevented_operations):
        """
        Sets the idcs_prevented_operations of this OAuthPartnerCertificate.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_prevented_operations: The idcs_prevented_operations of this OAuthPartnerCertificate.
        :type: list[str]
        """
        allowed_values = ["replace", "update", "delete"]
        if idcs_prevented_operations:
            idcs_prevented_operations[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in idcs_prevented_operations]
        self._idcs_prevented_operations = idcs_prevented_operations

    @property
    def tags(self):
        """
        Gets the tags of this OAuthPartnerCertificate.
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


        :return: The tags of this OAuthPartnerCertificate.
        :rtype: list[oci.identity_domains.models.Tags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this OAuthPartnerCertificate.
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


        :param tags: The tags of this OAuthPartnerCertificate.
        :type: list[oci.identity_domains.models.Tags]
        """
        self._tags = tags

    @property
    def delete_in_progress(self):
        """
        Gets the delete_in_progress of this OAuthPartnerCertificate.
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


        :return: The delete_in_progress of this OAuthPartnerCertificate.
        :rtype: bool
        """
        return self._delete_in_progress

    @delete_in_progress.setter
    def delete_in_progress(self, delete_in_progress):
        """
        Sets the delete_in_progress of this OAuthPartnerCertificate.
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


        :param delete_in_progress: The delete_in_progress of this OAuthPartnerCertificate.
        :type: bool
        """
        self._delete_in_progress = delete_in_progress

    @property
    def idcs_last_upgraded_in_release(self):
        """
        Gets the idcs_last_upgraded_in_release of this OAuthPartnerCertificate.
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


        :return: The idcs_last_upgraded_in_release of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._idcs_last_upgraded_in_release

    @idcs_last_upgraded_in_release.setter
    def idcs_last_upgraded_in_release(self, idcs_last_upgraded_in_release):
        """
        Sets the idcs_last_upgraded_in_release of this OAuthPartnerCertificate.
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


        :param idcs_last_upgraded_in_release: The idcs_last_upgraded_in_release of this OAuthPartnerCertificate.
        :type: str
        """
        self._idcs_last_upgraded_in_release = idcs_last_upgraded_in_release

    @property
    def domain_ocid(self):
        """
        Gets the domain_ocid of this OAuthPartnerCertificate.
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


        :return: The domain_ocid of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._domain_ocid

    @domain_ocid.setter
    def domain_ocid(self, domain_ocid):
        """
        Sets the domain_ocid of this OAuthPartnerCertificate.
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


        :param domain_ocid: The domain_ocid of this OAuthPartnerCertificate.
        :type: str
        """
        self._domain_ocid = domain_ocid

    @property
    def compartment_ocid(self):
        """
        Gets the compartment_ocid of this OAuthPartnerCertificate.
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


        :return: The compartment_ocid of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._compartment_ocid

    @compartment_ocid.setter
    def compartment_ocid(self, compartment_ocid):
        """
        Sets the compartment_ocid of this OAuthPartnerCertificate.
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


        :param compartment_ocid: The compartment_ocid of this OAuthPartnerCertificate.
        :type: str
        """
        self._compartment_ocid = compartment_ocid

    @property
    def tenancy_ocid(self):
        """
        Gets the tenancy_ocid of this OAuthPartnerCertificate.
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


        :return: The tenancy_ocid of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._tenancy_ocid

    @tenancy_ocid.setter
    def tenancy_ocid(self, tenancy_ocid):
        """
        Sets the tenancy_ocid of this OAuthPartnerCertificate.
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


        :param tenancy_ocid: The tenancy_ocid of this OAuthPartnerCertificate.
        :type: str
        """
        self._tenancy_ocid = tenancy_ocid

    @property
    def external_id(self):
        """
        Gets the external_id of this OAuthPartnerCertificate.
        An identifier for the Resource as defined by the Service Consumer. The externalId may simplify identification of the Resource between Service Consumer and Service Provider by allowing the Consumer to refer to the Resource with its own identifier, obviating the need to store a local mapping between the local identifier of the Resource and the identifier used by the Service Provider. Each Resource MAY include a non-empty externalId value. The value of the externalId attribute is always issued by the Service Consumer and can never be specified by the Service Provider. The Service Provider MUST always interpret the externalId as scoped to the Service Consumer's tenant.

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: false
         - caseExact: false
         - mutability: readWrite
         - returned: default
         - uniqueness: none


        :return: The external_id of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this OAuthPartnerCertificate.
        An identifier for the Resource as defined by the Service Consumer. The externalId may simplify identification of the Resource between Service Consumer and Service Provider by allowing the Consumer to refer to the Resource with its own identifier, obviating the need to store a local mapping between the local identifier of the Resource and the identifier used by the Service Provider. Each Resource MAY include a non-empty externalId value. The value of the externalId attribute is always issued by the Service Consumer and can never be specified by the Service Provider. The Service Provider MUST always interpret the externalId as scoped to the Service Consumer's tenant.

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: false
         - caseExact: false
         - mutability: readWrite
         - returned: default
         - uniqueness: none


        :param external_id: The external_id of this OAuthPartnerCertificate.
        :type: str
        """
        self._external_id = external_id

    @property
    def key_store_name(self):
        """
        Gets the key_store_name of this OAuthPartnerCertificate.
        Key store name

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: false
         - caseExact: false
         - returned: always
         - uniqueness: none


        :return: The key_store_name of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._key_store_name

    @key_store_name.setter
    def key_store_name(self, key_store_name):
        """
        Sets the key_store_name of this OAuthPartnerCertificate.
        Key store name

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: false
         - caseExact: false
         - returned: always
         - uniqueness: none


        :param key_store_name: The key_store_name of this OAuthPartnerCertificate.
        :type: str
        """
        self._key_store_name = key_store_name

    @property
    def map(self):
        """
        Gets the map of this OAuthPartnerCertificate.
        Map

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: false
         - caseExact: false
         - returned: always
         - uniqueness: none


        :return: The map of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._map

    @map.setter
    def map(self, map):
        """
        Sets the map of this OAuthPartnerCertificate.
        Map

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: false
         - caseExact: false
         - returned: always
         - uniqueness: none


        :param map: The map of this OAuthPartnerCertificate.
        :type: str
        """
        self._map = map

    @property
    def key_store_password(self):
        """
        Gets the key_store_password of this OAuthPartnerCertificate.
        Key store password

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - idcsSensitive: none
         - required: false
         - caseExact: true
         - returned: never
         - uniqueness: none


        :return: The key_store_password of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._key_store_password

    @key_store_password.setter
    def key_store_password(self, key_store_password):
        """
        Sets the key_store_password of this OAuthPartnerCertificate.
        Key store password

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - idcsSensitive: none
         - required: false
         - caseExact: true
         - returned: never
         - uniqueness: none


        :param key_store_password: The key_store_password of this OAuthPartnerCertificate.
        :type: str
        """
        self._key_store_password = key_store_password

    @property
    def key_store_id(self):
        """
        Gets the key_store_id of this OAuthPartnerCertificate.
        Key store ID

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: false
         - caseExact: true
         - returned: never
         - uniqueness: none
         - idcsSearchable: true


        :return: The key_store_id of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._key_store_id

    @key_store_id.setter
    def key_store_id(self, key_store_id):
        """
        Sets the key_store_id of this OAuthPartnerCertificate.
        Key store ID

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: false
         - caseExact: true
         - returned: never
         - uniqueness: none
         - idcsSearchable: true


        :param key_store_id: The key_store_id of this OAuthPartnerCertificate.
        :type: str
        """
        self._key_store_id = key_store_id

    @property
    def certificate_alias(self):
        """
        **[Required]** Gets the certificate_alias of this OAuthPartnerCertificate.
        Certificate alias

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: true
         - caseExact: false
         - mutability: readWrite
         - returned: always
         - uniqueness: none
         - idcsSearchable: true


        :return: The certificate_alias of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._certificate_alias

    @certificate_alias.setter
    def certificate_alias(self, certificate_alias):
        """
        Sets the certificate_alias of this OAuthPartnerCertificate.
        Certificate alias

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: true
         - caseExact: false
         - mutability: readWrite
         - returned: always
         - uniqueness: none
         - idcsSearchable: true


        :param certificate_alias: The certificate_alias of this OAuthPartnerCertificate.
        :type: str
        """
        self._certificate_alias = certificate_alias

    @property
    def sha1_thumbprint(self):
        """
        Gets the sha1_thumbprint of this OAuthPartnerCertificate.
        SHA-1 Thumbprint

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: false
         - caseExact: true
         - returned: default
         - idcsSearchable: true
         - uniqueness: none


        :return: The sha1_thumbprint of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._sha1_thumbprint

    @sha1_thumbprint.setter
    def sha1_thumbprint(self, sha1_thumbprint):
        """
        Sets the sha1_thumbprint of this OAuthPartnerCertificate.
        SHA-1 Thumbprint

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: false
         - caseExact: true
         - returned: default
         - idcsSearchable: true
         - uniqueness: none


        :param sha1_thumbprint: The sha1_thumbprint of this OAuthPartnerCertificate.
        :type: str
        """
        self._sha1_thumbprint = sha1_thumbprint

    @property
    def sha256_thumbprint(self):
        """
        Gets the sha256_thumbprint of this OAuthPartnerCertificate.
        SHA-256 Thumbprint

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: false
         - caseExact: true
         - returned: default
         - idcsSearchable: true
         - uniqueness: none


        :return: The sha256_thumbprint of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._sha256_thumbprint

    @sha256_thumbprint.setter
    def sha256_thumbprint(self, sha256_thumbprint):
        """
        Sets the sha256_thumbprint of this OAuthPartnerCertificate.
        SHA-256 Thumbprint

        **SCIM++ Properties:**
         - type: string
         - multiValued: false
         - required: false
         - caseExact: true
         - returned: default
         - idcsSearchable: true
         - uniqueness: none


        :param sha256_thumbprint: The sha256_thumbprint of this OAuthPartnerCertificate.
        :type: str
        """
        self._sha256_thumbprint = sha256_thumbprint

    @property
    def cert_start_date(self):
        """
        Gets the cert_start_date of this OAuthPartnerCertificate.
        Certificate start date

        **SCIM++ Properties:**
         - type: dateTime
         - multiValued: false
         - required: false
         - caseExact: true
         - mutability: readWrite
         - returned: default
         - uniqueness: none


        :return: The cert_start_date of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._cert_start_date

    @cert_start_date.setter
    def cert_start_date(self, cert_start_date):
        """
        Sets the cert_start_date of this OAuthPartnerCertificate.
        Certificate start date

        **SCIM++ Properties:**
         - type: dateTime
         - multiValued: false
         - required: false
         - caseExact: true
         - mutability: readWrite
         - returned: default
         - uniqueness: none


        :param cert_start_date: The cert_start_date of this OAuthPartnerCertificate.
        :type: str
        """
        self._cert_start_date = cert_start_date

    @property
    def x509_base64_certificate(self):
        """
        Gets the x509_base64_certificate of this OAuthPartnerCertificate.
        Base 64Key data attribute

        **SCIM++ Properties:**
         - caseExact: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The x509_base64_certificate of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._x509_base64_certificate

    @x509_base64_certificate.setter
    def x509_base64_certificate(self, x509_base64_certificate):
        """
        Sets the x509_base64_certificate of this OAuthPartnerCertificate.
        Base 64Key data attribute

        **SCIM++ Properties:**
         - caseExact: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param x509_base64_certificate: The x509_base64_certificate of this OAuthPartnerCertificate.
        :type: str
        """
        self._x509_base64_certificate = x509_base64_certificate

    @property
    def cert_end_date(self):
        """
        Gets the cert_end_date of this OAuthPartnerCertificate.
        Certificate end date

        **SCIM++ Properties:**
         - type: dateTime
         - multiValued: false
         - required: false
         - caseExact: true
         - mutability: readWrite
         - returned: default
         - uniqueness: none


        :return: The cert_end_date of this OAuthPartnerCertificate.
        :rtype: str
        """
        return self._cert_end_date

    @cert_end_date.setter
    def cert_end_date(self, cert_end_date):
        """
        Sets the cert_end_date of this OAuthPartnerCertificate.
        Certificate end date

        **SCIM++ Properties:**
         - type: dateTime
         - multiValued: false
         - required: false
         - caseExact: true
         - mutability: readWrite
         - returned: default
         - uniqueness: none


        :param cert_end_date: The cert_end_date of this OAuthPartnerCertificate.
        :type: str
        """
        self._cert_end_date = cert_end_date

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
