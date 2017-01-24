from flask import Flask, abort, jsonify, request
import uuid
from subprocess import call
import os
from redis import Redis

call(["/usr/sbin/sshd"])

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/securesnmp/api/v1.0/client', methods=['POST'])
def create_client():
    if not request.json or not 'client_public_key' in request.json or request.json['client_public_key'] == "":
        abort(400)

    id = str(uuid.uuid4()).replace('-','')

    with open('/etc/ssh/ssh_host_rsa_key.pub', 'r') as ssh_host_rsa_key_file:
        ssh_host_rsa_key=ssh_host_rsa_key_file.read().replace('\n', '')

    client = {
        'uuid': id,
        'client_public_key': request.json['client_public_key'],
        'server_public_key': ssh_host_rsa_key,
        'port': 5000+redis.incr('hits')
    }

    call([
        "useradd",
        "--create-home",
        "--groups", "dip",
        id])

    os.mkdir("/home/" + id + "/.ssh")
    call(["chmod", "700", "/home/" + id + "/.ssh"])

    with open("/home/" + id + "/.ssh/authorized_keys", "w") as f:
        f.write(client['client_public_key'])
    call(["chmod", "600", "/home/" + id + "/.ssh/authorized_keys"])
    call(["chown", "-R", id+":"+id, "/home/"+id+"/.ssh"])

    return jsonify({'client': client}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
