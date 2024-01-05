import click
import json_permits


# Group for Click commands
@click.group()
def cli():
    pass

#--------------------------------------------------------------------
# Creates a new user and adds it to the JSON data

@cli.command()
@click.option('--name', required=True, help='Name of the user')
@click.option('--age', required=True, help='age of the user')
@click.pass_context
def new(ctx, name, age):
    if not name or  not age:
        ctx.fail('the name and age are required')
    else:
        data = json_permits.read_json()
        new_id = len(data) + 1
        new_user = {
            'id': new_id,
            'name': name,
            'age': age,
        }
        data.append(new_user)
        json_permits.write_json(data)
        print(f"User {name} {age} create successfully with id {new_id}")

#--------------------------------------------------------------------
# Displays information about all users in the JSON data


@cli.command()
def users():
    users = json_permits.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['age']}")

#--------------------------------------------------------------------
# Displays information about a specific user based on the provided ID

@cli.command()
@click.argument('id', type=int)
def user(id):
    data = json_permits.read_json()
    user = None
    for x in data:
        if x['id'] == id:
            user = x
            break
    
    if user is None:
        print(f"User with id {id} not found")
    else:
        print(f"{user['id']} - {user['name']} - {user['age']}")

#--------------------------------------------------------------------
# Updates the information of a user based on the provided ID

@cli.command()
@click.argument('id', type=int)
@click.option('--name', required=True, help='Name of the user')
@click.option('--age', required=True, help='age of the user')
def update(id, name, age):
    data = json_permits.write_json()
    for user in data:
        if user['id'] == id:
            if name is None:
                user['name'] = name
            if age is None:
                user['age'] == age
            break
    json_permits.write_json(data)
    print(f"User with id {id} is update successfully")

#--------------------------------------------------------------------
# Deletes a user based on the provided ID

@cli.command()
@click.argument('id', type=int)
def delete(id):
    data = json_permits.read_json()
    user = None
    for x in data:
        if x['id'] == id:
            user = x
            break
    
    if user is None:
        print(f"User with id {id} not found")
    else:
        data.remove(user)
        json_permits.write_json(data)
        print(f"User with id {id} delete {user}")

if __name__ == '__main__':
    cli()

