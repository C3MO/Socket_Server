# Socket Server/Client Project

Python implementation of DSLP protocol for file transfer. This project includes:
- `sender.py` - Sends files to a server using DSLP protocol
- `receiver.py` - Receives files from a server using DSLP protocol
- `socket_utils.py` - Shared utilities for socket communication

## Usage

### Requirements
- Python 3.x

### Running the Receiver
```bash
python receiver.py [output_file]
```

Example:
```bash
python receiver.py received_file.txt
```

### Running the Sender
```bash
python sender.py [peer] [file_path]
```

Example:
```bash
python sender.py peer1 document.pdf
```

## Development for the Client

https://github.com/C3MO/Server_Client

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.