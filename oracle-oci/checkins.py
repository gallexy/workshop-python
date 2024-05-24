import oci
import sys
import time
import traceback


from oci.config import from_file


config = from_file()
print(config)
oci.config.validate_config(config)
#setting and initializing OCI parameters
identity = oci.identity.IdentityClient(config)

# Send the request to service, some parameters are not required, see API
# doc for more info

# Get the data from response
instance_num=0
        

compute_client = oci.core.ComputeClient(config)
identity = oci.identity.IdentityClient(config)
compartment_id = identity.get_user(config["user"]).data.compartment_id

list_instances_result = compute_client.list_instances(
    compartment_id=compartment_id)
#print(list_instances_result.data)

#print(instance_details)
#    ip_addresses = instance_details.public_ip
#    if ip_addresses:
#        public_ip = ip_addresses[0].ip_address
#    else:
#        public_ip = "None"
#print(f"Instance Name: {list_instances_result.display_name}, Status: {instance.lifecycle_state}")

instance_num=len(list_instances_result.data)
print(f'there are {instance_num} instances')
print(list_instances_result.data) 

