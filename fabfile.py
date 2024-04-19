from fabric import Connection, task

# Define the remote server details
HOST = '54.145.240.142'
USER = 'ubuntu'

# Define the directory paths
PROJECT_DIR = './Bard_Generated_Image.jpeg'
REMOTE_DIR = '~/'

@task
def deploy(c):
    """
    Deploy the project to the remote server
    """
    # Connect to the remote server
    with Connection(host=HOST, user=USER) as conn:
        try:
            # Upload the project files to the remote server
            conn.put(local=PROJECT_DIR, remote=REMOTE_DIR)
            # Restart the web server
            conn.sudo('service nginx restart')

            print('Deployment successful.')
        except Exception as e:
            print(f'Deployment failed: {e}')
