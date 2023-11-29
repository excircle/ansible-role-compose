import yaml

##########################
# Classes
##########################

class Options:
    def __init__(self):
        self.project_name                   = None
        self.install_location               = None
        self.project_owner                  = None
        self.project_group                  = None
        self.database_enabled               = None
        self.postgres_image                 = None
        self.postgres_password              = None
        self.postgres_db_name               = None
        self.postgres_user                  = None
        self.postgres_container_nickname    = None
        self.nextjs_enabled                 = None
        self.nextjs_image_name              = None
        self.nextjs_project_name            = None
        self.nextjs_container_nickname      = None
        self.nextjs_app_dir                 = None
        self.gin_api_enabled                = None
        self.gin_golang_docker_image        = None
        self.gin_image_name                 = None
        self.gin_install_location           = None
        self.gin_container_nickname         = None

    def check_attribute_match(self, str):
        attributes = list(self.__dict__.keys())
        return str in attributes

##########################
# Main
##########################
if __name__ == '__main__':

    inputs = Options()

    # Gather Core Settings
    inputs.project_name = input("Please provide project_name\n")
    inputs.install_location = input("Please provide install_location\n")
    inputs.project_owner = input("Please provide project_owner\n")
    inputs.project_group = input("Please provide project_group\n")

    # Database Settings
    db               = input("Would you like a database for this project? [Y/n]\n")

    # Gather input if database is enabled
    if db in ['Y', 'y', 'yes', 'Yes', 'YES']:
        inputs.database_enabled               = True
        inputs.postgres_image                 = input("Please provide postgres_image - [Default: 16.1-bookworm]\n") or "16.1-bookworm"
        inputs.postgres_password              = input("Please provide postgres_password\n")
        inputs.postgres_db_name               = input(f"Please provide postgres_db_name - [Default: {inputs.project_name}-db]\n") or f"{inputs.project_name}-db"
        inputs.postgres_user                  = input(f"Please provide postgres_user - [Default: {inputs.project_name}-usr]\n") or f"{inputs.project_name}-usr"
        inputs.postgres_container_nickname    = input("Please provide postgres_container_nickname - [Default: pg-container]\n") or "pg-container"

    # NextJS Settings
    nextjs                 = input("Would you like a NextJS app for this project? [Y/n]\n")

    # Gather input if NextJS is enabled
    if nextjs in ['Y', 'y', 'yes', 'Yes', 'YES']:
        inputs.nextjs_enabled                = True
        inputs.nextjs_image_name              = input(f"Please provide nextjs_image_name - [Default: {inputs.project_name}-ui]\n") or f"{inputs.project_name}-ui"
        inputs.nextjs_project_name            = input(f"Please provide nextjs_project_name - [Default: {inputs.project_name}]\n") or inputs.project_name
        inputs.nextjs_container_nickname      = input("Please provide nextjs_container_nickname - [Default: nextjs-container]\n") or "nextjs-container"
        inputs.nextjs_app_dir                 = input("Please provide nextjs_app_dir - [Default: /app]\n") or "/app"

    # Gin API Settings
    gin                = input("Would you like a Gin API for this project? [Y/n]\n")

    # Gather input if Gin API is enabled
    if gin in ['Y', 'y', 'yes', 'Yes', 'YES']:
        inputs.gin_api_enabled                = True
        inputs.gin_golang_docker_image        = input("Please provide gin_golang_docker_image - [Default: 1.20-bookworm]\n") or "1.20-bookworm"
        inputs.gin_image_name                 = input(f"Please provide gin_image_name - [Default: {inputs.project_name}-api]\n") or f"{inputs.project_name}-api"
        inputs.gin_install_location           = input("Please provide gin_install_location - [Default: /go/src/api]\n") or "/go/src/api"
        inputs.gin_container_nickname         = input("Please provide gin_container_nickname - [Default: gin-container]\n") or "gin-container"

    # Create YAML structure
    alter_input = yaml.safe_dump(inputs.__dict__)

    # Pretty-print the YAML data
    print(f"[Project Config]\n\n{alter_input}\n\n")

    # Write YAML file
    with open('./roles/project-setup-role/defaults/main.yml', 'w') as outfile:
        yaml.dump(inputs.__dict__, outfile, default_flow_style=False)
