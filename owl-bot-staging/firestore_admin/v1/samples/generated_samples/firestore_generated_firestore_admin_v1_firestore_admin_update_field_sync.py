# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateField
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-firestore-admin


# [START firestore_generated_firestore_admin_v1_FirestoreAdmin_UpdateField_sync]
from google.cloud import firestore_admin_v1


def sample_update_field():
    # Create a client
    client = firestore_admin_v1.FirestoreAdminClient()

    # Initialize request argument(s)
    field = firestore_admin_v1.Field()
    field.name = "name_value"

    request = firestore_admin_v1.UpdateFieldRequest(
        field=field,
    )

    # Make the request
    operation = client.update_field(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END firestore_generated_firestore_admin_v1_FirestoreAdmin_UpdateField_sync]
