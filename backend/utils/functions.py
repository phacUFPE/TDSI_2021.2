import os
import signal
from typing import Union


class UtilFunctions:
    """
    Class that contains useful functions.
    """

    @staticmethod
    def isfloat(number: Union[float, int, str]) -> bool:
        """
        Checks if the given number is convertible to float.
        """
        is_float = True
        try:
            float(number)
        except ValueError:
            is_float = False

        return is_float

    @staticmethod
    def kill_processes_on_port(port: int):
        """
        Kills processes that is running in the given port.
        """
        try:
            for line in os.popen(f'lsof -t -i:{port}'):
                fields = line.split()

                pid = fields[0]

                os.kill(int(pid), signal.SIGKILL)
            print('Process Successfully terminated')
        except:
            print('Error Encountered while running script')
