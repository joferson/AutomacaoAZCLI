import sys
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

def escape_unwanted_sequences(value):
    # Substitui sequências indesejadas por suas versões "escapadas"
    replacements = {
        '\n': '\\n',
        '\t': '\\t'
    }
    
    for original, replacement in replacements.items():
        value = value.replace(original, replacement)
    return value

def save_variables_to_file(file_name, variables):
    with open(file_name, 'w') as f:
        for key, variable_obj in variables.items():
            formatted_value = variable_obj.value.strip("'")  # Removendo aspas simples adicionais
            formatted_value = escape_unwanted_sequences(formatted_value)
            
            if not key.startswith("'"):  # Adicionando uma checagem aqui
                f.write(f"{key}={formatted_value}\n")

def get_variable_group(client, project, group_name):
    groups = client.get_variable_groups(project=project, group_name=group_name)
    for group in groups:
        if group.name == group_name:
            return group.id
    return None

def get_variables_from_group(client, project, group_id):
    group = client.get_variable_group(project, group_id)
    return group.variables

def main():
    TOKEN = sys.argv[1]
    ORG_URL = sys.argv[2]
    PROJECT = sys.argv[3]
    GROUP_NAME = sys.argv[4]

    credentials = BasicAuthentication('', TOKEN)
    connection = Connection(base_url=ORG_URL, creds=credentials)
    client = connection.clients.get_task_agent_client()

    group_id = get_variable_group(client, PROJECT, GROUP_NAME)
    
    if group_id:
        variables = get_variables_from_group(client, PROJECT, group_id)
        save_variables_to_file(f"{GROUP_NAME}_variables.txt", variables)
    else:
        print(f"Group {GROUP_NAME} not found.")

if __name__ == "__main__":
    main()