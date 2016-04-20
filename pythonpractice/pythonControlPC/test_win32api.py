#! python2
# encoding:utf-8
import win32api, win32con

def main():
	win32api.MessageBox(0, 'Hello, Win32API', 'WYM', win32con.MB_OK)

if __name__ == '__main__':
	main()