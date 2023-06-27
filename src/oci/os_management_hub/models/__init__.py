# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .attach_managed_instances_to_lifecycle_stage_details import AttachManagedInstancesToLifecycleStageDetails
from .attach_managed_instances_to_managed_instance_group_details import AttachManagedInstancesToManagedInstanceGroupDetails
from .attach_software_sources_to_managed_instance_details import AttachSoftwareSourcesToManagedInstanceDetails
from .attach_software_sources_to_managed_instance_group_details import AttachSoftwareSourcesToManagedInstanceGroupDetails
from .available_package_collection import AvailablePackageCollection
from .available_package_summary import AvailablePackageSummary
from .available_software_source_collection import AvailableSoftwareSourceCollection
from .available_software_source_summary import AvailableSoftwareSourceSummary
from .change_availability_of_software_sources_details import ChangeAvailabilityOfSoftwareSourcesDetails
from .create_custom_software_source_details import CreateCustomSoftwareSourceDetails
from .create_entitlement_details import CreateEntitlementDetails
from .create_group_profile_details import CreateGroupProfileDetails
from .create_lifecycle_environment_details import CreateLifecycleEnvironmentDetails
from .create_lifecycle_profile_details import CreateLifecycleProfileDetails
from .create_lifecycle_stage_details import CreateLifecycleStageDetails
from .create_managed_instance_group_details import CreateManagedInstanceGroupDetails
from .create_management_station_details import CreateManagementStationDetails
from .create_mirror_configuration_details import CreateMirrorConfigurationDetails
from .create_profile_details import CreateProfileDetails
from .create_proxy_configuration_details import CreateProxyConfigurationDetails
from .create_scheduled_job_details import CreateScheduledJobDetails
from .create_software_source_details import CreateSoftwareSourceDetails
from .create_software_source_profile_details import CreateSoftwareSourceProfileDetails
from .create_station_profile_details import CreateStationProfileDetails
from .create_versioned_custom_software_source_details import CreateVersionedCustomSoftwareSourceDetails
from .custom_software_source import CustomSoftwareSource
from .custom_software_source_filter import CustomSoftwareSourceFilter
from .custom_software_source_summary import CustomSoftwareSourceSummary
from .detach_managed_instances_from_lifecycle_stage_details import DetachManagedInstancesFromLifecycleStageDetails
from .detach_managed_instances_from_managed_instance_group_details import DetachManagedInstancesFromManagedInstanceGroupDetails
from .detach_software_sources_from_managed_instance_details import DetachSoftwareSourcesFromManagedInstanceDetails
from .detach_software_sources_from_managed_instance_group_details import DetachSoftwareSourcesFromManagedInstanceGroupDetails
from .disable_module_stream_on_managed_instance_details import DisableModuleStreamOnManagedInstanceDetails
from .disable_module_stream_on_managed_instance_group_details import DisableModuleStreamOnManagedInstanceGroupDetails
from .enable_module_stream_on_managed_instance_details import EnableModuleStreamOnManagedInstanceDetails
from .enable_module_stream_on_managed_instance_group_details import EnableModuleStreamOnManagedInstanceGroupDetails
from .entitlement_collection import EntitlementCollection
from .entitlement_summary import EntitlementSummary
from .erratum import Erratum
from .erratum_collection import ErratumCollection
from .erratum_summary import ErratumSummary
from .group_profile import GroupProfile
from .id import Id
from .install_module_stream_profile_on_managed_instance_details import InstallModuleStreamProfileOnManagedInstanceDetails
from .install_module_stream_profile_on_managed_instance_group_details import InstallModuleStreamProfileOnManagedInstanceGroupDetails
from .install_packages_on_managed_instance_details import InstallPackagesOnManagedInstanceDetails
from .install_packages_on_managed_instance_group_details import InstallPackagesOnManagedInstanceGroupDetails
from .installed_package_collection import InstalledPackageCollection
from .installed_package_summary import InstalledPackageSummary
from .lifecycle_environment import LifecycleEnvironment
from .lifecycle_environment_collection import LifecycleEnvironmentCollection
from .lifecycle_environment_details import LifecycleEnvironmentDetails
from .lifecycle_environment_summary import LifecycleEnvironmentSummary
from .lifecycle_profile import LifecycleProfile
from .lifecycle_stage import LifecycleStage
from .lifecycle_stage_collection import LifecycleStageCollection
from .lifecycle_stage_details import LifecycleStageDetails
from .lifecycle_stage_summary import LifecycleStageSummary
from .manage_module_streams_in_scheduled_job_details import ManageModuleStreamsInScheduledJobDetails
from .manage_module_streams_on_managed_instance_details import ManageModuleStreamsOnManagedInstanceDetails
from .manage_module_streams_on_managed_instance_group_details import ManageModuleStreamsOnManagedInstanceGroupDetails
from .managed_instance import ManagedInstance
from .managed_instance_analytic_collection import ManagedInstanceAnalyticCollection
from .managed_instance_analytic_summary import ManagedInstanceAnalyticSummary
from .managed_instance_collection import ManagedInstanceCollection
from .managed_instance_details import ManagedInstanceDetails
from .managed_instance_erratum_summary import ManagedInstanceErratumSummary
from .managed_instance_erratum_summary_collection import ManagedInstanceErratumSummaryCollection
from .managed_instance_group import ManagedInstanceGroup
from .managed_instance_group_available_module_collection import ManagedInstanceGroupAvailableModuleCollection
from .managed_instance_group_available_module_summary import ManagedInstanceGroupAvailableModuleSummary
from .managed_instance_group_available_package_collection import ManagedInstanceGroupAvailablePackageCollection
from .managed_instance_group_available_package_summary import ManagedInstanceGroupAvailablePackageSummary
from .managed_instance_group_collection import ManagedInstanceGroupCollection
from .managed_instance_group_details import ManagedInstanceGroupDetails
from .managed_instance_group_installed_package_collection import ManagedInstanceGroupInstalledPackageCollection
from .managed_instance_group_installed_package_summary import ManagedInstanceGroupInstalledPackageSummary
from .managed_instance_group_module_collection import ManagedInstanceGroupModuleCollection
from .managed_instance_group_module_summary import ManagedInstanceGroupModuleSummary
from .managed_instance_group_summary import ManagedInstanceGroupSummary
from .managed_instance_module_collection import ManagedInstanceModuleCollection
from .managed_instance_module_summary import ManagedInstanceModuleSummary
from .managed_instance_summary import ManagedInstanceSummary
from .managed_instances_details import ManagedInstancesDetails
from .management_station import ManagementStation
from .management_station_collection import ManagementStationCollection
from .management_station_details import ManagementStationDetails
from .management_station_summary import ManagementStationSummary
from .mirror_configuration import MirrorConfiguration
from .mirror_summary import MirrorSummary
from .mirror_sync_status import MirrorSyncStatus
from .mirrors_collection import MirrorsCollection
from .module_collection import ModuleCollection
from .module_spec_details import ModuleSpecDetails
from .module_stream import ModuleStream
from .module_stream_collection import ModuleStreamCollection
from .module_stream_details import ModuleStreamDetails
from .module_stream_details_body import ModuleStreamDetailsBody
from .module_stream_profile import ModuleStreamProfile
from .module_stream_profile_collection import ModuleStreamProfileCollection
from .module_stream_profile_details import ModuleStreamProfileDetails
from .module_stream_profile_details_body import ModuleStreamProfileDetailsBody
from .module_stream_profile_filter import ModuleStreamProfileFilter
from .module_stream_profile_summary import ModuleStreamProfileSummary
from .module_stream_summary import ModuleStreamSummary
from .module_summary import ModuleSummary
from .package_filter import PackageFilter
from .package_group import PackageGroup
from .package_group_collection import PackageGroupCollection
from .package_group_filter import PackageGroupFilter
from .package_group_summary import PackageGroupSummary
from .package_name_summary import PackageNameSummary
from .package_summary import PackageSummary
from .profile import Profile
from .profile_collection import ProfileCollection
from .profile_summary import ProfileSummary
from .promote_software_source_to_lifecycle_stage_details import PromoteSoftwareSourceToLifecycleStageDetails
from .proxy_configuration import ProxyConfiguration
from .remove_module_stream_profile_from_managed_instance_details import RemoveModuleStreamProfileFromManagedInstanceDetails
from .remove_module_stream_profile_from_managed_instance_group_details import RemoveModuleStreamProfileFromManagedInstanceGroupDetails
from .remove_packages_from_managed_instance_details import RemovePackagesFromManagedInstanceDetails
from .remove_packages_from_managed_instance_group_details import RemovePackagesFromManagedInstanceGroupDetails
from .scheduled_job import ScheduledJob
from .scheduled_job_collection import ScheduledJobCollection
from .scheduled_job_operation import ScheduledJobOperation
from .scheduled_job_summary import ScheduledJobSummary
from .search_software_source_module_streams_details import SearchSoftwareSourceModuleStreamsDetails
from .search_software_source_modules_details import SearchSoftwareSourceModulesDetails
from .search_software_source_package_groups_details import SearchSoftwareSourcePackageGroupsDetails
from .software_package import SoftwarePackage
from .software_package_collection import SoftwarePackageCollection
from .software_package_dependency import SoftwarePackageDependency
from .software_package_file import SoftwarePackageFile
from .software_package_summary import SoftwarePackageSummary
from .software_packages_details import SoftwarePackagesDetails
from .software_source import SoftwareSource
from .software_source_availability import SoftwareSourceAvailability
from .software_source_collection import SoftwareSourceCollection
from .software_source_details import SoftwareSourceDetails
from .software_source_profile import SoftwareSourceProfile
from .software_source_summary import SoftwareSourceSummary
from .software_source_vendor_collection import SoftwareSourceVendorCollection
from .software_source_vendor_summary import SoftwareSourceVendorSummary
from .software_sources_details import SoftwareSourcesDetails
from .station_profile import StationProfile
from .switch_module_stream_on_managed_instance_details import SwitchModuleStreamOnManagedInstanceDetails
from .synchronize_mirrors_details import SynchronizeMirrorsDetails
from .updatable_package_collection import UpdatablePackageCollection
from .updatable_package_summary import UpdatablePackageSummary
from .update_all_packages_on_managed_instance_group_details import UpdateAllPackagesOnManagedInstanceGroupDetails
from .update_all_packages_on_managed_instances_in_compartment_details import UpdateAllPackagesOnManagedInstancesInCompartmentDetails
from .update_custom_software_source_details import UpdateCustomSoftwareSourceDetails
from .update_lifecycle_environment_details import UpdateLifecycleEnvironmentDetails
from .update_lifecycle_stage_details import UpdateLifecycleStageDetails
from .update_managed_instance_details import UpdateManagedInstanceDetails
from .update_managed_instance_group_details import UpdateManagedInstanceGroupDetails
from .update_management_station_details import UpdateManagementStationDetails
from .update_mirror_configuration_details import UpdateMirrorConfigurationDetails
from .update_packages_on_managed_instance_details import UpdatePackagesOnManagedInstanceDetails
from .update_profile_details import UpdateProfileDetails
from .update_proxy_configuration_details import UpdateProxyConfigurationDetails
from .update_scheduled_job_details import UpdateScheduledJobDetails
from .update_software_source_details import UpdateSoftwareSourceDetails
from .update_vendor_software_source_details import UpdateVendorSoftwareSourceDetails
from .update_work_request_details import UpdateWorkRequestDetails
from .vendor_software_source import VendorSoftwareSource
from .vendor_software_source_summary import VendorSoftwareSourceSummary
from .versioned_custom_software_source import VersionedCustomSoftwareSource
from .versioned_custom_software_source_summary import VersionedCustomSoftwareSourceSummary
from .work_request import WorkRequest
from .work_request_details import WorkRequestDetails
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_management_station_details import WorkRequestManagementStationDetails
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for os_management_hub services.
os_management_hub_type_mapping = {
    "AttachManagedInstancesToLifecycleStageDetails": AttachManagedInstancesToLifecycleStageDetails,
    "AttachManagedInstancesToManagedInstanceGroupDetails": AttachManagedInstancesToManagedInstanceGroupDetails,
    "AttachSoftwareSourcesToManagedInstanceDetails": AttachSoftwareSourcesToManagedInstanceDetails,
    "AttachSoftwareSourcesToManagedInstanceGroupDetails": AttachSoftwareSourcesToManagedInstanceGroupDetails,
    "AvailablePackageCollection": AvailablePackageCollection,
    "AvailablePackageSummary": AvailablePackageSummary,
    "AvailableSoftwareSourceCollection": AvailableSoftwareSourceCollection,
    "AvailableSoftwareSourceSummary": AvailableSoftwareSourceSummary,
    "ChangeAvailabilityOfSoftwareSourcesDetails": ChangeAvailabilityOfSoftwareSourcesDetails,
    "CreateCustomSoftwareSourceDetails": CreateCustomSoftwareSourceDetails,
    "CreateEntitlementDetails": CreateEntitlementDetails,
    "CreateGroupProfileDetails": CreateGroupProfileDetails,
    "CreateLifecycleEnvironmentDetails": CreateLifecycleEnvironmentDetails,
    "CreateLifecycleProfileDetails": CreateLifecycleProfileDetails,
    "CreateLifecycleStageDetails": CreateLifecycleStageDetails,
    "CreateManagedInstanceGroupDetails": CreateManagedInstanceGroupDetails,
    "CreateManagementStationDetails": CreateManagementStationDetails,
    "CreateMirrorConfigurationDetails": CreateMirrorConfigurationDetails,
    "CreateProfileDetails": CreateProfileDetails,
    "CreateProxyConfigurationDetails": CreateProxyConfigurationDetails,
    "CreateScheduledJobDetails": CreateScheduledJobDetails,
    "CreateSoftwareSourceDetails": CreateSoftwareSourceDetails,
    "CreateSoftwareSourceProfileDetails": CreateSoftwareSourceProfileDetails,
    "CreateStationProfileDetails": CreateStationProfileDetails,
    "CreateVersionedCustomSoftwareSourceDetails": CreateVersionedCustomSoftwareSourceDetails,
    "CustomSoftwareSource": CustomSoftwareSource,
    "CustomSoftwareSourceFilter": CustomSoftwareSourceFilter,
    "CustomSoftwareSourceSummary": CustomSoftwareSourceSummary,
    "DetachManagedInstancesFromLifecycleStageDetails": DetachManagedInstancesFromLifecycleStageDetails,
    "DetachManagedInstancesFromManagedInstanceGroupDetails": DetachManagedInstancesFromManagedInstanceGroupDetails,
    "DetachSoftwareSourcesFromManagedInstanceDetails": DetachSoftwareSourcesFromManagedInstanceDetails,
    "DetachSoftwareSourcesFromManagedInstanceGroupDetails": DetachSoftwareSourcesFromManagedInstanceGroupDetails,
    "DisableModuleStreamOnManagedInstanceDetails": DisableModuleStreamOnManagedInstanceDetails,
    "DisableModuleStreamOnManagedInstanceGroupDetails": DisableModuleStreamOnManagedInstanceGroupDetails,
    "EnableModuleStreamOnManagedInstanceDetails": EnableModuleStreamOnManagedInstanceDetails,
    "EnableModuleStreamOnManagedInstanceGroupDetails": EnableModuleStreamOnManagedInstanceGroupDetails,
    "EntitlementCollection": EntitlementCollection,
    "EntitlementSummary": EntitlementSummary,
    "Erratum": Erratum,
    "ErratumCollection": ErratumCollection,
    "ErratumSummary": ErratumSummary,
    "GroupProfile": GroupProfile,
    "Id": Id,
    "InstallModuleStreamProfileOnManagedInstanceDetails": InstallModuleStreamProfileOnManagedInstanceDetails,
    "InstallModuleStreamProfileOnManagedInstanceGroupDetails": InstallModuleStreamProfileOnManagedInstanceGroupDetails,
    "InstallPackagesOnManagedInstanceDetails": InstallPackagesOnManagedInstanceDetails,
    "InstallPackagesOnManagedInstanceGroupDetails": InstallPackagesOnManagedInstanceGroupDetails,
    "InstalledPackageCollection": InstalledPackageCollection,
    "InstalledPackageSummary": InstalledPackageSummary,
    "LifecycleEnvironment": LifecycleEnvironment,
    "LifecycleEnvironmentCollection": LifecycleEnvironmentCollection,
    "LifecycleEnvironmentDetails": LifecycleEnvironmentDetails,
    "LifecycleEnvironmentSummary": LifecycleEnvironmentSummary,
    "LifecycleProfile": LifecycleProfile,
    "LifecycleStage": LifecycleStage,
    "LifecycleStageCollection": LifecycleStageCollection,
    "LifecycleStageDetails": LifecycleStageDetails,
    "LifecycleStageSummary": LifecycleStageSummary,
    "ManageModuleStreamsInScheduledJobDetails": ManageModuleStreamsInScheduledJobDetails,
    "ManageModuleStreamsOnManagedInstanceDetails": ManageModuleStreamsOnManagedInstanceDetails,
    "ManageModuleStreamsOnManagedInstanceGroupDetails": ManageModuleStreamsOnManagedInstanceGroupDetails,
    "ManagedInstance": ManagedInstance,
    "ManagedInstanceAnalyticCollection": ManagedInstanceAnalyticCollection,
    "ManagedInstanceAnalyticSummary": ManagedInstanceAnalyticSummary,
    "ManagedInstanceCollection": ManagedInstanceCollection,
    "ManagedInstanceDetails": ManagedInstanceDetails,
    "ManagedInstanceErratumSummary": ManagedInstanceErratumSummary,
    "ManagedInstanceErratumSummaryCollection": ManagedInstanceErratumSummaryCollection,
    "ManagedInstanceGroup": ManagedInstanceGroup,
    "ManagedInstanceGroupAvailableModuleCollection": ManagedInstanceGroupAvailableModuleCollection,
    "ManagedInstanceGroupAvailableModuleSummary": ManagedInstanceGroupAvailableModuleSummary,
    "ManagedInstanceGroupAvailablePackageCollection": ManagedInstanceGroupAvailablePackageCollection,
    "ManagedInstanceGroupAvailablePackageSummary": ManagedInstanceGroupAvailablePackageSummary,
    "ManagedInstanceGroupCollection": ManagedInstanceGroupCollection,
    "ManagedInstanceGroupDetails": ManagedInstanceGroupDetails,
    "ManagedInstanceGroupInstalledPackageCollection": ManagedInstanceGroupInstalledPackageCollection,
    "ManagedInstanceGroupInstalledPackageSummary": ManagedInstanceGroupInstalledPackageSummary,
    "ManagedInstanceGroupModuleCollection": ManagedInstanceGroupModuleCollection,
    "ManagedInstanceGroupModuleSummary": ManagedInstanceGroupModuleSummary,
    "ManagedInstanceGroupSummary": ManagedInstanceGroupSummary,
    "ManagedInstanceModuleCollection": ManagedInstanceModuleCollection,
    "ManagedInstanceModuleSummary": ManagedInstanceModuleSummary,
    "ManagedInstanceSummary": ManagedInstanceSummary,
    "ManagedInstancesDetails": ManagedInstancesDetails,
    "ManagementStation": ManagementStation,
    "ManagementStationCollection": ManagementStationCollection,
    "ManagementStationDetails": ManagementStationDetails,
    "ManagementStationSummary": ManagementStationSummary,
    "MirrorConfiguration": MirrorConfiguration,
    "MirrorSummary": MirrorSummary,
    "MirrorSyncStatus": MirrorSyncStatus,
    "MirrorsCollection": MirrorsCollection,
    "ModuleCollection": ModuleCollection,
    "ModuleSpecDetails": ModuleSpecDetails,
    "ModuleStream": ModuleStream,
    "ModuleStreamCollection": ModuleStreamCollection,
    "ModuleStreamDetails": ModuleStreamDetails,
    "ModuleStreamDetailsBody": ModuleStreamDetailsBody,
    "ModuleStreamProfile": ModuleStreamProfile,
    "ModuleStreamProfileCollection": ModuleStreamProfileCollection,
    "ModuleStreamProfileDetails": ModuleStreamProfileDetails,
    "ModuleStreamProfileDetailsBody": ModuleStreamProfileDetailsBody,
    "ModuleStreamProfileFilter": ModuleStreamProfileFilter,
    "ModuleStreamProfileSummary": ModuleStreamProfileSummary,
    "ModuleStreamSummary": ModuleStreamSummary,
    "ModuleSummary": ModuleSummary,
    "PackageFilter": PackageFilter,
    "PackageGroup": PackageGroup,
    "PackageGroupCollection": PackageGroupCollection,
    "PackageGroupFilter": PackageGroupFilter,
    "PackageGroupSummary": PackageGroupSummary,
    "PackageNameSummary": PackageNameSummary,
    "PackageSummary": PackageSummary,
    "Profile": Profile,
    "ProfileCollection": ProfileCollection,
    "ProfileSummary": ProfileSummary,
    "PromoteSoftwareSourceToLifecycleStageDetails": PromoteSoftwareSourceToLifecycleStageDetails,
    "ProxyConfiguration": ProxyConfiguration,
    "RemoveModuleStreamProfileFromManagedInstanceDetails": RemoveModuleStreamProfileFromManagedInstanceDetails,
    "RemoveModuleStreamProfileFromManagedInstanceGroupDetails": RemoveModuleStreamProfileFromManagedInstanceGroupDetails,
    "RemovePackagesFromManagedInstanceDetails": RemovePackagesFromManagedInstanceDetails,
    "RemovePackagesFromManagedInstanceGroupDetails": RemovePackagesFromManagedInstanceGroupDetails,
    "ScheduledJob": ScheduledJob,
    "ScheduledJobCollection": ScheduledJobCollection,
    "ScheduledJobOperation": ScheduledJobOperation,
    "ScheduledJobSummary": ScheduledJobSummary,
    "SearchSoftwareSourceModuleStreamsDetails": SearchSoftwareSourceModuleStreamsDetails,
    "SearchSoftwareSourceModulesDetails": SearchSoftwareSourceModulesDetails,
    "SearchSoftwareSourcePackageGroupsDetails": SearchSoftwareSourcePackageGroupsDetails,
    "SoftwarePackage": SoftwarePackage,
    "SoftwarePackageCollection": SoftwarePackageCollection,
    "SoftwarePackageDependency": SoftwarePackageDependency,
    "SoftwarePackageFile": SoftwarePackageFile,
    "SoftwarePackageSummary": SoftwarePackageSummary,
    "SoftwarePackagesDetails": SoftwarePackagesDetails,
    "SoftwareSource": SoftwareSource,
    "SoftwareSourceAvailability": SoftwareSourceAvailability,
    "SoftwareSourceCollection": SoftwareSourceCollection,
    "SoftwareSourceDetails": SoftwareSourceDetails,
    "SoftwareSourceProfile": SoftwareSourceProfile,
    "SoftwareSourceSummary": SoftwareSourceSummary,
    "SoftwareSourceVendorCollection": SoftwareSourceVendorCollection,
    "SoftwareSourceVendorSummary": SoftwareSourceVendorSummary,
    "SoftwareSourcesDetails": SoftwareSourcesDetails,
    "StationProfile": StationProfile,
    "SwitchModuleStreamOnManagedInstanceDetails": SwitchModuleStreamOnManagedInstanceDetails,
    "SynchronizeMirrorsDetails": SynchronizeMirrorsDetails,
    "UpdatablePackageCollection": UpdatablePackageCollection,
    "UpdatablePackageSummary": UpdatablePackageSummary,
    "UpdateAllPackagesOnManagedInstanceGroupDetails": UpdateAllPackagesOnManagedInstanceGroupDetails,
    "UpdateAllPackagesOnManagedInstancesInCompartmentDetails": UpdateAllPackagesOnManagedInstancesInCompartmentDetails,
    "UpdateCustomSoftwareSourceDetails": UpdateCustomSoftwareSourceDetails,
    "UpdateLifecycleEnvironmentDetails": UpdateLifecycleEnvironmentDetails,
    "UpdateLifecycleStageDetails": UpdateLifecycleStageDetails,
    "UpdateManagedInstanceDetails": UpdateManagedInstanceDetails,
    "UpdateManagedInstanceGroupDetails": UpdateManagedInstanceGroupDetails,
    "UpdateManagementStationDetails": UpdateManagementStationDetails,
    "UpdateMirrorConfigurationDetails": UpdateMirrorConfigurationDetails,
    "UpdatePackagesOnManagedInstanceDetails": UpdatePackagesOnManagedInstanceDetails,
    "UpdateProfileDetails": UpdateProfileDetails,
    "UpdateProxyConfigurationDetails": UpdateProxyConfigurationDetails,
    "UpdateScheduledJobDetails": UpdateScheduledJobDetails,
    "UpdateSoftwareSourceDetails": UpdateSoftwareSourceDetails,
    "UpdateVendorSoftwareSourceDetails": UpdateVendorSoftwareSourceDetails,
    "UpdateWorkRequestDetails": UpdateWorkRequestDetails,
    "VendorSoftwareSource": VendorSoftwareSource,
    "VendorSoftwareSourceSummary": VendorSoftwareSourceSummary,
    "VersionedCustomSoftwareSource": VersionedCustomSoftwareSource,
    "VersionedCustomSoftwareSourceSummary": VersionedCustomSoftwareSourceSummary,
    "WorkRequest": WorkRequest,
    "WorkRequestDetails": WorkRequestDetails,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestManagementStationDetails": WorkRequestManagementStationDetails,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}