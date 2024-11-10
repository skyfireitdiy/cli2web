import sys
import argparse
from .web_server import run_server

def main():
    parser = argparse.ArgumentParser(description='CLI2Web - 将命令行工具转换为 Web 界面')
    parser.add_argument('command', help='要转换的命令行工具名称')
    parser.add_argument('--host', default='localhost', help='监听的主机地址 (默认: localhost)')
    parser.add_argument('--port', type=int, default=5000, help='监听的端口号 (默认: 5000)')
    
    args = parser.parse_args()
    
    # 验证命令是否存在
    import shutil
    if not shutil.which(args.command):
        print(f"Error: Command '{args.command}' not found")
        sys.exit(1)
    
    print(f"Starting web server for command: {args.command}")
    print(f"Visit http://{args.host}:{args.port} to access the web interface")
    
    run_server(host=args.host, port=args.port, cmd_name=args.command)

if __name__ == '__main__':
    main() 