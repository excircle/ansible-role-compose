#!/bin/bash

# Name of the playbook
PLAYBOOK_NAME="project-setup.yml"

# Directory structure
DIRECTORIES=("group_vars" "host_vars" "roles" "files" "templates")

# Create main playbook file
tee $PLAYBOOK_NAME <<EOF
---
- hosts: all
  tasks:
    - name: Sample task
      command: echo 'Hello, World!'
EOF

# Create inventory file
tee inventory <<EOF
[all]
localhost
EOF

# Create ansible.cfg
tee ansible.cfg <<EOF
[defaults]
inventory = ./inventory
# Other ansible configurations can go here
EOF

# Create directories
for dir in "${DIRECTORIES[@]}"; do
    mkdir -p $dir
done

# Sample group_vars and host_vars
echo "sample_variable: 'This is a sample variable'" > group_vars/all.yml
echo "# Add host specific variables here" > host_vars/sample_host.yml

echo "Ansible playbook setup complete"
