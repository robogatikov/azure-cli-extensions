# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import Operations
from ._managed_clusters_operations import ManagedClustersOperations
from ._maintenance_configurations_operations import MaintenanceConfigurationsOperations
from ._agent_pools_operations import AgentPoolsOperations
from ._machines_operations import MachinesOperations
from ._private_endpoint_connections_operations import PrivateEndpointConnectionsOperations
from ._private_link_resources_operations import PrivateLinkResourcesOperations
from ._resolve_private_link_service_id_operations import ResolvePrivateLinkServiceIdOperations
from ._operation_status_result_operations import OperationStatusResultOperations
from ._snapshots_operations import SnapshotsOperations
from ._managed_cluster_snapshots_operations import ManagedClusterSnapshotsOperations
from ._trusted_access_roles_operations import TrustedAccessRolesOperations
from ._trusted_access_role_bindings_operations import TrustedAccessRoleBindingsOperations
from ._load_balancers_operations import LoadBalancersOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Operations",
    "ManagedClustersOperations",
    "MaintenanceConfigurationsOperations",
    "AgentPoolsOperations",
    "MachinesOperations",
    "PrivateEndpointConnectionsOperations",
    "PrivateLinkResourcesOperations",
    "ResolvePrivateLinkServiceIdOperations",
    "OperationStatusResultOperations",
    "SnapshotsOperations",
    "ManagedClusterSnapshotsOperations",
    "TrustedAccessRolesOperations",
    "TrustedAccessRoleBindingsOperations",
    "LoadBalancersOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
