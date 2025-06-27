import subprocess
import sys #for platform specific commands

def execute_comand(command, capture_output= True, text= True, check=False):
    try:
        result = subprocess.run(
            command,
            capture_output=capture_output,
            text=text,
            check=check,
            shell=isinstance(command, str)

        )
        return result 
    except subprocess.CalledProcessError as e:
        print(f"error: command {e.cmd} failed with exit code {e.returncode}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return None
    
    except FileNotFoundError:
         print(f"error: command {command} not found. Make sure it is there")
         return None
    
    except Exception as e:
        print(f"unexpected error occured: {e}")

def main():
    print("----system command executor----")
    print("\n----sexeuting list directory contents----")

    if sys.platform.startswith('win'):
        list_command = "dir"
    else:
        list_command = ["ls", "-1"]

    result = execute_comand(list_command)
    if result and result.returncode == 0:
        print("command executed successfully: output: ")
        print(result.stdout + "hjjhj")
    elif result:
        print(f"command failed with exit code{result.returncode}")
        print(f"steerr:{result.stderr}")

if __name__ == "__main__":
    main()


