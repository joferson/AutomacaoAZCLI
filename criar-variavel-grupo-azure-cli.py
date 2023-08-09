import sys
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

def get_variables_from_file(file_name):
    variables = {}
    with open(file_name, 'r') as f:
        for line in f.readlines():
            key, value = line.split("=")
            variables[key] = value.strip('"')
    return variables

def get_variable_group(client, project, group_name):
    groups = client.get_variable_groups(project=project, group_name=group_name)
    for group in groups:
        if group.name == group_name:
            return group.id
    return None

def get_variables_from_group(client, project, group_id):
    group = client.get_variable_group(project, group_id)
    return group.variables

def create_variable_group(client, project, group_name, variables):
    transformed_variables = {key: {"value": value} for key, value in variables.items()}

    group = {
        "description": "Variavel de grupo criada por script",
        "name": group_name,
        "type": "Vsts",
        "variables": transformed_variables,
        "variableGroupProjectReferences": [{"name": group_name, "projectReference": {"name": project}}]
    }
    try:
        created_group = client.add_variable_group(group)
        return created_group.id
    except Exception as e:
        print("Erro ao criar o grupo de variáveis:", e)
        if hasattr(e, 'response') and e.response:
            print("Resposta da API:", e.response.text)
        return None

def main():
    TOKEN = sys.argv[1]
    ORG_URL = sys.argv[2]
    PROJECT = sys.argv[3]
    GROUP_NAME = sys.argv[4]

    credentials = BasicAuthentication('', TOKEN)
    connection = Connection(base_url=ORG_URL, creds=credentials)
    client = connection.clients.get_task_agent_client()

    group_id = get_variable_group(client, PROJECT, GROUP_NAME)
    variables = get_variables_from_file('variables.txt')
    
    if group_id:
        print(f"Group {GROUP_NAME} already exists with ID {group_id}")
        existing_variables = get_variables_from_group(client, PROJECT, group_id)
        missing_variables = {key: {"value": value} for key, value in variables.items() if key not in existing_variables}

        if missing_variables:
            existing_variables.update(missing_variables)

            updated_group = {
                "id": group_id,
                "name": GROUP_NAME,
                "type": "Vsts",
                "variables": existing_variables,
                "variableGroupProjectReferences": [{"name": GROUP_NAME, "projectReference": {"name": PROJECT}}]
            }

            try:
                client.update_variable_group(updated_group, group_id=group_id)
                print(f"Updated group {GROUP_NAME} with new variables.")
            except Exception as e:
                print("Error updating variable group:", e)
                if hasattr(e, 'response') and e.response:
                    print("API response:", e.response.text)
        else:
            print("No new variables to add.")
    else:
        group_id = create_variable_group(client, PROJECT, GROUP_NAME, variables)
        if group_id:
            print(f"Created group {GROUP_NAME} with ID {group_id}")
        else:
            print(f"Failed to create group {GROUP_NAME}")

if __name__ == "__main__":
    main()