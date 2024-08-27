import speedtest
import subprocess
import time
import platform
from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

def check_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        return download_speed, upload_speed
    except Exception as e:
        return None, None

def check_connectivity(host='8.8.8.8'):
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output(['ping', '-n', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        else:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return True
    except subprocess.CalledProcessError:
        return False
    except PermissionError:
        return False
    except Exception:
        return False

def main():
    template = env.get_template('index.html')
    while True:
        connectivity = check_connectivity()
        if connectivity:
            download_speed, upload_speed = check_speed()
            if download_speed is not None and upload_speed is not None:
                data = {'connectivity': 'Connected', 'download_speed': f'{download_speed:.2f} Mbps', 'upload_speed': f'{upload_speed:.2f} Mbps'}
            else:
                data = {'connectivity': 'Connected', 'download_speed': 'N/A', 'upload_speed': 'N/A'}
        else:
            data = {'connectivity': 'Disconnected', 'download_speed': 'N/A', 'upload_speed': 'N/A'}
        html = template.render(data=data)
        print(html)
        time.sleep(60)  # Wait for 30 seconds before checking again

if __name__ == '__main__':
    main()