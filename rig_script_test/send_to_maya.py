import socket

class SendCmdsToMaya:
    def send_to_maya(self,command):
        if command is None:
            print("Error: Command is None.")
            return
        maya_host = '127.0.0.1'  # 로컬 호스트 (Maya가 실행 중인 컴퓨터)
        maya_port = 7001         # 명령 포트 번호 (Maya에서 연 포트)

        try:
            # 소켓 생성 및 연결
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((maya_host, maya_port))

            # 명령 전송
            sock.send(command.encode())
            sock.close()
        except Exception as e:
            print(f"Error: {e}")