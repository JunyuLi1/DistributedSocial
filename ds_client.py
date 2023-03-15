# Starter code for assignment 5 in ICS 32
# Programming with Software Libraries in Python
# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
"""Module of sending information to server"""
import socket
import ds_protocol


class JoinserverError(Exception):
    """Create an exception."""
    pass


def send(server, port, username, password, message, bio=None):
    """
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  """
    try:
        assert type(server) is str
        assert type(port) is int
        assert type(username) is str
        assert type(password) is str
        assert type(message) is str
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((server, port))
            send = client.makefile('w')
            receive = client.makefile('r')
            join_message = ds_protocol.join_action(username, password)
            send.write(join_message + '\r\n')
            send.flush()
            join_message = receive.readline()
            response = ds_protocol.extract_json(join_message).type
            if response != 'ok':
                raise JoinserverError
            else:
                token = ds_protocol.extract_json(join_message).token
                if bio is None:
                    if message.isspace():
                        raise ValueError
                    if len(message) == 0:
                        raise ValueError
                    return post_server(server, port, message, token)
                if bio is not None:  # If post all, what should we return?
                    if bio.isspace():
                        raise ValueError
                    if len(bio) == 0:
                        raise ValueError
                    if len(message) == 0:
                        return bio_server(server, port, bio, token)
                    else:
                        if message.isspace():
                            raise ValueError
                        r1 = post_server(server, port, message, token)
                        r2 = bio_server(server, port, bio, token)
                        if r1 is True and r2 is True:
                            return True
                        else:
                            return False
    except AssertionError:
        print('Incorrect type of parameters')
        return False
    except JoinserverError:
        print('Invalid password or username already taken')
        return False
    except ValueError:
        print('You cannot publish posts or bios '
              'that are empty or just whitespace.')
        return False
    except ConnectionRefusedError:
        print('Cannot connect to the server that you specified.')
        return False


def post_server(ip_address, port2, post, user_token):
    """Post information to the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as poserver:
        poserver.connect((ip_address, port2))
        send = poserver.makefile('w')
        receive = poserver.makefile('r')
        send_message = ds_protocol.post_action(user_token, post)
        send.write(send_message + '\r\n')
        send.flush()
        join_message = receive.readline()
        response = ds_protocol.extract_json(join_message).type
        if response != 'ok':
            print(ds_protocol.extract_json(join_message).message)
            return False
        else:
            print(ds_protocol.extract_json(join_message).message)
            return True


def bio_server(ip_address, port2, bio, user_token):
    """Change the bio on the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as bioserver:
        bioserver.connect((ip_address, port2))
        send = bioserver.makefile('w')
        receive = bioserver.makefile('r')
        send_message = ds_protocol.bio_action(user_token, bio)
        send.write(send_message + '\r\n')
        send.flush()
        join_message = receive.readline()
        response = ds_protocol.extract_json(join_message).type
        if response != 'ok':
            print(ds_protocol.extract_json(join_message).message)
            return False
        else:
            print(ds_protocol.extract_json(join_message).message)
            return True


if __name__ == '__main__':
    a = send('168.235.86.101', 3021, 'VC1', 'VC', message='ss 3')
    print(a)
