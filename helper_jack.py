import subprocess
import jack
import psutil


class PyJack:
    """Helper object to start and stop JACK deamon"""

    def __init__(self):
        self.jack_running: False

    def start(command):
        """Start JACK with relavent parameters"""
        subprocess.Popen(command)

    def stop():
        """Stop JACK"""
        for proc in psutil.process_iter():
            if proc.name() == "jackd":
                proc.kill()


class PyJackClient:
    """Helper context manager to interact with running JACK deamon"""

    def __init__(self):
        self.current = None

    def __enter__(self):
        self.current = jack.Client('jack-client')
        return self

    def __exit__(self, type, value, traceback):
        self.current.deactivate()
        self.current.close()

    def get_input_port_names(self):
        ports = self.current.get_ports(is_audio=True, is_output=True)
        port_names = []
        for port in ports:
            port_names.append(port.name)
        return port_names
